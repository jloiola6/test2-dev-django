from django.urls import include, path

from core.views import view1, view2


app_name = 'core'
 
urlpatterns = [
    path('', view1, name='index'),
    path('register/', view2, name='register')
]