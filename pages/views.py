from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Home and About Views
class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

# File Appeal View
@method_decorator(login_required, name='dispatch')  # Ensures the user is logged in
class FileAppeal(TemplateView):
    template_name = "pages/file_appeal.html"

    def post(self, request, *args, **kwargs):
        # Handle form submission
        appeal_number = request.POST.get('appeal_number')
        appeal_reason = request.POST.get('appeal_reason')

        # Process the form (e.g., save to database)
        # Example:
        # Appeal.objects.create(user=request.user, appeal_number=appeal_number, appeal_reason=appeal_reason)

        # Redirect to success page after form submission
        return redirect('appeal_success')


# Appeal Success View
@method_decorator(login_required, name='dispatch')
class AppealSuccess(TemplateView):
    template_name = "pages/appeal_success.html"



