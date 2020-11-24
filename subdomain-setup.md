Per aggiungere un sottodominio bisogna

- aggiungere un _Record sintetico_ nella sezione _DNS_ di google domains che punta all'ip del server
- Aggiungere questi due A record per il sottodominio nela sezione DNS di digitalocean che puntano all'ip del server
  - subdomain.domain.com
  - www.subdomain.domain.com
- Aspettare che il dns si aggiorna ( 24-48 h )
- Creare una configurazione VirtualHost di apache che punta alla directory /var/www/subdomain ( o qualsiasi cartella contnenete i file del sito )
- si puo anche far partire certbot sul sottodominio per avere l'ssl
