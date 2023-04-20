import pandas as pd

from core.models import Consumer, DiscountRules
from core.calculator import calculator


def load():
    if not Consumer.objects.exists():
        table = pd.read_excel("consumers.xlsx")

        for index, row in table.iterrows():
            # Extrair os valores de cada coluna
            name = row['Nome']
            document = row['Documento']
            city = row['Cidade']
            state = row['Estado']
            consumption = row['Consumo(kWh)']
            consumer_type = row['Tipo']
            cover_value = float(row['Cobertura(%)'])
            distributor_tax = row['Tarifa da Distribuidora']

            
            new_consumer = Consumer()
            new_consumer.name = name
            new_consumer.document = document
            new_consumer.city = city
            new_consumer.state = state
            new_consumer.consumption = consumption
            new_consumer.distributor_tax = distributor_tax

            discount_value, consumption_range = calculator(consumption, distributor_tax, consumer_type)
            new_rules = DiscountRules()
            new_rules.consumer_type = consumer_type
            new_rules.consumption_range = consumption_range #Fazer range
            new_rules.cover_value = cover_value 
            new_rules.discount_value =  discount_value
            new_rules.save()

            new_consumer.discount_rules = new_rules
            new_consumer.save()
