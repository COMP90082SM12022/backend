# SERVER

FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

# [START system dependencies]
RUN apk add --update curl gcc g++ \
    && rm -rf /var/cache/apk/*

RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

RUN apk add xvfb-run

RUN apk add sudo

RUN apk add ffmpeg

RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

ENV GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-glibc
ENV GLIBC_VERSION=2.30-r0

RUN set -ex && \
apk --update add libstdc++ curl ca-certificates && \
for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}; \
do curl -sSL ${GLIBC_REPO}/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk; done && \
apk add --allow-untrusted /tmp/*.apk && \
rm -v /tmp/*.apk && \
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib

# [START app environment]

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/


RUN pip install --no-cache-dir -r requirements.txt
COPY . /code/

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000
