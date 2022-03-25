from django.test import TestCase

class TestViews(TestCase):

    def test_get_register(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')
        
    def test_get_profile(self):
        response = self.client.get('/profile')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_can_register(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

