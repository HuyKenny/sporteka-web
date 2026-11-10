"""sporteka.cz — text of Pantofle a žabky (3. 11. 2026). Same rules as texty_vlna1a.py."""
from texty_vlna1a import T
from texty_vlna1x import B

NEW = {}

NEW['pantofle-a-zabky'] = dict(
    title='Pantofle a žabky – Crocs, Birkenstock, Adidas | Sporteka',
    desc='Pantofle, nazouváky a žabky pánské, dámské i dětské: Crocs, Birkenstock, Adidas, Ipanema. Porovnejte ceny a velikosti skladem v českých obchodech.',
    intro='<p><strong>Pantofle a žabky</strong> jsou obuv, kterou si vezmete na pláž, k bazénu, do šatny, do sprch i domů. Každý typ slouží trochu jinak: <strong>žabky</strong> mají řemínek mezi prsty a hodí se na horké dny, '
          '<strong>nazouváky</strong> (pantofle s plochou podrážkou a širokým pásem) se obují jedním pohybem a drží lépe, <strong>klapky Crocs</strong> jsou lehké a omyvatelné a <strong>domácí pantofle</strong> hřejí a chrání před studenou podlahou. '
          'Pokud potřebujete obuv se zapnutým páskem na chůzi i do terénu, podívejte se do kategorie <a href="/sandaly/">sandály</a>.</p>'
          '<p>Na Sportece porovnáte ceny pantoflí z českých obchodů, uvidíte slevy a velikosti, které mají obchody právě skladem, a výběr zúžíte podle značky, pohlaví a ceny.</p>',
    guide='<h2>Jak vybrat pantofle a žabky</h2>'
          '<p>Nejdřív si ujasněte, kde je budete nosit. Do sprch a na pláž hledejte materiál, který nenasákne vodou a nekluže. Na delší procházky je lepší model s tvarovanou stélkou, na doma měkký a teplý. Nejčastější chybou je koupě podle vzhledu bez ohledu na účel.</p>'
          '<h3>Typy a k čemu se hodí</h3>'
          + T(['Typ', 'Vhodné pro', 'Na co si dát pozor'], [['Žabky', 'pláž, bazén, horké dny', 'nejsou stabilní, řemínek mezi prsty může tlačit'], ['Nazouváky (slides)', 'sprchy, šatna, volný čas', 'chodidlo drží jen horní pás'], ['Crocs a klapky z pěny', 'voda, zahrada, práce v kuchyni', 'jiné střihy dle modelu, vyberte správnou šířku'], ['Kožené pantofle', 'volný čas, cesty, domů', 'kůže se roztáhne, ne zcela mokrá'], ['Domácí pantofle', 'doma, hosté, hotely', 'zvolte protiskluzovou podrážku']]) +
          '<h3>Materiál</h3>'
          '<ul><li><strong>EVA pěna a guma:</strong> lehká, rychle schne, nesmrdí, ideální k vodě.</li>'
          '<li><strong>Kůže a korek:</strong> pohodlnější a tvarují se podle nohy, voda jim ale škodí.</li>'
          '<li><strong>Textil a flís:</strong> měkký a teplý, hodí se do interiéru.</li>'
          '<li><strong>Ovčí kůže (typ Ugg):</strong> velmi teplá, vhodná na zimu a do chladné podlahy.</li></ul>'
          '<h3>Správná velikost</h3>'
          '<p>Pantofle mají sedět tak, aby pata nepřesahovala podrážku a prsty se nedotýkaly okraje. Větší velikost způsobuje šourání a zvyšuje riziko zakopnutí. Značky se liší: Birkenstock má užší i širší střihy (Regular a Narrow), Crocs mají volnější typy Roomy a Relaxed. U každého páru zkontrolujte tabulku velikostí v popisu.</p>'
          '<h3>Pantofle pro děti</h3>'
          '<p>Dětské pantofle by měly mít zadní pásek nebo pevnější špičku, aby je dítě neztrácelo při běhání. U menších dětí se vyplatí protiskluzová podrážka, na pláži barva, která je v písku vidět. Velikost kontrolujte přibližně každé tři měsíce, protože nožka roste rychle.</p>'
          '<h3>Značky v nabídce</h3>'
          f'<p>Největší nabídku mají {B(("crocs", "Crocs"), ("birkenstock", "Birkenstock"), ("adidas", "Adidas"), ("ugg", "Ugg"), ("ipanema", "Ipanema"), ("coqui", "Coqui"), ("aquos", "Aquos"), ("nike", "Nike"))}. '
          'Crocs jsou nejznámější u klapek a nazouváků, Birkenstock u anatomické stélky, Adidas a Nike u sportovních nazouváků a Coqui a Aquos nabízejí cenově dostupné modely pro děti i dospělé.</p>'
          '<h3>Časté chyby</h3>'
          '<ul><li>Žabky na dlouhé procházky. Nemají oporu klenby ani pevné držení paty.</li>'
          '<li>Domácí pantofle do sprch nebo do vody. Textil nasákne a hůř schne.</li>'
          '<li>Příliš velká velikost pro děti „na vyrůstání“. Dítě v nich klopýtá.</li>'
          '<li>Zanedbaná hygiena. Pantofle se nosí bez ponožek, proto je pravidelně myjte.</li></ul>'
          '<h3>Péče o pantofle</h3>'
          '<p>Gumové a pěnové pantofle opláchněte vlažnou vodou s mýdlem a nechte vyschnout ve stínu, na slunci a topení se deformují. Kožené a korkové ošetřete jemným ubrouskem a impregnací. Textilní domácí pantofle perte podle štítku, vlněné ručně. Pokud mají vyjímatelnou stélku, občas ji vyndejte a vysušte.</p>'
          '<h3>Kdy se vyplatí koupit</h3>'
          '<p>Letní žabky a nazouváky bývají nejlevnější na konci léta, zimní domácí pantofle a modely z ovčí kůže po zimě. Aktuální slevy vidíte přímo u každého zboží. Podobné sezónní produkty najdete i v kategoriích <a href="/obuv-do-vody/">obuv do vody</a> a <a href="/plavky/">plavky</a>.</p>',
    faq=[('Jaký je rozdíl mezi žabkami a nazouváky?', 'Žabky mají řemínek mezi prsty, nazouváky široký pás přes nárt. Nazouváky drží chodidlo stabilněji a nepoškrábou prsty.'),
         ('Jaké pantofle do bazénu a sprch?', 'Z EVA pěny nebo gumy s protiskluzovou podrážkou. Rychle schnou, nenasáknou a snadno se čistí.'),
         ('Jak vybrat velikost pantoflí?', 'Pata nesmí přesahovat podrážku a prsty nesmí narážet na okraj. U Birkenstock a Crocs sledujte šířku střihu a tabulku výrobce.'),
         ('Jsou Crocs vhodné na každý den?', 'Ano, jsou lehké a pohodlné, ale na delší chůzi do terénu se hodí pevnější obuv.'),
         ('Jak vyčistit gumové pantofle?', 'Vlažnou vodou a jemným mýdlem, osušit ve stínu. Nesušte je na topení ani na přímém slunci.'),
         ('Jaké domácí pantofle na zimu?', 'Z flísu, vlny nebo ovčí kůže s protiskluzovou podrážkou. Kůže a vlna lépe regulují teplo nohy.')],
)
