pipeline {
    agent any

    environment {
        WORKSPACE_DIR = '/var/lib/jenkins/workspace/car-pipeline'
    }

    stages {
        stage('Build') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    sh 'echo Building the project'
                }
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    sh '''#!/bin/bash
                    set -e
                    if [ ! -d "myenv" ]; then
                        echo "Creating virtual environment"
                        python3 -m venv myenv
                    else
                        echo "Virtual environment already exists"
                    fi
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    sh '''#!/bin/bash
                    set -e
                    echo Testing the project
                    source myenv/bin/activate
                    python3 manage.py test playground
                    deactivate
                    '''
                }
            }
        }
        
        stage('Deploy to Staging') {
            steps {
                sh  'echo Deploying....'
                sh 'ssh deploy@192.168.1.10 -o StrictHostKeyChecking=no "bash /var/www/JOYONWHEELS/scripts/deploy.sh"'
                
                }
        }
        stage('Deploy to production') {
            input {
                message 'Do you want to deploy to production?.'
                ok 'Yes.Deploy to Production..'}
            steps {
                sh  'echo Deploying....'
                sh 'ssh orsankalo@209.38.198.30 -o StrictHostKeyChecking=no "bash /var/www/JOYONWHEELS/scripts/deploy.sh"'
                
                }
        }
    }
    post {
        failure {
            mail bcc: '', body: "The pipeline is failed", cc: '',charset: 'UTF-8', from: 'jenkins@jenkins-build.com', mimeType: 'text/plain', subject: "Pipeline failed", to:"orsankalp@gmail.com" }
    }
    

}