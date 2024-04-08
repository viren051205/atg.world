FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /home/ubuntu/myproject
COPY . /home/ubuntu/myproject/
RUN pip install --no-cache-dir -r requirements.txt
# Expose the port the app runs on
EXPOSE 8000
# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
