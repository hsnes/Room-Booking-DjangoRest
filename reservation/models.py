from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    room_number = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('room_number',)


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    start_date = models.DateField('Start of the stay.')
    end_date = models.DateField('End of the stay.')

    def __str__(self):
        return "{} to {} at {} for {}".format(
            self.start_date.strftime("%Y-%m-%d"),
            self.end_date.strftime("%Y-%m-%d"),
            self.room.room_number,
            self.client_name
        )
