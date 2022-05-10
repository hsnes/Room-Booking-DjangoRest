from django.urls import path
from .views import ReservationList, ReservationCreate, RoomList

urlpatterns = [
    path('rooms', RoomList.as_view()),
    path('books', ReservationList.as_view()),
    path('add-book', ReservationCreate.as_view()),
]
