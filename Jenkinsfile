pipeline {
    agent any

    environment {
        IMAGE_NAME = "car-info-app"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        REGISTRY_URL = "https://registry.example.com"
        REGISTRY_CREDENTIALS = "registry-credentials"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VarshiniRameshh/car-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    try {
                        echo "Building Docker image: ${IMAGE_NAME}:${IMAGE_TAG}"
                        docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                    } catch (Exception e) {
                        error "Docker build failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        echo "Running tests in Docker container..."
                        sh "docker run --rm ${IMAGE_NAME}:${IMAGE_TAG} python -m unittest discover"
                    } catch (Exception e) {
                        error "Tests failed: ${e.getMessage()}"
                    }
                }
            }
        }

        stage('Push to Registry') {
            steps {
                script {
                    try {
                        echo "Pushing Docker image to registry..."
                        docker.withRegistry("${REGISTRY_URL}", "${REGISTRY_CREDENTIALS}") {
                            docker.image("${IMAGE_NAME}:${IMAGE_TAG}").push()
                        }
                    } catch (Exception e) {
                        error "Failed to push Docker image: ${e.getMessage()}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up dangling Docker images..."
            sh "docker system prune -f"
        }
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the logs."
        }
    }
}
