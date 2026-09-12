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
                bat 'C:/Users/T.A.ELAMPARITHI/AppData/Local/Microsoft/WindowsApps/python.exe -m py_compile app.py'
                echo 'Build successful: app.py compiled with no syntax errors'
            }
        }

        stage('Deploy') {
            steps {
                input message: 'Approve deployment to production?', ok: 'Deploy'
                bat 'C:/Users/T.A.ELAMPARITHI/AppData/Local/Microsoft/WindowsApps/python.exe app.py'
            }
        }
    }
}
