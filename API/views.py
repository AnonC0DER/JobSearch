from API.serializer import Eestekhdam, Yarijob, Karboom, JobSearch, JobInja
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
##############################################

@api_view(['GET'])
def AllMethods(request):
    '''All API methods which are available'''
    routes = [
        {
            'GET' : {
                '/job-search/query/',
                '/e-estekhdam/query/',
                '/yarijob/query/',
                '/karboom/query/'
            },
            'POST' : {
                '/job-search/'
            }
        }
    ]

    return Response(routes, status=status.HTTP_200_OK)


class JobSearchView(APIView):
    '''Search in JobSearch database and return jobs'''

    def get(self, request, query, format=None):
        '''GET method'''

        # Check the result
        if JobSearch(query) != 'Not found':
            # Get results
            data = JobSearch(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        '''POST method'''

        query = request.data['query']

        # Check the result
        if JobSearch(query) != 'Not found':
            # Get results
            data = JobSearch(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)



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


@api_view(['GET'])
def JobinjaView(request, query):
    '''Return results from jobinja.ir'''

    # Check the result
    if JobInja(query) != 'Not found':
        # Get results
        data = JobInja(query)

        # Return the response        
        return Response(data=data, status=status.HTTP_200_OK)

    # If not found
    else:
        data = {'Error' : 'Not found'}
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)