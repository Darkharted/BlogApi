from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.enums import Choices
from model_utils.fields import StatusField

User = get_user_model()



class CreateDateModel(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        abstract = True




class Product(CreateDateModel):
    STATUS = Choices('Available', 'Not existed')
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    status = StatusField
    description = models.TextField()

    def __str__(self):
        return self.title



