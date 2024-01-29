# Add a custom HTTP header with Puppet

exec { 'command':
  command  => 'apt-get --yes update;
  apt-get --yes install nginx;
  sudo sed --in-place "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  service nginx restart',
  provider => shell,
}
