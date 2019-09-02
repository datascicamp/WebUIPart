# Source Image
FROM python:3.7
# Author
MAINTAINER Leon "leontian1024@gmail.com"
# Set working director
WORKDIR /var/app/webServerDir
# Add source code from os into container
Add . /var/app/webServerDir
# Import packages
RUN pip install Flask
RUN pip install Flask-wtf
RUN pip install psycopg2-binary
RUN pip install flask-sqlalchemy
RUN pip install flask-migrate
RUN pip install pyjwt
RUN pip install flask_bootstrap
RUN pip install python-dotenv
# Expose port
EXPOSE 5000
# Run command
ENTRYPOINT ["python","./webServer.py"]

