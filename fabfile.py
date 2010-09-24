# A work in progress
from fabric.api import env, put, run

env.user = 'root'
env.warn_only = True

FORM_VARS = ('form.submitted:boolean=True',
    'extension_ids:list=plonetheme.sunburst:default',
    'setup_content:boolean=true')
MODULE_CONFS = ('less', 'proxy.conf', 'proxy.load', 'proxy_http.load',
    'rewrite.load')
PACKAGES = "apache2 apache2-dev build-essential libssl-dev libxslt-dev subversion "
PACKAGES += "unzip zlib1g-dev"


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
    from time import sleep
    run('mkdir /srv/plone')
    put('plone.cfg', '/srv/plone/buildout.cfg')
    put('bootstrap.py', '/srv/plone/bootstrap.py')
    put('rc.local', '/etc/rc.local')
    run('cd /srv/plone; /root/python/python-2.6/bin/python2.6 bootstrap.py -d')
    run('cd /srv/plone; bin/buildout')
    run('chown -R www-data:www-data /srv/plone')
    run('cd /srv/plone; sudo -u www-data bin/supervisord')
    sleep(5)
    create_site()
    install_theme()


def create_site():
    url = 'http://127.0.0.1:8080/@@plone-addsite?site_id=Plone'
    run('curl -u admin:admin -d %s %s' % (' -d '.join(FORM_VARS), url))


def install_theme():
    put('theme.zip', 'theme.zip')
    run('cd /srv/plone; unzip -o /root/theme.zip')

def configure_apache():
    put('000-default', '/etc/apache2/sites-enabled')
    run('mkdir /var/www/static')
    for conf in MODULE_CONFS:
        run('cd /etc/apache2/mods-enabled;ln -sf ../mods-available/%s' % conf)
    install_html_xslt()
    run('/etc/init.d/apache2 restart')


def install_html_xslt():
    url = 'http://html-xslt.googlecode.com/files/'
    url += 'mod-transform-html-xslt-2p2.tgz'
    run('wget %s' % url)
    run('tar zxvf mod-transform-html-xslt-2p2.tgz')
    run('cd mod-transform-html-xslt-2p2; ./configure; make; make install')
