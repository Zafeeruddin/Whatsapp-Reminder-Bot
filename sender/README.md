1. Login to twilio to fetch and replace env variables.
2. Add users to Sandbox whatsapp group.
3. Run this **main** locally with uvicorn.
4. Expose this port with ngrok.
5. Save ngrok url/whatsapp hook inside sandbox configuration


Commands:


# Run Local Server
uvicorn main:app --reload

# ngrok on windows
docker run --rm -it \
  -e NGROK_AUTHTOKEN=<your_token> \
  ngrok/ngrok http host.docker.internal:8000

