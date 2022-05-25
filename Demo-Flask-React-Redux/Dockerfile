FROM node:16.13.0-alpine
WORKDIR /core
ENV PATH="./node_modules/.bin:$PATH"

COPY . .
RUN npm run build


