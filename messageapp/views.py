from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg
# Create your views here.
def create(request):
    #print("Request is:",request.method)
    if request.method=="GET":
        #print("In if section")
        return render(request,'create.html')
    
    else:
        #fetch data from the form 
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        #validation 
        #insert 
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/dashboard')


def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)#fetch that object or row to be deleted
    #print(m)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    
    if request.method=="GET":
        m=Msg.objects.filter(id=rid)
        #select * from messageapp_msg where id=4;
        #print(m)
        context={}
        context['data']=m 
        return render(request,'edit.html',context)
    else:
        upname=request.POST['uname']
        upemail=request.POST['uemail']
        upmob=request.POST['mobile']
        upmsg=request.POST['msg']
        #print(upname)
        #print(upemail)
        #print(upmob)
        #print(upmsg)
        m=Msg.objects.filter(id=rid)
        m.update(name=upname,email=upemail,mobile=upmob,msg=upmsg)
        return redirect('/dashboard')

