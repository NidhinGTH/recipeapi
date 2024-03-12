from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import Recipe,Review
from .serializers import RecipeSerializer,ReviewSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer
class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Get parameters from the request
        cuisine = self.request.query_params.get('cuisine')
        meal_type = self.request.query_params.get('meal_type')
        ingredients = self.request.query_params.getlist('ingredients')

        # Apply filters if they exist
        if cuisine:
            queryset = queryset.filter(cuisine__icontains=cuisine)
        if meal_type:
            queryset = queryset.filter(meal_type__icontains=meal_type)
        if ingredients:
            ingredient_filters = Q()
            for ingredient in ingredients:
                ingredient_filters |= Q(ingredients__icontains=ingredient)
            queryset = queryset.filter(ingredient_filters)

        return queryset
class ReviewView(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

