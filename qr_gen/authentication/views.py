from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        cnfrm_password = request.POST.get('cnfrm_password', None)

        if password != cnfrm_password:
            messages.error(request, 'Passwords do not match!')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('authentication:signup')

        user = User.objects.create(email=email)
        user.set_password(password)
        user.save()
        login(request,user)
        return redirect('authentication:index')
    return render(request, 'authentication/registration.html')


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, mark_safe(f'You are already logged in as <b>{request.user.email}</b>.' ))
        return redirect('authentication:index')

    username = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'{user.email} logged in successfully!')
            # if not remember_me:
            #     request.session.set_expiry(0)
            # return redirect('website:index')
        else:
            messages.warning(request, 'Please check your credentials')

    return render(request, 'authentication/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You have logged out successfully!')
    return redirect('authentication:index')


# from rest_framework.generics import GenericAPIView
# from rest_framework import response, status, permissions
# from django.contrib.auth import authenticate
# from authentication.serializers import RegisterSerializer, LoginSerializer


# class AuthUserAPIView(GenericAPIView):

#     permission_classes = [
#         permissions.IsAuthenticated,
#     ]

#     def get(self, request):
#         user = request.user
#         serializer = RegisterSerializer(user)
#         return response.Response({"user": serializer.data})


# class RegisterAPIView(GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data, status=status.HTTP_201_CREATED)
#         return response.Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#         )  # bad request from user e.g inputer less than 6pasword


# class LoginAPIView(GenericAPIView):

#     serializer_class = LoginSerializer

#     def post(self, request):
#         email = request.data.get("email", None)
#         password = request.data.get("password", None)

#         user = authenticate(username=email, password=password)

#         if user:
#             serializer = self.serializer_class(user)

#             return response.Response(serializer.data, status=status.HTTP_200_OK)
#         return response.Response(
#             {"message": "Invalid credentials, try again"},
#             status=status.HTTP_401_UNAUTHORIZED,
#         )
