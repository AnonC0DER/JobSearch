from API.serializer import Eestekhdam
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
##############################################

@api_view(['GET'])
def AllMethods(request):
    '''All API methods which are available'''
    routes = [
        {'GET' : '/job-search/'},
        {'GET' : '/e-estekhdam/'},
        {'POST' : '/bing-search/'},
        {'POST' : '/pypi-search/'},
        {'POST' : '/subscene-search/'},
    ]

    return Response(routes)


@api_view(['GET'])
def EestekhdamView(request, query):
    '''Return results from e-estekhdam.com'''

    # Check the result
    if Eestekhdam(query) != 'Not found':
        # Get results
        data = Eestekhdam(query)

        # Return the response        
        return Response(data=data, status=status.HTTP_200_OK)

    # If not found
    else:
        data = {'Bad request' : 'Not found'}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



