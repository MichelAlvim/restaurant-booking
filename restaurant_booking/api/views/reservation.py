from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime
from ..models.reservation import Reservation
from ..serializers.reservation import ReservationSerializer

class ReservationCreate(generics.CreateAPIView):
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        table_number = request.data.get('table_number')
        reservation_date_str = request.data.get('reservation_date')
        reservation_date = datetime.strptime(reservation_date_str, '%Y-%m-%dT%H:%M:%SZ')
        end_time = reservation_date + timezone.timedelta(hours=2)

        conflicting_reservations = Reservation.objects.filter(
            table_number=table_number,
            reservation_date__range=(reservation_date, end_time),
            status='active'
        )

        if conflicting_reservations.exists():
            return Response({"error": "This table is already reserved in this time slot or within the next 2 hours."},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"success": "Reservation created successfully."}, status=status.HTTP_201_CREATED)


class ReservationList(generics.ListAPIView):
    queryset = Reservation.objects.filter(status='active')
    serializer_class = ReservationSerializer


class ReservationDetail(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": f"Reservation {instance.id} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.status = 'cancelled'
        instance.save()
