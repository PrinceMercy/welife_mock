import xmltodict
import time
import json

class WftPayOrder:
    def __init__(self,req_dict) -> None:
        self.req_dict = req_dict 
    
    
    # 下单接口
    def weixinjspay(self):
        print(self.req_dict['SpayWechatJspayReqBody'])
        # rep_dict = xmltodict.parse(pay_rep)
        # print(rep_dict['xml'])
        mch_id = self.req_dict['SpayWechatJspayReqBody']['mch_id']
        # print(int(time.time()*1000))
        # payinfo_dict = json.loads(rep_dict['xml']['pay_info'])
        # print(payinfo_dict)
        timeStamp = str(int(time.time()*1000))
        # rep_dict['xml']['pay_info'] = json.dumps(payinfo_dict)
        pay_rep = """<xml><appid><![CDATA[wx1f87d44db95cba7a]]></appid><charset><![CDATA[UTF-8]]></charset><device_info><![CDATA[HPAY_FIXATIONCODE_WXMINIAPP]]></device_info><mch_id><![CDATA[%s]]></mch_id><nonce_str><![CDATA[55a0a329004f4691813b0c4e9d1cab64]]></nonce_str><pay_info><![CDATA[{"timeStamp":%s,"callback_url":null,"package":"prepay_id=wx2414391080224610b34215c949183f0000","paySign":"F98B6C2C7F8172BBCE4DC51B87C79521","appId":"wx5ddb6c0a70a65956","signType":"MD5","nonceStr":%s,"status":"0"}]]></pay_info><result_code><![CDATA[0]]></result_code><sign><![CDATA[PLMAo7Snu0R0w7+20tDK1OJKsmASuQHBQkhqvmByMHpaP9jWzt3japbo/8Z4H/t3p53L35LtRzgqF9QPFz8QCBWRQEcR2N0ZCJF3FuCf1XEqSLP60aq3A2jpfkjEl3EDwEzGSnY3BmJS5riCjsHbiKKQHG+meinpMZ4uPHq//sfwk7b4muL0i3L64Esihhin+b2jj6JPzw2sojWhlB3h6hmyMr1EiM1IYbXAoDw82TVHoW5Yq1iPBD4BhthFAGzpKatpopiW3lDdOUpl5tZYpflc6PriO4GmbrxC19LGtR//VK+YOFX+jCYqXoMkWxFWLX/P9OiABjJXY447Rkiq7A==]]></sign><sign_type><![CDATA[RSA_1_256]]></sign_type><status><![CDATA[0]]></status><token_id><![CDATA[0bea3bba14a425b2a8c1cfc3e51cb13d5]]></token_id><version><![CDATA[2.0]]></version></xml>"""%(mch_id,timeStamp,timeStamp)
        rep_xml = pay_rep
        return rep_xml
    
    def queryorder(self):
        print(self.req_dict['SpayTradeQueryReqBody'])
        # rep_dict = xmltodict.parse(qo_rep)
        # print(rep_dict['xml'])
        mch_id = self.req_dict['SpayTradeQueryReqBody']['mch_id']
        open_app_id = self.req_dict['SpayTradeQueryReqBody']['open_app_id']
        # print(int(time.time()*1000))
        # payinfo_dict = json.loads(rep_dict['xml']['pay_info'])
        # print(payinfo_dict)
        # payinfo_dict['timeStamp'] = int(time.time()*1000)
        # rep_dict['xml']['pay_info'] = json.dumps(payinfo_dict)
        qo_rep = """<xml><appid><![CDATA[wx1f87d44db95cba7a]]></appid><bank_type><![CDATA[OTHERS]]></bank_type><cash_fee><![CDATA[2000]]></cash_fee><charset><![CDATA[UTF-8]]></charset><coupon_fee><![CDATA[0]]></coupon_fee><device_info><![CDATA[HPAY_FIXATIONCODE_WXMINIAPP_null]]></device_info><fee_type><![CDATA[CNY]]></fee_type><gmt_payment><![CDATA[20220321082230]]></gmt_payment><mch_id><![CDATA[%s]]></mch_id><mdiscount><![CDATA[0]]></mdiscount><nonce_str><![CDATA[136c34f9e16649bda6fbce0cda0e499f]]></nonce_str><open_app_id><![CDATA[%s]]></open_app_id><openid><![CDATA[owr_y4mVpOXEmZJPEHUKi_sNk8WY]]></openid><out_trade_no><![CDATA[2203212004185369586]]></out_trade_no><out_transaction_id><![CDATA[4200001375202203218743450265]]></out_transaction_id><result_code><![CDATA[0]]></result_code><sign><![CDATA[A2IPLk55o7c4PekJRypXdgLkUcIU+tlvZmde4M49DgXYbKVgV2XxAiZFgpOUC26NLvqLSiHWKwY79/HRhJAbnZ9Fk5UzZwZyreFfZqEoCtmBxl25AQZ3zpJSfTWONvixW4yIIFtglix272WqE7ubg9IyAeKAFCkgBwju2zYXSuPZ8irFD2UhEHrYby1G7pdvPqsusC4CRlYeroKuu4HiyPqwqTJAFVdCbN+kaag31M4uIXXT0hJXgURa/LRMvArBBIb7EAMuWl/Zdxm1hR9vWcGBiD0J2gaJt5UB8oXMQY8SJVZSpUU0FLaRL1JeWRBYIBBh8J54EoA7cqt1bvjZjA==]]></sign><sign_type><![CDATA[RSA_1_256]]></sign_type><status><![CDATA[0]]></status><sub_appid><![CDATA[wxe09a69b415762582]]></sub_appid><sub_openid><![CDATA[owr_y4mVpOXEmZJPEHUKi_sNk8WY]]></sub_openid><time_end><![CDATA[20220321082230]]></time_end><total_fee><![CDATA[2000]]></total_fee><trade_state><![CDATA[SUCCESS]]></trade_state><trade_type><![CDATA[pay.weixin.jspay]]></trade_type><transaction_id><![CDATA[159560003936202203217552726058]]></transaction_id><version><![CDATA[2.0]]></version></xml>"""%(mch_id,open_app_id)
        # rep_xml = xmltodict.unparse(rep_dict,pretty = True)
        rep_xml = qo_rep
        return rep_xml