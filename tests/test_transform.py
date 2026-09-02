from music_streaming_etl.transform import normalize_tracks


def test_normalize_tracks_joins_audio_features():
    rows = normalize_tracks(
        [{
            "id": "track-1",
            "name": "Example",
            "artists": [{"name": "Artist"}],
            "album": {"name": "Album", "release_date": "2024-01-01"},
            "duration_ms": 180000,
            "explicit": False,
            "popularity": 72,
        }],
        [{"id": "track-1", "energy": 0.8}],
    )

    assert rows[0]["track_id"] == "track-1"
    assert rows[0]["artists"] == ["Artist"]
    assert rows[0]["audio_features"]["energy"] == 0.8
    assert rows[0]["collected_at"].endswith("+00:00")
