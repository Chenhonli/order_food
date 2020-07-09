# -*- coding: utf-8 -*-
"""
@Author: chenftli
@Blog: https://blog.csdn.net/Chenftli
@CreateTime: 2020/7/9 16:33
"""
import hashlib, base64, random, string
import requests, json

from application import app


class MemberService:

    @staticmethod
    def geneAuthCode(menber_info=None):
        m = hashlib.md5()
        m_str = "%s-%s-%s" % (menber_info.id, menber_info.salt, menber_info.status)
        m.update(m_str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def geneSalt(length=16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range(length)]
        return ("".join(keylist))


    @staticmethod
    def getWeChatOpenId(code):
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}' \
              '&grant_type=authorization_code'.format(app.config['MINA_APP']['appid'],
                                                      app.config['MINA_APP']['appkey'], code)
        r = requests.get(url)
        res = json.loads(r.text)
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid
