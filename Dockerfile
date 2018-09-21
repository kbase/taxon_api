FROM kbase/kbase:sdkbase2.latest
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

# RUN apt-get update

# -----------------------------------------


#RUN pip install --upgrade ndg-httpsclient
RUN pip install cffi ndg-httpsclient pyopenssl==17.03 cryptography==2.0.3 --upgrade \
    && pip install pyasn1 --upgrade \
    && pip install requests --upgrade \
    && pip install 'requests[security]' --upgrade


#RUN mkdir -p /kb/module && \
#    cd /kb/module && \
#    git clone https://github.com/kbase/data_api -b 0.4.0-dev && \
#    mkdir lib/ && \
#    cp -a data_api/lib/doekbase lib/

#RUN pip install -r //kb/module/data_api/requirements.txt

RUN pip install functools32

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

EXPOSE 5000

CMD [ ]
