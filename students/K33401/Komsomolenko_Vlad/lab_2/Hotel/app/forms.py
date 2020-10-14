from django import forms
from accounts.models import Feedback, Reserve
from django.db.models import Q


class addFeedback(forms.ModelForm):
    reserve = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reserve'].queryset = Reserve.objects.filter(Q(hotel_id=args[1]) & Q(user_id=args[2]))

    class Meta:
        model = Feedback
        fields = [
            "reserve",
            "rating",
            "description",
        ]


class addReserve(forms.ModelForm):
    class Meta:
        exclude = ['user', 'hotel']
        model = Reserve
        fields = [
            "start_date",
            "end_date",
        ]
