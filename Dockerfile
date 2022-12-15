# Dockerfile, image,container
FROM python:3.10

ADD main.py .

RUN pip install requests beautifulsoup4

CMD [ "python", "./main.py" ]