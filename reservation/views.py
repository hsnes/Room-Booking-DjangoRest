from rest_framework import generics
from .serializers import RoomSerializer, ReservationSerializer
from .models import Room, Reservation


class RoomList(generics.ListAPIView):
    """
    List all Rooms.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ReservationList(generics.ListAPIView):
    """
    List all reservations.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationCreate(generics.CreateAPIView):
    """
    Retrieve, create reservation instance.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
