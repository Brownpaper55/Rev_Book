from django.test import TestCase, Client
from reviews.models import Book, Contributor, Publisher 

class TestPublisherModel(TestCase):
    "Test the publisher model"
    def setUp(self):
        self.p = Publisher(name='Packt', website='www.packt.com', email='contact@packt.com')

    def test_create_publisher(self):
        self.assertIsInstance(self.p, Publisher)

    def test_str_representation(self):
        self.assertEquals(str(self.p),"Packt")


class TestBookModel(TestCase):
    "Test the book model"
    def setUp(self):
        self.publisher = Publisher.objects.create(name='Packt', website='www.packt.com', email='contact@packt.com')
        self.contributor = Contributor.objects.create(first_names='kweku', last_names='gyan', email='kwaku@g.com')
       
    def test_create_book(self):
        self.book = Book.objects.create(title='rider', publication_date='2000-12-07', isbn='1234', publisher=self.publisher)
        self.book.contributor.set([self.contributor])

        self.assertIsInstance(self.book, Book)

    def test_str_representations(self):
        self.assertEquals(str(self.book), 'rider')
    
class TestContributorModel(TestCase):
    "Test the contributor model"
    def setUp(self):
        self.contributor = Contributor.objects.create(first_names='kweku', last_names='gyan', email='kwaku@g.com')

    def test_create_contributor(self):
        self.assertIsInstance(self.contributor, Contributor)

    def test_str_representation(self):
        self.assertEquals(str(self.contributor),'gyan')