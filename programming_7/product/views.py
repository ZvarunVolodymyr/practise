# Create your views here.
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from helping_func.permission import IsSuperUserOrReadOnly
from product.models import Product
from product.serializers import ProductSerializer


class view(ListAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.validator(data):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = JSONParser().parse(request)
        try:
            product = Product.objects.get(name=data['name'])
        except Exception:
            return Response({'message': 'такого продукту не існує'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class detail_view(APIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    def get_by_id(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response({'message': 'такого продукту не існує'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        obj = self.get_by_id(pk)
        if type(obj) == Response:
            return obj
        serializer = ProductSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_by_id(pk)
        if type(obj) == Response:
            return obj
        data = JSONParser().parse(request)
        data['name'] = obj.name
        serializer = ProductSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_by_id(pk)
        if type(obj) == Response:
            return obj
        obj.delete()
        return Response({'message': 'Продукт успішно видалено'}, status=status.HTTP_204_NO_CONTENT)