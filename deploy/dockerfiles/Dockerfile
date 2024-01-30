# Stage 1: Install Poetry and export dependencies
FROM python:3.11 as requirements-stage

WORKDIR /tmp

# Install Poetry
RUN pip install poetry==1.1.12

# Copy pyproject.toml and poetry.lock from the local machine to the Docker image
COPY ./pyproject.toml ./poetry.lock* /tmp/

# Copy requirements.txt for debugging purposes
COPY ./requirements.txt /tmp/

# Export dependencies using Poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with=dev || true

# Debugging: Print the content of requirements.txt
RUN cat /tmp/requirements.txt

# Stage 2: Build the final image
FROM python:3.11

# Set the working directory in the Docker image
WORKDIR /code

# Copy the requirements.txt file from the requirements-stage
COPY --from=requirements-stage /tmp/requirements.txt .

# Install additional system dependencies
RUN apt-get update && apt-get install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx

# Debugging: Print the content of requirements.txt in the final image
RUN cat ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Copy the rest of the application code
COPY . .

# Set the entry point for the container
ENTRYPOINT ["sh", "./scripts/launch.sh"]
