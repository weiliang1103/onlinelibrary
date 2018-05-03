from django.urls import path, re_path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # path('/cart/', ),
    # path('cart/', views.view_cart, name='view-cart'),
    # path('cart/add/<int:pk>', views.add_to_cart, name='add-to-cart'),
#     re_path(r'^cart/add/$', views.add_to_cart, name='add-to-cart'),
#     re_path(r'^cart/delete/$', views.remove_from_cart, name='remove-from-cart'),
#     path('cart/delete/all', views.empty_cart, name='empty-cart'),
#     path('cart/checkout', views.checkout, name='checkout'),
]
