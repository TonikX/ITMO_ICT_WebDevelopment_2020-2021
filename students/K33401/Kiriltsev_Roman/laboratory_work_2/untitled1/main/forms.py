from django import forms
from django.forms import ModelForm, Textarea, HiddenInput
from django.contrib.auth.models import User
from .models import Comment


class PostComment(ModelForm):
    class Meta:
        model = Comment
        fields = ["conference", "topic", "text", "author"]

        labels = {
            "topic": ("Выберите тип комментария"),
            "text": ("Введите свой комментарий"),
        }

        widgets = {
            "conference": HiddenInput(),
            "text": Textarea(attrs={"cols": 70, "rows": 10}),
            "author": HiddenInput(),
        }