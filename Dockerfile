FROM ubuntu

RUN apt-get update && apt-get install -y ffmpeg python3 python3-pip python3-venv

# Create and activate the virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install required packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Set the entry point
ENTRYPOINT ["python", "main.py"]