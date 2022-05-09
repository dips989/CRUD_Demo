from django.contrib import admin
from crud_app.models import LoginTable
from .models import Department_Master
from .models import Student_data
# Register your models here.

class LoginTableAdmin(admin.ModelAdmin):
    list_display = ["email", "password"]

admin.site.register(LoginTable, LoginTableAdmin)
admin.site.register(Department_Master)
admin.site.register(Student_data)
