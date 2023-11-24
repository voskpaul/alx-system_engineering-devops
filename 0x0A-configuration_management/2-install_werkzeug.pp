# File: 2-install_werkzeug.pp

# Puppet manifest to install Werkzeug using pip3

# Install Werkzeug version 2.1.1
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
