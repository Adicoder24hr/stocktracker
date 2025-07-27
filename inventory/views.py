from django.shortcuts import render,redirect
from .models import Product, Transaction, TransactionDetail
from django.views.decorators.csrf import csrf_exempt


def inventory_view(request):
    products = Product.objects.all()
    return render(request, 'inventory/inventory.html', {'products':products})

@csrf_exempt
def add_transaction(request):
    if request.method == 'POST':
        ref = request.POST['ref']
        product_id = int(request.POST['product'])
        qty = int(request.POST['qty'])

        # validation
        if not ref.strip():
            return render(request, 'inventory/add_transaction.html',{
                'products': Product.objects.all(),
                'error':"Reference number is required."
            })
        
        if qty == 0:
            return render(request, 'inventory/add_transaction.html',{
                'products':Product.objects.all(),
                'error':"Quantity cannot be 0"
            })
        
        transaction = Transaction.objects.create(Reference_number=ref)
        product = Product.objects.get(id=product_id)

        TransactionDetail.objects.create(
            transaction=transaction,
            product = product,
            quantity_changed = qty
        )

        product.quantity += qty
        product.save()

        return redirect('/')
    products = Product.objects.all()
    return render(request, 'inventory/add_transaction.html',{
        'products':products
    })