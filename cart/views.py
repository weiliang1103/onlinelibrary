from django.shortcuts import render, get_object_or_404
from .models import History
from catalog.models import BookInstance, Location
from django.http import JsonResponse

# Create your views here.
def view_cart(request):
    cart = request.session.get('cart')
    response_list = {}
    for pk in cart:
        pass
    return render(
        request,
        'cart.html',
        {'cart':cart, 'title':'Cart',},
    )

def add_to_cart(request):
    book_inst_id = request.GET.get('pk')
    book_inst = get_object_or_404(BookInstance, pk=book_inst_id)
    title = book_inst.book.title
    status = book_inst.status
    cart = request.session.get('cart')
    if book_inst.status == 'a':
        if cart:
            if book_inst_id in cart:
                msg = title + " is already in your cart."
                is_added = False
            else:
                request.session.get('cart').append(book_inst_id)
                request.session.modified = True
                status = 'r'
                book_inst.save()
                msg = title + " is added to your cart."
                is_added = True
        else:
            request.session['cart'] = [book_inst_id]
            request.session.modified = True
            status = 'r'
            book_inst.save()
            msg = title + " is added to your cart."
            is_added = True
    else:
        msg = title + " is not available."
        is_added = False    
    response = {
        'msg': msg,
        'status': book_inst.status,
        'is_added': is_added,
    }
    return JsonResponse(response)

def remove_from_cart(request):
    book_inst_id = request.GET.get('pk')
    book_inst = get_object_or_404(BookInstance, pk=book_inst_id)
    title = book_inst.book.title
    cart = request.session.get('cart')
    if cart:
        if book_inst_id in cart:
            request.session['cart'].remove(book_inst_id)
            request.session.modified = True
            is_removed = True
    response = {
        # 'msg': msg,
        'is_removed': is_removed,
    }
    return JsonResponse(response)

def empty_cart(request):
    if request.session.get('cart'):
        del request.session['cart']
        is_empty = True
    response = {
        'is_empty': is_empty,
    }
    return JsonResponse(response)

def checkout(request):
    cart = request.session.get('cart')
    response = {}
    h = {}
    for pk in cart:
        book_inst = get_object_or_404(BookInstance, pk=pk)
        book = book_inst.book
        title = book.title
        x_coor = book_inst.location.x_coor
        y_coor = book_inst.location.y_coor
        response[pk] = (title, x_coor, y_coor)
    history = History()
    for x in xrange(1,10):
        history.books.add(book)
        history.save()
    return JsonResponse(response)
