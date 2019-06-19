from rest_framework import serializers
from api.models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    price = serializers.FloatField()
    quantity = serializers.CharField(required=True)

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)


class ProductSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'created_by',)
        # fields = '__all__'


class UserProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.CharField(required=True)
    count = serializers.IntegerField()
    category = ProductSerializer2()
