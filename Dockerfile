FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files from local context into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install F5-TTS in editable mode from local folder
RUN pip install -e ./F5-TTS

# Start the handler
CMD ["python", "-u", "handler.py"]
