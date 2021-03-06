from rest_framework import serializers

from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=1000, required=True)
    name = serializers.CharField(max_length=1000, required=True)

    def create(self, validated_data):
        # Once the request data has been validated, we can create a product item instance in the database
        return Product.objects.create(
            category=validated_data.get('category'),
            name=validated_data.get('name')
        )

    def update(self, instance, validated_data):
        # Once the request data has been validated, we can update the product item instance in the database
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'name',
            'image'
        )
