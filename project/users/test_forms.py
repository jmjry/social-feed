from django.test import TestCase
from .forms import UserRegisterForm


class TestItemForm(TestCase):

    def test_username_required(self):
        form = UserRegisterForm({'username'})
        self.assertFalse(form.is_valid)
        self.assertIn('username', form.errors.keys)
        self.assertEqual(form.errors['username'][0], 'This field is required.')

    
    def test_email_required(self):
        form = UserRegisterForm({'email'})
        self.assertFalse(form.is_valid)
        self.assertIn('email', form.errors.keys)
        self.assertEqual(form.errors['email'][0], 'This field is required.')


    def test_password1_required(self):
        form = UserRegisterForm({'password1'})
        self.assertFalse(form.is_valid)
        self.assertIn('password1', form.errors.keys)
        self.assertEqual(form.errors['password1'][0], 'This field is required.')