/* Only keep the 5 most recent builds. */
def projectProperties = [
  buildDiscarder(logRotator(numToKeepStr: '5')),
  disableConcurrentBuilds(),
  [$class: 'GithubProjectProperty', displayName: 'Docker MySQL', projectUrlStr: 'https://github.com/devopskube/docker-mysql.git']
]
properties(projectProperties)

podTemplate(label: 'docker-mysql', containers: [
    containerTemplate(name: 'docker', image: 'docker:1.12.3-dind', ttyEnabled: true, command: 'cat', privileged: true, instanceCap: 1),
    containerTemplate(name: 'jnlp', image: 'jenkinsci/jnlp-slave:2.62-alpine', args: '${computer.jnlpmac} ${computer.name}'),
  ],
  volumes: [
        hostPathVolume(mountPath: "/var/run/docker.sock", hostPath: "/var/run/docker.sock")
  ]) {
  node() {
    stage('Preparation') { // for display purposes
      git url: 'https://github.com/devopskube/docker-mysql.git'

      def TAG_NAME = binding.variables.get("TAG_NAME")
      if (TAG_NAME != null) {
        sh "echo $TAG_NAME"
      } else {
        sh "echo Non-tag build"
      }
      
      container('docker') {
        stage('Build the docker image') {

        sh 'docker build -t devopskube/mysql:latest .'
        sh 'docker inspect -f {{.Id}} devopskube/mysql:latest'

        id = sh (
              script: 'docker inspect -f {{.Id}} devopskube/mysql:latest',
              returnStdout: true
             ).trim()
        }
        stage('next') {
          println 'manic'
        }
      }
    }
  }
}
