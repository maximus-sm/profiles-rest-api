from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

#Router is for ViewSet. Init a router with the specific ViewSet and a suburl. 
#Include it into the urlpatterns
router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello_viewset')

# basename - The base to use for the URL names that are created.
# If unset the basename will be automatically generated 
# based on the queryset attribute of the viewset, if it has one. 
# Note that if the viewset does not include a queryset attribute 
# then you must set basename when registering the viewset.
app_name = "profiles"
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('login/',views.UserLoginApiView.as_view(),name="login"),
    path('',include(router.urls))
]