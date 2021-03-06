# -*- coding: utf-8 -*-

from collective.cover import _
from collective.cover.tiles.base import IPersistentCoverTile, PersistentCoverTile
from zope import schema


class IIframeTile(IPersistentCoverTile):
    ''' '''

    remote_url = schema.TextLine(
        title=_(u'URL'),
        required=False,
    )

    height = schema.TextLine(
        title=_(u'Altura em pixels'),
        required=False,
    )


class IframeTile(PersistentCoverTile):
    is_configurable = True
    is_editable = True

    def getRemoteUrl(self):
        return self.data.get('remote_url', None)

    def getHeight(self):
        return self.data.get('height', None)
