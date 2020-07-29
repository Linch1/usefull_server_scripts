- bin/standalone.sh -c standalone-ha.xml -Djboss.socket.binding.port-offset=100

- mvn clean install wildfly:deploy -Djboss-as.home=$KEYCLOAK_HOME -X

# Allow keycloak public access
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


### Allow keycloak to read X-Forwarded-For header
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
