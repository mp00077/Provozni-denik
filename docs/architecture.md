# Architektura

`__main__` a balicí launcher volají `bootstrap.main`. Bootstrap vytvoří QApplication,
nastaví umístění dat a logování. `application.run` otevře databázi, provede migrace,
sestaví služby a otevře hlavní okno. Při ukončení zavře databázové spojení.

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
