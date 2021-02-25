# set base image (host OS)
FROM python:3.8

COPY . /app
WORKDIR /app

# install dependencies
RUN pip install flask flask_cors requests

ENTRYPOINT ["python"]
CMD ["app.py"]
