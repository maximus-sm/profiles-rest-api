from django.test import TestCase
from .models import UserProfile
from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
# Create your tests here.

def create_user(email,name,password):
    return UserProfile.objects.create_user(email,
                                           name,
                                           password)
    
class UserModelTest(TestCase):
    # manager = UserProfile()
    
    def test_error_no_email(self):
        # newuser = UserProfile.objects.create_user(email="",
        #                                    name="",
        #                                    password="",)
        # print(UserProfile.objects.create(email="test@email.com",
        #                                    name="1244424",
        #                                    password="124124",))
        # print(newuser)
        with self.assertRaises(ValueError):
            UserProfile.objects.create_user(email="",
                                           name="",
                                           password="")
    
    
    def test_create_users_with_same_email(self):
        email = "test@email.com"
        UserProfile.objects.create_user(email,
                                           name="abc",
                                           password="klmfgrec",)
        with self.assertRaises(IntegrityError):
            (UserProfile.objects
                        .create_user(email,
                                     name="zaggg",
                                     password="klmfgrec",))
    
    def test_name_of_the_user(self):
        name = "Messi"
        user = UserProfile.objects.create_user("test@email.com",name,"12345098")
        self.assertIs(name,user.name)
    

class LoginViewTest(TestCase):
    name = "Zaebis"
    email = "test@email.com"
    password = "12345678"
    json = { "username":email,
            "password":password
            }
    
    
    def test_success_login(self):
        user = create_user(self.email,self.name,self.password)
        # response = self.client.post("/api/login/",self.json)
        response = self.client.post(reverse("profiles:login"),self.json)
        print(response.json())
        self.assertEqual(response.status_code,200)
        # login = self.client.login(username=self.email, password=self.password)
        # self.assertTrue(login) 
        
    def test_succes_login_rest(self):
        user = create_user(self.email,self.name,self.password)
        client = APIClient()
        response = client.login(username=self.email, password=self.password)
        self.assertEqual(response,True)
        
    def test_wrong_credintials_login(self):
        response = self.client.post(reverse("profiles:login"),self.json)
        print(response.json())
        self.assertEqual(response.status_code,400)
        
        
        
        
        
        
        
    
    
            
    
            
        
            
    
    