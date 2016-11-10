from invoke import task

IMAGE_NAME = "devopskube/mysql"
IMAGE_VERSION = "0.0.1"

@task
def build(ctx):
    ctx.run("docker build -t {0} .".format(IMAGE_NAME))
