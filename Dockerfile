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