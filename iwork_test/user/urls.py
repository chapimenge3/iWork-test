from django.urls import path, include

# DRF import
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


# My app imports 
from .views import CreateUserView 

router = DefaultRouter()
router.register(r'signup', CreateUserView, )


urlpatterns = [
    path('',  include(router.urls) )
]
urlpatterns += [
    path('login/', views.obtain_auth_token),
    
]