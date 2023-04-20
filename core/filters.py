from core.models import Consumer

def filter_table(request):
    consumer = Consumer.objects.all().order_by('-id')

    type = request.GET.get('type')
    if type:
        consumer = consumer.filter(discount_rules__consumer_type=type)
        
    print(request.GET.get('range'))

    return consumer
