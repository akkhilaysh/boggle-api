FROM python:3.8.2-slim

# define a directory
WORKDIR /app

# copy the contents into the working dir
ADD . /app

# run pip to install the dependencies of the app
RUN pip install -r requirements.txt

EXPOSE 5000

# define the command to start the container
CMD ["python","application.py"]
