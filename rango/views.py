from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import Category, Page

def index(request):
    # Requesting context of request to inputting in context
    context = RequestContext(request)
    
    # getting top five category having maximum likes
    category_list = Category.objects.order_by('-likes')[:5]
    
    # Setting up context_dict dictionary variable for template variable
    context_dict = {'categories': category_list}
    
    for category in category_list:
        category.url = category.name.replace(' ', '_')
    
    # returning response to client browser using template as first parameter
    return render_to_response('rango/index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    return render_to_response('rango/about.html', context)

def category(request, category_name_url):
    context = RequestContext(request)
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name': category_name}
    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages 
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render_to_response('rango/category.html', context_dict, context)

