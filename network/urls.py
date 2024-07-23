from django.urls import path
from rest_framework.routers import DefaultRouter

from network.apps import NetworkConfig
from network.views import ProductViewSet, NetworkLinkCreateApiView, NetworkLinkListApiView, NetworkLinkRetrieveApiView, \
    NetworkLinkUpdateApiView, NetworkLinkDestroyApiView

app_name = NetworkConfig.name

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')


urlpatterns = [
    path('network/create/', NetworkLinkCreateApiView.as_view(), name='create'),
    path('network/list/', NetworkLinkListApiView.as_view(), name='list'),
    path('network/<int:pk>/', NetworkLinkRetrieveApiView.as_view(), name='get'),
    path('network/update/<int:pk>/', NetworkLinkUpdateApiView.as_view(), name='update'),
    path('network/delete/<int:pk>/', NetworkLinkDestroyApiView.as_view(), name='delete'),
] + router.urls
