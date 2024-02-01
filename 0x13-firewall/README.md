## 0x13-firewall

### 0-block_all_incoming_traffic_but
Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
* 22 (SSH)
* 443 (HTTPS SSL)
* 80 (HTTP)

### 100-port_forwarding
A copy of the ufw configuration file that you modified to configure web-01
so that its firewall redirects port 8080/TCP to port 80/TCP.
