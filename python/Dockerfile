#base image to run the appliction
FROM python:3.13.6

#work directory
WORKDIR /basic-python-application

#copy the application code to work directory
COPY . /basic-python-application/

CMD [ "python", "print-file-content.py" ]

#to run this
#docker build -t basic-python-application:1.0.0 .
#docker run -d -it basic-python-application:1.0.0

#to run with mount file from local
#docker run -d -it -v C:\Users\Sid\Learning\Frontend\learning-react\python\servers.txt:/basic-python-application/servers.txt basic-python-application:1.0.0