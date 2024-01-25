from django import forms

class CustomLostPostForm(forms.Form):
    
    postTitle = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',  'required': 'required'})
    )

    lostItem = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',  'required': 'required'})
    )

    location = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm',  'required': 'required'})
    )

    description = forms.CharField(
        max_length=1500,
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'rows': '3','style':'resize: none;height: 100px;'})
    )
    
    fileUpload = forms.FileField(
        widget=forms.FileInput(attrs={'id': 'input-image', 'required': 'required', 'class':'form-control', 'accept':'image/*'})
    )
    
