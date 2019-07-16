FROM kbase/sdkbase2:python
MAINTAINER KBase Developer

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module
RUN make all
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
EXPOSE 5000
CMD [ ]
