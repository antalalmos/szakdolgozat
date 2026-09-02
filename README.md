# Zenei streaming adatelemzés

Ez a repository a **„Zenei streaming szolgáltatások hallgatói trendjeinek elemzése felhőalapú adattárház-architektúrában”** című BSc szakdolgozat megvalósítási alapja.

## Cél

A projekt egy reprodukálható adatfeldolgozási folyamatot mutat be:

`Spotify Web API -> Python ETL -> BigQuery -> Power BI`

A kezdőverzió Spotify track- és audio-feature-metaadatok gyűjtését, ellenőrzését és BigQuery-kompatibilis JSONL exportját készíti elő. A felhasználói azonosítás és személyes hallgatási adatok csak külön, dokumentált engedéllyel kerülhetnek a rendszerbe.

## Gyors indítás

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
python -m music_streaming_etl --help
pytest
```

Az API-hoz Spotify Developer Dashboard alkalmazás szükséges. A `SPOTIFY_CLIENT_ID` és `SPOTIFY_CLIENT_SECRET` értékét csak a lokális `.env` fájlban kell megadni; ez a fájl nincs verziókezelve.

## Könyvtárszerkezet

- `src/music_streaming_etl/`: API-kliens, transzformáció és export
- `sql/schema.sql`: BigQuery-táblák és ajánlott partícionálás
- `docs/THESIS_PLAN.md`: kutatási kérdések, mérföldkövek és szakmai irányok
- `tests/`: determinisztikus egységtesztek

## Példa futtatás

```bash
python -m music_streaming_etl \
  --track-ids 4uLU6hMCjMI75M1A2tKUQC,0VjIjW4GlUZAMYd2vXMi3b \
  --output data/tracks.jsonl
```

A tényleges adatgyűjtés előtt rögzíteni kell az adatfelvétel időpontját, a lekérdezett azonosítókat, a használt API-végpontokat és az esetleges sikertelen kéréseket. Ez biztosítja a dolgozat reprodukálhatóságát.

## Következő lépések

1. A célváltozók és a mintavételi stratégia véglegesítése.
2. Adatgyűjtési napló és mintaadatkészlet hozzáadása.
3. BigQuery dataset létrehozása, majd a séma betöltése.
4. DAX-mutatók és Power BI dashboard elkészítése.
5. Eredmények, korlátok és reprodukálhatósági jegyzőkönyv dokumentálása.
