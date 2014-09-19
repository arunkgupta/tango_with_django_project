from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    # Requesting context of request to inputting in context
    context = RequestContext(request)
    
    # Setting up context_dict dictionary variable for template variable
    context_dict = {'boldmessage': "I am bold font from the context"}
    
    # returning response to client browser using template as first parameter
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    return render_to_response('rango/about.html', context)
