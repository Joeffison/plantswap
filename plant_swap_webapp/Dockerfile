FROM node:19.7.0-slim AS build-step

WORKDIR /app

COPY package.json .
COPY yarn.lock .

# install the dependencies using the exact versions in the lockfile
RUN yarn install --frozen-lockfile

COPY . .

ARG REACT_APP_PLANT_SWAP_API
ENV REACT_APP_PLANT_SWAP_API=$REACT_APP_PLANT_SWAP_API

RUN yarn build

CMD [ "npx", "serve", "build" ]


FROM nginx:stable-alpine
COPY --from=build-step /app/build /usr/share/nginx/html
COPY ./deplyoment/nginx.default.conf /etc/nginx/conf.d/default.conf
