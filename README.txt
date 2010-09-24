
Introduction
============

Deploy Plone to Debian (to make my life easier and hopefully yours too).

Install
-------

If you are me (or you'd like to give me root access to your server) do this::

    $ git clone git://github.com/aclark4life/Deploy-Debian-Project.git
    $ python bootstrap.py
    $ bin/buildout
    $ bin/fab -H <host> deploy

But seriously… I created this deployment package for me. If you find it
useful, please feel free to use it (just edit or remove the id_rsa.pub file first).
If you find it really useful, please give something back (by clicking on the
donation link in the upper right hand corner of this page, thanks GitHub for making
it so easy!)

Issues
------

- Currently you must run ``aptitude update`` once by hand. Looking into fixing
  this with pexpect (Fabric does not seem to handle complex interactions
  well).
