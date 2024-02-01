## 0x0A-configuration_management
Learning configuration management using puppet

### 0-create_a_file.pp
Using Puppet, create a file in `/tmp`.

Requirements:
* File path is `/tmp/holberton`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`

### 1-install_a_package.pp
Using Puppet, install puppet-lint.

Requirements:
* Install `puppet-lint`
* Version must be `2.1.1`

### 2-execute_a_command.pp
Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:
* Must use the `exec` Puppet resource
* Must use `pkill`
