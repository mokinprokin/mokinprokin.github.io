from django import forms
from editor.models import Item
class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields="__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input',"id":"nameForm"}),
            'description': forms.TextInput(attrs={'class': 'input',"id":"descriptionForm"}),
            'cost': forms.NumberInput(attrs={'class': 'input',"id":"costForm"}),
            'count': forms.NumberInput(attrs={'class': 'input',"id":"countForm"}),
            'fileName': forms.FileInput(attrs={'class': 'input'}),
        }