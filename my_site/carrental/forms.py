from django import forms


class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    email_name = forms.EmailField(label="Email", max_length=100)
    review = forms.CharField(label="Kindly review", max_length=1000)
    stars = forms.IntegerField(label="Stars", min_value=0, max_value=5)