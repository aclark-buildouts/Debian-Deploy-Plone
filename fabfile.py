
from fabric.api import env, put, run

env.user = 'root'
env.warn_only = True 

def deploy():
    update_packages()
    copy_pub_key()

def update_packages():
    run('aptitude update')
    run('aptitude -y safe-upgrade')

def copy_pub_key():
    run('mkdir /root/.ssh')
    run('chmod 700 /root/.ssh')
    put('id_rsa.pub','/root/.ssh/authorized_keys')
