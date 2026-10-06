# Nativní build

Build spouští uživatel ručně: `python scripts/build.py`.
Použijte prostředí s nainstalovanými závislostmi `pip install -e ".[build]"`.
Po zjištění volitelného Git tagu skript odstraní celé existující adresáře `build` a `dist`
v kořeni projektu, včetně výstupů ostatních platforem. Poté generuje formuláře
a sestaví aplikaci. Odkazy na jiné adresáře odmítne; při chybě mazání build zastaví.

## Verze, autor a ikony

Verze se odvozuje pomocí `git describe --tags --abbrev=0 HEAD` z nejbližšího
dostupného tagu v historii aktuálního commitu. Podporovány jsou tagy `v1.2.3`,
`1.2.3`, `1.2.3.4` a přípony jako `v1.2.3-rc.1`. Bez dostupného tagu nebo Gitu
build pokračuje a textové položky verze vynechá. Autor, popis a ikona zůstávají.
Pevný Windows resource vyžaduje číselnou verzi; bez tagu má nulovou hodnotu
`0.0.0.0`. Aplikace pak v informacích zobrazuje „bez verze“. Na macOS se explicitní
verze nepředává balicímu nástroji. Nepodporovaný existující tag je nadále chyba.
Například první tag můžete volitelně vytvořit ručně:

```shell
git tag v0.1.0
```

Pro vydání vytvářejte tag přímo na vydávaném commitu. Části číselné verze musí
být v rozsahu 0–65535. Textová verze v EXE zachovává celý tag, pevná číselná verze
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
