from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from network.filter import SearchNetworkLink
from network.models import Product, NetworkLink
from network.serializers import ProductSerializers, NetworkLinkSerializers


class ProductViewSet(viewsets.ModelViewSet):
    """ CRUD модели продукта """
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class NetworkLinkCreateApiView(CreateAPIView):
    """ Создание звена сети"""
    serializer_class = NetworkLinkSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save()
        user.user = self.request.user
        user.save()


class NetworkLinkListApiView(ListAPIView):
    """ Просмотр звена сети и также фильтрация по стране """
    serializer_class = NetworkLinkSerializers
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SearchNetworkLink


class NetworkLinkRetrieveApiView(RetrieveAPIView):
    """ Просмотр текущего звена сети """
    serializer_class = NetworkLinkSerializers
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated]


class NetworkLinkUpdateApiView(UpdateAPIView):
    """ Редактирование звена сети"""
    serializer_class = NetworkLinkSerializers
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated]


class NetworkLinkDestroyApiView(DestroyAPIView):
    """ Удаление звена сети """
    serializer_class = NetworkLinkSerializers
    queryset = NetworkLink.objects.all()
    permission_classes = [IsAuthenticated]
