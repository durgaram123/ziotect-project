

from django.db.models.fields import EmailField
from django.http import request
from django.shortcuts import render, redirect,get_list_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Details
from .models import News, Testimonial
from .models import Subscribe
from .forms import *
from django.contrib.auth.decorators import login_required


def home(request):
    product=News.objects
    test=Testimonial.objects
    top=Top.objects
    context={'form':SubscribeForm}
    if request.method == 'POST':
            product=Details()
            product.title=request.POST.get('title')
            product.phone_number=request.POST.get('phone_number')
            product.field_name=request.POST.get('field_name')
            product.body=request.POST.get('body')
            product.save()
    
    return render(request,'public/index.html',{'product':product,'test':test,'top':top} ,context)


def base(request):
       return render(request,'public/index.html')
    

def contact(request):
    if request.method == 'POST':
        product=Details()
        product.title=request.POST.get('title')
        product.phone_number=request.POST.get('phone_number')
        product.field_name=request.POST.get('field_name')
        product.body=request.POST.get('body')
        product.save()
        return redirect('contact')
    else:
      return render(request, 'public/contact.html', {'context':Details.objects.all })

    

def about(request):
    return render(request, 'public/about.html')

def service(request):
    return render(request, 'public/service.html')

def news(request):
    product=News.objects
    return render(request, 'public/news.html',{'product':product})

def card(request):
    return render(request, 'public/card.html')



#---------pluto------------>


@login_required(login_url="/login/")
def sub(request):
    forms=SubscribeForm(request.POST or None)
    if request.method =='POST':
        if forms.is_valid():
            product=Subscribe()
            product.email=request.POST.get('email')
            product.save()
            return redirect('home')
    
    return render(request,'public/index.html',{'context':Subscribe.objects.all})

@login_required(login_url="/login/")
def contact1(request):
    return render(request, 'private/contact1.html',{'context':Details.objects.all})

@login_required(login_url="/login/")
def dashboard_2(request):
    return render(request, 'private/dashboard_2.html')

@login_required(login_url="/login/")
def dashboard(request):
    return render(request, 'private/dashboard.html')


@login_required(login_url="/login/")
def index1(request):
    return render(request, 'private/index1.html')



def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('contact1')
        else:
            return render(request, 'private/login.html',{'error':'username or password is incorrect.'})
    else:
       return render(request, 'private/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')   
         
    else:
        return render(request, 'private/login.html')

#pluto news
@login_required(login_url="/login/")
def plutonews(request):
    return render(request, 'private/plutonews.html',{'context':News.objects.all})

def edit_1(request,id):
    get_id = News.objects.get(id = id)
    form = NewsForm(request.POST or None, request.FILES or None, instance=get_id)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('plutonews') 
    else:       
      return render(request, 'private/edit_1.html',{'context': News.objects.all(),'form': form})
    
def delete_1(request,id):
    get_id = News.objects.get(id=id)
    get_id.delete ()
    return redirect ('plutonews')

def add_1(request):
    forms_ = NewsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if forms_.is_valid():
            forms_.save()
            return redirect('plutonews')
    return render(request, 'private/add_1.html',{'context': News.objects.all(),'form': forms_})
#end pluto news


#Testimonial
@login_required(login_url="/login/")
def plutotest(request):
    return render(request, 'private/plutotest.html',{'context':Testimonial.objects.all})

def edit(request,id):
    get_id = Testimonial.objects.get(id = id)
    formtest = TestimonialForm(request.POST or None, request.FILES or None, instance=get_id)
    if request.method == 'POST':
        if formtest.is_valid():
            formtest.save()
            return redirect('plutotest') 
    else:       
      return render(request, 'private/edit.html',{'context': Testimonial.objects.all(),'form': formtest})
    
def delete_2(request,id):
    get_id = Testimonial.objects.get(id=id)
    get_id.delete ()
    return redirect ('plutOtest')

def add_2(request):
    forms_1 = TestimonialForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if forms_1.is_valid():
            forms_1.save()
            return redirect('plutotest')
    return render(request, 'private/add_2.html',{'context': Testimonial.objects.all(),'form': forms_1})

#end Testimonial

def settings(request):
    return render(request, 'private/settings.html')


def subscribe(request):
    return render(request, 'private/subscribe.html', {'context':Subscribe.objects.all})