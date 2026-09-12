pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/elamparithita2024-cloud/plan.git'
            }
        }

        stage('Build') {
            steps {
                bat 'py -m py_compile app.py'
                echo 'Build successful: app.py compiled with no syntax errors'
            }
        }

        stage('Deploy') {
            steps {
                input message: 'Approve deployment to production?', ok: 'Deploy'
                bat 'py app.py'
            }
        }
    }
}
