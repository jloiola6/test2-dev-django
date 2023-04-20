from core.models import Consumer

def filter_table(request):
    consumer = Consumer.objects.all().order_by('-id')

    type = request.GET.get('type')
    range = request.GET.get('range')
    if type:
        consumer = consumer.filter(discount_rules__consumer_type=type)
        
    if range:
        consumer = consumer.filter(discount_rules__consumption_range=range)

    return consumer
