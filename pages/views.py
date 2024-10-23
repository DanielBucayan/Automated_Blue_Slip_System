from django.views.generic import TemplateView
from django.utils.timezone import now
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class AdminHomePageView(UserPassesTestMixin, TemplateView):
    template_name = "pages/admin_home.html"

    # Test to check if the user is an admin
    def test_func(self):
        return self.request.user.is_superuser  # or use self.request.user.is_superuser for superadmins

    # Redirect non-admin users
    def handle_no_permission(self):
        messages.error(self.request, "You are not authorized to access this page.")
        return redirect('home')  # Redirect to a 'home' or any other page

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

class ViewStatus(TemplateView):
    template_name = "pages/view_status.html"




