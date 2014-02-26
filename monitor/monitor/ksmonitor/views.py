from django.shortcuts import render
import  zenoss_api
import json


# Create your views here.
def overview(request):
    return render(request,'overview.html',{})

def event(request):
    z = zenoss_api.ZenossAPIExample()
    d = z.get_events()
    context = {'events':d['events']}
    return render(request,'event.html',context)
