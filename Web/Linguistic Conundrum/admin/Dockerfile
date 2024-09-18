FROM node:20-bullseye-slim

RUN useradd --user-group --system --create-home --no-log-init app

USER app

WORKDIR /home/app

COPY --chown=app:app ./src/package.json /home/app

RUN npm install

COPY --chown=app:app ./src /home/app

COPY --chown=app:app ./src/public/fake_error.log /var/log/apache2/error.log

ENV FLAG="WE_W1N_7H3S3"
EXPOSE 3000

CMD ["npm", "start"]
