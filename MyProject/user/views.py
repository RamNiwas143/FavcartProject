from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.db import connection
# Create your views here.
#########################################################################################
def index(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    x=category.objects.all().order_by('-id')[0:6]
    pdata = myproduct.objects.all().order_by('-id')[0:7]
    mydict = {"data": x, "prodata": pdata,"cart":ct}
    return render(request,'user/index.html',context=mydict)


#########################################################################################
def about(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    return render(request,'user/aboutus.html',{"cart":ct})


#########################################################################################

def product(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    return render(request,'user/product.html',{"cart":ct})
############################################################################################

def myorder(request):
    user=request.session.get('userid')
    oid=request.GET.get('oid')
    pdata=""
    ddata=""
    if user:
        if oid is not None:
            morder.objects.all().filter(id=oid).delete()
            return HttpResponse("<script>alert('Your Order has been Canclled....');location.href='/user/myorder/'</script>")
        cursor=connection.cursor()
        cursor.execute("select p.*,o.* from user_myproduct p,user_morder o where p.id=o.pid and o.userid='"+str(user)+"' and o.remarks='pending'")
        pdata=cursor.fetchall()
        cursor.execute("select p.*,o.* from user_myproduct p,user_morder o where p.id=o.pid and o.userid='" + str( user) + "' and o.remarks='Delivered'")
        ddata = cursor.fetchall()


    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    return render(request,'user/myorder.html',{"cart":ct,"pdata":pdata,"ddata":ddata})

##############################################################################################################

def enquiry(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    status = ""
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mob')
        d=request.POST.get('msg')
        contactus(Name=a,Mobile=c,Email=b,Message=d).save()
        status = True

#######################################################################

       # mdict={"Name":a,"Email":b,"Mobile":c,"Message":d}

    msg = {"m":status, "cart":ct}
    return render(request,'user/enquiry.html',context=msg)

#################################################################
def signup(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mob')
        d=request.POST.get('passwd')
        e=request.FILES.get('ppic')
        f=request.POST.get('address')
        x=register.objects.all().filter(email=b).count()
        if x==0:
            register(name=a,mobile=c,email=b,passwd=d,ppic=e,address=f).save()
            return HttpResponse("<script>alert('You Are registerd Successfully...');location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('Your email id already registerd ...');location.href='/user/signup/'</script>")


    return render(request, 'user/signup.html')

################################################################################
def signout(request):
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('you are signed out..');location.href='/user/index/'</script>")
#################################################################################

def myordr(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    user=request.session.get('userid')
    pid=request.GET.get('msg')
    if user:
        if pid is not None:
            morder(userid=user,pid=pid,remarks="pending",odate=datetime.now().date(),status=True).save()
            return HttpResponse("<script>alert('your order confirmed..');location.href='/user/index/'</script>")
    else:
        return HttpResponse("<script>alert('you have to login first..');location.href='/user/myordr/'</script>")
    return render(request,'user/myordr.html',{"cart":ct})

#################################################################################

##################################################################################

def myprofile(request):
    user=request.session.get('userid')
    x=""
    if user:
        if request.method=="POST":
            a = request.POST.get('name')
            c = request.POST.get('mob')
            d = request.POST.get('passwd')
            e = request.FILES.get('ppic')
            f = request.POST.get('address')
            register(email=user,name=a,mobile=c,ppic=e,passwd=d,address=f).save()
            return HttpResponse("<script>alert('Your profile Updated Successfully..');location.href='/user/myprofile/'</script>")

        x=register.objects.all().filter(email=user)
    return render(request,'user/myprofile.html',{"mdata":x})

#######################################################################################

def signin(request):
    if request.method=="POST":
       Email= request.POST.get('email')
       Passwd=request.POST.get('passwd')
       x=register.objects.all().filter(email=Email,passwd=Passwd).count()
       y=register.objects.all().filter(email=Email,passwd=Passwd)
       if x==1:
           request.session['userid']=Email
           request.session['userpic']=str(y[0].ppic)
           return HttpResponse("<script>alert('login Successfully..');location.href='/user/myprofile'</script>")
       else:
           HttpResponse("<script>alert('Your userId or password is incorrect..');location.href='/user/signin'</script>")

    return render(request,'user/signin.html')


##########################################################################################################
def mens(request):
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().filter(mcategory=4)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=4,pcategory=cid)

    mydict={"cats":cat, "data":d,"a":cid}
    return render(request,'user/mens.html',mydict)

################################################################################################################

def womens(request):
    cid = request.GET.get('msg')
    cat = category.objects.all().order_by('-id')
    d = myproduct.objects.all().filter(mcategory=5)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=5, pcategory=cid)

    mydict = {"cats": cat, "data": d, "a": cid}
    return render(request,'user/womens.html',mydict)

##############################################################################################################

def kids(request):
    cid = request.GET.get('msg')
    cat = category.objects.all().order_by('-id')
    d = myproduct.objects.all().filter(mcategory=6)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=6, pcategory=cid)

    mydict = {"cats": cat, "data": d, "a": cid}
    return render(request,'user/kids.html',mydict)

##############################################################################################################

def viewproduct(request):
    a=request.GET.get('msg')
    x=myproduct.objects.all().filter(id=a)
    return render(request,'user/viewproduct.html',{"pdata":x})

#################################################################################################################


def mycart(request):
    p=request.GET.get('pid')
    user= request.session.get('userid')
    if user:
        if p is not None:
            mcart(userid=user,pid=p,cdate=datetime.now().date(),status=True).save()
            return HttpResponse("<script>alert('Your Item Is Added cart..');location.href='/user/index/'</script>")
    else:
        return HttpResponse("<script>alert('You Have To Login First...');location.href='/user/signin/'</script>")
    return render(request,'user/mcart.html')
#################################################################################################


def showcart(request):
    user=request.session.get('userid')
    a=request.GET.get('msg')
    cid=request.GET.get('cid')
    pid=request.GET.get('pid')
    cdata=""
    if user:
        if a is not None:
            mcart.objects.all().filter(id=a).delete()
            return HttpResponse("<script>alert('Your Item are deleted from cart..');location.href='/user/showcart/'</script>")
        elif pid is not None:
            mcart.objects.all().filter(id=cid).delete()
            morder(userid=user,pid=pid,remarks="pending",status=True,odate=datetime.now().date()).save()
            return HttpResponse("<script>alert('Your order has been Placed successfully..');location.href='/user/myorder/'</script>")
        cursor=connection.cursor()
        cursor.execute("select p.*,c.* from user_myproduct p,user_mcart c where p.id=c.pid and c.userid='" + str(user) + "'")
        cdata=cursor.fetchall()

    return render(request,'user/showcart.html',{"cdata":cdata})


####################################################################################################

def cpdetail(request):
    c=request.GET.get('cid')
    p=myproduct.objects.all().filter(pcategory=c)
    return render(request,'user/cpdetail.html',{"pdata":p,})

####################################################################################################