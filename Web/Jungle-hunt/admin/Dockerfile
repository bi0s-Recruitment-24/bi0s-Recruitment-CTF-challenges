FROM node:16-buster-slim

WORKDIR /app

COPY package.json /app

RUN npm install --global

COPY . /app

EXPOSE 1337

CMD ["npm", "start"]