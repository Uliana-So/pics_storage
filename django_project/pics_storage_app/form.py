from django import forms


class UploadImageForm(forms.Form):
    title = forms.CharField(label='Image\'s name')
    image = forms.ImageField(label='Add images')
