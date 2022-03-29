from flask import  Flask,request
import xmltodict
import time
import json
from wft.PayOrder import WftPayOrder
from wft.PublicTfpapiUnify import WftPublicApiUnify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/pay/openapi/gateway',methods=['get','post'])
def pay_order():
    req_str = str(request.get_data(),'utf-8')
    app.logger.info(req_str)
    req_dict = xmltodict.parse(req_str)
    po = WftPayOrder(req_dict)
    if req_dict.get('SpayWechatJspayReqBody'):
        rep_xml = po.weixinjspay()
    elif req_dict.get('SpayTradeQueryReqBody'):
        rep_xml = po.queryorder()
    app.logger.info(rep_xml)
    return rep_xml

@app.route('/public/tfpApi/unify',methods=['get','post'])
def  pubilc_tfpapi_unify():
    req_str = str(request.get_data(),'utf-8')
    app.logger.info(req_str)
    req_dict = xmltodict.parse(req_str)
    ptu = WftPublicApiUnify(req_dict)
    if req_dict.get('TfpMchQueryReqBody'):
        rep_xml = ptu.query_merchant_detail()
    elif req_dict.get('TfpPayNotifyReqBody'):
        rep_xml = ptu.pay_notify()
    app.logger.info(rep_xml)
    return rep_xml

if __name__ == '__main__':
    app.run(port=29991, debug=True, host='0.0.0.0')