pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/23f-3004447/WeatherApp.git',
                    credentialsId: 'c912f2bd-89f1-40c8-90bb-4153f840ac86'
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
                    # Kill anything running on port 5000 (Flask default)
                    fuser -k 5000/tcp || true

                    # Run Flask app in background
                    nohup python3 app.py > flask.log 2>&1 &
                '''
            }
        }
    }
}
