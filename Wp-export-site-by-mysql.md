### Export Wordpress using Mysql

1. Export the Database of the wordpress website using one of the below commands 
```
mysqldump -p -u username database_name > dbname.sql
```
```
sudo mysqldump database_name > dbname.sql
```

2. Export wordpress medias ( use filezilla or ssh ) You have to download the path **/var/www/path/to/wordpress/wp-content/uploads** ( or the interested sub-directories )

3. Open the dbname.sql and replace all the occurences of `https://oldDomain.com/wordpress-path`( `http://localhost/wordpress-path` if in local development ) with  `https://myNewDomain.com/wordpress-path`
 
4. connect to your server and import the `dbname.sql` file
5. use the `dbname.sql` to import the wordpress datas  using one of the below commands 

```
mysql -p -u username database_name < file.sql 
```
```
sudo mysql database_name < file.sql 
```

5. replace the **/var/www/path/to/wordpress/wp-content/uploads** ( or the interested sub-directories ) folder in the server with the one that you toke before
