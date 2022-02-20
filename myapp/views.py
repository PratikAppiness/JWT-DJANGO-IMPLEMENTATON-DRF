from itertools import product
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication

from . import models
from . import serializers

# Create your views here.
class TestApi(APIView):
  authentication_classes = [JWTTokenUserAuthentication,]
  permission_classes = [IsAuthenticated]

  def get(self, request):
    """
    Write Operations
    """
    queryset      = models.Product.objects.all()
    serializer    = serializers.ProductSerializer(queryset, many=True)
    return JsonResponse({'status':200, 'data':serializer.data})

  def post(self, request):
    """
    Write Operations
    """
    queryset      = models.ProductCategory.objects.all()
    serializer    = serializers.ProductCategorySerializer(queryset, many=True)
    return JsonResponse({'status':200, 'data':serializer.data})