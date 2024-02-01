## 0x09-web_infrastructure_design
Learning about Web Infrastructure

### 0-simple_web_stack
On a whiteboard, design a one server web infrastructure that hosts the website  
that is reachable via www.foobar.com. Start your explanation by having a user  
wanting to access your website.

Requirements:
* You must use:
	* 1 server
	* 1 web server (Nginx)
	* 1 application server
	* 1 application files (your code base)
	* 1 database (MySQL)
	* 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

### 1-distributed_web_infrastructure
On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.
Requirements:
* You must add:
	* 2 servers
	* 1 web server (Nginx)
	* 1 application server
	* 1 load-balancer (HAproxy)
	* 1 set of application files (your code base)
	* 1 database (MySQL)


### 2-secured_and_monitored_web_infrastructure
On a whiteboard, design a three server web infrastructure that hosts the website  
www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
Requirements:
* You must add:
	* 3 firewalls
	* 1 SSL certificate to serve www.foobar.com over HTTPS
	* 3 monitoring clients (data collector for Sumologic or other monitoring services)
