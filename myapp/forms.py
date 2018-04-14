from django import forms

class ProductForm(forms.Form):
    # variable for the title of the product
    author = forms.CharField(label="Title", max_length=100)
    # variable for the description of the product
    title = forms.CharField(label="Description",max_length=300)
    text = forms.CharField(label="Text", max_length=100)
    created_date = forms.DateField(label="Created Date")
    published_date = forms.DateField(label="Published Date")

