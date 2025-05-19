from django.http import JsonResponse

# Rest Framework Stack Dependencies
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Drink

from .serializers import DrinkSerializer


# API Endpoint Views
@api_view(['GET', 'POST']) # Decorator for CRUD ops the corresponding endpoint should respond to
def drinkListView(request):
  # Defualt Request Method (in django when just hitting a url) is: get (read)
  # We can add other request to do other operations in CRUD
  # (C)rete = POST
  # (R)ead =  GET
  # (U)pdate = PUT or PATCH
  # (D)elete = DELETE

  if request.method == 'GET': 
    # Serialization Work Flow (Python -> JSON)
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)

    return JsonResponse({'drinks':serializer.data}) # Returns a JSON 

  if request.method == 'POST':
    # Deserialization Work Flow (JSON -> Python)
    serializer = DrinkSerializer(data=request.data) # getting data from request
    if serializer.is_valid():
      serializer.save() # Save the instance of the serialized JSON data

      return Response(serializer.data, status=status.HTTP_201_CREATED)


class classDrinkListView(APIView):
  # The Class Views need to inherit from the Import: APIView
  
  def get(self, request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)

    return Response(serializer.data)





# Notes About Reponses

# By default, JsonResponse expects a dictionary (dict) as its first argument. That’s because:
  # JSON objects map to Python dicts.
  # Lists could be returned by mistake and cause unexpected issues.
  # Django enforces this unless you explicitly override it.

# *******
# Making the Response list of objects into a dict with a key
# and the data being the value of that key (data is a list of objects still)
# (Basically making the return data into an object)
  # return the serializer.data in a static typed data brackets
  # The key being what you want the name of the object to be
  # The value being the serializer.data


# Rest Framework Responses
  # This type of JSON response handles all basic python containers and does not
  # require the safe parameter to be set to false

  # It is tightly coupled to the framework stack of redering views however
  # IT required the use of classed based views