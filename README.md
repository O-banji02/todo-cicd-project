# 🚀 Todo App with CI/CD Pipeline

![CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci-cd.yml/badge.svg)

A simple Todo REST API built with Flask, containerized with Docker, and automatically deployed using GitHub Actions CI/CD pipeline.

## 📋 Features

- Create, Read, Update, Delete (CRUD) todos
- RESTful API endpoints
- Dockerized application
- Automated testing with pytest
- CI/CD pipeline with GitHub Actions
- Automatic deployment to AWS EC2
- Nginx reverse proxy

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Deployment**: AWS EC2
- **Web Server**: Nginx
- **Testing**: pytest

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/health` | Health check |
| GET | `/todos` | Get all todos |
| POST | `/todos` | Create a new todo |
| PUT | `/todos/<id>` | Update a todo |
| DELETE | `/todos/<id>` | Delete a todo |

## 🚀 Quick Start

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/O-banji02/todo-cicd-project.git
cd todo-cicd-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Test the API:
```bash
curl http://localhost:5000
```

### Docker

1. Build the image:
```bash
docker build -t todo-app .
```

2. Run the container:
```bash
docker run -p 5000:5000 todo-app
```

## 🧪 Running Tests

```bash
pytest test_app.py -v
```

## 🔄 CI/CD Pipeline

The pipeline automatically:
1. Runs tests on every push
2. Builds Docker image
3. Pushes image to Docker Hub
4. Deploys to Render

## 📦 Deployment

The app is deployed at: https://todo-cicd-project.onrender.com

## 🤝 Contributing

Pull requests are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🔥 Status
CI/CD Pipeline Active!!