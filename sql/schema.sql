-- BigQuery starter schema. Replace PROJECT_ID and DATASET before execution.
CREATE TABLE IF NOT EXISTS `PROJECT_ID.DATASET.tracks_snapshot` (
  track_id STRING NOT NULL,
  track_name STRING,
  artists ARRAY<STRING>,
  album_name STRING,
  release_date STRING,
  duration_ms INT64,
  explicit BOOL,
  popularity INT64,
  audio_features JSON,
  collected_at TIMESTAMP NOT NULL
)
PARTITION BY DATE(collected_at)
CLUSTER BY track_id;
