FROM alpine 
RUN apk --update add py3-pip && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/* && \
    pip3 install kubernetes
COPY ./watch.py /
CMD [ "/usr/bin/python3", "/watch.py" ]
