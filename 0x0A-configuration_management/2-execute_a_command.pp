# Puppet code to kill a process

exec { 'Kill':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow'
}
