from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class CustomerUserManagerTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='user@user.com,',password='foo')
        self.assertEqual(user.email,'user@user.com')
        self.assertEqual(user.password,'foo')
        self.assertTrue(user.active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='',password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        adminuser = User.objects.create_user(email='test@test.com,',password='pass')

        
        self.assertEqual(adminuser.email,'test@test.com')
        self.assertEqual(adminuser.password,'pass')

        self.assertTrue(adminuser.is_staff) 
        self.assertTrue(adminuser.is_superuser)
        self.assertTrue(adminuser.active)
