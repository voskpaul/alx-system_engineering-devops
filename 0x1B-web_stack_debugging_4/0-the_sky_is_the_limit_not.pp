# Increase the ULIMIT of the default file from 15 to 5000
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#restart Nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
