from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .models import Test
from decouple import config
light_theme = config('DEFAULT_LIGHT_THEME')
dark_theme = config('DEFAULT_DARK_THEME')
system_theme_name = config('SYSTEM_THEME_NAME')

from .forms import ThemeSelectionForm

def index(request, *args, **kwargs):
    """."""
    template = "testing/index.html"
    context = {}
    if request.method == 'POST':
        theme_selection_form = ThemeSelectionForm(request.POST)
        if theme_selection_form.is_valid():
            # Save the selected theme in session
            selected_theme = theme_selection_form.cleaned_data['theme']
            active_theme = selected_theme
            if selected_theme == system_theme_name:
                system_theme = request.POST.get('system_theme', "light")
                if system_theme == "dark":
                    active_theme = dark_theme
                else:
                    active_theme = light_theme
            request.session['active_theme'] = active_theme
            request.session['selected_theme'] = selected_theme
            context['theme_selection_form'] = theme_selection_form
            context['active_theme'] = active_theme
            context['selected_theme'] = selected_theme
            return render(request, template, context)
    else:
        # Pre-fill form theme selection from session if exists
        initial_theme = request.session.get('active_theme')
        theme_selection_form = ThemeSelectionForm(initial={'theme': initial_theme})
    
    active_theme = request.session.get('active_theme', light_theme)
    selected_theme = request.session.get('selected_theme', light_theme)
    context['theme_selection_form'] = theme_selection_form
    context['active_theme'] = active_theme
    context['selected_theme'] = selected_theme
    # Initialize counter in session if not present
    if 'counter' not in request.session:
        request.session['counter'] = 0
    context['counter']: request.session['counter']

    template = "testing/index.html"
    context["test"] = Test.objects.all()
    context["page_h1_title"] = "Testing"

    theme = request.session.get('theme', dark_theme)
    context['theme'] = theme

    context["light_theme"] = light_theme
    context["dark_theme"] = dark_theme

    return render(request, template, context)

# def get_system_theme(request):
#     # Attempt to detect system theme from cookie 'color-scheme'
#     cookie_pref = request.COOKIES.get('color-scheme')
#     if cookie_pref == dark_theme:
#         return dark_theme
#     elif cookie_pref == light_theme:
#         return light_theme
#     # Default fallback theme
#     return light_theme

# @require_POST
# def toggle_theme(request):
#     current = request.session.get('theme', get_system_theme(request))
#     new_theme = dark_theme if current == light_theme else light_theme
#     request.session['theme'] = new_theme
#     return redirect('testing:index')

# #@require_POST
# def detect_theme(request):
#     if request.htmx or request.method == "POST": 
#         prefers_dark = request.POST.get('prefers_dark')
#         preferred_theme = light_theme
#         if prefers_dark:
#             preferred_theme = dark_theme
#         request.session['theme'] = preferred_theme
#         return HttpResponse(f'<html id="data_theme" data-theme="{preferred_theme}">')


# def increment_counter(request): #htmx
#     # Increment counter stored in session
#     counter = request.session.get('counter', 0)
#     counter += 1
#     request.session['counter'] = counter
#     request.session.modified = True
#     # Return updated counter wrapped in div with id "counter" to correctly swap outerHTML
#     return HttpResponse(counter)
#     #return HttpResponse(f'<html id="data_theme" data-theme="{counter}">')