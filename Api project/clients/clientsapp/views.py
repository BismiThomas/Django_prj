from django.shortcuts import render,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from clientsapp.models import Client,Project
from django.contrib.auth.models import User
import datetime
# Create your views here.
def get_client(request):
 c=Client.objects.all() 
 print(c)
 context={}
 #print("In get_client function")
 #res={'success':"Response from get_client"}
 i=0
 for x in c:
   context[i]={
     'id':x.id,
     'client_name':x.client_name,
     'created_at':x.created_at,
     'created_by':x.uid.first_name
    }
   i+=1
   
 print(context)
 json_data=json.dumps(context,default=str)
 return HttpResponse(json_data,content_type="application/json")#it tells the browser that the data is in json format
 
@csrf_exempt
def create_client(request):
  #print("In create_client function")
  print(request.method)
  print(request.POST)
  print(type(request.POST))
  cname=request.POST['cname']#var name should be same in key of postman
  user_id=request.POST['user_id']#var name should be same in key of postman
 # print(cname)
  #print(user_id)
  u=User.objects.filter(id=user_id)
  print(u)
  print(u[0])
  c=Client.objects.create(client_name=cname,uid=u[0])
  c.save()
  res={'success':"client created"}
  json_data=json.dumps(res)
  return HttpResponse(json_data,content_type="application/json")
 
@csrf_exempt
def update_client(request,rid):
  #print("In update_client function")
  print(request.method)
  print(request.body)
  d=json.loads(request.body)
  #print(d)
  #print(type(d))
  #print("Record ID:",rid)
  ucname=d['cname']
  c=Client.objects.filter(id=rid)
  print(c)
  c.update(client_name=ucname,updated_at=datetime.datetime.now())
  res={'success':"client updated"}
  json_data=json.dumps(res)
  return HttpResponse(json_data,content_type="application/json")
 
@csrf_exempt
def delete_client(request,rid):
  c=Client.objects.filter(id=rid)
  c.delete()
  print("In delete_client function")
  res={'success':"client deleted"}
  json_data=json.dumps(res)
  return HttpResponse(json_data,content_type="application/json")
 