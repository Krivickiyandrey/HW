from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import datetime

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {'message':'Hello django templates'}
    return HttpResponse(template.render(context, request))


def query(request):
    return HttpResponse(request.GET('test'))

def result(request):
    template = loader.get_template('result.html')
    f1 = request.POST.get('F1')
    f2 = request.POST.get('F2')
    f3 = request.POST.get('F3')
    if len(f1) > len(f2):
        if len(f1) > len(f3):
            max = f1
        else:
            max = f3
    else:
        if len(f2) > len(f3):
            max = f2
        else:
            max = f3
    context = {'message': max}
    return HttpResponse(template.render(context, request))

def dateshow(request):
    template = loader.get_template('dateshow.html')
    context = {'msg': 'Формат Месяц/День'}
    return HttpResponse(template.render(context, request))

def show(request):
    template = loader.get_template('show.html')
    template1 = loader.get_template('show1.html')
    context = {'msg': datetime.datetime.today().strftime("%Y"),
               'msg2': datetime.datetime.today().strftime("%Y-%m-%d")}
    if str(request.POST.get('dataRN')) == '01/01':
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template1.render(context, request))
