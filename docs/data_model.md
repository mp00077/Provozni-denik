# Datový model

`visits`: ID, osoba, serverovna, účel, doprovod, UTC příchod, volitelný UTC odchod,
operátor vytvoření. Osoba a serverovna jsou v první verzi textové identifikátory.
Unikátní částečný index brání dvěma otevřeným návštěvám stejné osoby v téže
serverovně. Porovnání identifikátorů je přesné a rozlišuje velikost písmen.

`audit_events`: ID, návštěva, typ události, UTC čas, operátor, původní hodnoty JSON,
nové hodnoty JSON, důvod. Události: arrival, departure, correction.
Zápis návštěvy i auditu je jedna transakce. SQL triggery zakazují UPDATE a DELETE
auditních událostí. Přístup s právem měnit databázový soubor může tato omezení
obejít; nejde o kryptografickou ochranu ani centrálně zabezpečený audit.

Oprava mění osobu, serverovnu, účel nebo doprovod a vyžaduje důvod.
Ruční změna časů, odstranění návštěvy a opětovné otevření uzavřené návštěvy nejsou
v první verzi dostupné. Příchod a odchod používají čas počítače.

Verze schématu je v `PRAGMA user_version`. Nová databáze vzniká transakční migrací
`001_initial.sql`. Novější neznámé schéma se odmítne. Budoucí verze musí doplnit
sekvenční migrace a zálohu před změnou schématu.
