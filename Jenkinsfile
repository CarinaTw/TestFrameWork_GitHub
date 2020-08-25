pipeline {
    agent {
        docker {
            image 'otus_project_10'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my_otus_project_10 .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run my_otus_project_10'
            }
        }

    }
}