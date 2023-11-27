# This Puppet manifest installs and configures Nginx web server on an Ubuntu machine.

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;
    server_name _;

    location / {
        return 301 http://\$host/redirect_me;
    }

    location /redirect_me {
        return 200 'Hello World!';
    }
}
",
  notify  => Service['nginx'],
}

# Create symbolic link to enable the default site
file { '/etc/nginx/sites-enabled/000-default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  hasrestart => true,
}

