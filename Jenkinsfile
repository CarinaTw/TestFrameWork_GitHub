pipeline {
	agent any

	stages {
		stage('Move to working dir') {
			steps {
				sh 'cd /var/jenkins_home/workspace/first_pipeline'
			}
		}
		stage('Create image') {
			steps {
				sh 'docker build -f Dockerfile -t my_otus_project_1 .'
			}
		}
		stage('Run Tests') {
			steps {
				sh 'docker run my_otus_project_1'
			}
		}
	}
}