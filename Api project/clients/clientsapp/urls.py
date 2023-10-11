from django.urls import path
from clientsapp import views

urlpatterns = [
    path('getclient',views.get_client),
    path('createclient',views.create_client),
    path('updateclient/<rid>',views.update_client),
    path('deleteclient/<rid>',views.delete_client),
]
   
