from django.test import Testcase, Client
from reviews.views import index

class TestIndexView(Testcase):
    "Test the index view"
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)