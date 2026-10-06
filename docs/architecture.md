# Architektura

`__main__` a balicí launcher volají `bootstrap.main`. Bootstrap vytvoří QApplication
a zobrazí úvodní okno „Načítá se aplikace…“. Po spuštění Qt event loop nastaví
logování a vytvoří `ApplicationSession`. Inicializace po krocích otevře databázi,
provede migrace, sestaví služby a připraví hlavní okno. Každý krok nejprve oznámí
svůj stav; další pokračování se naplánuje přes QTimer. Importy služeb a hlavního
okna probíhají až v těchto krocích. Při ukončení se zavře databázové spojení.
Inicializace zůstává v GUI vlákně kvůli Qt a vlastnictví SQLite spojení; jednotlivé
synchronní operace mohou na dobu svého běhu pozastavit animaci indikátoru.

Databáze je v `db/denik.sqlite3` v kořeni projektu při vývoji, vedle spustitelného
souboru u Windows/Linux balíčku, nebo vedle `.app` na macOS. Logy jsou v `logs`
ve stejném kořenovém adresáři. Data se neukládají do uživatelského profilu.

Směr závislostí: UI → služby → doména a rozhraní (`ports`). Implementace úložiště
je v `infrastructure`; sestavení konkrétních implementací je v `application.py`.
Doména neimportuje Qt ani SQLite. Balíčkové `__init__.py` nemají vedlejší efekty.

Méně používané dialogy, export, zálohy a pracovní úlohy mají lokální lazy importy.
Seznam dynamických modulů je zachycen také v PyInstaller spec souboru.
Základní Qt moduly se načítají při startu GUI.

SQL zápisy probíhají v GUI vlákně a v krátkých transakcích. CSV worker dostane
snapshot dat. Worker zálohy otevře vlastní read-only spojení; nesdílí spojení GUI.
Během exportu/zálohy se blokuje spuštění další takové úlohy a zavření okna.
Velké objemy dat budou vyžadovat stránkování a asynchronní načítání.

Formuláře se editují v Qt Designeru. `ui/generated/` je výhradně výstup generátoru.
Resources, vlastní ikony a PDF export se přidají při dalším rozšíření; build
generátor již podporuje `.qrc` soubory. Osoby a serverovny jsou zatím textová pole,
nikoli samostatné spravované číselníky.
