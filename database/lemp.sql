----------------------
--< DB User config >--
----------------------
-- CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'insecure';
-- SET PASSWORD FOR root@localhost = PASSWORD('insecure');
-- GRANT ALL ON *.* TO root@localhost WITH GRANT OPTION;
-- CREATE USER IF NOT EXISTS root@'%' IDENTIFIED BY 'insecure';
-- SET PASSWORD FOR root@'%' = PASSWORD('insecure');
-- GRANT ALL ON *.* TO root@'%' WITH GRANT OPTION;

CREATE USER IF NOT EXISTS lemp@localhost IDENTIFIED BY 'lemp';
SET PASSWORD FOR lemp@localhost = PASSWORD('lemp');
GRANT ALL ON lemp.* TO lemp@localhost;
CREATE USER IF NOT EXISTS lemp@'%' IDENTIFIED BY 'lemp';
SET PASSWORD FOR lemp@'%' = PASSWORD('lemp');
GRANT ALL ON lemp.* TO lemp@'%';

FLUSH PRIVILEGES;

-----------------------
--< DB Table config >--
-----------------------
CREATE DATABASE IF NOT EXISTS lemp;
USE lemp
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(255),
    text TEXT
);
INSERT INTO messages (sender, text)
VALUES ('', 'Bryan Antonis');
