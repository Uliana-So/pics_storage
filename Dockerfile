FROM    python:3.8

WORKDIR /opt/django_project/

RUN     mkdir static && \
        mkdir media

COPY    ./django_project/ .

RUN     pip install --upgrade pip && \
        pip install --no-cache-dir -r requirements.txt

CMD     ["tail", "-f", "/dev/null"]