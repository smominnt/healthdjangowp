from django.urls import path
from .views import(
    entry_list_view,
    entry_create_view
)

app_name = 'entries'
urlpatterns = [
    path('entries/', entry_list_view, name='entry-list'),
    path('entries/create/', entry_create_view, name='entry-create')
]