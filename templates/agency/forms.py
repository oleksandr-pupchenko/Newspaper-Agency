from django import forms

from agency.models import Topic


class TopicForm(forms.ModelForm):
    cancel = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = Topic
        fields = ["name"]
