from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    spotify_client_id: str
    spotify_client_secret: str
    bigquery_project_id: str | None
    bigquery_dataset: str

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        return cls(
            spotify_client_id=os.getenv("SPOTIFY_CLIENT_ID", ""),
            spotify_client_secret=os.getenv("SPOTIFY_CLIENT_SECRET", ""),
            bigquery_project_id=os.getenv("BIGQUERY_PROJECT_ID") or None,
            bigquery_dataset=os.getenv("BIGQUERY_DATASET", "music_streaming"),
        )

    def validate_spotify(self) -> None:
        if not self.spotify_client_id or not self.spotify_client_secret:
            raise ValueError(
                "SPOTIFY_CLIENT_ID és SPOTIFY_CLIENT_SECRET beállítása szükséges."
            )
