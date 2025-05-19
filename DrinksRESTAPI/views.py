from django.http import JsonResponse

# Rest Framework Stack Dependencies
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Drink

from .serializers import DrinkSerializer


# API Endpoints
def drinkListView(request):
  # Get all drinks
  # Serialize them
  # Return JSON

  # Getting Query Set of all drinks 
  drinks = Drink.objects.all()

  serializer = DrinkSerializer(drinks, many=True)
  # Since we are passing the serializer a container of objects,
  # We have to set the many equal to true so it knows it a container
  # of serializable objects

  return JsonResponse({'drinks':serializer.data}) # Returns a JSON \


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