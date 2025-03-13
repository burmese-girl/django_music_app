pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DJANGO_SETTINGS_MODULE = 'django_music_app.settings'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/burmese-girl/django_music_app.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python manage.py test'
            }
        }

        stage('Build & Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment steps here (e.g., Docker, SSH, AWS, etc.)
            }
        }
    }
}

