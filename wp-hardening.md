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