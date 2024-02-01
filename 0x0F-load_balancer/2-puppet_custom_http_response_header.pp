# Puppet manifest to configure custom responses headers from nginx

exec { 'update':
    command => '/usr/bin/apt-get update -y',
}

package { 'nginx':
    ensure  => installed,
    require => Exec['update']
}

file_line {'addHeader':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $HOSTNAME;',
    require => Package['nginx'],
}

service {'nginx':
    ensure  => running,
    require => Package['nginx'],
}
