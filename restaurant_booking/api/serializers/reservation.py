from rest_framework import serializers
from ..models.reservation import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'customer_name', 'reservation_date', 'number_of_guests', 'table_number', 'status']
