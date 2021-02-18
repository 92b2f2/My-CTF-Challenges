FROM php:7.4.14-apache-buster

WORKDIR /var/www/
COPY a.py /
COPY web/ /var/www/html/

ENV APACHE_DOCUMENT_ROOT /var/www/html/

RUN apt update -y && \
    apt install -y --no-install-recommends python3

RUN chmod +x /a.py


