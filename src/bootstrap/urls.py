from django.urls import path
from .views import index_view, calc_view, result_view


app_name = 'bootstrap'
urlpatterns = [
    path('', index_view, name='index'),
    path('tdee/result', calc_view, name='calc'),
    path('tdee/', result_view, name='result')
]


