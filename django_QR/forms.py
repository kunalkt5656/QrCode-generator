from django import forms



class QRCodeForm(forms.Form):
    restaurent_name = forms.CharField (
        max_length=50,
        label='Restaurent Name',
        widget=forms.TextInput(attrs={
        'class': 'form-control', 
         'placeholder':'Enter Restaurent Name',
         'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1)'
         
         })                               
    )
    url = forms.URLField(
        max_length=200,
        label='Menu URL',
        widget=forms.URLInput(attrs={ 'class': 'form-control','placeholder': 'Enter Menu URL of your menu','style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-shadow: inset 0 1px 3px rgba(0,0,0,0.1)'
         })
    )