## 0x0B-ssh
Learning about ssh keys

### 0-use_a_private_key
Bash script that uses ssh to connect to your server using the private key `~/.ssh/holberton` with the user `ubuntu`.
Requirements:
* Only use `ssh` single-character flags
* You cannot use `-l`
* You do not need to handle the case of a private key protected by a passphrase

### 1-create_ssh_key_pair
A Bash script that creates an RSA key pair.
Requirements:
* Name of the created private key must be holberton
* Number of bits in the created key to be created 4096
* The created key must be protected by the passphrase betty

### 2-ssh_config
An ssh configuration file with the following requirements:
* Your SSH client configuration must be configured to use the private key ~/.ssh/holberton
* Your SSH client configuration must be configured to refuse to authenticate using a password
