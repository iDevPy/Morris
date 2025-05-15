"""."""
from django.urls import path
from .views import index#, toggle_theme, detect_theme, increment_counter

app_name = 'testing'
urlpatterns = [
    path('', index, name="index"),
    # path('toggle-theme/', toggle_theme, name='toggle_theme'),
    # path('detect-theme/', detect_theme, name='detect_theme'),
    # path('increment/', increment_counter, name='increment_counter'),
]
