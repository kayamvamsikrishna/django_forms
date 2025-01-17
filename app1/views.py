from django.shortcuts import render

# Create your views here.
from app1.forms import *
from app1.models import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topicname']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Topic is Created')



    return render(request,'h1.html',d)




def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topicname']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']

            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]
            WO.save()
            return HttpResponse('Webpage is Created')

    return render(request,'h2.html',d)

def insert_accessrecord(request):
    EWFO=AccessRecordForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=AccessRecordForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['name']
            na=WFDO.cleaned_data['date']
            TO=Webpage.objects.get(name=tn)
            WO=AccessRecord.objects.get_or_create(name=TO,date=na)[0]
            WO.save()
            return HttpResponse('Webpage is Created')

    return render(request,'h3.html',d)


















