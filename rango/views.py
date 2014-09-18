from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango Says: Hello World! <a href='rango/about'>about</a>")

def about(request):
    return HttpResponse("About Us page ! <a href='/rango/'>Back to home</a>")
