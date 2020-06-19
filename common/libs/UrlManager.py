# -*- coding: utf-8 -*-


class UrlManager(object):

    def __init__(self):
        pass

    @staticmethod
    def builUrl(path):
        return path

    @staticmethod
    def builStaticUrl(path):
        ver = '%s' % ("202006171300")
        path = '/static' + path + "?ver=" + ver
        return UrlManager.builUrl(path)