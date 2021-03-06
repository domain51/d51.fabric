from fabric.api import env, local, put, run
import os

D51_PACKAGES = [
    'd51.fabric.tasks.django',
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

        local('rm -rf ./docs/%s' % package)
        local('cp -R src/%(package)s/docs ./docs/%(package)s' % {'package': package})
        local('cp src/%(package)s/README.rst ./docs/%(package)s/README.rst' % {'package': package})
        orig_readme = open("./docs/%s/index.rst" % package, "r").read()
        new_readme = orig_readme.replace('../README.rst', './README.rst')
        open("./docs/%s/index.rst" % package, "w").write(new_readme)

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

def docs():
    src()
    local("cd docs && make html")

def deploy_docs():
    docs()
    REMOTE_DIR = "/home/tswicegood/domains/domain51.com/public/docs/"
    local("cd ./docs/_build/ && "
          "cp -R ./html ./d51.fabric && "
          "tar -cjf d51.fabric.tar.bz2 d51.fabric/")
    put("./docs/_build/d51.fabric.tar.bz2",
        REMOTE_DIR + "d51.fabric.tar.bz2")
    run("cd %s && tar -xjf d51.fabric.tar.bz2" % REMOTE_DIR)
    local("rm -rf ./docs/_build/d51.fabric*")
