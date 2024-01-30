# Fix problem of too many files opened
exec {'holberton hard nofile 5':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 5/nofile 500/" /etc/security/limits.conf',
}

exec {'holberton soft nofile 4':
  provider => shell,
  command  => 'sudo sed -i "s/nofile 4/nofile 400/" /etc/security/limits.conf',
}
