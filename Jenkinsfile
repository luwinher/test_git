pipeline {
  agent {
    node {
      label 'dev'
    }

  }
  stages {
    stage('git') {
      steps {
        dir(path: '/home/shiyanlou/test_git') {
          git(url: 'git@github.com:luwinher/test_git', credentialsId: '550e63fb-bd48-4982-8093-45acabb3c98b')
        }

      }
    }
    stage('build') {
      steps {
        sh 'sudo -H pip install -r requirements.txt'
      }
    }
    stage('error') {
      steps {
        sh 'python app.py'
      }
    }
  }
}