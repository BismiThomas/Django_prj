from django.shortcuts import render,HttpResponse

# Create your views here.

def homepage(request):
   # return HttpResponse("Hello from home page")
   context={}
   context['msg']="Hello,good afternoon"
   context['x']=100
   context['y']=200
   context['data']=[10,20,30,40,50,60]

   return render(request,"storeapp/home.html",context)

def contactpage(request):
    return HttpResponse("Hello from contact page")

def aboutpage(request):
    return HttpResponse("Hello from about page")

def edit(request,id):
    print("id to be edited:",id)
    return HttpResponse("Id to be updated:"+id)

def delete(request,id):
    print("deleted:",id)
    return HttpResponse("Deleted:"+id)

def add(request,x,y):
    res=int(x)+int(y)
    print("Addition is:",res)
    return HttpResponse("Addition is:"+str(res))