from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=140)
    description = forms.CharField(widget=forms.Textarea, required=False)
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password_conf = forms.CharField(max_length=50, widget=forms.PasswordInput, required=False)

