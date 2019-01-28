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
          git 'https://github.com/luwinher/test_git'
        }

      }
    }
    stage('build') {
      steps {
        sh 'sudo -H pip install -r requirements.txt'
      }
    }
    stage('') {
      steps {
        sh 'python app.py'
      }
    }
  }
}