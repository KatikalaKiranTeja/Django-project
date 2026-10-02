-- 02_schema_fresh.sql
USE iplmanagement;

CREATE TABLE IF NOT EXISTS teams (
    teamCode VARCHAR(10) PRIMARY KEY,
    teamName VARCHAR(100) NOT NULL,
    country VARCHAR(50) NOT NULL DEFAULT 'India',
    coachName VARCHAR(100) NOT NULL,
    captainName VARCHAR(100) NOT NULL,
    logoPath VARCHAR(255) NULL
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS players (
    jerseyNumber INT NOT NULL,
    playerName VARCHAR(120) NOT NULL,
    age INT NOT NULL,
    role VARCHAR(80) NOT NULL,
    nationality VARCHAR(80) NOT NULL,
    teamCode VARCHAR(10) NOT NULL,
    imagePath VARCHAR(255) NULL,
    PRIMARY KEY (jerseyNumber, teamCode),
    CONSTRAINT fk_players_team FOREIGN KEY (teamCode)
        REFERENCES teams(teamCode)
        ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS matches (
    match_id INT PRIMARY KEY,
    match_date DATE NULL,
    match_time TIME NULL,
    team1_code VARCHAR(10) NULL,
    team2_code VARCHAR(10) NULL,
    venue VARCHAR(120) NULL,
    status VARCHAR(30) NOT NULL,
    winner_code VARCHAR(10) NULL,
    team1_score VARCHAR(60) NULL,
    team2_score VARCHAR(60) NULL,
    player_of_match VARCHAR(120) NULL,
    CONSTRAINT fk_matches_team1 FOREIGN KEY (team1_code)
        REFERENCES teams(teamCode)
        ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT fk_matches_team2 FOREIGN KEY (team2_code)
        REFERENCES teams(teamCode)
        ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT fk_matches_winner FOREIGN KEY (winner_code)
        REFERENCES teams(teamCode)
        ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT chk_match_status CHECK (LOWER(status) IN ('upcoming','completed','running'))
) ENGINE=InnoDB;

CREATE INDEX idx_players_team ON players(teamCode);
CREATE INDEX idx_matches_status ON matches(status);
CREATE INDEX idx_matches_date ON matches(match_date);
