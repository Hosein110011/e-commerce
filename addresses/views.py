from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from billing.models import BillingProfile
from .forms import AddressForm
from django.contrib import messages



def checkout_address_create_view(request):
    form = AddressForm(request.POST or None)
    context = {'form':form}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        instance = form.save(commit=False)
        billing_profile , billing_profile_created = BillingProfile.objects.new_or_get(request)
        if billing_profile is not None:
            address_type = request.POST.get('address_type','shipping')
            instance.billing_profile = billing_profile
            instance.address_type = address_type
            instance.save()
            request.session[address_type + "_address_id"] = instance.id
        else:
            messages.error(request, 'Error!!!')
            return redirect('carts:checkout')
        if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('carts:checkout')
    return redirect('carts:checkout')


