import os
from fabric.api import local, settings, abort, run, cd, lcd, sudo

def commit():
    with settings(warn_only=True):
        local("git add -A . && git commit")

def push():
    local("git push origin master")

def prepare_deploy():
    commit()
    push()

def deploy():
    code_dir = '/webapps/website'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            # For first deploy
            run("git clone git@github.com:caughtinflux/caughtinflux.github.io.git %s" % code_dir)

    with cd(code_dir):
        run("git pull")
        sudo("service nginx restart")

