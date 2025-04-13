FROM python:3.12.5-bullseye


WORKDIR /app

RUN apt-get update && apt-get install ffmpeg -y \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN export PYTHONPATH=/workspaces/yt-assistant-ai/backend

# expose port 7687
EXPOSE 7687

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
