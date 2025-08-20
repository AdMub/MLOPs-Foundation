# FROM python:3.10-slim

# COPY . /app

# WORKDIR /app

# RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "app.py"]

FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy only requirements first (so caching works better)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy your app code
COPY . .

CMD ["python", "app.py"]
