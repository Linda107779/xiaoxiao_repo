# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import  request
import hashlib
import werkzeug
from lxml import etree

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class WeixinServer(http.Controller):


    def check_signature(self, signature, timestamp, nonce):
        L = [timestamp, nonce, 'weixinxiaoxiao']
        L.sort()
        s = L[0] + L[1] + L[2]
        return hashlib.sha1(s).hexdigest() == signature

    @http.route('/MP_verify_sjFn3qdwQxTBwxKl.txt', auth='public', csrf=False)
    def index2(self):
        import os
        print os.getcwd()
        return open(os.path.join(os.getcwd(), 'MP_verify_sjFn3qdwQxTBwxKl.txt')).read()

    @http.route('/weixin_server/', auth='public', csrf=False)
    def echo(self, **kwargs):
        # print dir(request)
        print request.params
        print request.httprequest.data



        # root = tree.getroot()

        signature = kwargs.get('signature')
        timestamp = kwargs.get('timestamp')
        nonce = kwargs.get('nonce')
        echostr = kwargs.get('echostr')
        print 'echosrt %s' % echostr
        # if self.check_signature(signature, timestamp, nonce):
        if True:

            if echostr:
                print '输出的数据是多少?'
                return echostr
            else:
                print u'走的是这条路吗!!!'

                data = request.httprequest.data
                print u'data is %s' % data
                tree = etree.fromstring(data)
                parse = etree.XMLParser(strip_cdata=False)
                parsed = etree.XML(data, parse)

                a = parsed.xpath('//ToUserName')[0]
                a_text = a.text
                b = parsed.xpath('//FromUserName')[0]
                b_text = b.text

                #content = parsed.xpath('//Content')[0]
                #context_text = content.text
		#content.text = u'![CDATA[%s]]' % u'kkkkk'

                a.text = u'![CDATA[%s]]' % b_text
                b.text = u'![CDATA[%s]]' % a_text

                # content.text = u''

                print etree.tostring(parsed)

                response = werkzeug.wrappers.Response()
                response.mimetype = 'text/xml'

                response.data = etree.tostring(parsed)
                return response
                # return 'success'

        else:
            return 'error'



        # @http.route('/weixin_server/', auth='public', csrf=False)
    # def echo(self, echostr, signature, timestamp, nonce):
    #     # print dir(request)
    #     print request.params
    #     print request.httprequest.data
    #     if self.check_signature(signature, timestamp, nonce):
    #         return echostr
    #        # return '<xml> \
    #        #          <ToUserName><![CDATA[toUser]]></ToUserName> \
    #        #          <FromUserName><![CDATA[fromUser]]></FromUserName> \
    #        #          <CreateTime>12345678</CreateTime> \
    #        #          <MsgType><![CDATA[text]]></MsgType> \
    #        #          <Content><![CDATA[你好]]></Content> \
    #        #      </xml>'
    #     else:
    #         return 'error'




#     @http.route('/weixin_server/weixin_server/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/weixin_server/weixin_server/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('weixin_server.listing', {
#             'root': '/weixin_server/weixin_server',
#             'objects': http.request.env['weixin_server.weixin_server'].search([]),
#         })

#     @http.route('/weixin_server/weixin_server/objects/<model("weixin_server.weixin_server"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('weixin_server.object', {
#             'object': obj
#         })
