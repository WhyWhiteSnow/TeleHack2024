FROM node:20.8.1

WORKDIR /app

RUN npm install -g http-server

COPY package.json /app
COPY package-lock.json /app

RUN npm install

COPY . .

RUN npm run build