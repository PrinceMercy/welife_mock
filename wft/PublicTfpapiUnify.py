

class WftPublicApiUnify:
    def __init__(self,req_dict) -> None:
        self.req_dict = req_dict
    
    def query_merchant_detail(self):
        rep_str = """<?xml version='1.0' encoding='UTF-8'?><xml><mch_pay_conf_list>[{"thi_pay_org_id":2,"pay_center_id":4,"pay_type_id":100007297,"pay_api_code":"pay.alipay.jspayv8","pay_api_type":"pay.alipay.jspay"},{"thi_pay_org_id":2,"pay_center_id":4,"pay_type_id":100007296,"pay_api_code":"pay.alipay.micropayv8","pay_api_type":"pay.alipay.micropay"},{"thi_pay_org_id":2,"pay_center_id":4,"pay_type_id":100007295,"pay_api_code":"pay.alipay.nativev8","pay_api_type":"pay.alipay.native"},{"thi_pay_org_id":1,"pay_center_id":66,"pay_type_id":10000052,"pay_api_code":"pay.weixin.jspay","pay_api_type":"pay.weixin.jspay"},{"thi_pay_org_id":1,"pay_center_id":66,"pay_type_id":10000054,"pay_api_code":"pay.weixin.micropay","pay_api_type":"pay.weixin.micropay"},{"thi_pay_org_id":1,"pay_center_id":66,"pay_type_id":10000053,"pay_api_code":"pay.weixin.native","pay_api_type":"pay.weixin.native"}]</mch_pay_conf_list><merchant_id>208500000082</merchant_id><merchant_name>Jane测试商户</merchant_name><pay_accpet_org>208520000001</pay_accpet_org><result_code>0</result_code><sign>G9sUKGCMK4fj6CNaS7t1DKlcs7uzGfm/kXZY5P0w/QK7Ck/8aOs1RxuHWuhYexucnYzsAklIjEUwkogG0wSXU/zsNPCoiwZq0eGW7auZaXo/p661Ox+8nkNOlb1BwC1WiVWqAy5W9FBnyDS87GMUwn3qkZzK2Mpn9Pfx+xpjvD4=</sign><status>0</status><version>1.0</version></xml>"""
        return rep_str
    
    def pay_notify(self):
        rep_str = """
        
        """
        return rep_str