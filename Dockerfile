# Use the official Python image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install selenium webdriver-manager

# Install Chrome & ChromeDriver for Selenium
# Install Chrome & ChromeDriver inside Docker
RUN apt-get update && apt-get install -y \
    wget unzip \
    && wget -qO- https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb > chrome.deb \
    && apt install -y ./chrome.deb \
    && rm chrome.deb \
    && wget -qO- https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip > chromedriver.zip \
    && unzip chromedriver.zip -d /usr/local/bin/ \
    && rm chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver


# Expose Flask's default port
EXPOSE 5000

# Run the Flask application
CMD ["python", "awslogin.py"]
