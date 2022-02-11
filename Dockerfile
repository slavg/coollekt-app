# pull official base image
FROM python:3.9.6

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apt-get update  && apt-get install postgresql-dev gcc python3-dev musl-dev

# apk add geos libc-dev musl-dev
#yum install libgeos-c1v5 libgeos-3.7.1
#RUN pip install shapely --upgrade


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

RUN pytest
