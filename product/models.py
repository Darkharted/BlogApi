from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.enums import Choices
from model_utils.fields import StatusField
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like


User = get_user_model()



class CreateDateModel(models.Model):
    created_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        abstract = True



# модель продуктов
class Product(CreateDateModel):
    STATUS = Choices('Available', 'Not existed')
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media', null=False, blank=False)
    status = StatusField
    description = models.TextField()
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title


# модель отзывов
class ProductReview(CreateDateModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='reviews'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews', null=True
    )
    text = models.TextField()
    rating = models.PositiveIntegerField(default=1)


