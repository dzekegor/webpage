# our base image
FROM alpine:3.7

# Install python and pip
RUN apk add --update py3-pip

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/webpage/
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r /usr/src/webpage/requirements.txt
WORKDIR /usr/src/webpage
# copy files required for the app to run
COPY ./ ./

# tell the port number the container should expose
EXPOSE 8080

# run the application
CMD python3 /usr/src/webpage/serv.py
