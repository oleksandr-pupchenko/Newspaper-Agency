from django import forms
from django.contrib.auth import get_user_model

from agency.models import Topic, Newspaper


class TopicForm(forms.ModelForm):
    cancel = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = Topic
        fields = ["name"]


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    cancel = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Newspaper
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter article title"}),
            "content": forms.Textarea(attrs={"rows": 15, "placeholder": "Insert content of the article"}),
            "topic": forms.Select(attrs={"placeholder": "Select topic.."})
        }
