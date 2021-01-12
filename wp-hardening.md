### Disable Wp Api if not needed

Add the following code in your `functions.php`

```
/******************** 
DISABLE API
*/
add_filter ('json_enabled', '__return_false');
add_filter ('json_jsonp_enabled', '__return_false');
```

### Restict files `.htaccess` and `wp-config.php`
Add the following code at the end of the `.htaccess`

```
<Files wp-config.php>
order allow,deny
deny from all
</Files>
```
```
<Files ~ "^.*\.([Hh][Tt][Aa])">
order allow,deny
deny from all
</Files>

```

### Move the `wp-config.php` out of the wp directory

just move the `wp-config.php` one level above the wordpress installation and wp will detect it automatically.
If you get some error reloading the site maybe is for wrong `wp-config.php` file permissions

### Restrict ips
Add the following code at the end of the `.htaccess`
```
<Limit GET POST PUT>
order allow,deny
allow from all
deny from 52.90.97.162
deny from xxx.xxxx.xxx.xxx
</Limit>
```
