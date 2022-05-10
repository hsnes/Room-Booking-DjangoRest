from django.shortcuts import render

from reservation.models import Reservation


def book_list(request):
    books = Reservation.objects.all()
    context = {
        "books": books
    }
    return render(request, 'Books.html', context)
