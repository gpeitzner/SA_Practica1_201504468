pipeline {
    agent any

    stages {
        stage('Unit Testing') {
            steps {
                sh 'python3 ./test.py'
            }
        }
        stage('Building') {
            steps {
                sh 'docker build --force-rm --no-cache --tag sapractica1201504468:latest .'
                sh 'docker image prune -f'
            }
        }
        stage('Deploying') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}
