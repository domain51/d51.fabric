from fabric.api import local
import os

D51_PACKAGES = [
    #'d51.fabric.tasks.django',
    'd51.fabric.tasks.mosso',
    'd51.fabric.tasks.rabbitmq',
    'd51.fabric.tasks.ubuntu',
]

def src():
    if not os.path.exists('src'):
        os.mkdir('src')

    for package in D51_PACKAGES:
        if not os.path.exists('src/%s' % package):
            repo = "git://github.com/domain51/%s.git" % package
            local('git clone %s src/%s' % (repo, package))
        else:
            os.chdir('src/%s' % package)
            local('git pull origin')
            os.chdir('../..')

        local('cp -R src/%s/d51 .' % package)

def setup(type):
    src()
    if os.path.exists('MANIFEST'):
        local('rm MANIFEST')
    local('python setup.py %s' % type)

def build():
    setup('build')

def install():
    setup('install')

def sdist():
    setup('sdist')

def clean():
    local('rm -rf build/ d51/ MANIFEST')
