FROM python:3.12
WORKDIR /app
COPY ratingbot .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]