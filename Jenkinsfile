pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/23f-3004447/WeatherApp.git',
                    credentialsId: 'a5308c41-1e1b-4839-af30-fe85ccdef2fa'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    fuser -k 5000/tcp || true
                    nohup python3 app.py > flask.log 2>&1 &
                '''
            }
        }
    }
}
