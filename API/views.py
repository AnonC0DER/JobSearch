from API.serializer import Eestekhdam, Yarijob, Karboom
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
##############################################

@api_view(['GET'])
def AllMethods(request):
    '''All API methods which are available'''
    routes = [
        {'GET' : '/job-search/query/'},
        {'GET' : '/e-estekhdam/query/'},
        {'GET' : '/yarijob/query/'},
        {'GET' : '/karboom/query/'},
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
        data = {'Error' : 'Not found'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def YarijobView(request, query):
    '''Return results from yarijob.ir'''

    # Check the result
    if Yarijob(query) != 'Not found':
        # Get results
        data = Yarijob(query)

        # Return the response        
        return Response(data=data, status=status.HTTP_200_OK)

    # If not found
    else:
        data = {'Error' : 'Not found'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def KarboomView(request, query):
    '''Return results from karboom.io'''

    # Check the result
    if Karboom(query) != 'Not found':
        # Get results
        data = Karboom(query)

        # Return the response        
        return Response(data=data, status=status.HTTP_200_OK)

    # If not found
    else:
        data = {'Error' : 'Not found'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)