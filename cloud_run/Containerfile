FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN sample_auth create-db
RUN sample_auth populate-db
RUN sample_auth add-user -u admin -p admin
EXPOSE 5000
CMD ["sample_auth", "run"]
