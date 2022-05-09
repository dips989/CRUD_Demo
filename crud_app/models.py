from django.db import models

# Create your models here.

class LoginTable(models.Model):
    email = models.EmailField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "LoginTable"

#Master table for ForeignKey
class Department_Master(models.Model):
    dept_name = models.CharField(max_length=50)
    dept_course = models.CharField(max_length=50)
    def __str__(self):
        return self.dept_name

    class Meta:
        verbose_name_plural = "Department_Master"

class Student_data(models.Model):
    st_first_name = models.CharField(max_length=50, null=True, blank=True)
    st_last_name = models.CharField(max_length=50, null=True, blank=True)
    st_age = models.IntegerField()
    st_mobile = models.CharField(max_length=25, null=True, blank=True)
    st_reg_date = models.DateField(null=True, blank=True)
    st_fk_dept = models.ForeignKey(Department_Master, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.st_first_name
