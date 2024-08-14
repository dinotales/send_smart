from django.urls import path
from login.views import cadastro, loginView, logout_view
 
app_name='login'

urlpatterns=[
    path ('cadastro',cadastro, name='cadastro'),
    path ('login',loginView, name='login'),
    path ('logout',logout_view, name='logout'),

]