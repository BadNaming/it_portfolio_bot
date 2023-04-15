FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY src/ .
CMD ["python3", "finder/bot_optimized.py"]