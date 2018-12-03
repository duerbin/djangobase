from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.template import loader

from .models import ManHandle
import os
from silenceCheck import getimagefile
def index(request):
    #return HttpResponse("hello this is webstudy index")
    latest_handle_list=ManHandle.objects.order_by('insertdata')[:5]
    print(latest_handle_list)
    template=loader.get_template('webstudy/index.html')
    context={
        'latest_handle_list':latest_handle_list,
    }
    return HttpResponse(template.render(context,request))


def detail(request,handle_name):
    try:
        handle=ManHandle.objects.get(pk=handle_name)
    except ManHandle.DoesNotExist:
        raise Http404("file name not exist")
    #return HttpResponse("You are looking at handlesvoice %s" % handle_name)

    basedir= os.path.abspath(os.path.dirname(__file__))
    staticwavdir=basedir+"/../static/wav/"
    wavpath=staticwavdir+handle.filename+".wav"
    imgpath=basedir+"/../static/img/"+handle.filename+".gif"

    getimagefile(wavpath,imgpath)
    return render(request,'webstudy/detail.html',{'handle':handle})


def updateResult(request):
    if request.method=='GET':
        print request.GET
    elif request.method=='POST':
        print request.POST.get('newresult')
