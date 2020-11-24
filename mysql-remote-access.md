#MYSQL REMOTE ACCESS
_use the following steps to configure the remote acces on mysql_

- Create the remote user
```
sudo mysql
CREATE USER 'myuser'@'localhost' IDENTIFIED BY 'mypass';
CREATE USER 'myuser'@'%' IDENTIFIED BY 'mypass';
GRANT ALL ON *.* TO 'myuser'@'localhost';
GRANT ALL ON *.* TO 'myuser'@'%';
flush privileges;
```

- Allow mysql external connections
```
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
```
In the nano editor chenge the following line
bind-address            = 127.0.0.1 --> **bind-address            = 0.0.0.0**

- Allow Server external connections on mysql port ( default: 3306 )
```
sudo ufw allow 3306
```
