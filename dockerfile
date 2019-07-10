# Python 3.7.4

FROM python:3.7.4

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

# Specifies a command that will always be executed when the container starts.
# In this case we want to start the python interpreter

ENTRYPOINT ["python"]

# We want to start app.py file. (change it with your file name)

# Argument to python command
CMD ["app.py"]