from typing import Any

import requests


class SpotifyClient:
    """Small app-only client for public Spotify catalog metadata."""

    def __init__(self, client_id: str, client_secret: str, timeout: int = 30):
        self.timeout = timeout
        token_response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={"grant_type": "client_credentials"},
            auth=(client_id, client_secret),
            timeout=timeout,
        )
        token_response.raise_for_status()
        self.session = requests.Session()
        self.session.headers.update(
            {"Authorization": f"Bearer {token_response.json()['access_token']}"}
        )

    def get_tracks(self, track_ids: list[str]) -> list[dict[str, Any]]:
        if not track_ids:
            return []
        response = self.session.get(
            "https://api.spotify.com/v1/tracks",
            params={"ids": ",".join(track_ids)},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return [track for track in response.json().get("tracks", []) if track]

    def get_audio_features(self, track_ids: list[str]) -> list[dict[str, Any]]:
        if not track_ids:
            return []
        response = self.session.get(
            "https://api.spotify.com/v1/audio-features",
            params={"ids": ",".join(track_ids)},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return [feature for feature in response.json().get("audio_features", []) if feature]
