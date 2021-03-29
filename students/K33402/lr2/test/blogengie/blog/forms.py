from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title', 'slung']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slung': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slung(self):
        new_slung = self.cleaned_data['slung'].lower()

        if new_slung == 'create':
            raise ValidationError('slug my not be "Create"')
        if Tag.objects.filter(slung__iexact=new_slung).count():
            raise ValidationError('Slug mus be unique. We have "{}" slug already'.format(new_slung))
        return new_slung


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slung', 'body', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slung': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slung(self):
        new_slung = self.cleaned_data['slung'].lower()

        if new_slung == 'create':
            raise ValidationError('slug my not be "Create"')
        return new_slung
