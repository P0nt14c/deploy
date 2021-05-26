#!/usr/local/bin/bash

# remove old nginx install
rm -rf /usr/local/etc/nginx/

# kill all nginx processes
pkill nginx

# install build dependencies
pkg install -y libpcre3 libpcre3-dev zlib1g zlib1g-dev openssl libssl-dev libxslt1-dev libgd-dev libgeoip-dev

# if on centos do these
# yum install -y pcre pcre-devel zlib zlib-devel openssl openssl-devel

# pull down nginx
wget https://nginx.org/download/nginx-1.18.0.tar.gz
tar zxf nginx-1.18.0.tar.gz
cd nginx-1.18.0

# add our module as a dependency
./configure --add-module=../ --user=root --with-cc-opt='-I /usr/local/include' --with-ld-opt='-L /usr/local/lib' --conf-path=/usr/local/etc/nginx/nginx.conf --sbin-path=/usr/local/sbin/nginx --pid-path=/var/run/nginx.pid --error-log-path=/var/log/nginx/error.log --user=www --group=www --modules-path=/usr/local/libexec/nginx --with-file-aio --http-client-body-temp-path=/var/tmp/nginx/client_body_temp --http-fastcgi-temp-path=/var/tmp/nginx/fastcgi_temp --http-proxy-temp-path=/var/tmp/nginx/proxy_temp --http-scgi-temp-path=/var/tmp/nginx/scgi_temp --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi_temp --http-log-path=/var/log/nginx/access.log --with-http_v2_module --with-http_addition_module --with-http_auth_request_module --with-http_dav_module --with-http_flv_module --with-http_gunzip_module --with-http_gzip_static_module --with-http_mp4_module --with-http_random_index_module --with-http_realip_module --with-pcre --with-http_secure_link_module --with-http_slice_module --with-http_ssl_module --with-http_stub_status_module --with-http_sub_module --without-mail_imap_module --without-mail_pop3_module --without-mail_smtp_module --with-mail_ssl_module --with-stream_ssl_module --with-stream_ssl_preread_module --with-threads --with-mail=dynamic --with-stream=dynamic

#make and install
make && make install

#clean up
rm -rf nginx-1.18.0/ nginx-1.18.0.tar.gz
