# Python 3.6.7

FROM python:3.6.7-alpine3.6

# author of file
LABEL maintainer="Joshua Yeung <joshuayeung@hk.chinamobile.com>"

# Packages that we need
COPY requirement.txt /app/
WORKDIR /app

# instruction to be run during image build
RUN pip install -r requirement.txt

# Copy all the files from current source directory (from your system) to

# Docker container in /app directory
COPY . /app