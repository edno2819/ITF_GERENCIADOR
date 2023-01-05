from django import forms
from django.forms import ModelForm

from .models import DigitacaoProblema, SugestaoMelhora

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class SaqMesDigitacao(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SaqMesDigitacao, self).__init__(*args, **kwargs)
        self.fields['descricao'].widget = forms.Textarea(attrs={'rows': 3, 'cols': 25})

    class Meta:
        model = DigitacaoProblema
        fields = ['nome', 'area', 'item', 'descricao']


class SugestaoMelhoraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SugestaoMelhoraForm, self).__init__(*args, **kwargs)
        self.fields['contribuicao'].widget = forms.Textarea(attrs={'rows': 2, 'cols': 20})
        self.fields['sugestao'].widget = forms.Textarea(attrs={'rows': 3, 'cols': 25})


    class Meta:
        model = SugestaoMelhora
        fields = ['nome', "id_ambev", 'area', 'contribuicao', 'sugestao']
