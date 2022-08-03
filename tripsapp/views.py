from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import UserCreateSerializer
from .serializers import UserLoginSerializer
from .serializers import UpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Profile


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    
    
    
class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
    
class UserUpdateAPIView(UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserCreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    
    