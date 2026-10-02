-- 04_verify_schema.sql
USE iplmanagement;

SHOW TABLES;
DESCRIBE teams;
DESCRIBE players;
DESCRIBE matches;

SELECT COUNT(*) AS team_count FROM teams;
SELECT COUNT(*) AS player_count FROM players;
SELECT COUNT(*) AS match_count FROM matches;
