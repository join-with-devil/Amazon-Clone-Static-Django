from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('computer',views.computer,name="computer"),
    path('sell',views.sell,name="sell"),
    path('mobiles',views.mobiles,name="mobiles"),
    path('fresh',views.fresh,name="fresh"),
    path('signup',views.signup,name="signup"),
    path('newrelease',views.newrelease,name="newrelease"),
    path('fashion',views.fashion,name="fashion"),
    path('bestseller',views.bestseller,name="bestseller"),
    path('customserv',views.customserv,name="customserv"),
    path('todaydeals',views.todaydeals,name="todaydeals"),
    path('electronics',views.electronics,name="electronics"),
    path('handk',views.handk,name="handk")
]