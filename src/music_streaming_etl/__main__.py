import argparse
import json
from pathlib import Path

from .config import Settings
from .spotify_client import SpotifyClient
from .transform import normalize_tracks


def main() -> None:
    parser = argparse.ArgumentParser(description="Spotify metadata ETL export")
    parser.add_argument("--track-ids", required=True, help="Comma-separated Spotify track IDs")
    parser.add_argument("--output", default="data/tracks.jsonl")
    args = parser.parse_args()

    settings = Settings.from_env()
    settings.validate_spotify()
    track_ids = [value.strip() for value in args.track_ids.split(",") if value.strip()]
    client = SpotifyClient(settings.spotify_client_id, settings.spotify_client_secret)
    tracks = client.get_tracks(track_ids)
    features = client.get_audio_features(track_ids)
    rows = normalize_tracks(tracks, features)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Exported {len(rows)} records to {output}")


if __name__ == "__main__":
    main()
