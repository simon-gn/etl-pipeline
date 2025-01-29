FROM node:18-slim AS build

WORKDIR /client

COPY package.json package-lock.json /client/
RUN npm install
COPY . /client
RUN npm run build

FROM nginx:alpine

RUN rm -rf /usr/share/nginx/html/*

COPY --from=build /client/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]