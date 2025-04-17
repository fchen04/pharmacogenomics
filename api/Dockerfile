FROM python:3.11-slim

WORKDIR /apicode

# Install necessary system dependencies for the application
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    pkg-config \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 4000

# Copy API code into container
COPY ./api /appcode

CMD [ "python", "backend_app.py"]

