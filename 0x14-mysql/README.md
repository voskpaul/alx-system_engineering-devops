Needed Knowledge What is a primary-replica cluster

MySQL primary replica setup

Build a robust database backup strategy

mysqldump

Learning Objectives What is the main role of a database What is a database replica What is the purpose of a database replica Why database backups need to be stored in different physical locations What operation should you regularly perform to make sure that your database backup strategy actually works Project Requirements Allowed editors: vi, vim, emacs All your files will be interpreted on Ubuntu 16.04 LTS All your files should end with a new line A README.md file, at the root of the folder of the project, is mandatory All your Bash script files must be executable Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error The first line of all your Bash scripts should be exactly #!/usr/bin/env bash The second line of all your Bash scripts should be a comment explaining what is the script doing Installation Guide for mysql 5.7.* First go to site dev.mysql.com and copy the PGP PUBLIC KEY just immediately under the Notice section to your clipboard.

Create a new file in your terminal with a .key extension and paste the PGP PUB KEY copied to clipboard.

Then do the following

$ sudo apt-key add name_of_file.key OK

adding it to the apt repo
$ sudo sh -c 'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list'

updating the apt repo to add the url i added earlier
$ sudo apt-get update

now check your available versions
$ sudo apt-cache policy mysql-server mysql-server: Installed: (none) Candidate: 8.0.31-0ubuntu0.20.04.2 Version table: 8.0.31-0ubuntu0.20.04.2 500 500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages 8.0.31-0ubuntu0.20.04.1 500 500 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages 8.0.19-0ubuntu5 500 500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 Packages 5.7.40-1ubuntu18.04 500 500 http://repo.mysql.com/apt/ubuntu bionic/mysql-5.7 amd64 Packages

Now am installing mysql 5.7.*
$ sudo apt-get install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y Project Task Creating a user and Granting Priviledges in mysql $ mysql -root -p Password: /* Type root password

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

mysql> GRANT GRANT REPLICATION CLIENT ON . TO 'holberton_user'@'localhost';

mysql> FLUSH PRIVILEGES; Creating Database, Tables and adding Data to the Tables -- create a table named nexus6 and add at least one entry to it. -- Make sure that holberton_user has SELECT permissions on your table

CREATE DATABASE IF NOT EXISTS tyrell_corp; -- use the created database USE tyrell_corp; -- create table nexus6 CREATE TABLE IF NOT EXISTS nexus6 ( id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) ); -- Add at least one entry to the table, add a row to the table INSERT INTO nexus6 (name) VALUES ('Leon'); -- Grant SELECT permissions to holberton_user GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

-- Verify if data was added succesfully do mysql> SELECT col_1, col_2 FROM tb_name; Setting Up MySQL Replication First create replication user and grant replication priviledge ( best practice). mysql> CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_pwd';

mysql> GRANT REPLICATION SLAVE ON . TO 'replica_user'@'%'; SELECT user, Repl_slave_priv FROM mysql.user; -- error that occurs for permission add this line GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost'; mysql> FLUSH PRIVILEGES;

-- to verify mysql> SELECT user, Repl_slave_priv FROM mysql.user;

mysql> exit Next up you go to the /etc/mysql/mysql.conf.d/mysqld.cnf and comment the bind address and then add this lines to it

By default we only accept connections from localhost
bind-address = 127.0.0.1
server-id = 1 log_bin = /var/log/mysql/mysql-bin.log binlog_do_db = tyrell_corp Then you enable incoming connection to port 3306 on web-01 and sudo service restart mysql-server sudo ufw allow 3306 $ sudo ufw allow from 3306

$ sudo service mysql restart

mysql> SHOW MASTER STATUS;

+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      154 | tyrell_corp  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+

# Now edit the config file in /etc/mysql/mysql.conf.d/mysqld.cnf and then reload mysql-server on web-02
# our replica server

```bash

server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = tyrell_corp
relay_log = /var/log/mysql/mysql-relay-bin.log

$ sudo service mysql restart
Login to mysql server in replica to configure replication
$ mysql -uroot -p
password:


mysql>
-- our master is web-01 configure its ip
-- log file and log position u can find it from web-01, Type
-- mysql> show master status;
mysql> CHANGE MASTER TO
    -> MASTER_HOST='54.90.12.230',
    -> MASTER_USER='replica_user',
    -> MASTER_PASSWORD='sumaya',
    -> MASTER_LOG_FILE='mysql-bin.000001',
    -> MASTER_LOG_POS=154;

-- Then you start slave
mysql> START SLAVE;
mysql> show slave status\G
Task 5: Mysql backup Requirements: The MySQL dump must contain all your MySQL databases The MySQL dump must be named backup.sql The MySQL dump file has to be compressed to a tar.gz archive This archive must have the following name format: day-month-year.tar.gz The user to connect to the MySQL database must be root The Bash script accepts one argument that is the password used to connect to the MySQL database

mysqldump -u root -p"$1" --all-databases > backup.sql
tar -zcvf "$(date '+%d-%m-%Y').tar.gz" backup.sql
