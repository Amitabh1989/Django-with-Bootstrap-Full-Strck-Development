from django import forms
from .models import Feedback
from django.forms import ModelForm

STARS = [
    (0, "0"),
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
]

# DJANGO FORMS EXAMPLE BELOW
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label="First name", max_length=100)
#     last_name = forms.CharField(label="Last name", max_length=100)
#     email_name = forms.EmailField(label="Email", max_length=100)
#     stars = forms.ChoiceField(choices=STARS)
#     review = forms.CharField(label="Kindly review", max_length=1000,
#             widget=forms.Textarea(attrs={"class": "myform",
#                                          "rows": 5,
#                                          "columns": 2}))
    
# DJANGO MODEL FORM
class ReviewForm(ModelForm):
    class Meta:
        model = Feedback
        labels = {
            "first_name": "Kya bolti public"
        }
        fields = ["first_name", "last_name", "email", "stars", "review"] #  or "__all__" for inclusing everything
        # https://docs.djangoproject.com/en/4.2/ref/forms/fields/#charfield
        error_messages = {
            "first_name": {
                "required": "Naam bol apna, bhidu!"
            }
        }