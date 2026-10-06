# Nativní build

Build spouští uživatel ručně: `python scripts/build.py`.
Použijte prostředí s nainstalovanými závislostmi `pip install -e ".[build]"`.

1. `generate_ui.py` najde Qt nástroje v adresáři scripts aktivního Pythonu.
2. Každý `.ui` převede pomocí `pyside6-uic` do `ui/generated/`.
3. Případné `.qrc` převede pomocí `pyside6-rcc`.
4. PyInstaller použije `packaging/app.spec`, včetně migrací a lazy importů.
5. Výstup: `dist/win32/ProvozniDenik`, `dist/darwin/ProvozniDenik.app`
   nebo `dist/linux/ProvozniDenik`.

Režim `onedir` usnadňuje diagnostiku a nevyžaduje rozbalování celé aplikace při
každém startu. `.app` vzniká pouze na macOS. Build není cross-kompilace.
Ikony, instalátory, podpisy, notarizace macOS a distribuční Linux balíčky nejsou
zatím součástí konfigurace. Linuxový build je nutné připravit a ověřit na vhodné
základní distribuci pro cílové prostředí.

Před distribucí na každém OS ověřte start, zápis, audit, export, zálohu a cestu dat.
Úspěšné testy zdrojového kódu samy nepotvrzují funkčnost zabalené aplikace.
