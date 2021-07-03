from django.db import models

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Product(models.Model):
    PUBLISHED = 'published'
    PENDING = 'pending'
    REJECTED = 'rejected'
    STATUS = (
        (PUBLISHED, "Published"),
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
    )
    # fields
    name = models.CharField(max_length=250, help_text='Name max length 250, as helper text')
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default=PENDING)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
