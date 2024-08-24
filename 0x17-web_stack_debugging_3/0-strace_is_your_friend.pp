# 0-strace_is_your_friend.pp
# A fix for why Apache is returning a 500 error

exec { 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php':
  path => '/usr/bin:/usr/sbin:/bin',
}
-> exec {'restart service':
  command => '/usr/sbin/service apache2 restart',
}
