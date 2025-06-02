from django import forms
from .models import FormAuthor,FormBook
class AuthorForm(forms.ModelForm):
    class Meta:
        model=FormAuthor
        fields=['auth_name']
class BookForm(forms.ModelForm):
    class Meta:
        model=FormBook
        fields=['book','author','price','book_image']