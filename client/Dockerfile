FROM node:18-slim

WORKDIR /client  

COPY package.json package-lock.json /client/

RUN npm install

COPY . /client

EXPOSE 5173

CMD ["npm", "run", "dev"]
