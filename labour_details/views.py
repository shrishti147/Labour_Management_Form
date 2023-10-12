from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from labour_details.models import Labourdetails
from django.contrib import admin

def labour_details(request):
  template = loader.get_template('labourform.html')
  return HttpResponse(template.render())
  return HttpResponse('django!')
@csrf_exempt
def labourdata(request):
    if request.method == 'POST':
        Employeename= request.POST['employee_name']
        Employeeid= request.POST['employee_id']
        Employeeage= request.POST['employee_age']
        Department= request.POST['department']
        Task= request.POST['task']
        Due_date = request.POST['due_date']
        Start_time = request.POST['start_time']
        End_time = request.POST['end_time'] 


        labourtable = Labourdetails(
           employee_name= Employeename,
           employee_id = Employeeid,
           employee_age = Employeeage,
           department = Department,
           task = Task,
           due_date = Due_date,
           start_time = Start_time,
           end_time = End_time
        )
        labourtable.save()
        cc = {
           'employee_name': Employeename,
           'employee_id' : Employeeid,
           'employee_age' : Employeeage,
           'department' : Department,
           'task' : Task,
           'due_date' : Due_date,
           'start_time' : Start_time,
           'end_time' : End_time
        }
        #return render(request,'labourdata.html')

  #context = request.POST
  #print(context)
  
        labourtable= Labourdetails.objects.all().values()
        
        template = loader.get_template('labourdata.html')
        context={'labourtable':labourtable}
        #print(context)
        return render(request, "labourdata.html", {'labourtable':labourtable})
        return HttpResponse(template.render(cc,request))


'''def testing(request):
  template = loader.get_template('labourdata.html')
  context = {
            'labourdetails': Labourdetails,
             }
  return HttpResponse(template.render(context, request))'''
    
    
#admin.site.register(Labourdetails)
