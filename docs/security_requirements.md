# Bezpečnostní požadavky k dopracování

Dokument zachycuje technické hranice a otevřené požadavky. Právní výklad ani
konkrétní zákonná ustanovení nebyly v této fázi ověřovány.

Před provozním nasazením určit s odpovědnou osobou:

- režim organizace a závazná pravidla vedení deníku;
- povinné údaje, účel zpracování, dobu uchování a oprávnění k exportu;
- správu identit, přihlašování a role operátora, správce a auditora;
- požadovanou odolnost auditu proti manipulaci a případné centrální ukládání;
- ochranu databáze a záloh, oprávnění OS, šifrování a obnovu;
- důvěryhodný zdroj času a pravidla oprav chybných časových údajů;
- způsob stabilní identifikace osob a serveroven;
- požadavky na více stanic, centrální API a dostupnost.

Implementováno: transakční audit, opravy s důvodem, zákaz úprav auditních řádků
přes běžné SQL, oddělení technických logů, konzistentní ruční zálohy a ochrana
CSV buněk proti běžným vzorcům. Technické logy mohou při výjimkách obsahovat
diagnostické údaje; jejich přístup a dobu uchování je třeba spravovat.

Identita OS není samostatně ověřené přihlášení do aplikace. Lokální vlastník
databáze může soubor změnit. Aplikace zatím neposkytuje deklaraci právního souladu.
