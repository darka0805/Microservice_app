import subprocess

business = subprocess.Popen(["uvicorn", "business_service:app", "--port", "8001"])
db = subprocess.Popen(["uvicorn", "db_service:app", "--port", "8002"])
client = subprocess.Popen(["uvicorn", "client_service:app", "--port", "8000"])

print("All services started. Press Ctrl+C to stop.")
try:
    business.wait()
    db.wait()
    client.wait()
except KeyboardInterrupt:
    print("Shutting down...")
    business.terminate()
    db.terminate()
    client.terminate()
