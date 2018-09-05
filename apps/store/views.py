# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'store/index.html')

def process(request):
    price = 0
    if not 'total' in request.session:
        request.session['total'] = 0
    # Display amount of items purchased
    if not 'item_count' in request.session:
        request.session['item_count'] = 1
    request.session['item_count'] += 1
    # Select price with corresponding product id
    if request.POST['product_id'] == '1000':
        price = 19.99
    elif request.POST['product_id'] == '2000':
        price = 29.99
    elif request.POST['product_id'] == '3000':
        price = 4.99
    elif request.POST['product_id'] == '4000':
        price = 49.99
    # Total amount of current purchase
    request.session['current_purchase'] = float(request.POST['quanity'])*price
    request.session['total'] += request.session['current_purchase']
    return redirect('/checkout')

def checkout(request):
    return render(request, 'store/checkout.html')

def reset(request):
    request.session['total'] = 0
    request.session['item_count'] = 0
    request.session['current_purchase'] = 0
    return render(request, 'store/checkout.html')
