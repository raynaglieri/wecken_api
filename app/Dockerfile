# Dockerfile for wecken
FROM python:3.8-slim

# Create then copy our application into our application directory
RUN mkdir -p /wecken/app
COPY . /wecken/app
WORKDIR /wecken
# SECTION: PYTHON

# Setting PYTHONUNBUFFERED=TRUE or PYTHONUNBUFFERED=1 allows for log messages to be immediately dumped to the stream instead of being buffered. 
# This is useful for receiving timely log messages and avoiding situations where the application crashes without emitting a relevant message,
# due to the message being "stuck" in a buffer.
ENV PYTHONUNBUFFERED=1

# Python dependencies consists in specifying them in a declarative way in a dedicated text file (requirements.txt)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r app/requirements.txt

