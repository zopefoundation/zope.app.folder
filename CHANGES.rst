=======
CHANGES
=======

4.0.0 (2017-05-09)
------------------

- Add support for Python 3.4. 3.5, 3.6 and PyPy.


3.5.2 (2010-12-28)
------------------

- Removed testing.py. There are no functional tests and ftesting.zcml now.

- Removed unneeded dependencies.


3.5.1 (2009-02-14)
------------------

- Added missing dependency to zope.app.content.

- Fixed e-mail address and homepage.

- Fixed buildout.cfg, as there is no test extra.


3.5.0 (2009-01-31)
------------------

- Everything except zope.app.folder.browser moved to zope.site
  and zope.container.

- Import IPossibleSite from zope.location.interfaces
  instead of deprecated place in zope.app.component.interfaces.

- Use zope.container instead of zope.app.container.

3.4.0 (2007-10-24)
------------------

- Initial release independent of the main Zope tree.
