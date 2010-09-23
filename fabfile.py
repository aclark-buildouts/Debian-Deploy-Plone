# A work in progress
from fabric.api import env, put, run

env.user = 'root'
env.warn_only = True


def deploy():
    update_packages()
    copy_pub_key()
    install_developer()
    install_python()
    install_plone()


def update_packages():
    run('aptitude update')

    # XXX What do I do when aptitude asks "harder" questions? i.e. How
    # does Fabric handle more complex interactions (with remote hosts)
    # a la (TCL) Expect? My understanding is that it currently does not.
    run('aptitude -y safe-upgrade')


def copy_pub_key():
    run('mkdir /root/.ssh')
    run('chmod 700 /root/.ssh')
    put('id_rsa.pub', '/root/.ssh/authorized_keys')


def install_developer():
    run('aptitude -y install build-essential')
    run('aptitude -y install subversion')
    run('aptitude -y install zlib1g-dev')
    

def install_python():
    run('aptitude -y install python')
    put('distribute_setup.py', 'distribute_setup.py')
    run('python distribute_setup.py')
    run('easy_install pip')
    run('pip install virtualenv')
    run('virtualenv --no-site-packages --distribute python')
    run('svn co http://svn.plone.org/svn/collective/buildout/python/')
    run('cd python; bin/python bootstrap.py -d')
    run('cd python; bin/buildout')


def install_plone():
    run('mkdir /srv/plone')
    put('plone.cfg', '/srv/plone/buildout.cfg')
    put('bootstrap.py', '/srv/plone')
    run('cd /srv/plone; /root/python/python-2.6/bin/python2.6 bootstrap.py -d')
    run('cd /srv/plone; bin/buildout')
    run('cd /srv/plone; bin/supervisord')
