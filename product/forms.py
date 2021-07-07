from django import forms

class ProductForm(forms.Form):
    STATUS = (
        ('published', "Published"),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    )
    name = forms.CharField(max_length=250, help_text="Name max length 250, as helper text")
    description = forms.CharField(widget=forms.Textarea())
    status = forms.ChoiceField(choices=STATUS)
    is_active = forms.BooleanField()

