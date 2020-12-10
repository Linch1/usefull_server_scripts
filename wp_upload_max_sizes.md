## When wp gives you uplad max size error

- Try this

#### edit .htaccess
```
$ sudo nano /var/www/<wp_folder>/.htaccess
```

add the following lines after `# END WordPress`

```
# END WordPress
php_value post_max_size 256M
php_value upload_max_filesize 256M
```

#### edit php.ini

```
$ sudo nano /etc/php/7.4/apache2/php.ini
```

and change this line
```
upload_max_filesize = 256M
```

#### edit wp-config.php

```
$ sudo nano /var/wp/<wp_folder>/wp-config.php
```
add the following line after `table_prfix`

```
$table_prefix = 'wp_'; 
@ini_set('upload_max_size' , '256M' );
```
