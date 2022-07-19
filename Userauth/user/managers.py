from django.contrib.auth.base_user import BaseUserManager

class CustomerUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        '''
        creates and save a user with the given email and password
        '''
        
        if not email:
            raise ValueError('email is required')
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra_fields):
        '''
        creates and save a superuser with the given email and password
        '''
        
        user = self.create_user(email,password,**extra_fields)
        user.is_staff = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

        