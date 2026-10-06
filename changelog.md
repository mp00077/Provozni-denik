# Přehled změn

Změny jsou řazené od nejnovějšího data. Datum odpovídá dni provedení změny
v časovém pásmu Europe/Prague. Starší záznamy byly doplněny zpětně podle průběhu
vývoje v této konverzaci; datum změny se může lišit od data Git commitu.

## 2026-10-06

### Vzhled a ovládání

- Přidáno úvodní okno „Načítá se aplikace…“ s ikonou, indikátorem průběhu
  a aktuálním krokem inicializace. Po dokončení se nahradí hlavním oknem.
- Bootstrap spouští inicializaci až po otevření úvodního okna a mezi jednotlivými
  kroky vrací řízení Qt. Databáze, služby a hlavní okno se načítají přes lazy importy.
- Při chybě startu se zavře úvodní okno i databázové spojení a zobrazí se chyba.
- Přidán Designer formulář úvodního okna a jeho zahrnutí do konfigurace balení,
  doplněny testy inicializace a dokumentace startu.
- Vytvořena ikona aplikace se serverovým rackem, štítem a značkou ověřeného
  přístupu. Připraveny formáty PNG, ICO a ICNS a nástroj pro jejich převod.
- Ikona se zobrazuje v oknech aplikace a přidává se při sestavení do Windows EXE
  a macOS balíčku. PNG je přibalena pro všechny podporované platformy.
- Okna přepracována do jednotného světlého motivu s tyrkysovými hlavními akcemi,
  sjednocenou typografií, rozestupy, rámečky a stavy ovládacích prvků.
- Hlavní okno doplněno o přehled přítomných osob, celkového počtu návštěv
  a uzavřených návštěv. Upraveno rozložení akcí, filtru a tabulky.
- Doplněn počet zobrazených záznamů a informace při prázdné evidenci nebo
  hledání bez výsledků. Přehled přítomnosti počítá unikátní jména přítomných osob.
- Dialogy příchodu, opravy, historie a nastavení dostaly sjednocený vzhled,
  nadpisy, vysvětlující texty a zřetelná tlačítka pro uložení.
- Upraveny výšky řádků, šířky sloupců a formát zobrazení časů. Plné časové údaje
  s UTC offsetem a celé hodnoty buněk jsou dostupné v popiscích po najetí myší.
- Auditní historie zobrazuje původní a nové hodnoty s českými názvy polí
  místo surového JSON.
- Přidán skript pro vykreslení náhledů oken s dočasnými ukázkovými daty
  a uložené náhledy v `docs/images/`.
- Přidáno menu **Nápověda → O aplikaci** s autorem, datem a časem sestavení,
  Git tagem, Git commitem a verzí Pythonu použitého při sestavení.
- Při spuštění ze zdrojů dialog označuje datum jako „Nesestaveno“ a zobrazuje
  dostupné údaje vývojového prostředí. Zabalená aplikace čte přibalená metadata.
- Git commit v dialogu zkrácen na 7 znaků; celý hash je dostupný po najetí myší.
- Jméno autora v dialogu změněno na odkaz na https://mp00077.github.io.
  Odkaz se otevírá ve výchozím prohlížeči.

### Build a metadata

- Do Windows EXE přidána položka „Autorská práva“ (`LegalCopyright`)
  s hodnotou „M. Pospíšil“; ověřena v testu Windows version resource.
- Doplněna metadata Windows EXE: autor a společnost **Miroslav Pospíšil**,
  popis souboru **provozní deník serverovny** a textová verze z Git tagu.
- Doplněno generování metadat sestavení: datum a čas v UTC, celý Git commit,
  Git tag a verze Pythonu. Datum se v dialogu převádí do místního časového pásma.
- Verze z Gitu se získává z nejbližšího dostupného tagu v historii HEAD.
  Chybějící Git nebo tag již nezastaví build; textová verze se vynechá.
- Odstraněno odmítání tagů podle syntaxe. Libovolný tag se zachová jako textová
  verze. Číselná verze OS se odvozuje z číslic; při nemožném převodu se použije
  `0.0.0.0` bez zastavení buildu.
- Verze v informacích sestavené aplikace odpovídá tagu; bez tagu se zobrazí
  „bez verze“. Vývojové spuštění používá výchozí verzi `0.1.0`.
- Odstraněn podadresář platformy z výstupu. Windows výstup je nyní
  `dist/provozní deník/ProvozniDenik.exe`; macOS vytváří také
  `dist/provozní deník.app`.
- Přidáno čištění starých výstupů před sestavením. Aktuální chování odstraní
  celý adresář `build` a pouze `dist/provozní deník`; ostatní obsah `dist` zachová.
- Před mazáním se ověřují cílové cesty i rodičovský adresář `dist`.
  Symbolické odkazy, junctions a neadresářové cíle se odmítají.
- Aktualizována dokumentace sestavení, metadat, ikon a výstupních cest.
  Build zůstává ručně spouštěný.

### Umístění dat

- Databáze přesunuta z uživatelského profilu do `db/denik.sqlite3` u aplikace.
  Windows a Linux používají adresář vedle spustitelného souboru, macOS vedle
  `.app` a vývojové spuštění kořen projektu.
- Cesty k datům nezávisejí na aktuálním pracovním adresáři ani dočasném
  adresáři rozbalení PyInstalleru.
- Technické logy se ukládají do sousedního adresáře `logs`.
- Adresáře `db` a `logs` přidány do `.gitignore`. Starší databáze v profilu
  se automaticky nepřesouvá ani nemaže.

### Ověření a dokumentace

- Doplněny testy metadat, libovolných a chybějících tagů, Windows version resource,
  zachování autora bez verze a výběru ikon podle platformy.
- Doplněny testy čištění výstupů v dočasných adresářích včetně zachování
  ostatního obsahu `dist` a odmítnutí odkazů.
- Doplněny testy cest databáze pro zdrojové spuštění, Windows a macOS.
- Doplněny testy otevření dialogu z menu, údajů sestavení, chybějících Git údajů,
  krátkého commitu a odkazu autora.
- Vytvořen tento `changelog.md` v kořeni projektu a zpětně zaznamenán dosavadní vývoj.
- Přidány pokyny projektu pro průběžné zapisování dalších změn pod aktuální datum.

## 2026-10-01

### Základ projektu

- Navržena a vytvořena struktura Python projektu s balíčkem `provozni_denik`
  v `src`, konfigurací `pyproject.toml`, dokumentací a testy.
- Odděleny doména, aplikační služby, rozhraní úložiště, infrastruktura a GUI.
  Doména nevyžaduje Qt ani SQLite.
- Přidán bootstrap pro inicializaci QApplication, konfigurace a logování
  a sestavení konkrétních služeb při startu.
- Přidáno spuštění pomocí `python -m provozni_denik` a vstupní bod pro balení.
- Vytvořeny Qt Designer formuláře a oddělené třídy hlavního okna a dialogů.
- Přidáno generování formulářů pomocí `pyside6-uic`, podpora resources přes
  `pyside6-rcc` a adresář pro generovaný kód.
- Použity lazy importy méně používaných dialogů, exportu a záloh.
- Připraven ruční nativní build pomocí PyInstalleru pro Windows, macOS a Linux
  v režimu `onedir`, včetně migrací a dynamicky načítaných modulů.

### Evidence a úložiště

- Implementována lokální SQLite databáze, první transakční migrace a kontrola
  verze schématu. Aktivovány cizí klíče a režim WAL.
- Implementovány příchody a odchody s osobou, serverovnou, účelem návštěvy,
  volitelným doprovodem a operátorem převzatým z účtu OS.
- Přidána validace povinných údajů a omezení délek polí.
- Doplněna ochrana před duplicitní otevřenou návštěvou stejné osoby v serverovně
  a před opakovaným zapsáním odchodu.
- Implementovány opravy údajů s povinným důvodem a auditní historie
  s původními a novými hodnotami.
- Změny návštěv a auditní události se ukládají společně v jedné transakci.
  SQL triggery zakazují běžnou aktualizaci a mazání auditních řádků.
- Před odchodem a opravou se získává databázový zámek pro zápis.
- Časy ukládány v UTC a zobrazovány v místním časovém pásmu.
- Technické logování odděleno od auditní evidence a doplněna rotace logů.

### Funkce GUI a ověření

- Přidáno hledání, řazení návštěv, filtr přítomných osob a výchozí serverovna
  uložená přes QSettings.
- Implementován CSV export všech návštěv včetně ochrany buněk před běžnými vzorci.
- Implementována konzistentní ruční záloha přes SQLite backup API
  s odmítnutím zálohy do provozního databázového souboru.
- Export a zálohování přesunuty do pracovních úloh na pozadí.
  Záloha používá vlastní databázové spojení a export snapshot dat.
- Během úlohy se blokuje souběžné spuštění dalšího exportu či zálohy a zavření okna.
- Doplněno zobrazení chyb a bezpečné uzavření databázového spojení.
- Vytvořeny testy evidence, auditních transakcí a rollbacku, oprav, CSV exportu,
  záloh, migrace, filtrování a práce s okny.
- Doplněna dokumentace architektury, datového modelu, sestavení a otevřených
  bezpečnostních požadavků. Lokální verze nemá samostatné přihlášení, role,
  centrální server ani potvrzení právního souladu.
