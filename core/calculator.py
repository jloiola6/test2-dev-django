def calculator(average_consumption: int, distributor_tax: float, tax_type: str) -> tuple:
    """
    returns a tuple of floats contained anual savings, monthly savings, applied_discount and coverage
    """

    # Verificação do applied_discount aplicável
    if average_consumption < 10000:
        consumption_range = '< 10.000 kWh'

        if tax_type == "Residencial":
            applied_discount = 0.18
        elif tax_type == "Comercial":
            applied_discount = 0.16
        else:
            applied_discount = 0.12
            
    elif average_consumption >= 10000 and average_consumption <= 20000:
        consumption_range = '>= 10.000 kWh e <= 20.000 kWh'

        if tax_type == "Residencial":
            applied_discount = 0.22
        elif tax_type == "Comercial":
            applied_discount = 0.18
        else:
            applied_discount = 0.15
    else:
        consumption_range = '> 20.000 kWh'

        if tax_type == "Residencial":
            applied_discount = 0.25
        elif tax_type == "Comercial":
            applied_discount = 0.22
        else:
            applied_discount = 0.18


    return applied_discount, consumption_range
