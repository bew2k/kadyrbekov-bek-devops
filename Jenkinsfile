pipeline {
  agent any
  environment {
    STUDENT_NAME = 'Bek'
    STUDENT_SURNAME = 'Kadyrbekov'
    STUDENT_GROUP = 'IT2-2306'
    STUDENT_ID = '35534'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'git log -1 --oneline'
        sh 'echo "Student: $STUDENT_NAME $STUDENT_SURNAME"; echo "Group: $STUDENT_GROUP"; echo "Student ID: $STUDENT_ID"'
      }
    }
    stage('Build') {
      steps { sh 'ls -la && bash -n scripts/Kadyrbekov_Bek_system.sh && echo Build OK' }
    }
    stage('Test') {
      steps { sh 'test -f Kadyrbekov_Bek_info.txt && test -f app/app.py && grep -q "35534" Kadyrbekov_Bek_info.txt && echo Tests passed' }
    }
    stage('Docker Build') {
      steps { sh 'docker build -t kadyrbekov-bek-devops .' }
    }
    stage('Docker Run') {
      steps {
        sh 'docker rm -f kadyrbekov-bek-container || true'
        sh 'docker run --name kadyrbekov-bek-container -e STUDENT_NAME=$STUDENT_NAME -e STUDENT_SURNAME=$STUDENT_SURNAME -e STUDENT_GROUP=$STUDENT_GROUP -e STUDENT_ID=$STUDENT_ID kadyrbekov-bek-devops'
      }
    }
  }
}
