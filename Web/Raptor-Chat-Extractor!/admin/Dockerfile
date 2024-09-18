FROM php:8.2-apache

RUN a2enmod rewrite

RUN mkdir -p /var/log/httpd

COPY . /var/www/html

RUN mv /var/www/html/flag.txt /flag.txt

RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-available/*.conf
ADD apache-config.conf /etc/apache2/sites-available/000-default.conf

EXPOSE 80

CMD ["apache2-foreground"]
