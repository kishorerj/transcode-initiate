
   
# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Copy local code to the container image.
ENV APP_HOME /transcode
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --upgrade -r requirements.txt

# Run the web service on container startup. 
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --chdir transcode app:app
