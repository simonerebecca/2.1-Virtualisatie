#Dockerfile
#Student: Simone Verhagen
#Studentnummer: 494729

FROM python:3.11-slim
WORKDIR /app

COPY app.py /app/
RUN pip install flask redis

EXPOSE 5000
CMD ["python", "app.py"]

