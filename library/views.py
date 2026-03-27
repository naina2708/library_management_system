from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User 
from .models import Item, Transaction
from datetime import date

# LOGIN (Password hidden automatically)
def user_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


# HOME PAGE (User)
def home(request):
    items = Item.objects.all()
    return render(request, 'dashboard.html', {'items': items})

from datetime import date

def my_books(request):
    issues = Transaction.objects.filter(user=request.user, return_date=None)

    for i in issues:
        if date.today() > i.due_date:
            days = (date.today() - i.due_date).days
            i.current_fine = days * 10
        else:
            i.current_fine = 0

    return render(request, 'mybooks.html', {'issues': issues})
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            User.objects.create_user(username=username, password=password) # type: ignore
            return redirect('login')

    return render(request, 'register.html')
# SEARCH VALIDATION
def search(request):
    name = request.GET.get('name')
    author = request.GET.get('author')

    if not name and not author:
        return render(request, 'dashboard.html', {'error': 'Enter at least one field'})

    items = Item.objects.filter(title__icontains=name or "", author__icontains=author or "")
    return render(request, 'dashboard.html', {'items': items})


# ISSUE BOOK
def issue_item(request, item_id):
    item = Item.objects.get(id=item_id)

    if item.quantity > 0:
        Transaction.objects.create(user=request.user, item=item)
        item.quantity -= 1
        item.save()

    return redirect('home')


# RETURN BOOK (with fine enforcement)
def return_item(request, trans_id):
    trans = Transaction.objects.get(id=trans_id)
    trans.return_date = date.today()

    fine = trans.fine()

    if fine > 0 and not trans.fine_paid:
        return render(request, 'fine.html', {'fine': fine, 'id': trans.id})

    trans.save()

    item = trans.item
    item.quantity += 1
    item.save()

    return redirect('home')


# PAY FINE
def pay_fine(request, trans_id):
    trans = Transaction.objects.get(id=trans_id)
    trans.fine_paid = True
    trans.save()
    return redirect('return', trans_id=trans.id)