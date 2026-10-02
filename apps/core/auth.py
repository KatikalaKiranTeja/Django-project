from functools import wraps

from django.shortcuts import redirect


def admin_login_required(view_func):
    @wraps(view_func)
    def _wrapped(request, *args, **kwargs):
        if not request.session.get('admin_user'):
            return redirect('admin_auth:login')
        return view_func(request, *args, **kwargs)

    return _wrapped
