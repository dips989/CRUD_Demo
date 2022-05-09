from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import LoginTable, Department_Master, Student_data
from datetime import datetime
# Create your views here.

def login_form(request):

    return render(request, 'login_form.html')

@csrf_exempt
def login_ajax(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(email, password)
    if LoginTable.objects.filter(email=email, password=password).exists():
        print("Done")
        request.session['user_id'] = LoginTable.objects.get(email = email, password = password).id
        request.session['email'] = email
        response = "success"
    else:
        print("Not done")
        response = "invalid"
    return HttpResponse(response)

def dashboard_page(request):
    dept = Department_Master.objects.all()
    stud_data = Student_data.objects.all().order_by('-st_first_name')
    return render(request, 'dashboard_page.html', { 'dept': dept, 'stud_data':stud_data})

def user_logout(request):
    del request.session['email']
    print('session Deleted')
    return redirect('login_form')

@csrf_exempt
def save_student_ajax(request):
    if request.method == "POST":
        sid = request.POST.get('sid')
        first_name = request.POST.get('fn')
        last_name = request.POST.get('ln')
        age = request.POST.get('age')
        mobile = request.POST.get('mb')
        dept = request.POST.get('dept')
        print(dept)

        d = Department_Master.objects.get(pk=dept)
        if( sid==''):
            usr = Student_data(st_first_name=first_name, st_last_name=last_name, st_age=age, st_mobile=mobile, st_reg_date=datetime.now(), st_fk_dept=d)
            print("data saved")
        else:
            usr = Student_data(id=sid, st_first_name=first_name, st_last_name=last_name, st_age=age, st_mobile=mobile, st_reg_date=datetime.now(), st_fk_dept=d)
            print("data saved with id")
        usr.save()
        stud = Student_data.objects.values()
        student_data = list(stud)
        return JsonResponse({'status':'Save', 'student_data':student_data})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        student = Student_data.objects.get(pk=id)
        student_data = {"id":student.id, "fname":student.st_first_name, "lname":student.st_last_name, "age":student.st_age, "mobile":student.st_mobile}
        return JsonResponse(student_data)

def delete(request):
     if request.method == "POST":
        id = request.POST.get('sid')
        pi = Student_data.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
     else:
        return JsonResponse({'status':0})
