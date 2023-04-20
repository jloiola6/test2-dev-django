from django import forms
from .models import Consumer, DiscountRules

class ConsumerForm(forms.Form):
    name = forms.CharField(label="Nome do Consumidor", max_length=128)
    document = forms.CharField(label="Documento (CPF/CNPJ)", max_length=14)
    zip_code = forms.CharField(label="CEP", max_length=8, required=False)
    city = forms.CharField(label="Cidade", max_length=128)
    state = forms.CharField(label="Estado", max_length=128)
    consumption = forms.IntegerField(label="Consumo (kWh)", required=False)
    distributor_tax = forms.FloatField(label="Tarifa da Distribuidora", required=False)


class DiscountForm(forms.Form):
    type_options = (
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    )

    tax_options = (
        (90, '90%'),
        (95, '95%'),
        (99, '99%'),
    )

    consumer_type = forms.ChoiceField(label='Tipo de consumo', choices=type_options, required=True)
    cover_value = forms.ChoiceField(label="Cobertura (%)", choices=tax_options, required=True)
