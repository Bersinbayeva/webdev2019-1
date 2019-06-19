from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Product, UserProduct
from api.serializers import ProductSerializer2, UserProductSerializer


class ProductList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Product.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return ProductSerializer2

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserProductList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return UserProduct.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return  UserProductSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class UserProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class =  UserProductSerializer