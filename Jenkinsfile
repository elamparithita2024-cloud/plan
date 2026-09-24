pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT', 
            choices: ['dev', 'staging', 'prod'], 
            description: 'Select the target deployment environment'
        )
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Fetching codebase..."
           
                sh 'echo "print(\'Hello from app.py!\')" > app.py'
            }
        }

        stage('Build') {
            steps {
                echo "Performing compile check on app.py..."
              
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Deploy') {
            steps {
                // Pause pipeline and prompt user for intervention
                input message: "Approve deployment to ${params.ENVIRONMENT}?", ok: "Go"
                
                echo "Deploying to ${params.ENVIRONMENT} environment..."
                sh 'python3 app.py'
            }
        }
    }
}
