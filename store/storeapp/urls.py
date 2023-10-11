
from django.urls import path
from storeapp import views

urlpatterns = [
    path('home',views.homepage),
    path('contact',views.contactpage),
    path('about',views.aboutpage),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('add/<x>/<y>',views.add),
]
