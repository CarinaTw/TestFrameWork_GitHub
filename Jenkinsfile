pipeline {
    agent { dockerfile true }

    stages {

    stage('Move to working dir') {
			steps {
				sh 'cd /var/jenkins_home/workspace/first_pipeline'
			}
		}
        stage('Test GitHub Api') {
            steps {
                sh 'docker build -f Dockerfile -t my_otus_project_10 .'
            }
        }

        stage('Run Tests') {
			steps {
				sh 'docker run my_otus_project_10'
			}
        }
    }
}
