from datetime import datetime, timezone
from typing import Any


def normalize_tracks(
    tracks: list[dict[str, Any]], features: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    features_by_id = {item["id"]: item for item in features if item.get("id")}
    collected_at = datetime.now(timezone.utc).isoformat()
    rows = []
    for track in tracks:
        track_id = track.get("id")
        if not track_id:
            continue
        rows.append(
            {
                "track_id": track_id,
                "track_name": track.get("name"),
                "artists": [artist.get("name") for artist in track.get("artists", [])],
                "album_name": (track.get("album") or {}).get("name"),
                "release_date": (track.get("album") or {}).get("release_date"),
                "duration_ms": track.get("duration_ms"),
                "explicit": track.get("explicit"),
                "popularity": track.get("popularity"),
                "audio_features": features_by_id.get(track_id),
                "collected_at": collected_at,
            }
        )
    return rows
