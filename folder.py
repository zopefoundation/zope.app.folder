##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.0 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""
$Id: folder.py,v 1.3 2004/02/25 23:02:25 faassen Exp $
"""

from persistent import Persistent
from BTrees.OOBTree import OOBTree
from zope.exceptions import DuplicationError
from zope.interface import implements, directlyProvides

from zope.app.container.contained import Contained, setitem, uncontained
from zope.app.services.servicecontainer import ServiceManagerContainer

from interfaces import IFolder, IRootFolder

__metaclass__ = type

class Folder(Persistent, ServiceManagerContainer, Contained):
    """The standard Zope Folder implementation.
    """

    implements(IFolder)

    def __init__(self):
        self.data = OOBTree()

    def keys(self):
        """Return a sequence-like object containing the names
           associated with the objects that appear in the folder
        """
        return self.data.keys()

    def __iter__(self):
        return iter(self.data.keys())

    def values(self):
        """Return a sequence-like object containing the objects that
           appear in the folder.
        """
        return self.data.values()

    def items(self):
        """Return a sequence-like object containing tuples of the form
           (name, object) for the objects that appear in the folder.
        """
        return self.data.items()

    def __getitem__(self, name):
        """Return the named object, or the value of the default
           argument if given and the named object is not found.
           If no default is given and the object is not found a
           KeyError is raised.
        """
        return self.data[name]

    def get(self, name, default=None):
        """Return the named object, or the value of the default
           argument if given and the named object is not found.
           If no default is given and the object is not found a
           KeyError is raised.
        """
        return self.data.get(name, default)

    def __contains__(self, name):
        """Return true if the named object appears in the folder."""
        return self.data.has_key(name)

    def __len__(self):
        """Return the number of objects in the folder."""
        return len(self.data)

    def __setitem__(self, name, object):
        """Add the given object to the folder under the given name."""

        if not (isinstance(name, str) or isinstance(name, unicode)):
            raise TypeError("Name must be a string rather than a %s" %
                            name.__class__.__name__)
        try:
            unicode(name)
        except UnicodeError:
            raise TypeError("Non-unicode names must be 7-bit-ascii only")
        if not name:
            raise TypeError("Name must not be empty")

        if name in self.data:
            raise DuplicationError("name, %s, is already in use" % name)

        setitem(self, self.data.__setitem__, name, object)

    def __delitem__(self, name):
        """Delete the named object from the folder. Raises a KeyError
           if the object is not found."""
        uncontained(self.data[name], self, name)
        del self.data[name]

def rootFolder():
    f = Folder()
    directlyProvides(f, IRootFolder)
    return f
