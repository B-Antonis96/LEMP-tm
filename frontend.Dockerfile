FROM node:alpine as build-stage
WORKDIR /app
ARG REACT_APP_NAME
ARG REACT_APP_TITLE
ARG REACT_APP_BACKEND
COPY frontend ./
RUN npm install
RUN npm run build

FROM nginx:1.22.1
COPY --from=build-stage /app/build/ /var/www/html