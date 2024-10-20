from django.urls import path

from .views import HomePageView, AboutPageView, FileAppeal, AppealSuccess

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("file_appeal/", FileAppeal.as_view(), name="file_appeal"),
    path('appeal-success/', AppealSuccess.as_view(), name='appeal_success'),
]
