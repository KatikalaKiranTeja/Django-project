from django.contrib import messages
from django.shortcuts import redirect, render

from apps.admin_auth.services.impl import AdminAuthService


auth_service = AdminAuthService()


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        if auth_service.validate_credentials(username, password):
            request.session['admin_user'] = username
            return redirect('teams:admin_dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'admin_auth/login.html')


def logout_view(request):
    request.session.flush()
    return redirect('public:home')
