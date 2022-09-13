from django import forms

class MainForm(forms.Form):
    OPCOES = (
        ('0', 'Opção 1'),
        ('1', 'Opção 2'),
    )
    email = forms.CharField()
    email_bootstrap = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    opcoes = forms.IntegerField(
        widget=forms.Select(choices=OPCOES)
    )
    opcoes_bootstrap = forms.IntegerField(
        widget=forms.Select(attrs={'class': 'form-select'}, choices=OPCOES)
    )