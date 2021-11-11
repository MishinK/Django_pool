from django.shortcuts import redirect
from functools import wraps
from moviemon.utils.game import load_session_data

def load_midd(view_function):
    @wraps(view_function)
    def wrap(request, *args, **kwargs):
        data = load_session_data()
        if data is None:
            return redirect("title")
        return view_function(request, *args, **kwargs)
    return wrap
