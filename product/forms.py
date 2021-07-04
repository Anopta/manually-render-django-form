from django import forms

class ProductForm(forms.Form):
    STATUS = (
        ('published', "Published"),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    )
    name = forms.CharField(max_length=250, label='Product Name')
    description = forms.CharField(widget=forms.Textarea())
    status = forms.ChoiceField(choices=STATUS)
    is_active = forms.BooleanField()

