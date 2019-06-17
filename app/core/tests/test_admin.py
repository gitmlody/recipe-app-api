from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client() #we created client object
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'mygmail@gmail.com',
            password = 'password1234'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email = 'myuser@gmail.com',
            password = 'password1234',
            name = 'user name'
        )

    def test_user_listed(self):
        url =reverse('admin:core_user_changelist')
        res = self.client.get(url) #we get object and save it to the "res" from the given url

        self.assertContains(res, self.user.name) #we check if there are names and emails of our users 
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page wokrks"""
        url = reverse('admin:core_user_change',args=[self.user.id])
        #/admin/core/user/1(user id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)