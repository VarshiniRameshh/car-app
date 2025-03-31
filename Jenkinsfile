pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/VarshiniRameshh/car-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("car-info-app:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Test') {
            steps {
                sh 'docker run car-info-app:${env.BUILD_NUMBER} python -m unittest discover'
            }
        }
        stage('Push to Registry') {
            steps {
                script {
                    docker.withRegistry('https://registry.example.com', 'registry-credentials') {
                        docker.image("car-info-app:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
    }
}
