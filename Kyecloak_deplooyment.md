Allora inanzitutto ti puoi vedere questo file che ho scritto https://github.com/Linch1/usefull_server_scripts/blob/master/Keycloak.md.
La parte getting started del documento riporta a due guide di base sull' installazione di keycloak e la crazione dei realm e dei client che servono a fare comunicare le  app con keycloak.
Tu dovrai creare un realm con nome Realm e un client per comunicare con l'app con nome Realm-app .
Probabilmente quando li farai partire tutti e due avrai un conflitto di porte che puoi risolvere aggiungendo l'attributo -Djboss.socket.binding.port-offset=100 che fa partire keycloak sulla porta 8180 ( questa e' quella che ho usato nei parametri di configurazione di keycloak nelle file properties ).
Dopo di cio' ti devi creare i ruoli USER, ADMIN, SUPER_ADMIN nel realm di Realm e aggiungere come ruolo di default il ruolo USER.
Ora che hai creato i ruoli puo andare nella sezione users e creare un utente. Una volta dalvato l'utente avra' come ruolo di default USER, dal suo pannello di configurazione se vai in Role mappings puoi aggiungergli anche gli altri ruoli.
Ora se fai partire l'applicazione dovrebbe richiederti di fare il login e se ti loggi con l'utente ( a cui hai dato il ruolo Admin o Super_admin ) potrai accedere alle rispettive zone abilitate.
Una volta che hai fatto questa prima parte e hai verificato che tutto funziona dovrai scaricarti questa repo https://github.com/Linch1/mysql-keycloak-storage-spi.
Nel readme della repo ci sta scritto come deployarlo su keycloak.
Praticamente serve a far leggere a keycloak gli utenti dal db di mysql. Tecnicamente le impostazioni che ho usato io sono uguali alle tue quindi non gli dovresti modificare nulla ma solo deployarlo.
Io ho avuto difficolta ha deployarlo tramite eclipse, mi dava errori di mancanza di dipendenze che in realta ci stavano e alla fine ho usato il terminale.
Deployato su keycloak il pacchetto dovrai andare di nuovo nel realm UNoone > User federation e nel pannello dovrebbe comparire mysql-mysql-storage , seleziona quella e verifica che funzioni andando su utenti > view all users , da questo pannello dovresti leggere un utente con nick_name = stefano.deangelis@unoone.it (edited) 
