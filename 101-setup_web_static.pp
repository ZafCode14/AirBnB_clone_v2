# File: setup_web_servers.pp

# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html><body>Test HTML content</body></html>',
}

# Create symbolic link (delete and recreate if it exists)
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
}

# Update Nginx configuration
exec { 'hbnb_static':
  command	=> "sed -i '57i\\n\tlocation \/hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default",
  provider  => 'shell'
}

# Restart Nginx after configuration change
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
