
Introduction
============

Deploy client sites post-Debian virtual machine creation (to make my life and hopefully
yours too easier).

Install
-------

If you are me or you'd like to give me root access to your server, do this::

    $ git clone git://github.com/aclark4life/Deploy-Debian-Project.git
    $ python bootstrap.py
    $ bin/buildout
    $ bin/fab -H <host> deploy
