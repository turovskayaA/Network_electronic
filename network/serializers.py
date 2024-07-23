from rest_framework import serializers

from network.models import Product, NetworkLink


class ProductSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели продукта """

    class Meta:
        model = Product
        fields = '__all__'


class NetworkLinkSerializers(serializers.ModelSerializer):
    """ Сериализатор для модели звена сети """

    class Meta:
        model = NetworkLink
        fields = "__all__"
        read_only_fields = ["indebtedness"]
