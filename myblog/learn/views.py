#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"你好，欢迎！")
def home(request):
	title_string = 'django study'
	content_dict = {'sports': 'http://www.hupu.com','news':'http://www.163.com',
					'economy':'http://zhongguojingji.com','finance':'http://www.finance.com',
					'life':'http://www.life.com',
					'travel':'http://www.travel.com'}
	return render(request, 'learn/home.html', {'title': title_string,'content_list': content_dict})
def cal(request):
    operator_a = request.GET['a']
    operator_b = request.GET['b']
    
    if  request.GET['opt'] == 'add':
        result = float(operator_a) + float(operator_b)
    elif request.GET['opt'] == u'sub':
        result = float(operator_a) - float(operator_b)
    elif request.GET['opt'] == u'multi':
        result = float(operator_a) * float(operator_b)
    elif request.GET['opt'] == u'div':
        result = float(operator_a) / float(operator_b)
    else:
        result = u"输入错误，请重试！"
    return HttpResponse(u"结果：%s" % (str(result)))

def cal2(request, a, b):
    operator_a = a
    operator_b = b
    result = float(operator_a) + float(operator_b)
    return HttpResponse(u"结果：%s" % (str(result)))
    
    

# Create your views here.
