from django.shortcuts import render, redirect
from .forms import CancelTransactionForm
from .models import Transaction_model
from django.db import transaction
# Create your views here.

def cancel_transaction(request):
    if request.method == 'POST':
        form = CancelTransactionForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    transaction_instance, created = Transaction_model.objects.get_or_create(
                        name=form.cleaned_data['name'],
                        description=form.cleaned_data['description']
                    )
                    if not created:
                        transaction_instance.is_successful = False
                        transaction_instance.save()
                    return redirect('success')
            except Transaction_model.DoesNotExist:
                form.add_error(None, 'Transaction not found.')
    else:
        form = CancelTransactionForm()

    return render(request, 'cancel_transaction.html', {'form': form})


def success(request):
    return render(request, 'success.html')