#Dockerfile
#Student: Simone Verhagen
#Studentnummer: 494729

FROM ubuntu:22.04
FROM python:3.11-slim
WORKDIR /app

#metadata
LABEL maintainer="494729@student.saxion.nl"
LABEL project="2.1 Virtualisatie"

#installatie pakketten
RUN apt-get update && \
    apt-get install -y nginx curl && \
    apt-get clean


#webpagina maken
RUN echo "<h1 style='color:pink; text-align:center;'>Welkom op de webpagina van Simone Verhagen (494729)</h1>" > /var/www/html/index.html

COPY app.py /app/
RUN pip install flask redis

#poort 80 open
EXPOSE 80

EXPOSE 5000

#start nginx
CMD ["nginx", "-g", "daemon off;","python", "app.py"]
