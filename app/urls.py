# transaction_app/urls.py
from django.urls import path
from .views import cancel_transaction, success

urlpatterns = [
    path('', cancel_transaction, name='cancel_transaction'),
    path('success/',success, name='success')
]
