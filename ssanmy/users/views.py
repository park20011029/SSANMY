import json, re, traceback,bcrypt, jwt, my_settings

from django.http            import JsonResponse  
from django.views           import View          
from django.core.exceptions import ValidationError
from django.db.models       import Q                                                                                                                
from .models                import Account      
from django.shortcuts import render

MINIMUM_PASSWORD_LENGTH = 8 
def login_page(request):
     return render(request, 'login.html')

class SignUp(View):
    def post(self, request):
        data =json.loads(request.body)

def validate_email(email):
     pattern = re.compile('^.+@+.+\.+.+$')
     if not pattern.match(email):
         return JsonResponse({'message':'INVALID_EMAIL'}, status=400)

 # 패스워드 길이 검사
def validate_password(password):
     if len(password) < MINIMUM_PASSWORD_LENGTH:
         return JsonResponse({'message':'SHORT_PASSWORD'}, status=400)

 # 핸드폰 번호 검사        
def validate_phone(phone):
     pattern = re.compile('^[0]\d{9, 10}$')
     if not pattern.match(phone):
         return JsonResponse({'message':'USER_ALREADY_EXISTS'}, status=409)

class SignUpView(View):
         def post(self, request):
            data =json.loads(request.body)
            e_data = request.GET.get('Email')
            n_data = request.GET.get('Name')
            p_data = request.GET.get('Password')
            try:                                             
                 email    = e_data
                 #email    = data.get('email', None)
                 password = p_data        
                 #password = data.get('password', None)          
                 name     = n_data
                 #name     = data.get('name', None)
                 nickname = data.get('nickname', None)
                 phone    = data.get('phone', None)


                 # KEY_ERROR check                            
                 if not(password and email and name and phone and nickname):
                     return JsonResponse({'message': 'KEY_ERROR'}, status=400)                  

                 # validation check                                                             
                 validate_email(email)
                 validate_password(password)                                                               
                 # unique check                                                                 
                 user = Account.objects.filter(Q(email=email) | Q(name=name) | Q(phone=phone))  
                 if not user:                                                                   
                     Account.objects.create(         
                     email    = email,                            
                     name     = name,
                     phone    = phone,
                     nickname = nickname,
                     password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                     )
                     return JsonResponse({'message': 'SUCCESS'}, status=200)

                 return JsonResponse({'message': 'USER_ALREADY_EXISTS'}, status=409)

            except KeyError:  
                return JsonResponse({"message": "KEY_ERROR"}, status=400)
            
class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        try :
            email    = data.get('email')
            phone    = data.get('phone')
            password = data.get('password')

            # 입력한 값이 Email인지 핸드폰 번호인지 검사
            if Account.objects.filter(Q(email=email) | Q(phone=phone)).exists():
                  # 입력한 값이 Email 또는 핸드폰이면 DB에서 확인을 하여 해당 계정의 아이디 값을 account에 저장 
                account = Account.objects.get(Q(email=email) | Q(phone=phone))
                  # Password 검사 및 암호화
                if bcrypt.checkpw(password.encode('utf-8'), account.password.encode('utf-8')):
                    token = jwt.encode({'email' : email}, my_settings.SECRET_KEY, algorithm = 'HS256')
                     # 성공시 200 return 
                    return JsonResponse({'message' : 'SUCCESS'}, status=200)
                 # Password 틀렸을시 return   
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)
             # ID 틀렸을시 return    
            return JsonResponse({"message": "INVALID_USER"}, status=401)
      # 다른 값을 입력했을시 return
        except KeyError: 
            return JsonResponse({"message": "KEY_ERROR"}, status=400)