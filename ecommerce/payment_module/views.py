from django.shortcuts import render, redirect
from .models import PaymentGateway, Invoice, InvoiceDetail
from product_module.models import CartItem, Product
from datetime import date, datetime
from django.db import transaction
from django.urls import reverse

# Create your views here.
def confirmpayment(request):
    if request.method == "POST":
        token = request.POST.get("token")
        amount = request.POST.get("amount")

        token = token.strip()
        amount = float(amount)

        try:
            with transaction.atomic():
                make_payment(token, amount)
                maintain_invoice(request, token, amount)

        except Exception as e:
            request.session["message"] = str(e)
            return redirect(reverse('error_page'))
    
    
    request.session["message"] = f"Payment successfully completed with NRs. {amount} from your balance!"
    return redirect(reverse('success_page'))


def make_payment(token, amount):
    try:
        payment_gateway = PaymentGateway.objects.get(token=token)
    except:
        raise Exception(f"Invalid token '{token}'")

    if payment_gateway.balance < amount:
        raise Exception("Insufficent balance")

    if payment_gateway.expiry_date < date.today():
        raise Exception("Token has expired !")

    payment_gateway.balance -= amount
    payment_gateway.save()


def maintain_invoice(request, token, amount):
    cart_items = CartItem.objects.filter(user=request.user)

    invoice = Invoice(
        user=request.user,
        token=token,
        total_amount=amount,
        payment_date=datetime.now()
    )

    invoice.save()

    for cart_item in cart_items:
        invoice_detail = InvoiceDetail(
            invoice=invoice,
            product=cart_item.product,
            quantity=cart_item.quantity,
            sub_amount=cart_item.quantity * cart_item.product.price
        )

        invoice_detail.save()

    for cart_item in cart_items:
        product = Product.objects.get(id=cart_item.product.id)

        if product.quantity < cart_item.quantity:
            raise Exception(f"Insufficient quantity {cart_item.quantity} for {product.name}")

        product.quantity -= cart_item.quantity
        product.save()

        cart_item.delete()