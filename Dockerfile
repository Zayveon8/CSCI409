FROM python:3.12-alpine3.19
LABEL maintainer="Robert Evans"

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Copy requirements files and application code
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./api /api

# Set working directory
WORKDIR /api 

# Expose port 8000
EXPOSE 8000

# Define build argument for development mode
ARG DEV=false

# Install dependencies and set up environment
RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser -D django-user

# Set the PATH to include Python binaries
ENV PATH="/py/bin:$PATH"

# Set the user for subsequent commands
USER django-user

# Default command to run the server
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
