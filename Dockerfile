# FROM python:3.9
# ENV PYTHONUNBUFFERED 1
# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/

# # postgresqlのインストール
# RUN apt-get install libpq-dev
# # インストール可能なパッケージ一覧を更新する
# RUN ["apt-get", "update"]
# RUN ["apt-get", "install", "-y", "vim"]
# RUN pip install -r requirements.txt
# COPY . /code/

FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

# インストール可能なパッケージ一覧を更新する
RUN apt-get update && \
    apt-get install -y libpq-dev vim

RUN pip install -r requirements.txt
COPY . /code/

