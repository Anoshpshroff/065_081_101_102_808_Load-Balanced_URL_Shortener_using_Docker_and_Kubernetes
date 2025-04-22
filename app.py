from flask import Flask, request, jsonify, redirect
import redis
import os

app = Flask(__name__)

# Connect to Redis using Docker container name
redis_host = os.getenv("REDIS_HOST", "redis")
redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/", methods=["GET"])
def home():
    return "✨ URL Shortener is up and running! ✨"


@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")
    if not original_url:
        return jsonify({"error": "No URL provided"}), 400
    
    short_code = "SwtouF"  # Placeholder; generate dynamically
    redis_client.set(short_code, original_url)
    
    return jsonify({"short_url": f"http://127.0.0.1:5000/{short_code}"})

@app.route("/<short_code>")
def redirect_url(short_code):
    original_url = redis_client.get(short_code)
    if original_url:
        return redirect(original_url, code=302)  # Proper HTTP redirect
    return "URL not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
