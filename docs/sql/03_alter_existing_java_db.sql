-- 03_alter_existing_java_db.sql
USE iplmanagement;

-- Ensure player_of_match exists because Django version writes this field.
ALTER TABLE matches
    ADD COLUMN IF NOT EXISTS player_of_match VARCHAR(120) NULL;

-- Normalize status values to lowercase for consistency.
UPDATE matches SET status = LOWER(status) WHERE status IS NOT NULL;

-- Ensure score columns exist (some legacy variants may differ)
ALTER TABLE matches
    ADD COLUMN IF NOT EXISTS team1_score VARCHAR(60) NULL,
    ADD COLUMN IF NOT EXISTS team2_score VARCHAR(60) NULL;
