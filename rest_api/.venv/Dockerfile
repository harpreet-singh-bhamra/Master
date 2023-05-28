FROM python:3.11.3
EXPOSE 5000
WORKDIR /rest_api
RUN pip install flask
COPY . /rest_api
CMD ["flask", "run", "--host", "0.0.0.0"]