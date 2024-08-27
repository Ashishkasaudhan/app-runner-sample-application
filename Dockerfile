# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Tkinter
RUN apt-get update && apt-get install -y python3-tk

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt (if any)
# In this case, no external packages are needed, so we skip this step

# Run welcome_app.py when the container launches
CMD ["python", "./welcome_app.py"]
