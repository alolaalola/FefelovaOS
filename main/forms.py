from django import forms
from django.contrib.auth.models import User
from .models import ContactMessage
from .models import Review


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'content']

    
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']