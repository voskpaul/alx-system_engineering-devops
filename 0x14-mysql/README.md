## 0x14-mysql
Learning about database infrastructures

### 4-mysql_configuration_primary
My MySQL primary configuration

### 4-mysql_configuration_replica
My MySQL replica configuration

### 5-mysql_backup
A Bash script that generates a MySQL dump and creates a compressed archive out of it.
Requirements:
* The MySQL dump must contain all your MySQL databases
* The MySQL dump must be named backup.sql
* The MySQL dump file has to be compressed to a tar.gz archive
* This archive must have the following name format: day-month-year.tar.gz
* The user to connect to the MySQL database must be root
* The Bash script accepts one argument that is the password used to connect to the MySQL database
