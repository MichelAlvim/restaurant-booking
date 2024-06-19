from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
    )

    customer_name = models.CharField(max_length=255)
    reservation_date = models.DateTimeField()
    number_of_guests = models.IntegerField()
    table_number = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.customer_name} - {self.reservation_date}"

    def save(self, *args, **kwargs):
        if not self.id:  # Se é uma nova reserva
            self.expire_at = self.reservation_date + timezone.timedelta(hours=2)
        super().save(*args, **kwargs)
