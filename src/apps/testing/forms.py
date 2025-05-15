from django import forms
from decouple import config

def clean_env(env):
    env = env.lower().replace(" ", "").strip('"').strip("'")
    return env

def get_themes_choices():
    light_theme = clean_env(config('DEFAULT_LIGHT_THEME'))
    dark_theme = clean_env(config('DEFAULT_DARK_THEME'))
    other_themes = clean_env(config('OTHER_THEMES')).split(",")
    system_theme_is_active = config('ENABLE_SYSTEM_THEME', cast=bool)
    theme_choices = [light_theme, dark_theme]
    if system_theme_is_active:
        system_theme_name = clean_env(config('SYSTEM_THEME_NAME'))
        theme_choices.insert(0, system_theme_name)
    theme_choices.extend(other_themes)
    theme_choices_dict = {k: v.title() for k , v in zip(theme_choices, theme_choices)}
    if "light" not in theme_choices:
        theme_choices_dict.update({light_theme: "Light"})
    if "dark" not in theme_choices:
        theme_choices_dict.update({dark_theme: "Dark"})
    return theme_choices_dict

class ThemeSelectionForm(forms.Form):
    CHOICES = get_themes_choices()
    theme = forms.ChoiceField(choices=CHOICES, widget=forms.Select, label='Select your theme')
