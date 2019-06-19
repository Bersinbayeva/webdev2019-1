from api.models import ProductsList, UserProducts, UserProductsList
from api.serializers import ProductsListSerializer2, UserProductSerializer2, UserProductListSerializer2
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from django.http.response import Http404

class ProductsList(APIView):
    def get(self, request):
        task_lists = ProductsList.objects.all()
        serializer = ProductsListSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserProducts(APIView):
    def get(self, request):
        task_lists = UserProducts.objects.all()
        serializer = UserProductSerializer2(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserProductSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProductDetail(APIView):

    def get_object(self, pk):
        try:
            return UserProducts.objects.get(id=pk)
        except UserProducts.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        userProductsList = self.get_object(pk)
        serializer = UserProductSerializer2(userProductsList)
        return Response(serializer.data)

    def delete(self, request, pk):
        userProductsList = self.get_object(pk)
        userProductsList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
