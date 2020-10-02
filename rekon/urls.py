from django.urls import path
from .views import GetImage

app_name = 'rekon'

urlpatterns = [
    # path('',Index.as_view(),name='index'),
    path('',GetImage.as_view(),name='index'),
    path('create',GetImage.as_view(),name='createimage')
]