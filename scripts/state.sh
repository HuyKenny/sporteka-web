#!/usr/bin/env bash
# Encrypted state between GitHub Actions runs (the repository and its releases are PUBLIC): release "state" holds
# AES-256 encrypted, zstd-compressed tarballs, unreadable without STATE_KEY (a GitHub secret).
#   scripts/state.sh pull catalog|feeds|web|gsc    download + decrypt (no-op when the part does not exist yet)
#   scripts/state.sh push catalog|feeds|web|gsc    encrypt + upload
# Parts (each < 2 GB, the release asset limit):
#   catalog  data/live-production.db          catalogue mirror (what the site shows), base of the weekly diff
#   feeds    data/cj data/dec                 last good feed files (shops that block GitHub IPs keep the previous file)
#   web      data/static-state.db tmp-static/keep-astro data/state   deployed files + hashes, old /_astro bundles, IndexNow
#   gsc      data/gsc.json                    Search Console impressions, pushed weekly from Malina (bin/sporteka-gsc.sh):
#                                             the Google service account has access to every site, so it stays there
set -euo pipefail
cd "$(dirname "$0")/.."
: "${STATE_KEY:?STATE_KEY missing}"
part="${2:-}"
case "$part" in
  catalog) paths=(data/live-production.db) ;;
  feeds) paths=(data/cj data/dec) ;;
  web) paths=(data/static-state.db tmp-static/keep-astro data/state) ;;
  gsc) paths=(data/gsc.json) ;;
  *) echo "usage: $0 pull|push catalog|feeds|web|gsc"; exit 2 ;;
esac
asset="$part.tar.zst.enc"
tmp="${RUNNER_TEMP:-/tmp}/$asset"
enc() { openssl enc -aes-256-cbc -pbkdf2 -iter 200000 "$@" -pass env:STATE_KEY; }
case "${1:-}" in
  pull)
    if gh release download state -p "$asset" -O "$tmp" --clobber 2>/dev/null; then
      enc -d -in "$tmp" | zstd -dq | tar x
      rm -f "$tmp"
      echo "state $part restored"
    else
      echo "no state $part yet"
    fi ;;
  push)
    existing=()
    for p in "${paths[@]}"; do [ -e "$p" ] && existing+=("$p"); done
    [ ${#existing[@]} -gt 0 ] || { echo "nothing to save for $part"; exit 0; }
    tar c "${existing[@]}" | zstd -q -T0 -6 | enc -salt -out "$tmp"
    gh release view state >/dev/null 2>&1 || gh release create state --title "build state (encrypted)" --latest=false \
      --notes "Encrypted state between builds (AES-256, key in a GitHub secret). Not a software release."
    gh release upload state "$tmp" --clobber
    echo "state $part saved ($(du -h "$tmp" | cut -f1))"
    rm -f "$tmp" ;;
  *) echo "usage: $0 pull|push catalog|feeds|web"; exit 2 ;;
esac
