from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello(request):
    name = "nasim"
    html = "<html><body>It is now working %s </body></html>" %name
    return HttpResponse(html)


