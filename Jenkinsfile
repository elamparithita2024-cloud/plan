pipeline {
    agent any
    

    environment {
        APP_NAME    = 'MyPythonApp'
        APP_VERSION = '1.2.0'
    }
    
    parameters {
        
        booleanParam(
            name: 'SEND_EMAIL', 
            defaultValue: true, 
            description: 'Check this box to send an email notification upon build completion'
        )
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching codebase from repository...'
            }
        }
        
        stage('Build') {
            steps {
               
                echo "Building application: ${env.APP_NAME} v${env.APP_VERSION}"
                bat 'python -m py_compile app.py'
            }
        }
        
        stage('Send Notification') {
           
            when {
                expression { return params.SEND_EMAIL == true }
            }
            steps {
            
                echo "Sending Email Notification..."
                echo "Subject: [Deployment] ${env.APP_NAME} - Version ${env.APP_VERSION} status"
                echo "Body: The pipeline has completed successfully."
                
               
                mail to: 'elamparithi.ta2024@vitstudent.ac.in',
                     subject: "[Deployment] ${env.APP_NAME} - Version ${env.APP_VERSION} status",
                     body: "The pipeline has completed successfully."
                */
            }
        }
    }
}
