from django.shortcuts import render,HttpResponse,redirect
from productapp.models import Product

# Create your views here.
def homepage(request):
    return HttpResponse("hello from product app")

def add_product(request): 
    print("Method Name:",request.method)
    if request.method=="GET":
        print("In if get section")
        return render(request,'product/store_product.html')
    else:  #retrieving the data
     name=request.POST['pname']
     price=request.POST['price']
     qty=request.POST['qty']
     category=request.POST['cat']
     is_available=request.POST['avail']


     print("Product name:",name)# printing the data in terminal
     print("Product price:",price)
     print("Quantity:",qty)
     print("Category:",category)
     print("is_available:",is_available)
      
      #creating the model obj & inserting the record
     p=Product.objects.create(name=name,price=price,qty=qty,cat=category,is_vail=is_available)
     #print(p)
     p.save()
     return redirect("/productapp/productdash")
     #return HttpResponse("In data fetched")
    
def product_dashboard(request):
   context={} #creating the dictionary
   #fetch data from model/table
   p=Product.objects.all()
   '''
   print(p)
   print(p[0])#accessing the single object
   print(p[1])

   print("Product Name:",p[0].name)# accessing("product name:",object.datamember name)
   print("Product price:",p[0].price)
   print("Product Name:",p[1].name)
   print("Product price:",p[1].price)
# using for loop
   for x in p:
      print(x)
      print(x.name)
      print(x.price)
      '''
   context['products']=p #assigning
   return render(request,'product/dashboard.html',context)#passing the data to the dashboard

def delete_product(request,pid):
      #fetch object to be deleted
      p=Product.objects.filter(id=pid)
      print("object deleted:",p)
      #delet the object
      p.delete()
      #redirect to dashboard
      return redirect("/productapp/productdash") 
   
      return render(request,'product/dashboard.html')

def update_product(request,pid):
   p=Product.objects.filter(id=pid)
   if request.method=="GET":
    context={} #creating the dictionary
    context['product']=p
    return render(request,'product/editproduct.html',context)

    #print(p)
    #return HttpResponse("data fetched")
   else: #fetching the data from update product
    uname=request.POST['pname']
    uprice=request.POST['price']
    uqty=request.POST['qty']
    ucat=request.POST['cat']
    uavail=request.POST['avail']

   ''' print(uname)
    print(uprice)
    print(uqty)
    print(ucat)
    print(uavail)'''
   
   p.update(name=uname,price=uprice,qty=uqty,cat=ucat,is_vail=uavail)# name=models.py datamembers
   return redirect('/productapp/productdash')

   #return HttpResponse("Data fetched")