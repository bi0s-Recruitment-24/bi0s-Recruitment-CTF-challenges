FROM node:14

WORKDIR /home/app
COPY  ./src /home/app/
RUN npm install

EXPOSE 9015

CMD ["npm", "start"]