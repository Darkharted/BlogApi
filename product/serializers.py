from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    """
    Класс для перевода типов данных Python в json формат
    """
    class Meta:
        """
        Класс для передачи дополнительных данных
        """
        model = Product
        fields = "__all__"
