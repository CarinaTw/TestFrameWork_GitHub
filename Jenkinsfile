pipeline {
    agent { dockerfile true }

    stages {

    stage('Move to working dir') {
			steps {
				sh 'cd Users/carina/Desktop/Jenkins_Home/workspace/otus_test_job2'
			}
		}
        stage('Test GitHub Api') {
            steps {
                sh 'docker build -t my_otus_project_10 .'
            }
        }

        stage('Run Tests') {
			steps {
				sh 'docker run my_otus_project_10'
			}
        }
    }
}
