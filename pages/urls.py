from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path('admin_home/', AdminHomePageView.as_view(), name='admin_home'),
]
