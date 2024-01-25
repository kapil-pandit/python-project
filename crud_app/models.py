from django.db import models

class Employee(models.Model):
    EmpId = models.CharField(max_length=3)
    EmpName = models.CharField(max_length=200)
    EmpGender = models.CharField(max_length=10)
    EmpEmail = models.EmailField()
    password = models.EmailField()
    EmpDesignation = models.CharField(max_length=150)
    class Meta:
        db_table="Employee"