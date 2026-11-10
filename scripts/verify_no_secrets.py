#!/usr/bin/env python3
"""Fail if a secret value or a secret-looking string is in the repository files (and, with --out, in rendered pages).

The repository is PUBLIC. In CI the secret VALUES come from the environment (GitHub secrets); locally from
~/ai/credentials/. Values are never printed — only the file and the secret's NAME.

    python3 scripts/verify_no_secrets.py            # files git would commit
    python3 scripts/verify_no_secrets.py --out      # + a sample of rendered pages in tmp-static/out
"""
import json
import os
import random
import re
import subprocess
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent
# env vars that hold secrets in GitHub Actions
SECRET_ENV = ["CJ_API_KEY", "CLOUDFLARE_API_TOKEN", "STATE_KEY", "IMG_SECRET", "AFFILIATEPORT_API_KEY", "AFFILIATEPORT_API_KEY_FULL",
              "DISCORD_WEBHOOK_URL", "CF_API_KEY", "CF_GLOBAL_API_KEY", "CF_API_TOKEN_SPORTEKA"]
# public by design: CJ PID/CID (in every affiliate link / useless without the key), IndexNow key (served as a file), site URL
PUBLIC = {"SITE_URL", "CJ_PID", "CJ_CID", "INDEXNOW_KEY", "CF_ACCOUNT_ID", "CF_ZONE_ID", "CF_WORKERS_SUBDOMAIN", "WP_URL", "WP_USER",
          "FTP_HOST", "FTP_PORT", "FTP_USER", "CF_EMAIL", "EHUB_PUBLISHER_ID", "CJ_WEBSITE_ID", "GA4_ID", "DECATHLON_AFF_QS"}
PATTERNS = [
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key"),
    (r"\bAKIA[0-9A-Z]{16}\b", "AWS key"),
    (r"\bgh[pousr]_[A-Za-z0-9]{30,}\b", "GitHub token"),
    (r"discord(?:app)?\.com/api/webhooks/\d+/[\w-]{20,}", "Discord webhook"),
    (r"(?i)\b(api[_-]?key|apikey|secret|password|passwd|token)\b\s*[:=]\s*['\"][A-Za-z0-9_\-/+=]{16,}['\"]", "hard-coded credential"),
    (r"(?i)[?&](apiKey|api-key|api_key|token|access_token)=[A-Za-z0-9_\-]{16,}", "credential in URL"),
]


def env_lines(text):
    for line in text.splitlines():
        m = re.match(r"^(?:export\s+)?([A-Za-z0-9_]+)=(.+)$", line.strip())
        if m:
            yield m.group(1), m.group(2).strip("\"' ")


def secret_values():
    vals = {}
    for n in SECRET_ENV:
        v = os.environ.get(n, "")
        if len(v) >= 10:
            vals[n] = v
    # whole credential files passed as secrets (env-file format / JSON)
    for n in ("SPT_CRED_SPORTEKA", "SPT_CRED_AFFILIATEPORT"):
        for k, v in env_lines(os.environ.get(n, "")):
            if k not in PUBLIC and len(v) >= 10:
                vals[f"{n}:{k}"] = v
    for n in ("GSC_SA_JSON", "SPT_FEEDY_JSON"):
        raw = os.environ.get(n, "")
        if raw:
            def walk(o, k=""):
                if isinstance(o, dict):
                    for kk, vv in o.items():
                        walk(vv, f"{k}.{kk}")
                elif isinstance(o, list):
                    for vv in o:
                        walk(vv, k)
                elif isinstance(o, str):
                    for q in re.findall(r"(?:key|token|hash|apikey|api_key|pass)=([A-Za-z0-9_\-]{12,})", o, re.I):
                        vals[f"{n}{k}"] = q
                    if n == "GSC_SA_JSON" and k in (".private_key", ".private_key_id"):
                        vals[f"{n}{k}"] = o
            try:
                walk(json.loads(raw))
            except ValueError:
                pass
    cred = Path(os.environ.get("SPT_ROOT", "/home/kenny/ai")) / "credentials"
    if not os.environ.get("GITHUB_ACTIONS") and cred.exists():
        for f in cred.glob(".*"):
            if not f.is_file() or f.suffix not in (".env", ".json", ".secret"):
                continue
            try:
                text = f.read_text()
            except (UnicodeDecodeError, PermissionError):
                continue
            for k, v in env_lines(text):
                if k not in PUBLIC and not k.endswith(("ACCOUNT_ID", "TEAM_DOMAIN", "SUBDOMAIN")) and len(v) >= 12:
                    vals[f"{f.name}:{k}"] = v
    return vals


def files(out):
    listed = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"], cwd=APP, capture_output=True, text=True).stdout.split("\n")
    fs = [APP / f for f in listed if f]
    o = APP / "tmp-static" / "out"
    if out and o.exists():
        pages = [p for p in o.rglob("*.html")]
        fs += random.Random(1).sample(pages, min(2000, len(pages)))
    return fs


def main():
    vals = secret_values()
    bad = []
    for f in files("--out" in sys.argv):
        try:
            text = f.read_text()
        except (UnicodeDecodeError, IsADirectoryError, FileNotFoundError):
            continue
        rel = f.relative_to(APP)
        for name, v in vals.items():
            if v in text:
                bad.append(f"{rel}: contains the value of {name}")
        if str(rel).startswith("tmp-static/"):
            continue   # rendered pages carry affiliate links (tracking parameters look like credentials)
        for rx, what in PATTERNS:
            if re.search(rx, text):
                bad.append(f"{rel}: looks like a {what}")
    if bad:
        print("SECRET CHECK FAILED:\n  " + "\n  ".join(sorted(set(bad))[:50]))
        sys.exit(1)
    print(f"secret check ok ({len(vals)} secret values)")


if __name__ == "__main__":
    main()
