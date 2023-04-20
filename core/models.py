from django.db import models

# Create your models here.

class DiscountRules(models.Model):    
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

    consumer_type = models.CharField("Tipo de consumo", max_length=25, choices=type_options)
    consumption_range = models.CharField("Intervalo", max_length=25)
    cover_value = models.FloatField("Cobertura (%)", choices=tax_options)
    discount_value = models.FloatField("Desconto")


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField("Tarifa da Distribuidora", blank=True, null=True)
    discount_rules = models.OneToOneField(DiscountRules, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name




# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
