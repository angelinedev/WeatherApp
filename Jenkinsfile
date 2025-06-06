pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/23f-3004447/WeatherApp.git', branch: 'main'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                # Stop anything already using port 5000
                fuser -k 5000/tcp || true

                # Optional: create a Python venv if you're fancy
                # python3 -m venv venv && source venv/bin/activate

                # Install Flask & requests
                pip3 install flask requests || true

                # Start Flask app in background
                nohup python3 app.py > flask.log 2>&1 &
                '''
            }
        }
    }
}
