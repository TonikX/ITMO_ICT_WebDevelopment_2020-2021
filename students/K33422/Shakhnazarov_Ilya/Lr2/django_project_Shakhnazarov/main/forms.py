from django import forms
from django.forms import ModelForm, Textarea, HiddenInput
from django.contrib.auth.models import User
from .models import Comment


class PostComment(ModelForm):
    class Meta:
        model = Comment
        fields = ["conference", "comment_type", "comment_text", "comment_author"]

        labels = {
            "comment_type": "Выберите тип комментария",
            "comment_text": "Введите свой комментарий"
        }

        widgets = {
            "conference": HiddenInput(),
            "comment_text": Textarea(attrs={"cols": 70, "rows": 10}),
            "comment_author": HiddenInput()
        }
