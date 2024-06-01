pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Shiishiji/world_of_games.git'
            }
        }
        stage('Build') {
            steps {
                bat 'docker compose -f docker-compose.yml -f docker-compose.test.yml build'
            }
        }
        stage('Run') {
            steps {
                bat 'docker compose -f docker-compose.yml -f docker-compose.test.yml up -d --remove-orphans'
            }
        }
        stage('Test') {
            steps {
                bat 'docker compose -f docker-compose.yml -f docker-compose.test.yml run tests python tests/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                bat 'docker compose -f docker-compose.yml -f docker-compose.test.yml down -v --remove-orphans'
            }
        }
    }
}