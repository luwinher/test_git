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
          git(url: 'https://github.com/luwinher/test_git.git', branch: 'master', credentialsId: '550e63fb-bd48-4982-8093-45acabb3c98b')
        }

      }
    }
    stage('build') {
      steps {
        sh 'sudo -H pip install -r requirements.txt'
      }
    }
    stage('run') {
      steps {
        sh 'python app.py'
      }
    }
  }
}