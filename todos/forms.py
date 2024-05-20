from django import forms

from accounts.models import RegisterUserModel
from .models import TodosUserModel, LabelTodosModel


class CreateTodoForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(
        queryset=LabelTodosModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    user = forms.ModelChoiceField(
        queryset=RegisterUserModel.objects.all(),
        required=False
    )

    class Meta:
        model = TodosUserModel
        fields = '__all__'
