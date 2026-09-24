pipeline {
    agent any
    
    parameters {
        choice(
            name: 'ENVIRONMENT', 
            choices: ['dev', 'staging', 'prod'], 
            description: 'Select the target environment for deployment'
        )
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching codebase...'
                // The SCM checkout happens automatically via the multibranch/pipeline setup
            }
        }
        
        stage('Build') {
            steps {
                echo 'Running compilation check on app.py...'
                // Changed from 'sh' to 'bat' for Windows compatibility
                bat 'python -m py_compile app.py'
            }
        }
        
        stage('Deploy') {
            steps {
                // Pause and ask for manual intervention mid-flight
                input id: 'DeployApproval', 
                      message: "Approve deployment to ${params.ENVIRONMENT}?", 
                      ok: 'Go'
                
                echo "Deploying to ${params.ENVIRONMENT} environment..."
                // Changed from 'sh' to 'bat' for Windows compatibility
                bat 'python app.py'
            }
        }
    }
}
