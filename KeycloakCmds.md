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

