from django import forms
from tinymce import TinyMCE
from .models import BookModel, SuggestionModel


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class SuggestionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name*',
        'style': 'border-top: 0; border-right:0; border-left:0; color:#828282'
    }), label='', max_length=100)
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email*',
        'style': 'border-top: 0; border-right:0; border-left:0; color:#828282'
    }), label='')
    book_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Book Name',
        'style': 'border-top: 0; border-right:0; border-left:0; color:#828282'
    }), label='', max_length=100, required=False)
    suggestion = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 2,
        'class': 'form-control',
        'placeholder': 'Suggestion or Message*',
        'style': 'border-top: 0; border-right:0; border-left:0; color:#828282'
    }), label='', max_length=100)

    class Meta:
        model = SuggestionModel
        fields = ['name', 'email', 'book_name', 'suggestion']


class AddBookForm(forms.ModelForm):
    book_title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Book Title', max_length=100)
    book_author = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Book Author', max_length=120)
    book_image_url = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'class': 'form-control',
    }), label='Book Image Url')
    book_summary = forms.CharField(widget=TinyMCEWidget(
            attrs={'class': 'form-control', 'required': False, 'rows': 10}
        ),label='Book Summary')
    book_publish_on = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control w-50'
    })
    )
    publish_status = forms.BooleanField()

    class Meta:
        model = BookModel
        fields = ['book_title', 'book_author', 'book_image_url', 'book_summary', 'book_publish_on', 'tag', 'publish_status']


class EditBookForm(forms.ModelForm):
    book_title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Book Title', max_length=100)
    book_author = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), label='Book Author', max_length=120)
    book_image_url = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 3,
        'class': 'form-control',
    }), label='Book Image Url')
    book_summary = forms.CharField(widget=TinyMCEWidget(attrs={
        'rows': 12,
    }), label='Book Summary')
    book_publish_on = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control w-50'
    })
    )
    publish_status = forms.BooleanField()

    class Meta:
        model = BookModel
        fields = ['book_title', 'book_author', 'book_image_url', 'book_summary', 'book_publish_on', 'tag', 'publish_status']