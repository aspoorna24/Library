from django.shortcuts import redirect, render
from  home.models import Librarians,Sregistr,Book,Issu
from django.contrib import messages
from  datetime import datetime
context1={
    "user":"passed","usn":" ","iss":" "
}
stu={'stn':" ",'usern':" ",'books':" ","bl":" ","iss":" "}
passed = False
passed1 = False
# Create your views here.
def home(request):
    global passed
    passed = False 
    return render(request, 'home.html')

def Librarian(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Librarians.objects.filter(email=email,password=password):
            x = Librarians.objects.filter(email=email,password=password)
            uname = (str(x).split(" "))
            n=uname[2].split(">")
            nu = n[0]
            stu.update({"usern":nu })
            global passed
            passed = True
            return redirect("main")
        else:
             messages.warning(request,"WRONG USERNAME OR PASSWORD!!.")
    return render(request, 'index.html')
    #return HttpResponse("thid is homepage")
    
def main(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        if request.method=="POST":
            stu.update({"usern":"passed"})
            
            return redirect("home")
        return render(request,'Lhp.html',stu)

def book(request):
     if(passed==False):
        return redirect("error")
     if(passed==True):
        return render(request,'Lbk.html',stu)

def sl(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        stn=Sregistr.objects.all()
        stu.update({'stn':stn})
        return render(request,'sl.html',stu)

def sreg(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        if request.method=="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            usn=request.POST.get('usn')
            passw=request.POST.get('pass')
            if(passw==password):
                Sregist = Sregistr(name=name,email=email,usn=usn,password=password)
                Sregist.save()
                messages.success(request,"STUDENT INFO IS SUBMITTED")
            else:
                messages.warning(request,"PASSWORD IS NOT MATCHING")
        return render(request,'Lsr.html',stu)



def Students(request):
    if request.method=="POST":
        usn=request.POST.get('usn')
        password=request.POST.get('password')
        if Sregistr.objects.filter(usn=usn,password=password):
            x = Sregistr.objects.filter(usn=usn,password=password)
            uname = (str(x).split(" "))
            n=uname[2].split(">")
            nu = n[0]
            global us
            us = usn
            context1.update({"user":nu })
            global passed1
            passed1 = True
            print(nu)
            return redirect("mains")
        else:
            print("Wrong")
            messages.warning(request,"WRONG USERNAME OR PASSWORD!!.")
    return render(request, 'student.html')



def mains(request):
    if(passed1==False):
        return redirect("error")
    if(passed1==True):
        if request.method=="POST":
            context1.update({"user":"passed"})
            return redirect("home")
        iss=Issu.objects.filter(usn=us).all()
        context1.update({'iss':iss})           
        return render(request,'Shp.html',context1)



def insertbook(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        if request.method=="POST":
            name=request.POST.get('name')
            bkid=request.POST.get('bkid')
            aut=request.POST.get('aut')
            if Book.objects.filter(book_id=bkid):
                messages.warning(request,"Book id is already existing")
            else:
                book=Book(book_name=name,book_id=bkid,author=aut,date=datetime.today())
                book.save()
                messages.success(request,"Book is added!!.")
        return render(request,'insertbook.html',stu)

def bookava(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        stn=Book.objects.all()
        stu.update({'book':stn})
        return render(request,'bookava.html',stu)  

def booklib(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        l = Book.objects.values('book_name').distinct()
        stu.update({"bl":l})
        return render(request,'booklib.html',stu)  



def issue(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        if request.method=="POST":
            bkid = request.POST.get('bkid')
            usn = request.POST.get('usn')
            book = request.POST.get('book')
            if Book.objects.filter(book_id=bkid):
                if Sregistr.objects.filter(usn=usn):
                    a = Issu.objects.filter(usn=usn).all()
                    if(len(a)>=2):
                        messages.warning(request,"User have already 2 books")
                    else:
                        if  Issu.objects.filter(book_id=bkid):
                            messages.warning(request,"Book is Already Taken")
                        else:
                            issus=Issu(book_name=book,book_id=bkid,usn=usn,date=datetime.today())
                            issus.save()
                            messages.success(request,"ISSUED!!.")
                else:
                    messages.warning(request,"Data is not matching!!")
            else:
                messages.warning(request,"Failed!!.")

        return render(request,'issue.html',stu)



def issulist(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        iss=Issu.objects.all()
        stu.update({'iss':iss})
        return render(request,'issulist.html',stu)
          

def retur(request):
    if(passed==False):
        return redirect("error")
    if(passed==True):
        if request.method=="POST":
            bkid = request.POST.get('bkid')
            if  Issu.objects.filter(book_id=bkid):
                i = Issu.objects.filter(book_id=bkid)
                i.delete()
                messages.success(request,"Retured")
            else:
                messages.warning(request,"Book is not issued yet")
        return render(request,'retur.html',stu)



def error(request):
    return render(request,'404.html')