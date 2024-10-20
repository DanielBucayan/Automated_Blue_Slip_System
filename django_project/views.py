from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def submit_appeal(request):
    if request.method == 'POST':
        # Process form data here
        appeal_number = request.POST.get('appeal_number')
        appeal_reason = request.POST.get('appeal_reason')

        # You would typically save the appeal details to the database here
        # For example:
        # Appeal.objects.create(user=request.user, appeal_number=appeal_number, appeal_reason=appeal_reason)

        # Redirect to the success page after submission
        return redirect('appeal_success')  # Redirects to the success page

    return render(request, 'appeal_form.html')  # If not POST, render the appeal form