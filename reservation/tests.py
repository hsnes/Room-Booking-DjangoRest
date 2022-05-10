from io import BytesIO

# Create your tests here.
from django.test import TestCase
from .models import Room, Reservation
from .serializers import ReservationSerializer

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


def get_reservation_serializer(reservation):
    serializer = ReservationSerializer(reservation)
    content = JSONRenderer().render(serializer.data)
    stream = BytesIO(content)
    data = JSONParser().parse(stream)
    return ReservationSerializer(data=data)


class ReservationTestCase(TestCase):

    def test_reservation_create(self):
        """Reservation can be created"""
        room = Room.objects.create(name="room 1", room_number=3)
        reservation = Reservation.objects.create(room=room,
                                                 client_name="Smith",
                                                 start_date="2020-01-01",
                                                 end_date="2020-01-07")
        self.assertEqual(reservation.client_name, "Smith")

    def test_bad_end_date(self):
        """
        End date cannot be before the start date
        """
        room = Room.objects.create(name="room 1", room_number=3)
        d = {'room': room, 'client_name': 'Smith',
             'start_date': "2020-02-01",
             'end_date': '1999-01-01'}
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), False)

    def test_past_date(self):
        """
        Can't book dates in the past
        """
        room = Room.objects.create(name="room 1", room_number=3)
        d = {'room': room, 'client_name': 'Smith',
             'start_date': "1999-01-01",
             'end_date': '1999-01-02'}
        reservation = Reservation(**d)
        serializer = get_reservation_serializer(reservation)
        self.assertEqual(serializer.is_valid(), False)
