from django import forms
from .models import Scrap

class ScrapForm(forms.ModelForm):
    class Meta:
        model = Scrap
        fields = ['title', 'project_tag', 'code_content', 'explanation']
        # We add "widgets" to make the text boxes look nice with our aesthetic
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What did you solve?'}),
            'project_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '#DuskLight, #Django...'}),
            'code_content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Paste code here...'}),
            'explanation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Why does this work?'}),
        }