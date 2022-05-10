from datetime import date
from rest_framework import serializers
from .models import Room, Reservation


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


def validate_for_overbook(room, start, end):
    books = Reservation.objects.filter(room=room)
    for item in books:
        """
        Verify each day in the range is not overbooked
        """
        if (item.end_date >= start >= item.start_date) or (item.end_date >= end >= item.start_date):
            raise serializers.ValidationError(f"Room is full on {item.start_date} at {item.end_date}.")


class ReservationSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate(data, **kwargs):

        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError('End date must be AFTER the start date.')

        if data['start_date'] < date.today() or data['end_date'] < date.today():
            raise serializers.ValidationError("Can't book days in the PAST.")

        validate_for_overbook(data['room'], data['start_date'], data['end_date'])

        return data

    class Meta:
        model = Reservation
        fields = ('id', 'room', 'client_name', 'start_date', 'end_date')
