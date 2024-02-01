## 0x0F-load_balancer

### 0-custom_http_response_header
A bash script that configures a brand new Ubuntu machine as below:
* Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
   * The name of the custom HTTP header must be X-Served-By
   * The value of the custom HTTP header must be the hostname of the server Nginx is running on

### 1-install_load_balancer
A bash script that installs and configures HAProxy 

### 2-puppet_custom_http_response_header.pp
A puppet manifest that configures a brand new Ubuntu machine as below:
* Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)
   * The name of the custom HTTP header must be X-Served-By
   * The value of the custom HTTP header must be the hostname of the server Nginx is running on

### Resources
Command for checking that conf file is valid  `haproxy -f /etc/haproxy/haproxy.cfg -c`
https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604.html
