from django.urls import path
from . import views
urlpatterns =[
  path('', views.index, name='index'),
  path('signup/',views.signup,name= 'signup'),
  path('login/',views.login,name= 'login'),
  path('housedetails/',views.housedetails,name='housedetails'),
  path('house/<int:house_id>/', views.house_details, name='house_details'),
]
