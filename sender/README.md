1. Login to twilio to fetch and replace env variables.
2. Add users to Sandbox whatsapp group.
3. Run this **main** locally with uvicorn.
4. Expose this port with ngrok.
5. Save ngrok url/whatsapp hook inside sandbox configuration


Commands:


# Create env
uv venv
source  sender/.venv/bin/activate

# Install dependencies
uv pip install

# Run Local Server
uv run uvicorn sender.main:app --reload

# ngrok on windows
docker run --rm -it \
  -e NGROK_AUTHTOKEN=<your_token> \
  ngrok/ngrok http host.docker.internal:8000


# ngrok on linux
docker run --rm -it \
  --network host \
  -e NGROK_AUTHTOKEN=<your_token> \
  ngrok/ngrok http localhost:8000

## Replace the ngrok live url in twilio Sandbox

# Run redis locally
docker run -d -p 6379:6379 --name my-redis


# Run celery in backend
uv run celery -A worker.tasks worker --loglevel=info
