# Getting started

- For start with keycloak cehck this guides
	- [Introduction to keycloak](https://www.thomasvitale.com/introducing-keycloak-identity-access-management/)
	- [Base setup of keycloak](https://www.thomasvitale.com/keycloak-configuration-authentication-authorisation/)
	
(-Djboss.socket.binding.port-offset=100)
	
#### Invalid redirect uri

If when you try to log to your app using keycloak appears the error **Invalid parameter: redirect_uri**
- Go to keycloak console
- Check the _WARNING_ message of the invalid redirect and take the **redirect_uri** attribute _value_ ( it should be the last message if no other operationg have been done )
	- Usually in localhost ( if it happens on the login attempt ) the url should be **http://localhost:8080/sso/login**
- go to keycloak admin panel
- Open the app client
- add the url that you toke in the **Valid Redirect URIs** field.

# Add roles

### Add role
1. go to keycloak admin panel
2. Select the wanted realm
3. Go to roles
4. Click add role
5. Specify the role name and save it

### Add composite role
This allow to create a role that implicitly contains the permissions of other roles too
1. Once that you have saved te role check the _COMPOSITE ROLE_ field
2. Add the roles that you want
3. Now the role that you have created have also the other role permissions 

### Default roles on user creation
1. go to keycloak admin panel
2. Select the wanted realm
3. Go to roles
4. Go to _DEFAULT ROLES_
5. add the roles that you want
6. From now all the newly created users will have the specified roles

# Deploy custom user storage spi

#### Before deploying

- Check that you have added the file **resources/META-INF/services/org.keycloak.storage.UserStorageProviderFactory** inside **resources/META-INF/services** ( create them if not present) that contains the Factory qualified name. Ex:
```
unoone.storage.main.DemoUserStorageProviderFactory
```

- If it has external dependencies not included in keycloak deploy it as an ear.

#### Deployment

- Run the keycloak server **bin/standalone.sh -c standalone.xml**
- Go to the project folder in the terminal and type the cmd: **mvn clean install wildfly:deploy -X**
- For a project example view [this demo](https://github.com/Linch1/Keycloak-user-storage-demo-mysql) that implements keycloak storage with mysql


# Allow keycloak public access
- DOC: https://www.keycloak.org/docs/latest/server_installation/index.html#_setting-up-a-load-balancer-or-proxy
- edit *standalone-ha.xml* or *standalone.xml* following lines

**Replace this**
```
<interface name="management">
	<inet-address value="${jboss.bind.address.management:127.0.0.1}"/>
</interface>
<interface name="public">
	<inet-address value="${jboss.bind.address:0.0.0.0}"/>
</interface>
```

**with this**
```
<interface name="management">
	<any-address/>
</interface>
<interface name="public">
	<any-address/>
</interface>
```

# Setup keycloak behind reverse proxy

- Configure your reverse proxy or loadbalancer to properly set X-Forwarded-For and X-Forwarded-Proto HTTP headers.
- Configure your reverse proxy or loadbalancer to preserve the original 'Host' HTTP header.
- Configure the authentication server to read the client’s IP address from X-Forwarded-For header.


#### Allow keycloak to read X-Forwarded-For header ( HTTP ) 
- open up the profile configuration file (*standalone.xml*, *standalone-ha.xml*, or *domain.xml* ) and add **proxy-address-forwarding=true** attribute to **http-listener**
```
<subsystem xmlns="urn:jboss:domain:undertow:10.0">
   <buffer-cache name="default"/>
   <server name="default-server">
      <ajp-listener name="ajp" socket-binding="ajp"/>
      <http-listener name="default" socket-binding="http" redirect-socket="https"
          proxy-address-forwarding="true"/>
      ...
   </server>
   ...
</subsystem>
```

#### Enable HTTPS/SSL with a Reverse Proxy

- Add the **redirect-socket** attribute to the **http-listener** element
```
<subsystem xmlns="urn:jboss:domain:undertow:10.0">
    ...
    <http-listener name="default" socket-binding="http"
        proxy-address-forwarding="true" redirect-socket="proxy-https"/>
    ...
</subsystem>
```

- Then add a new **socket-binding** element to the **socket-binding-group** element:
```
<socket-binding-group name="standard-sockets" default-interface="public"
    port-offset="${jboss.socket.binding.port-offset:0}">
    ...
    <socket-binding name="proxy-https" port="443"/>
    ...
</socket-binding-group>
```

#### VERIFY THE CONFIGURATION

- go to **/auth/realms/master/.well-known/openid-configuration** ( _ex: ttps://myDomain.com/auth/realms/master/.well-known/openid-configuration_). This will show a JSON document listing a number of endpoints for Keycloak. Make sure the endpoints starts with the address (scheme, domain and port) of your reverse proxy or load balancer. By doing this you make sure that Keycloak is using the correct endpoint.


- verify that Keycloak sees the correct source IP address for requests. To check this, you can try to login to the admin console with an invalid username and/or password and check the keyloak logs on the server, check that the value of **ipAddress** is the IP address of the machine you tried to login
```
08:14:21,287 WARN  XNIO-1 task-45 [org.keycloak.events] type=LOGIN_ERROR, realmId=master, clientId=security-admin-console, userId=8f20d7ba-4974-4811-a695-242c8fbd1bf8, ipAddress=X.X.X.X, error=invalid_user_credentials, auth_method=openid-connect, auth_type=code, redirect_uri=http://localhost:8080/auth/admin/master/console/?redirect_fragment=%2Frealms%2Fmaster%2Fevents-settings, code_id=a3d48b67-a439-4546-b992-e93311d6493e, username=admin
```
