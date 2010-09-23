# A work in progress
from fabric.api import env, put, run

env.user = 'root'
env.warn_only = True

MODULE_CONFS = ('proxy.conf', 'proxy.load', 'proxy_http.load', 'rewrite.load')
PACKAGES = "apache2 build-essential libssl-dev subversion zlib1g-dev"

def deploy():
    copy_pub_key()
    update_packages()
    install_packages()
    install_python()
    install_plone()
    configure_apache()


def update_packages():
    run('aptitude update')
    run('aptitude -y safe-upgrade')


def copy_pub_key():
    run('mkdir /root/.ssh')
    run('chmod 700 /root/.ssh')
    put('id_rsa.pub', '/root/.ssh/authorized_keys')


def install_packages():
    run('aptitude -y install %s' % PACKAGES)


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
    put('site.cfg', '/srv/plone/plonesite.cfg')
    put('bootstrap.py', '/srv/plone/bootstrap.py')
    put('rc.local', '/etc/rc.local')
    run('cd /srv/plone; /root/python/python-2.6/bin/python2.6 bootstrap.py -d')
    run('cd /srv/plone; bin/buildout')
    run('chown -R www-data:www-data /srv/plone')
    run('cd /srv/plone; sudo -u www-data bin/supervisord')
    run('cd /srv/plone; bin/buildout -c plonesite.cfg')


def configure_apache():
    put('rewrite.conf', '/etc/apache2/conf.d')
    for conf in MODULE_CONFS:
        run('cd /etc/apache2/mods-enabled')
        run('ln -sf ../mods-available/%s' % conf)
    run('/etc/init.d/apache2 restart')
