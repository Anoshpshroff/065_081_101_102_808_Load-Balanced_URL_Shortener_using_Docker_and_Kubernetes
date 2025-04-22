## Week 1 Deliverables

### Features
- Flask app to handle URL shortening and redirection
- Redis used as a key-value store for mappings
- Dockerfile for containerizing the application

### How to Run Locally
```bash
# Start Redis
docker run --name redis-container -d -p 6379:6379 redis

# Build Flask app image
docker build -t url-shortener .

# Run Flask app
docker run -d -p 5000:5000 --name my-url-shortener --network container:redis-container url-shortener

## Week 2 Deliverables
Deploy Steps (Minikube)
# Start minikube
minikube start

# Connect Docker to Minikube
& minikube -p minikube docker-env --shell powershell | Invoke-Expression

# Build app inside Minikube
docker build -t url-shortener .

# Apply Kubernetes manifests
kubectl create namespace url-shortener
kubectl apply -f k8s/ -n url-shortener

# Access the App
minikube service url-shortener-service -n url-shortener

# API Usage
# Shorten a URL:
POST /shorten
Content-Type: application/json

{
  "url": "https://example.com"
}


# Redirect from short URL:
GET /<short_code>

## Week 3 Deliverables
# Stress Testing
for ($i=0; $i -lt 1000; $i++) {
  Invoke-RestMethod -Uri "http://127.0.0.1:<port>/shorten" `
    -Method Post `
    -Body '{"url":"https://example.com"}' `
    -ContentType "application/json"
}

kubectl get hpa -n url-shortener --watch

# Monitoring Usage
kubectl top pods -n url-shortener
kubectl logs <pod-name> -n url-shortener



