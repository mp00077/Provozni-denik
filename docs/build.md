# Nativní build

Build spouští uživatel ručně: `python scripts/build.py`.
Použijte prostředí s nainstalovanými závislostmi `pip install -e ".[build]"`.
Po zjištění volitelného Git tagu skript odstraní celý existující adresář `build`
a pouze podadresář `dist/provozní deník`. Ostatní obsah `dist` zůstává zachovaný.
Poté generuje formuláře
a sestaví aplikaci. Odkazy na jiné adresáře odmítne; při chybě mazání build zastaví.

## Verze, autor a ikony

Verze se odvozuje pomocí `git describe --tags --abbrev=0 HEAD` z nejbližšího
dostupného tagu v historii aktuálního commitu. Formát tagu se nekontroluje;
libovolný tag se zachová jako textová verze. Bez dostupného tagu nebo Gitu
build pokračuje a textové položky verze vynechá. Autor, popis a ikona zůstávají.
Pevný Windows resource vyžaduje číselnou verzi; bez tagu má nulovou hodnotu
`0.0.0.0`. Aplikace pak v informacích zobrazuje „bez verze“. Na macOS se explicitní
verze nepředává balicímu nástroji.
Například první tag můžete volitelně vytvořit ručně:

```shell
git tag v0.1.0
```

Pro vydání vytvářejte tag přímo na vydávaném commitu. Pro číselnou verzi OS se
použijí první čtyři skupiny číslic před příponou oddělenou `-` nebo `+`;
chybějící části se doplní nulami. Pokud tag neobsahuje čísla nebo jsou mimo rozsah
0–65535, použije se číselná verze `0.0.0.0` a build pokračuje.
Textová verze v EXE a aplikaci zachovává celý tag, pevná číselná verze
Windows například pro `v1.2.3` obsahuje `1.2.3.0`. Zabalená aplikace zobrazuje
stejný Git tag v informacích. Vývojové spuštění nadále používá `0.1.0`.

Windows EXE obsahuje CompanyName a vlastní položku Author = `Miroslav Pospíšil`,
FileDescription = `provozní deník serverovny` a FileVersion/ProductVersion z tagu.
Průzkumník Windows nemusí vlastní pole Author zobrazit; autor je proto rovněž
v běžném poli Společnost. Nejde o digitální podpis ani ověřeného vydavatele.

`packaging/icons/app.ico` je vložena do Windows EXE, `app.icns` do macOS `.app`.
Linux používá PNG pro ikonu oken; ELF soubor nemá Windows záložku Podrobnosti
ani obdobný vložený ICO resource. PNG je přibalena i pro ostatní platformy.
Metadata se generují pod `build/<platforma>/metadata/`.
Do aplikace se přibalí také datum a čas sestavení v UTC, celý Git commit a verze
Pythonu build prostředí. Menu **Nápověda → O aplikaci** tyto údaje zobrazuje;
čas sestavení převede do místního pásma a uvede UTC offset. Zabalená aplikace
nepotřebuje Git na cílovém počítači. Při spuštění ze zdrojů ukáže „Nesestaveno“,
aktuální Python a Git údaje zdrojového repozitáře, pokud jsou dostupné.

Ikony jsou již připravené; build nevyžaduje Pillow. Při budoucí výměně PNG je
možné použít `python scripts/prepare_icons.py cesta/k/ikone.png` (vyžaduje Pillow).

1. `generate_ui.py` najde Qt nástroje v adresáři scripts aktivního Pythonu.
2. Každý `.ui` převede pomocí `pyside6-uic` do `ui/generated/`.
3. Případné `.qrc` převede pomocí `pyside6-rcc`.
4. PyInstaller použije `packaging/app.spec`, včetně migrací a lazy importů.
5. Výstup: `dist/provozní deník/` bez podadresáře platformy.
   Na Windows obsahuje `ProvozniDenik.exe`; na macOS vzniká také
   `dist/provozní deník.app`.

Režim `onedir` usnadňuje diagnostiku a nevyžaduje rozbalování celé aplikace při
každém startu. `.app` vzniká pouze na macOS. Build není cross-kompilace.
Instalátory, podpisy, notarizace macOS a distribuční Linux balíčky nejsou
zatím součástí konfigurace. Linuxový build je nutné připravit a ověřit na vhodné
základní distribuci pro cílové prostředí.

Před distribucí na každém OS ověřte start, zápis, audit, export, zálohu a cestu dat.
Úspěšné testy zdrojového kódu samy nepotvrzují funkčnost zabalené aplikace.
