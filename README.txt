
Introduction
============

Deploy Plone to Debian to make my life easier and hopefully yours too.

Install
-------

If you are me (or you'd like to give me root access to your server) do this::

    $ git clone git://github.com/aclark4life/Deploy-Debian-Project.git
    $ python bootstrap.py
    $ bin/buildout
    $ bin/fab -H <host> deploy

But seriously, I created this deployment package for me. If you find it
useful, please feel free to use it; edit or remove the id_rsa.pub file first.

Issues
------

- Currently you must run ``aptitude update`` once by hand. Looking into fixing
  this with pexpect (Fabric does not seem to handle complex interactions
  well).
