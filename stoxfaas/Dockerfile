FROM python:2.7

# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN apt-get update \ 
    && apt-get install curl \
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.6.1/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog \
    && apt-get -y remove curl

WORKDIR /root/

COPY index.py           .
COPY requirements.txt   .
RUN pip install -r requirements.txt

COPY function           function

RUN touch ./function/__init__.py

WORKDIR /root/

ENV fprocess="python index.py"
ENV http_proxy="http://10.44.233.217:3128"
ENV https_proxy="http://10.44.233.217:3128"

HEALTHCHECK --interval=1s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
