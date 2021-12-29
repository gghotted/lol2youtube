FROM python:3.9.2

ADD lol2youtube/requirements.txt /
ADD .secrets /.secrets
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
