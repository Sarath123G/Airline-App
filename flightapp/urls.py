from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns=[

path('',views.dashboard,name='dashboard'),

path('register/',views.register,name='register'),

path('login/',auth.LoginView.as_view(template_name='login.html'),name='login'),

path('logout/',auth.LogoutView.as_view(),name='logout'),

path('addflight/',views.add_flight,name='addflight'),

path('edit/<int:id>/',views.edit_flight,name='edit'),

path('delete/<int:id>/',views.delete_flight,name='delete'),

path('addpassenger/',views.add_passenger,name='addpassenger'),

path('book/',views.book,name='book'),

]