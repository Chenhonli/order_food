# -*- coding: utf-8 -*-


class UrlManager(object):
    @staticmethod
    def builUrl(path):
        return path

    @staticmethod
    def builStaticUrl(path):
        path = path + "?ver=" + "202006171300"
        return UrlManager.builUrl(path)