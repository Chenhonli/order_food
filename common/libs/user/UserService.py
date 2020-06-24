# -*- encoding: utf-8 -*-
import hashlib, base64


class UserService:

    @staticmethod
    def genePwd(pwd, salt):
        m = hashlib.md5()
        m_str = "%s-%s" % (base64.encodebytes(pwd.encode('utf-8')), salt)
        m.update(m_str.encode('utf-8'))
        return m.hexdigest()