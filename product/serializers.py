from rest_framework import serializers
from .models import Product, ProductReview



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




class ProductReviewSerializer(serializers.ModelSerializer):

    product_title = serializers.SerializerMethodField("get_product_title")

    def get_product_title(self, product_review):
        title = product_review.product.title
        return title

    class Meta:
        model = ProductReview
        fields = "__all__"

    def validate_product(self,product):
        if self.Meta.model.objects.filter(product=product).exists() == True:
            raise serializers.ValidationError('Вы уже оставляли отзыв на данных продукт')
        return  product

    def validate_rating(self, rating):
        if rating not in range(1,6):
            raise serializers.ValidationError(
                'Рейтинг должен быть от 1 до 5'
            )
        return rating

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user
        print(author)
        return ProductReview.objects.create(author=author, **validated_data)