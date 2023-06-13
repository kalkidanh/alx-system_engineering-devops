#Script to increase the amount of traffic the server can handle

#increase the user limit on nginx default file
exec { 'nginx-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#nginx restart

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
