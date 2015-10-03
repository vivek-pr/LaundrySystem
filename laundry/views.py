from django.shortcuts import render
from .models import Person,detail,Cloth
from .form import PersonForm,LoginForm,ClothForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def check(request):
    form=LoginForm(request.POST)
    user_nam=form.data['login_id']
    passw=form.data['password']
    det=Person()
    det=Person.objects.get(user_name=user_nam,password=passw)
    request.session['name']=det.first_name+" "+det.last_name
    request.session['u_name']=user_nam
    context={"f_name":det.first_name}
    return render(request,"home.html",context)

def newCloth(request):
    form=ClothForm(request.POST)
    context={
    'form':form
    }
    return render(request,"cloth.html",context)

def addCloth(request):
    form=ClothForm(request.POST or None)
    context={'form':form}
    if form.is_valid():
        #user_name=request.session['u_name']
        person=Person.objects.get(user_name='vivekpradhan1')
        person=person
        Cloth_type=form.cleaned_data["cloth_type"]
        Catagory=form.cleaned_data["catagory"]
        Color=form.cleaned_data["color"]
        Brand=form.cleaned_data["brand"]
        Material=form.cleaned_data["material"]
        Status=form.cleaned_data["status"]
        Cost=form.cleaned_data["cost"]
        context['cloth']=Cloth_type
        data_val=Cloth(person=person,cloth_type=Cloth_type,catagory=Catagory,color=Color,brand=Brand,material=Material,status=Status,cost=Cost)
        data_val.save()
    return render(request,'cloth.html',context)

def clothdisplay(request):
    user=Person.objects.get(user_name='vivekpradhan1')
    listdata=Cloth.objects.get(person=user)
    print(listdata)
    context={
    'data':listdata
    }
    return render(request,'clothdisplay.html',context)



def PersonRegister(request):
    form=PersonForm(request.POST or None)
    context={"form":form}
    return render(request,"registration_form.html",context)


def login(request):
    form=LoginForm()
    context={
    "form":form
    }
    return render(request,"login.html",context)

def home(request):
    return render(request,"home.html",{})


def PersonValue(request):
    if request.method=='POST':
        instance=form.save()
    return render(request,"home.html",{})

@csrf_exempt
def register(request):
    form1=LoginForm()
    context={
    "form":form1
    }
    form=PersonForm(request.POST)
    f_name=form.data["first_name"]
    #photo=form.data["photos"]
    if form.is_valid():
        u_name=form.cleaned_data["user_name"]
        f_name=form.cleaned_data["first_name"]
        print(f_name)
        l_name=form.cleaned_data["last_name"]
        sex=form.cleaned_data["sex"]
        phone_no=form.cleaned_data["phone_no"]
        email_id=form.cleaned_data["email_id"]
        sec_phone_no=form.cleaned_data["secondary_phone_no"]
        address=form.cleaned_data["address"]
        passw=form.cleaned_data["password"]
        print(f_name)
        #photo=form.cleaned_data["photos"]
        new_user=Person(user_name=u_name,first_name=f_name,last_name=l_name,sex=sex,address=address,email_id=email_id,phone_no=phone_no,secondary_phone_no=sec_phone_no,password=passw)
        new_user.save()
    return render(request,"login.html",context)
