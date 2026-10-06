# Provozní deník

Základ lokální desktopové aplikace PySide6 pro evidenci přístupů do serverovny.
Podporuje příchody, odchody, opravy s důvodem, auditní historii, hledání,
filtr přítomných osob, export všech záznamů do CSV a konzistentní zálohu SQLite.

Rozhraní používá jednotný světlý motiv s tyrkysovými hlavními akcemi, přehledem
přítomných osob a návštěv a přehlednými dialogy. Náhledy s ukázkovými daty jsou
v `docs/images/`; obnovíte je příkazem `python scripts/preview_ui.py`.

## Vývojové spuštění

Python 3.11 nebo novější. Příkazy spusťte v kořeni projektu ve stejném prostředí:

```shell
python -m venv .venv
```

Aktivace na Windows (PowerShell): `.venv\Scripts\Activate.ps1`.
Na macOS/Linux: `source .venv/bin/activate`.

```shell
python -m pip install -e ".[build]"
python scripts/generate_ui.py
python -m provozni_denik
```

Generované Python formuláře jsou součástí projektu, ale změny rozhraní se dělají
v `.ui` souborech. Po úpravě formulářů je znovu vygenerujte.

## Ověření

```shell
python -m unittest discover -s tests -v
```

Testy používají dočasnou databázi. GUI testy pracují v režimu `offscreen`.

## Ruční build

```shell
python scripts/build.py
```

Build nejprve volá `pyside6-uic` (a pro případné `.qrc` také `pyside6-rcc`),
potom PyInstaller. Výstup vznikne v `dist/provozní deník/`
(na macOS také balíček `dist/provozní deník.app`).
Git tag (např. `v0.1.0`) je volitelný; bez tagu build pokračuje bez verze z Gitu.
Windows EXE obsahuje ikonu, autora Miroslav Pospíšil, popis souboru
„provozní deník serverovny“ a verzi podle Git tagu. Podrobnosti: [build](docs/build.md).
Windows, macOS a Linux se sestavují každý na svém systému. Build není automaticky
spouštěn při startu aplikace ani při testech.

## Data a současné hranice

- Windows: `%LOCALAPPDATA%/ProvozniDenik`.
- macOS: `~/Library/Application Support/ProvozniDenik`.
- Linux: `$XDG_DATA_HOME/ProvozniDenik`, případně `~/.local/share/ProvozniDenik`.

Databáze obsahuje UTC časy; okna je zobrazují v časovém pásmu počítače.
Operátor je přebírán z účtu OS. Aplikace nemá samostatné přihlášení, role,
šifrování, centrální server, automatickou retenci ani PDF export.
SQLite soubor je určen pro lokální používání, nikoli společnou síťovou složku.
Export CSV obsahuje všechny návštěvy, nikoli aktuální filtr ani auditní historii;
úplnou evidenci včetně auditu obsahuje záloha databáze.

Jde o technický základ, nikoli potvrzení souladu s právními požadavky.
Podrobnosti: [architektura](docs/architecture.md), [datový model](docs/data_model.md),
[bezpečnostní požadavky](docs/security_requirements.md), [build](docs/build.md).
