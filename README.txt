
Introduction
============

Some Fabric code to deploy client sites post-Debian VM creation (to make my
life easier, and to have some fun with Fabric).

Install
-------

If you are me or you'd like to give me root access to your server, do this::

    $ git clone git://github.com/aclark4life/Deploy-Debian-Project.git
    $ python bootstrap.py
    $ bin/buildout
    $ bin/fab -H <host> deploy

PEP8
----

Also for kicks, you can run pep8 on the fabfile::

    $ bin/pep8 fabfile.py
