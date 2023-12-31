-- Create a MySQL user named holberton_user with hostname localhost
-- and password projectcorrection280hbtn
-- holberton_user has permission to check the primary/replica status of  database

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
