from django.db import models

class Labourdetails(models.Model):
  employee_name = models.CharField(max_length=255)
  employee_id = models.CharField(max_length=255)
  employee_age = models.CharField(max_length=255)
  department = models.CharField(max_length=255)
  task = models.CharField(max_length=255)
  due_date = models.CharField(max_length=255)
  start_time = models.CharField(max_length=255)
  end_time = models.CharField(max_length=255)
  list_type=['labourdata.html']