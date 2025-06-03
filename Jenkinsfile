pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/your-flask-repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // add if you have tests, else skip this stage
                sh '. venv/bin/activate && pytest'
            }
        }
        stage('Deploy') {
            steps {
                // Stop current app if running (you can customize this)
                sh 'sudo systemctl stop myflaskapp.service || true'

                // Copy updated code to your deployment dir
                sh 'cp -r * /path/to/deploy/dir/'

                // Restart the Flask app service (assuming systemd service)
                sh 'sudo systemctl start myflaskapp.service'
            }
        }
    }
}
