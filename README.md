# AWS APP RUNNER 

# Simple HTTP Server with AWS App Runner

This is a sample Python application using `http.server` that serves the content of the current directory as a basic HTML page. The project is designed for deployment on AWS App Runner to simplify the process of hosting this application in the cloud.

## Overview

This project demonstrates a simple Python web server that serves the contents of a directory (HTML files or other static files) over HTTP. It is designed to be deployed on AWS App Runner, making it a convenient way to run containerized applications with minimal setup.

## Prerequisites

Before you begin, make sure you have:

- **AWS CLI**: The AWS Command Line Interface installed and configured.
- **Docker**: Installed if you plan to build a container image locally.
- **AWS Account**: With permissions to create and manage App Runner services.

## Application Logic

The core application uses Python’s built-in `http.server` module, which provides a simple HTTP server that can serve files from the local file system. It uses the following components:

- `SimpleHTTPRequestHandler`: Serves files from a directory over HTTP.
- `HTTPServer`: Creates the server to listen for requests on a specific port.

When a request is made to the server, the `SimpleHTTPRequestHandler` fetches files from the current directory and serves them. The server is designed to run on port `8080` by default, which aligns with AWS App Runner's default port configuration.

## Code Explanation

Here’s a breakdown of the Python code in `app.py`:

```python
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Custom handler that serves files from the current directory
class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        # Set the directory to the current directory ('.')
        super().__init__(*args, directory='.', **kwargs)

# Function to start the HTTP server
def run(server_class=HTTPServer, handler_class=CustomHandler, port=8080):
    # Define the address and port the server will listen on
    server_address = ('', port)
    
    # Create the HTTP server
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    
    # Start the server, it will run indefinitely
    httpd.serve_forever()

if __name__ == "__main__":
    # Entry point to start the server
    run()
```

### Code Breakdown:

1. **`CustomHandler` Class**:
   - Inherits from `SimpleHTTPRequestHandler` to serve files.
   - The `directory='.'` argument sets the directory to the current directory (`.`), meaning it will serve files from wherever the script is located.
   
2. **`run()` Function**:
   - Creates the HTTP server by specifying the `server_class` and `handler_class`. It uses port `8080` by default.
   - Starts the server by calling `serve_forever()`, which keeps the server running and listens for incoming HTTP requests.

3. **Main Execution**:
   - When the script is executed, the `run()` function is called to start the server. It prints a message showing that the server is running on port `8080`.

## AWS App Runner Configuration

To deploy this application to AWS App Runner, you can use the following configuration:

```yaml
version: 1.0
runtime: python311
build:
  commands:
    build:
      - pip3 install --no-cache-dir -r requirements.txt
run:
  command: python3 app.py
  network:
    port: 8080
```

## Key Parts of the Configuration

- **Runtime**: Specifies `python311` as the runtime environment, meaning the application will run in a Python 3.11 environment.
- **Build Commands**: Installs dependencies from the `requirements.txt` file (you can leave it empty if there are no dependencies).
- **Run Command**: Starts the application by running the `app.py` script with `python3`.
- **Network**: Exposes port `8080`, which is where the application will listen for HTTP requests. This port must match what the Python server is configured to use.

## Steps to Deploy

### 1. Build Docker Image (Optional)
If you want to build the application locally using Docker, create a `Dockerfile` with the following contents:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
```

Then build the Docker image:

```bash
docker build -t my-python-app .
```

### 2. Deploy on AWS App Runner

Follow these steps to deploy the application on AWS App Runner:

1. **Navigate to AWS App Runner**:
   - Go to the AWS Management Console and navigate to **AWS App Runner**.

2. **Create a New Service**:
   - Create a new App Runner service.
   - Link your source code repository or a container registry (if you’re using a pre-built Docker image).

3. **Configure Build and Run Commands**:
   - Ensure the correct build and run commands are provided. You can use the default commands specified in the `app-runner.yaml`.

4. **Set Environment Variables (Optional)**:
   - Set any necessary environment variables if your application requires them.

5. **Deploy**:
   - Deploy the application. App Runner will handle building and running the application, automatically exposing it at a publicly accessible URL.

### 3. Access the Application

Once the deployment is complete, your application will be available at the URL provided by AWS App Runner. You can visit this URL to see the contents of the HTML page (or other files) served by the application.

## Requirements

If your project doesn’t require any specific Python dependencies, you can create an empty `requirements.txt` file:

```bash
touch requirements.txt
```

If your project has dependencies, list them in `requirements.txt` like so:

```bash
flask
gunicorn
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
```

---

This version of the `README.md` includes detailed explanations for each section, including the code breakdown, AWS App Runner configuration, and deployment steps. Please let me know if you need any more changes!
