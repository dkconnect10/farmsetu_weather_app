import pandas as pd 
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serialization import User_serialization
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate  
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import logout



class user_register(APIView):
    def post(self,request):
        file = request.FILES.get('files')
        print('file:',file)
        
        df = pd.read_excel(file)
       
        user_created = []
        for header , row in df.iterrows():
            print("header :",header)
            print('row:',row)
            user_data = {
                "first_name" : row.get('first_name'),
                "last_name" : row.get('last_name'),
                "email" : row.get('email'),
                "username":row.get('username'),
                "password":row.get('password') 
                
            }
            
            serializ = User_serialization(data = user_data)
            
            if serializ.is_valid():
                user = serializ.save()
                token,_ = Token.objects.get_or_create(user= user )
                user_created.append({
                    "username":user.username,
                    "email":user.email,
                    "token":token.key
                })
            else:
                return Response({"status":404,"error":serializ.errors})    
       
        return Response({'status':200,"user":user_created}) 
    
    
class login_user(APIView):
    def post(self,request):
        username = request.data.get('username')  
        password = request.data.get('password')
        
        print(f"{username},{password}")
        
        if not username and password:
            return Response({"status":404,"message":"username and password is required"},status=404) 
        
        user = authenticate(username=username,password=password) 
        
        if not user:
            return Response({"status":404,"message":"user not register"},status=404)
        if user:
            token,_=Token.objects.get_or_create(user=user)
     
            return Response({
                "status":201,
                "success":True,
                "user":user.username,
                "token":token.key,     
            })
            
            
class logout_user(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]   
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message":"Logout Successfully"},status=status.HTTP_200_OK)
                
        
