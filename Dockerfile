FROM python:3.11-slim-bullseye
LABEL maintainer="Branko Milosavljevic <mbranko@uns.ac.rs>"
RUN apt-get -y update
RUN apt-get -y install gcc libmariadb-dev-compat graphviz-dev libffi-dev libmagic1 libtiff-dev libopenjp2-7-dev liblcms-dev zlib1g-dev libjpeg-dev musl-dev
RUN /usr/local/bin/python3 -m pip install --upgrade pip
RUN pip3 install -U setuptools
COPY requirements2.txt /app/requirements2.txt
RUN pip3 install -r /app/requirements2.txt
COPY . /app
RUN mkdir -p /app/staticfiles
WORKDIR /app
RUN mkdir /private
RUN touch /private/secrets
RUN rm -rf /app/log
RUN mkdir /app/log
ARG django_settings=prod
ENV DJANGO_SETTINGS=$django_settings
RUN python3 /app/manage.py collectstatic --noinput
RUN rm -rf /app/log/*
RUN rm -rf /private
RUN chmod +x /app/run_prod.sh
EXPOSE 8000
ENTRYPOINT ["/app/run_prod.sh"]
