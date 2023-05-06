#Setting up an nginx server using puppet script

package { 'nginx':
	ensure => 'present',
}
execute { 'install':
	command  => 'sudo apt-get update; sudo apt-get -y install nginx',
	provider => shell,
}
execute { 'Hello':
	command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
	provider => shell,
}
excecute {'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.faccebook.com\/;\\n\\t}/" /etc/nginx/sites-available/default':
	provider => shell,
}
excecute { 'run':
	command  => 'sudo service nginx restart',
	provider => shell,
}
