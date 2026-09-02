# Szakdolgozati irány és megvalósítási terv

## Javasolt fókusz

A dolgozat fő állítása az legyen, hogy egy felhőalapú adattárház-architektúra hogyan teszi lehetővé zenei streaming-metaadatok reprodukálható gyűjtését, egységesítését és elemzését. A BSc-szintű terjedelemhez a nyilvános katalógusadatok elemzése elegendő; személyes hallgatási adatok és gépi tanulás csak opcionális bővítés.

## Kutatási kérdések

1. Milyen adatminőségi és adatmodellbeli problémák jelennek meg a Spotify API-ból gyűjtött adatoknál?
2. Milyen BigQuery-sémával és partícionálással kezelhető hatékonyan az időbélyegzett snapshot-adat?
3. Milyen trendek azonosíthatók a népszerűség, megjelenési idő és audio-feature-változók alapján?
4. Milyen korlátai vannak a Spotify popularity és audio-feature mezők üzleti értelmezésének?

## Kötelező mérföldkövek

- A kutatási kérdések, adatforrás és mintavételi időszak rögzítése.
- API-lekérdezés, rate limit-kezelés, hibalogolás és nyers adatarchiválás.
- Normalizált BigQuery-séma, betöltés és költségtudatos lekérdezések.
- Legalább három ellenőrizhető elemzési eredmény és Power BI-oldal.
- Adatminőségi ellenőrzések, reprodukálhatósági leírás és korlátok.

## A témaleírás javítandó pontjai

A végleges dolgozatban minden ideiglenes fejezetcím és kitöltőszöveg kerüljön ki. A módszertani fejezet válassza külön az adatgyűjtést, az ETL-lépéseket, az adattárház-modellt és a vizualizációt. Minden ábra és táblázat kapjon sorszámot, címet és forrást.

## Etikai és technikai korlátok

API-kulcs, token és személyes adat nem kerülhet Gitbe. Az adatgyűjtés dokumentálja a Spotify API használati feltételeit, az időpontot és a lekérdezési mintát. A popularity nem kezelhető valós idejű hallgatásszámként, ezért a következtetésekben ezt a különbséget világosan jelezni kell.
