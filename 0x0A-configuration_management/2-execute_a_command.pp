# create a manifest that kills a process using exec
exec { 'pkill killmenow':
  path => '/usr/bin';
}
