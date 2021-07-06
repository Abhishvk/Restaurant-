from django.contrib.auth.models import User
from django.core.checks import messages
from django.shortcuts import redirect, render,HttpResponse
from .models import Customer, Customer1Form, ContactMessage,BookTable
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages as msg
def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":
        f=Customer1Form(request.POST)
        try:
            f.save()
        except ValueError:
            msg.error(request,"Please! Enter Data In Given Formate.")
            f=Customer1Form
            context={'form':f}
            return render(request,'form.html',context)
        except:
            msg.error(request,"Please! Enter Information in Given Formate.")
            f=Customer1Form
            context={'form':f}
            return render(request,'form.html',context)
        return redirect('/')
    else:
        f=Customer1Form
        context={'form':f}
        return render(request,'form.html',context)

def login_view(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        upass=request.POST.get('upass')
        user=authenticate(request,username=uname,password=upass)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            msg.error(request,"Please! Enter Valid Email or Password")
            return render (request,'login.html')
    else:
        return render (request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')


def contact_msg(request):
    if request.method=="POST":
        f=ContactMessage()
        f.name=request.POST.get('name')
        f.email=request.POST.get('email')
        f.phone=request.POST.get('phone')
        f.subject=request.POST.get('subject')
        f.message=request.POST.get('message')
        try:
            f.save()
            msg.success(request,"Message has Send Succesfuly.")
        except ValueError:
            msg.error(request,"Please! Enter Data in Rigth Format")
            return render(request,'contact.html')
        except:
            return render(request,'contact.html')
        return render(request,'contact.html')
    else:
        return render(request,'contact.html')

def book_table(request):
    if request.method=="POST":
        try:
            current_user=request.user
            f=BookTable()
            ph=Customer.objects.get(id=current_user.id)
            f.name=request.POST.get('name')
            if f.name=="":
                f.fname=current_user.first_name
                f.lname=current_user.last_name
                f.name=f.fname +" "+ f.lname

            f.email=request.POST.get('email')
            if f.email=="":
                f.email=current_user.email

            f.phone=request.POST.get('phone')
            if f.phone=="":
                f.phone=ph.phone

            f.bdate=request.POST.get('date')
            f.btime=request.POST.get('time')
            f.npeople=request.POST.get('people')
            
            f.bmessage=request.POST.get('message')
            if f.bmessage=="":
                f.bmessage="No Msg"
            f.customer=Customer.objects.get(id=current_user.id)
            f.save()
            msg.success(request,"Your Table had Booked Succesfuly.")
        except:
            msg.error(request,"Please! Enter Date in (YYYY-MM-DD) Format")
            return render (request,'booktable.html')
        return render (request,'booktable.html')
    else:
        return render(request,'booktable.html')


def edit_info(request):
    uid=request.session.get('uid')
    u=Customer.objects.get(id=uid)
    if request.method=="POST":
        f=Customer1Form(request.POST,instance=u)
        try:
            f.save()
        except ValueError:
            msg.error(request,"Please! Enter Data In Given Formate.")
            f=Customer1Form(instance=u)
            context={'form':f}
            return render(request,'form.html',context)
        except:
            msg.error(request,"Please! Enter Information in Given Formate.")
            f=Customer1Form(instance=u)
            context={'form':f}
            return render(request,'form.html',context)
        return redirect('/')
    else:
        f=Customer1Form(instance=u)
        context={'form':f}
        return render(request,'editinfo.html',context)
