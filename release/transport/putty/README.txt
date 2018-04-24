        PuTTY for Nokia 9200 Communicator Series
        ----------------------------------------

Version 1.3.2, 6 January 2005

Copyright 2002-2005 Petteri Kangaslampi
Based on PuTTY 0.56 beta, Copyright 1997-2004 Simon Tatham.
See license.txt for full copyright and license information.


Introduction
------------

This package contains version 1.3.2 of PuTTY SSH Client for the Nokia
9200 and 9500 Communicator series. This version includes important
security fixes (CAN-2004-1008) and all users should upgrade. There are
no changes compared to 1.3.2 RC1, only a new installation certificate
is used.

PuTTY is free software, and available with full source code under a
very liberal license agreement.

See the user's guide document in this package for more documentation.


Package signatures
------------------

All PuTTY installation packages originating from me are signed using a
self-signed certificate. To be able to verify the packages, you'll
need to install the certificate to the device. The steps needed are:

1. Fetch the certificate from 
   http://www.s2.org/~pekangas/petteri_kangaslampi_2005.cer.zip
   and unzip it.
2. Verify the certificate. Its MD5 sum is
   605b9e955f2e4fb0b038bfc78b3c8a70. A PGP signature is available at
   http://www.s2.org/~pekangas/petteri_kangaslampi_2005.asc, the key is
   http://www.s2.org/~pekangas/pekangas.public.asc. The key is also
   available at the MIT keyserver, http://pgp.mit.edu/ (ID 2A5111C9).
3. Copy the certificate to a file in the communicator.
4. Open Certificate manager from the communicator's Control panel.
5. Select "Add" and choose the file
6. Select the certificate from the list, select "View details", 
   select "Trust settings" and enable "Software installation"


Changes
-------

Changes since 1.3.1 RC1:
- Created a new installation certificate, the old one expires soon

Main changes since 1.3.1:
- PuTTY core updated to 0.56 beta, which includes important security
  fixes.
- Fixed Enter on several dialogs on the 9500. Thanks to Adam Boardman.
- Fixed 1089852: Pine crashes with 9500 (hopefully)

Main changes since 1.3.0:
- PuTTY core updated to 0.55 beta, which includes important security
  fixes.

Main changes since 1.2:
- Merged in changes for Series 60 support
- Dialog boxes for username and password prompts
- New certificate, the old had expired
- Fixed random number generator init at first startup
- Added user's guide document

Main changes since 1.1 beta 1:
- Major internal reorganization.
- Icons. This icon is made by myself based on the PuTTY windows
  icon. I have received other proposals too (though more are still
  welcome), and may change the icon after I have evaluated the
  alternatives on a real 9210.
- Support for saving the current settings as default settings
- Logging
- Font size and full screen mode are now saved in the settings

Main changes since 1.0:
- Configuration support. Basic configuration options can be changed
  using the UI, advanced settings can be written directly to the
  config files. Configuration is saved to a text file.
- Added support for sending special characters. Chr opens the standard
  character map, some additional characters are available in the menu.
- Public key authentication works


Future plans
------------

Changes planned for future 1.3 releases:
- Add more keys to the menu if needed
- Fix any bugs

Features planned for future versions, in rough priority order
- Possibly more configuration options
- Check SSH 2 support again, try to determine what causes the
  performance problems we have seen so far
- Better support for the new 9500 Communicator
- Copy/paste support
- Any good ideas? Contact me, preferably with patches


Contact information
-------------------

The project home page is at
        http://s2putty.sourceforge.net/

The site also contains the source code, news, and other useful
information.

Feedback, bug reports, comments, and questions can be e-mailed to
        pekangas@s2.org

I can't promise to answer all e-mail, but will definitely read it all.

Mailing lists, downloads, and other information can be found at
        http://www.sourceforge.net/projects/s2putty/


Acknowledgements
----------------

This Symbian OS port is partially based on the SyOSsh by Gabor
Keresztfavli. Especially the network code, noise generation, and
storage implementation borrow heavily from SyOSsh.

Obviously this program wouldn't exist without the original PuTTY SSH
client by Simon Tatham and others. Many thanks for writing such an
excellent application and releasing it as free software!
