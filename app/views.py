
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings
import random
import json
from django.http import JsonResponse
from django.db.models import Count
# from dateutil.relativedelta import relativedelta
from datetime import datetime
import datetime as dt
from django.core.serializers import serialize
from django.http import JsonResponse

# Create your views here.

def send_otp_email(otp, email):
    subject = "Verify your Email - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to verify your account is : " + \
        str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def send_psw_email(otp, email):
    subject = "Reset your Password - {}".format(email)
    print(otp)
    message = "Your 4-digit OTP to reset your password is : " + \
        str(otp) + ". Please don't share it with anyone else"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def Index(request):
    return render(request, "app/index.html")


def Register(request):
    # if email not in request.session:
    if request.method == "POST":
        fnd = User.objects.filter(email=request.POST['email'].lower())
        if len(fnd) == 0:
            name = request.POST['name']
            email = request.POST['email'].lower()
            password = request.POST['password']
            confirmPassword = request.POST['confirmPassword']
            if password == confirmPassword:
                AddUser = User.objects.create(
                    name=name,
                    email=email,
                    password=make_password(password)
                )
                messages.success(
                    request, "You have registered successfully. Please login to continue")
                return redirect("login")
            else:
                messages.error(
                    request, "Password and Confirm Password do not match. Please try again")
                return redirect("register")
        else:
            messages.error(request, "User already exists. Please login")
            return redirect("login")
    else:
        return render(request, "app/register.html")


def Login(request):
    # if email not in request.session:
    if request.method == "POST":
        email = request.POST['email'].lower()
        password = request.POST['password']
        fnd = User.objects.filter(email=email)
        if len(fnd) > 0:
            if check_password(password, fnd[0].password):
                request.session['id'] = fnd[0].id
                request.session['email'] = fnd[0].email
                request.session['is_member'] = fnd[0].is_member
                return redirect("advance-filter")
            else:
                messages.error(request, "Please enter a valid password")
                return redirect("login")
        else:
            messages.error(request, "User does not exist. Please register.")
            return redirect("register")
    else:
        return render(request, "app/login.html")


def Logout(request):
    if 'email' in request.session:
        del request.session['id']
        del request.session['email']
        del request.session['is_member']
        return redirect("index")
    else:
        return redirect("index")


def AdvanceFilter(request):
    if 'email' in request.session:
        if request.method == "POST":
            print(request.POST['query'])
            splittedQueries = json.loads(request.POST['splittedQueries'])
            
            parameters = [f.name for f in Stocks._meta.get_fields()]
            print(parameters)
            operators = ['>', '<', '+', '-', '*', '/', '=']
            sqlQuery = 'SELECT * FROM app_Stocks WHERE '
            for i in splittedQueries:
                print(type(i))
                if isinstance(i, str):
                    sqlQuery += f"{i.strip()} "
                else:
                    print(i)
                    i = [x.replace(" ", "") for x in i]
                    for t in i:
                        print(t)
                        try:
                            float_value = float(t)
                            sqlQuery += f"{t} "
                        except ValueError:
                            if t in operators:
                                sqlQuery += f"{t} "
                            else:
                                if t in parameters:
                                    sqlQuery += f"{t} "
                                else:
                                    return JsonResponse({"msgType": "error", "msg": "There seems to be an error in the query. Please select parameters from the given list."})
                    string = " ".join(i)
                print(sqlQuery)
            
            q = Stocks.objects.raw(sqlQuery + " ORDER BY Company")
            serialized_data = serialize('python', q)
            json_data = json.dumps(serialized_data, indent=4)
    
            return JsonResponse({"msgType": "success", "msg": json_data}, safe=False)
            # json_data = JsonResponse(serialized_data, safe=False)
            # json_data = json.dumps(json_data.json())
            # print(json_data)    
            # return JsonResponse({"msgType": "success", "msg": json_data})
        else:
            stocks = Stocks.objects.all().order_by('Company')
            return render(request, "app/advance-filter.html", {"stocks": stocks})
    else:
        messages.error(request, "Please login to view the advance filter")
        return redirect("login")


def SimpleFilter(request):
    query_result = Stocks.objects.all().order_by('Company')
    stocks = Stocks.objects.all().order_by('Company')
    return render(request, "app/simple-filter.html", {'stocks': stocks, 'query_result': query_result})


def FilterSimpleStocks(request):
    if request.method == "POST":
        print(request.POST)
        stocks = request.POST.getlist('stocks')
        query_result = Stocks.objects.filter(
            Company__in=stocks).order_by('Company')
        stocks = Stocks.objects.all().order_by('Company')
        return render(request, "app/simple-filter.html", {'stocks': stocks, 'query_result': query_result})


def Samp(request):
    if 'email' in request.session:
        if request.method == "POST":
            print(request.POST['query'])
            splittedQueries = json.loads(request.POST['splittedQueries'])
            
            parameters = [f.name for f in Stocks._meta.get_fields()]
            print(parameters)
            operators = ['>', '<', '+', '-', '*', '/', '=']
            sqlQuery = 'SELECT * FROM app_Stocks WHERE '
            for i in splittedQueries:
                print(type(i))
                if isinstance(i, str):
                    sqlQuery += f"{i.strip()} "
                else:
                    print(i)
                    i = [x.replace(" ", "") for x in i]
                    for t in i:
                        print(t)
                        try:
                            float_value = float(t)
                            sqlQuery += f"{t} "
                        except ValueError:
                            if t in operators:
                                sqlQuery += f"{t} "
                            else:
                                if t in parameters:
                                    sqlQuery += f"{t} "
                                else:
                                    return JsonResponse({"msgType": "error", "msg": "There seems to be an error in the query. Please select parameters from the given list."})
                    string = " ".join(i)
                print(sqlQuery)
            
            q = Stocks.objects.raw(sqlQuery + " ORDER BY Company")
            serialized_data = serialize('python', q)
            json_data = json.dumps(serialized_data, indent=4)
    
            return JsonResponse({"msgType": "success", "msg": json_data}, safe=False)
            # json_data = JsonResponse(serialized_data, safe=False)
            # json_data = json.dumps(json_data.json())
            # print(json_data)    
            # return JsonResponse({"msgType": "success", "msg": json_data})
        else:
            stocks = Stocks.objects.all().order_by('Company')
            return render(request, "app/samp2.html", {"stocks": stocks})
    else:
        messages.error(request, "Please login to view the advance filter")
        return redirect("login")
