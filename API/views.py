from API.serializer import Eestekhdam, Yarijob, Karboom, JobSearch, JobInja, Linkedin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
##############################################

class AllMethods(APIView):
    '''All API methods which are available'''

    data = [
        {
            'GET' : {
                '/job-search/query/',
                '/linkedin/query/',
                '/e-estekhdam/query/',
                '/yarijob/query/',
                '/karboom/query/',
                '/jobinja/query/',
            },
            'POST' : {
                '/job-search/',
                '/linkedin/',
                '/e-estekhdam/',
                '/yarijob/',
                '/karboom/',
                '/jobinja/',
            },
            'Create token and get authtoken (POST)' : {
                    '/users/create/',
                    '/users/token/',
            },
            'Documentation' : {
                '/docs/',
            }
        }
    ]

    def get(self, request, format=None):
        '''GET method'''
        
        return Response(data=self.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        '''POST method'''
        
        return Response(data=self.data, status=status.HTTP_200_OK)


class JobSearchView(APIView):
    '''Search in JobSearch database and return jobs'''

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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


class LinkedinView(APIView):
    '''Return results from linkedin.com'''

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, query, format=None):
        '''GET method'''

        # Check the result
        if Linkedin(query) != 'Not found':
            # Get results
            data = Linkedin(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        '''POST method'''

        query = request.data['query']

        # Check the result
        if Linkedin(query) != 'Not found':
            # Get results
            data = Linkedin(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)


class EestekhdamView(APIView):
    '''Return results from e-estekhdam.com'''

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, query, format=None):
        '''GET method'''

        # Check the result
        if Eestekhdam(query) != 'Not found':
            # Get results
            data = Eestekhdam(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        '''POST method'''

        query = request.data['query']

        # Check the result
        if Eestekhdam(query) != 'Not found':
            # Get results
            data = Eestekhdam(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)


class YarijobView(APIView):
    '''Return results from yarijob.ir'''

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, query, format=None):
        '''GET method'''

        # Check the result
        if Yarijob(query) != 'Not found':
            # Get results
            data = Yarijob(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        '''POST method'''

        query = request.data['query']

        # Check the result
        if Yarijob(query) != 'Not found':
            # Get results
            data = Yarijob(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)


class KarboomView(APIView):
    '''Return results from karboom.io'''

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, query, format=None):
        '''GET method'''

        # Check the result
        if Karboom(query) != 'Not found':
            # Get results
            data = Karboom(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        '''POST method'''

        query = request.data['query']

        # Check the result
        if Karboom(query) != 'Not found':
            # Get results
            data = Karboom(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)


class JobinjaView(APIView):
    '''Return results from jobinja.ir'''

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, query, format=None):
        '''GET method'''

        # Check the result
        if JobInja(query) != 'Not found':
            # Get results
            data = JobInja(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        '''POST method'''

        query = request.data['query']

        # Check the result
        if JobInja(query) != 'Not found':
            # Get results
            data = JobInja(query)
        
            return Response(data=data, status=status.HTTP_200_OK)

        # If not found
        else:
            data = {'Error' : 'Not found'}
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)