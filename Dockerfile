FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install F5-TTS in editable mode (from local copy)
RUN pip install -e ./F5-TTS

# Start the handler
CMD ["python", "-u", "handler.py"]
