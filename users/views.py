from django.shortcuts import render, redirect
from users.forms import CustomUserForm

def register(request):
    
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            # Save the form data to create/update a CustomUser instance
            custom_user = form.save()
            return redirect('success_view')  # Redirect to a success page
    else:
        form = CustomUserForm()

    return render(request, 'register.html', {'form': form})
