#base image to run the appliction
FROM python:3.13.6

#work directory
WORKDIR /basic-python-application

#copy the application code to work directory
COPY . /basic-python-application/

CMD [ "python", "print-file-content.py" ]