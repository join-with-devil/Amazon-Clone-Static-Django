from django.urls import path
from . import views

urlpatterns=[
    path('payment',views.amzonpay,name="amazonpay")
]