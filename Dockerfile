FROM python:3.9-bullseye
RUN mkdir /app
COPY /requirements.txt /app/
COPY /workers /app/workers
COPY /main.py /app/main.py
WORKDIR /app
RUN python3 -m pip install -r requirements.txt

ARG CONDUCTOR_AUTH_KEY
ARG CONDUCTOR_AUTH_SECRET
ARG CONDUCTOR_SERVER_URL
ENV CONDUCTOR_AUTH_KEY=${KEY}
ENV CONDUCTOR_AUTH_SECRET=${SECRET}
ENV CONDUCTOR_SERVER_URL=${CONDUCTOR_SERVER_URL}
WORKDIR /app
CMD [ "python3", "main.py" ]
