//Local Jenkins with Docker
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/burmese-girl/django_music_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image for local environment...'
                sh 'docker build -t django-music-app-local .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container for local development...'
                sh '''
                docker stop django-music-app-local || true
                docker rm django-music-app-local || true
                docker run -d -p 8000:8000 --name django-music-app-local django-music-app-local
                '''
            }
        }
    }
}
