#base image to run the application
FROM node:current-alpine3.22

#set the working directory
WORKDIR /basic-react-application

#copy the application code to working directory
COPY . /basic-react-application/

#install the node modles
RUN npm install

#expose the port
EXPOSE 3000

#start the application
CMD ["npm", "start"]

# to run this 
#docker build -t basic-react-application:1.0.0 .
#docker run -p 3000:3000 -d basic-react-application:1.0.0