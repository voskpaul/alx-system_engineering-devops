#!/usr/bin/env bash
# Using Puppet to change our server configuration files
# Configure SSH to use the private key ~/.ssh/school for authentication
echo -e "file { '/etc/ssh/ssh_config':\n  ensure  => present,\n  content => \"    IdentityFile ~/.ssh/school\n    PasswordAuthentication no\"\n}" > 100-puppet_ssh_config.pp

