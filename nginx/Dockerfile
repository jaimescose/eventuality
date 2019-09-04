FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/eventuality.conf /etc/nginx/conf.d/
COPY nginx/upstreams.conf /etc/nginx/conf.d/
