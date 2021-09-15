from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path('',views.index, name = "index"),
    path('<int:couses_id>' , views.do_couses , name = "couses"),
    path('<int:couses_id>/book' , views.book , name = "book"),
    
]