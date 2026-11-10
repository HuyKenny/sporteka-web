"""sporteka.cz — static pages (posts table, type 'page'), written by scripts/katalog.py on every build.
Edit the text here and run `katalog.py build` + `push`; ids are fixed (slugs table kind 'page')."""

OPERATOR = 'Ha Duy Huy, IČO 07876823'
EMAIL = 'info@sporteka.cz'

PAGES = [
    (1, 'jak-srovnavame', 'Jak srovnáváme ceny', 'Odkud bereme ceny, jak párujeme stejné zboží napříč obchody a jak na Sporteka.cz vyděláváme.', f'''
<p>Sporteka.cz je nezávislý srovnávač cen sportovního vybavení, oblečení, obuvi a outdoorového vybavení. Nic neprodáváme: ukážeme vám, jak se liší nabídky stejného zboží, a nákup dokončíte přímo v e-shopu.</p>
<h2>Odkud bereme nabídky</h2>
<p>Ceny, velikosti, dostupnost a fotky načítáme z produktových feedů českých sportovních e-shopů, se kterými spolupracujeme přes affiliate sítě. Nabídky aktualizujeme pravidelně každý týden. U každého produktu uvidíte, kdy jsme cenu naposledy ověřili.</p>
<h2>Jak párujeme stejné zboží</h2>
<p>Stejný model bot nebo bundy prodává více obchodů pod různými názvy. Nabídky spojujeme podle kódu EAN, a kde chybí, podle značky, názvu modelu, barvy a určení (pánské, dámské, dětské). Velikosti jednoho modelu v jednom obchodě sloučíme do jedné nabídky a vypíšeme, které velikosti má obchod skladem.</p>
<h2>Jak řadíme</h2>
<p>Výchozí řazení je podle oblíbenosti: produkty, které nabízí více obchodů a o které je větší zájem, jsou výš. Řadit můžete také podle ceny, slevy nebo novinek. Pořadí si nikdo nemůže zaplatit.</p>
<h2>Slevy a vývoj ceny</h2>
<p>Slevu ukazujeme jen tehdy, když ji uvádí sám obchod (původní a akční cena). U produktů sledujeme nejnižší cenu v čase, takže poznáte, jestli je aktuální cena opravdu výhodná.</p>
<h2>Jak vyděláváme</h2>
<p>Když přes naše odkazy nakoupíte, obchod nám může zaplatit provizi. Cena se pro vás nemění a provize nemá vliv na to, které nabídky a v jakém pořadí ukazujeme.</p>
<h2>Kontakt</h2>
<p>Našli jste chybu v ceně nebo špatně spárovaný produkt? Napište nám na <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
'''),
    (2, 'podminky-pouziti', 'Podmínky použití', 'Podmínky používání srovnávače Sporteka.cz.', f'''
<p>Provozovatelem webu Sporteka.cz je {OPERATOR} (dále jen „provozovatel“). Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Co Sporteka.cz je</h2>
<p>Sporteka.cz je srovnávač cen. Provozovatel není prodávajícím zboží, které na webu najdete, a není stranou kupní smlouvy. Smlouvu uzavíráte přímo s e-shopem, do kterého z našeho webu přejdete, a platí jeho obchodní podmínky, reklamační řád a ceny.</p>
<h2>Správnost údajů</h2>
<p>Ceny, dostupnost, velikosti, popisy a fotky přebíráme z podkladů obchodů a aktualizujeme je pravidelně. Mezi aktualizacemi se mohou změnit. Rozhodující je vždy cena a dostupnost uvedená v e-shopu v okamžiku objednávky. Za chyby v podkladech obchodů provozovatel neodpovídá.</p>
<h2>Odkazy do obchodů</h2>
<p>Odkazy do e-shopů jsou partnerské (affiliate). Při nákupu může provozovatel od obchodu získat provizi. Cena pro vás se tím nemění.</p>
<h2>Autorská práva</h2>
<p>Texty a grafika webu jsou chráněny autorským právem. Fotky a popisy produktů patří příslušným obchodům a výrobcům.</p>
<h2>Závěrečná ustanovení</h2>
<p>Provozovatel může tyto podmínky měnit; platí verze zveřejněná na této stránce.</p>
'''),
    (3, 'ochrana-osobnich-udaju', 'Ochrana osobních údajů a cookies', 'Jaké údaje Sporteka.cz zpracovává, cookies a vaše práva.', f'''
<p>Správcem údajů je {OPERATOR}, kontakt <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Jaké údaje zpracováváme</h2>
<p>Na webu se nikam nepřihlašujete a nevyplňujete žádné osobní údaje. Zpracováváme jen technické údaje nutné pro provoz:</p>
<ul>
<li><strong>Prokliky do obchodů</strong> — když kliknete na odkaz do e-shopu, uložíme, na jakou nabídku jste klikli a kdy, spolu s jednosměrným otiskem IP adresy, který se mění každý den (z otisku nelze IP adresu zpětně zjistit). Slouží ke statistice oblíbenosti produktů a k ochraně před zneužitím.</li>
<li><strong>Serverové záznamy</strong> — poskytovatel hostingu (Cloudflare) krátkodobě zpracovává technické záznamy o požadavcích kvůli bezpečnosti a ochraně před útoky.</li>
</ul>
<h2 id="cookies">Cookies</h2>
<p>Web sám nepoužívá reklamní ani sledovací cookies. Pokud zapneme měření návštěvnosti (Google Analytics), spustí se až po vašem souhlasu v liště na webu a volbu si pamatujeme v úložišti vašeho prohlížeče. Souhlas můžete kdykoli odvolat smazáním dat webu v prohlížeči.</p>
<p>Po přechodu do e-shopu platí zásady ochrany osobních údajů a cookies daného obchodu a affiliate sítě, přes kterou odkaz vede (např. CJ, eHub).</p>
<h2>Vaše práva</h2>
<p>Máte právo na přístup k údajům, jejich opravu nebo výmaz, omezení zpracování a právo vznést námitku. Stížnost můžete podat u Úřadu pro ochranu osobních údajů (www.uoou.cz).</p>
'''),
    (4, 'o-nas', 'O Sporteka.cz a redakční zásady', 'Kdo za Sporteka.cz stojí, jak vybíráme obchody a značky a čím se řídíme při popisu produktů a kategorií.', f'''
<p>Sporteka.cz je nezávislý srovnávač sportovního vybavení, oblečení a obuvi. Pomáháme vám zorientovat se v nabídce českých e-shopů: ukážeme stejné zboží od více prodejců vedle sebe, velikosti skladem a vývoj ceny. Rozhodnutí ale zůstává na vás, a proto k nabídkám přidáváme i průvodce výběrem.</p>
<h2>Kdo web provozuje</h2>
<p>Provozovatelem je {OPERATOR}. Sporteka.cz nic neprodává, objednávku vždy dokončíte v e-shopu prodejce. Kontakt: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Kdo za webem stojí</h2>
<p>Sporteku postavil a provozuje Ha Duy Huy (Kenny). Živí se jako SEO konzultant a srovnávače cen si staví sám. Jak Sporteka vznikala, popsal v <a href="https://huy.cz/projekty/sporteka/" rel="nofollow">případové studii na huy.cz</a>.</p>
<h2>Jak vybíráme obchody</h2>
<p>Zařazujeme české a slovenské e-shopy se sportovním, outdoorovým, cyklistickým, fitness a podobným zbožím, které nabízejí produktový feed přes partnerské sítě. Obchod, který neaktualizuje ceny nebo dlouhodobě posílá chybná data, ze srovnání vyřazujeme.</p>
<h2>Jak pracujeme s texty</h2>
<ul>
<li>Průvodci „jak vybrat“ vycházejí z parametrů, které opravdu rozhodují: velikost a střih, sezóna, materiál, objem nebo vodotěsnost.</li>
<li>Slevu uvádíme jen tehdy, když ji udává obchod. Skutečnou výhodnost nabídky ukazuje graf vývoje ceny u produktu.</li>
<li>Pořadí produktů si nikdo nemůže koupit. Provize od obchodů cenu pro vás nemění.</li>
<li>Chybu v ceně, špatné zařazení nebo spárování produktu opravíme, jakmile nám ji nahlásíte.</li>
</ul>
<p>Podrobně popisujeme postup na stránce <a href="/jak-srovnavame/">Jak srovnáváme ceny</a>.</p>
'''),
]
