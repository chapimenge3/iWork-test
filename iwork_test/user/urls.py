from django.urls import path, include

# DRF import
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter


# My app imports
from .views import CreateUserView, ItemViewset

router = DefaultRouter()
router.register(r'signup', CreateUserView, )
router.register(r'items', ItemViewset)


urlpatterns = [
    path('',  include(router.urls))
]
urlpatterns += [
    # in this the username and pass must provide by json format in the body
    path('login/', views.obtain_auth_token),

]
