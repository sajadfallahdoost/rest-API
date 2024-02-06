FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.5.1  

WORKDIR /code

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Copy only the necessary files for installing dependencies
COPY pyproject.toml poetry.lock* /code/

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of your application code
COPY . /code/

EXPOSE 8000

# Copy the entrypoint script into the container
COPY entrypoint.sh /code/entrypoint.sh

# Give execution rights on the entrypoint script
RUN chmod +x /code/entrypoint.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["/code/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
