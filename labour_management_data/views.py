from django.http import HttpResponse
from django.template import loader

def labour_management_data(request):
  template = loader.get_template('1.html')
  return HttpResponse(template.render())
  return HttpResponse('python!')

