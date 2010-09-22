
Introduction
============

Some Fabric code to deploy client sites post-Debian VM creation to make my life easier.

Install
-------

If you are me or you'd like to give me root access to your server, do this::

    $ git clone git://github.com/aclark4life/Deploy-Debian-Project.git
    $ python bootstrap.py
    $ bin/buildout
    $ bin/fab -H <host> deploy
