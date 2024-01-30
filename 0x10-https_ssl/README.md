0-world_wide_web
Learning about SSL termination

0-world_wide_web
A script that will display information about subdomains. It must accept 2 arguments:

domain:
type: string
what: domain name to audit
mandatory: yes
subdomain:
type: string
what: specific subdomain to audit
mandatory: no Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points  to [DESTINATION] When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
1-haproxy_ssl_termination
Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.. Requirements:

HAproxy must be listening on port TCP 443
HAproxy must be accepting SSL traffic
HAproxy must serve encrypted traffic that will return the / of your web server
When querying the root of your domain name, the page returned must contain Holberton School
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
100-redirect_http_to_https
Configure HAproxy to automatically redirect HTTP traffic to HTTPS. Requirements:

This should be transparent to the user
HAproxy should return a 301
HAproxy should redirect HTTP traffic to HTTPS
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg) The file 100-redirect_http_to_https must be your HAproxy configuration file
Resources
https://serversforhackers.com/c/letsencrypt-with-haproxy
