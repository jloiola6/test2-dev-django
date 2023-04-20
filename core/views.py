from django.shortcuts import render, HttpResponseRedirect

from core.load_data import load
from core.filters import filter_table
from core.calculator import calculator
from core.forms import ConsumerForm, DiscountForm
from core.models import Consumer, DiscountRules

# Create your views here.
# Todo: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    template_name = 'index.html'

    load()
    consumer_form = ConsumerForm()
    discount_form = DiscountForm()


    consumers = filter_table(request)

    context = {
        'consumers' : consumers, 
        'consumer_form' : consumer_form, 
        'discount_form' : discount_form
    }

    return render(request, template_name, context)


# Todo: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2(request):
    if request.method == 'POST':
        consumer_form = ConsumerForm(request.POST)
        discount_form = DiscountForm(request.POST)

        if consumer_form.is_valid() and discount_form.is_valid():
            consumption = consumer_form.cleaned_data['consumption']
            distributor_tax = consumer_form.cleaned_data['distributor_tax']
            consumer_type = discount_form.cleaned_data['consumer_type']

            new_consumer = Consumer()
            new_consumer.name = consumer_form.cleaned_data['name']
            new_consumer.document = consumer_form.cleaned_data['document']
            new_consumer.city = consumer_form.cleaned_data['city']
            new_consumer.state = consumer_form.cleaned_data['state']
            new_consumer.consumption = consumption
            new_consumer.distributor_tax = distributor_tax

            discount_value, consumption_range = calculator(consumption, distributor_tax, consumer_type)
            new_rules = DiscountRules()
            new_rules.consumer_type = consumer_type
            new_rules.consumption_range = consumption_range
            new_rules.cover_value = discount_form.cleaned_data['cover_value'] 
            new_rules.discount_value =  discount_value
            new_rules.save()

            new_consumer.discount_rules = new_rules
            new_consumer.save()
    return HttpResponseRedirect('/')
