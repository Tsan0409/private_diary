FROM python:3.9
ENV PYTHONNUMBERFUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/

# postgresqlのインストール
RUN apt-get install libpq-dev
# インストール可能なパッケージ一覧を更新する
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN pip install -r requirements.txt
COPY . /code/


# CMD ["python", "manage.py", "runserver"]
