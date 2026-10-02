-- 01_create_db_and_user.sql
CREATE DATABASE IF NOT EXISTS iplmanagement CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Optional: dedicated app user (recommended)
CREATE USER IF NOT EXISTS 'ipl_user'@'localhost' IDENTIFIED BY 'ipl_password_change_me';
GRANT ALL PRIVILEGES ON iplmanagement.* TO 'ipl_user'@'localhost';
FLUSH PRIVILEGES;
