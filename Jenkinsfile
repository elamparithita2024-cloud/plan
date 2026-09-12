pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/elamparithita2024-cloud/part.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\T.A.ELAMPARITHI\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '"C:\\Users\\T.A.ELAMPARITHI\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pytest test_app.py -v'
            }
        }
    }
}
