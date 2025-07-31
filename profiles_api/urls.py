from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

#Router is for ViewSet. Init a router with the specific ViewSet and a suburl. 
#Include it into the urlpatterns
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello_viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]