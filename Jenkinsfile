#!/usr/bin/env groovy
@Grab('org.yaml:snakeyaml:1.17')
import org.yaml.snakeyaml.*

/* Only keep the 5 most recent builds. */
def projectProperties = [
        buildDiscarder(logRotator(numToKeepStr: '5')),
        disableConcurrentBuilds(),
        [$class: 'GithubProjectProperty', displayName: 'Docker MySQL', projectUrlStr: 'https://github.com/devopskube/docker-mysql.git']
]
properties(projectProperties)

def IMAGE_NAME = 'devopskube/mysql'
def tag_name = ''
def image_name = ''

podTemplate(label: 'docker-mysql', containers: [
            containerTemplate(name: 'jnlp', image: 'jenkinsci/jnlp-slave:2.62-alpine', args: '${computer.jnlpmac} ${computer.name}'),
            containerTemplate(name: 'docker', image: 'docker:1.12.3-dind', ttyEnabled: true, command: 'cat', privileged: true, instanceCap: 1)
        ],
        volumes: [
            hostPathVolume(mountPath: "/var/run/docker.sock", hostPath: "/var/run/docker.sock")
        ]) {
    node() {
        stage('checkout') { // happens on master?
            git url: 'https://github.com/devopskube/docker-mysql.git'
            tag_name = sh (
                    script: 'git tag -l --points-at HEAD',
                    returnStdout: true
            ).trim()

            def projectFile = readFile("project.yml")

            Yaml yaml = new Yaml();
            Map map = (Map) yaml.load(projectFile);
            image_name = map.get("imageName")

        }
        container('docker') {
            stage('Build the docker image') {
                sh("docker build -t ${IMAGE_NAME} .")
            }
            stage('tag the image') {
                sh "docker tag ${IMAGE_NAME} ${IMAGE_NAME}:latest"

                if (tag_name?.trim()) {
                    sh "docker tag ${IMAGE_NAME} ${IMAGE_NAME}:${tag_name}"
                }
            }
            stage('Push the image') {
//                sh "docker push ${IMAGE_NAME}:latest"
                println "push latest"

                if (tag_name?.trim()) {
                    println "push ${tag_name}"
//                    sh "docker push ${IMAGE_NAME}:${tag_name}"
                }
            }
        }
    }
}
