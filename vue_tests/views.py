from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from shop.models import Category, Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin


class ProductListView(
    APIView, # Basic View class provided by the Django Rest Framework
    UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
    DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

    def get(self, request, id=None):
        if id:
            # If an id is provided in the GET request, retrieve the Product item by that id
            try:
                # Check if the Product item the user wants to update exists
                queryset = Product.objects.get(id=id)
            except Product.DoesNotExist:
                # If the Product item does not exist, return an error response
                return Response({'errors': 'This Product item does not exist.'}, status=400)

            # Serialize Product item from Django queryset object to JSON formatted data
            read_serializer = ProductSerializer(queryset)

        else:
            # Get all Product items from the database using Django's model ORM
            queryset = Product.objects.all()

            # Serialize list of Products item from Django queryset object to JSON formatted data
            read_serializer = ProductSerializer(queryset, many=True)

        # Return a HTTP response object with the list of Product items as JSON
        return Response(read_serializer.data)

    def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
        create_serializer = ProductSerializer(data=request.data)

        # Check if user POST data passes validation checks from serializer
        if create_serializer.is_valid():

            # If user data is valid, create a new Product item record in the database
            product_item_object = create_serializer.save()

            # Serialize the new Product item from a Python object to JSON format
            read_serializer = ProductSerializer(product_item_object)

            # Return a HTTP response with the newly created Product item data
            return Response(read_serializer.data, status=201)

        # If the users POST data is not valid, return a 400 response with an error message
        return Response(create_serializer.errors, status=400)

    def put(self, request, id=None):
        try:
            # Check if the Product item the user wants to update exists
            product_item = Product.objects.get(id=id)
        except Product.DoesNotExist:
            # If the Product item does not exist, return an error response
            return Response({'errors': 'This Product item does not exist.'}, status=400)

        # If the Product item does exists, use the serializer to validate the updated data
        update_serializer = ProductSerializer(product_item, data=request.data)

        # If the data to update the Product item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

            # Data was valid, update the Product item in the database
            product_item_object = update_serializer.save()

            # Serialize the Product item from Python object to JSON format
            read_serializer = ProductSerializer(product_item_object)

            # Return a HTTP response with the newly updated Product item
            return Response(read_serializer.data, status=200)

        # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

    def delete(self, request, id=None):
        try:
            # Check if the Product item the user wants to update exists
            product_item = Product.objects.get(id=id)
        except Product.DoesNotExist:
            # If the Product item does not exist, return an error response
            return Response({'errors': 'This Product item does not exist.'}, status=400)

        # Delete the chosen Product item from the database
        product_item.delete()

        # Return a HTTP response notifying that the Product item was successfully deleted
        return Response(status=204)
