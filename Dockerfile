# syntax=docker/dockerfile:1.7
FROM alpine:3.20 as app
LABEL maintainer="shiishiji.dev@gmail.com"

# Install python
RUN apk add --no-cache py3-pip python3

WORKDIR /srv/wog

# Install dependencies first to prevent reinstallation after source code changes
COPY requirements.txt .
RUN pip install -r requirements.txt --break-system-packages

# Define volumes
VOLUME /srv/wog
VOLUME /srv/wog/scoring/storage

# Copy files
# Using --link allows to reuse already built layers in subsequent builds with --cache-from even if the previous layers have changed.
COPY --link games ./games
COPY --link menu ./menu
COPY --link scoring ./scoring
COPY --link utils ./utils
COPY --link app.py .
COPY --link cli.py .

