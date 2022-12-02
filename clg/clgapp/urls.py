from . import views
from django.urls import path, include

urlpatterns = [

    path('',views.function,name='function'),
    path('home',views.home,name='home'),
    # path('form',views.form,name='form'),
    path("signup",views.signup,name="signup"),
    path('signin',views.signin,name='signin'),
    path('new',views.new,name='new'),
    path('submit', views.submit, name='submit'),
    path('action',views.action,name='action'),
# drop
    path('dp', views.index, name='index'),
    path('load-courses/', views.load_courses, name='ajax_load_courses'),

]