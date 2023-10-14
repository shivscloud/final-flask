# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
ENV DB_HOST your_database_host
ENV DB_NAME your_database_name
ENV DB_USER your_database_user
ENV DB_PASSWORD your_database_password
ENV DB_PORT your_database_port
# Copy the application code to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# # Set the environment variable
# ENV DATABASE_URL=postgresql://postgres:password@db:5432/user_management_db

# Run the Flask application
CMD ["python", "app.py"]
