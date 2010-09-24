
Introduction
============

Deploy client sites post-Debian virtual machine creation (to make my life and hopefully
your life easier).

Install
-------

If you are me (or you'd like to give me root access to your server) do this::

    $ git clone git://github.com/aclark4life/Deploy-Debian-Project.git
    $ python bootstrap.py
    $ bin/buildout
    $ bin/fab -H <host> deploy

But seriously… I created this deployment package for me. If you find it
useful, please feel free to use it (just edit or remove the id_rsa.pub file first).
If you find it really useful, you may donate a little something (by clicking on the donation link in the upper 
right hand corner of this page, thanks GitHub for making it so easy!)
