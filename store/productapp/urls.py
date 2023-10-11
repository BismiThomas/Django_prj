from django.urls import path
from productapp import views

urlpatterns = [
    path('home', views.homepage),
    path('addproduct',views.add_product),
    path('productdash',views.product_dashboard),
    path('delete/<pid>',views.delete_product), #<pid> should be same in views.py def of delete_product(request,pid)
    path('edit/<pid>',views.update_product),
]
