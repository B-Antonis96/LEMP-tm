FROM node:alpine as build-stage
WORKDIR /app
ENV REACT_APP_NAME="LEMP App"
ENV REACT_APP_TITLE="Welkom bij mijn eindopdracht!"
ENV REACT_APP_BACKEND="localhost:8000"
COPY frontend/package.json ./
COPY frontend/package-lock.json ./
COPY frontend ./
RUN npm install
RUN npm run build

FROM nginx:1.22.1
COPY --from=build-stage /app/build/ /var/www/html