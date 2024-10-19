from django.views.generic import TemplateView
from django.utils.timezone import now

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class AdminHomePageView(TemplateView):
    template_name = "pages/admin_home.html"

