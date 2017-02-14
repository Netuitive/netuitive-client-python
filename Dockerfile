FROM python:2-slim

RUN mkdir -p /opt/app/
WORKDIR /opt/app/

RUN ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

ADD requirements.txt /opt/app/
ADD test_requirements.txt /opt/app/

RUN pip install -r /opt/app/requirements.txt
RUN pip install -r /opt/app/test_requirements.txt

ADD . /opt/app/

RUN python setup.py test
RUN python setup.py install

RUN ln -sf /usr/share/zoneinfo/UTC  /etc/localtime

ENV API_URL https://api.app.netuitive.com/ingest
ENV CUSTOM_API_KEY change-me-apikey

CMD python example/example.py
