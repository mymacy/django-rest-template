# Views are for actual functionality, very special validation and responses
###############################################################################
from django.http.response import HttpResponseRedirect
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
# Serializers and Models
from .serializers import *
from .models import *
# Base Class Views
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# Permissions and Custom Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
# Other
import requests
import time         # for activation TODO

'''
##########################    User Profile and Auth
'''
class UserList(ListAPIView):
    '''
    list all
    '''
    queryset = CustomUser.objects.all()                         # was wollen wir alles sehen ?
    serializer_class = CustomUserSerializer                     # needs to be set always


class ActivationLink(APIView):
    '''
    activates the account by sending the correct request to self
    '''
    def get(self, request, uid, token, format=None):
        domain = 'http://' + request.META['HTTP_HOST']
        target = domain + '/api/users/activate/'
        r = requests.post(target, data = {'uid': uid, 'token': token})
        time.sleep(0.5)
        return HttpResponseRedirect(redirect_to=domain)


class ResetConfirm(APIView):
    '''
    Redirects the User to the website with uid and token given as parameters
    '''
    def get(self, request, uid, token, format=None):
        return HttpResponseRedirect(redirect_to='http://127.0.0.1:8080/?uid='+uid+'&token='+token)


class CheckAuth(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        user = CustomUser.objects.get(id=request.user.id)
        print(user)
        print(user.profile)
        serializer = CustomUserSerializer(user)
        print(serializer.data)
        return Response(serializer.data)


class UpdateProfile(APIView):                                   # TODO
    permission_classes = [IsAuthenticated,]
    def get(self, request, format=None):
        respo = "yalla lol"
        user = User.objects.get(pk=4)
        user.profile.customField1 = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
        user.save()
        print(user.profile.customField1)
        return Response("yesyoa")



'''
##########################    GENERICS API VIEWS
rud -> retrieve update destory
'''
class RezeptListView(ListAPIView):
    ''' list all '''
    queryset = Rezept.objects.all().order_by('url')         # was wollen wir alles sehen ? welche order?
    serializer_class = RezeptSerializer                     # needs to be set always


class RezeptCreateView(CreateAPIView):
    queryset = Rezept.objects.all()
    serializer_class = RezeptSerializer
    permission_classes = [IsAuthenticated,]

    def perform_create(self, serializer):                   # OPTIONAL Overwrite
        print(self.request.user.profile.customField1)       # nur mal so als reminder das es geht
        serializer.save(author=self.request.user)           # necessary here weil Rezept Autor braucht !


class RezeptRudView(RetrieveUpdateDestroyAPIView):
    ''' master class for changing '''
    queryset = Rezept.objects.all()
    serializer_class = DetailSerializer
    http_method_names = ['get', 'post', 'head']             # change allowed methods here !

    # lookup_field = 'titel'                                # OPTIONAL specific target

    # def get_object(self):                                 # OPTIONAL speicifc target
    #     titel = self.kwargs.get("title")                  # can be used to change the target
    #     return Rezept.objects.get(title=title)            # weitere alternative um es noch genaur zu machen

    # def get_queryset(self):                               # OPTIONAL specific queryset
    #    qs = Rezept.objects.all()                          # https://www.youtube.com/watch?v=tG6O8YF91HE 30 mins
    #    query = self.request.GET.get("q")                  # spezielle suchen mit GET params
    #    if query is not None:
    #        qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
    #    return qs


'''
##########################    Main API Classes
'''
class StockListClass(APIView):
    def post(self, request, format=None):
        response = {
            "url": "http://www.healthy-horses.net",
            "success": True,
            "cms": "Wordpress",
            "version": "1.5.6",
            "vendorVersion": "1.7.3",
            "up2date": False,
            }
        return Response(response, status=status.HTTP_201_CREATED)

    def get(self, request, format=None):
        stocks = Stock.objects.all()
        print(stocks)
        serializer = StockSerializer(stocks, many=True)
        print(serializer.data)
        print(serializer.data[0])
        return Response("serializer.data")

    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            stock = Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = StockSerializer(stock)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = StockSerializer(stock, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
