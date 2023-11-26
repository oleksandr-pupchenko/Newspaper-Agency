from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from agency.models import Topic, Newspaper, Publisher

TOPIC_LIST_URL = reverse("agency:topic-list")
NEWSPAPER_LIST_URL = reverse("agency:newspaper-list")
PUBLISHER_LIST_URL = reverse("agency:publisher-list")


class TopicSearchFormTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user1 = get_user_model().objects.create_user(
            username="admin_test1",
            password="test123"
        )
        self.client.force_login(self.user1)

    def test_search_topic_by_name(self):
        response = self.client.get(TOPIC_LIST_URL + "?name=Crime")

        self.assertEqual(
            list(response.context["topic_list"]),
            list(Topic.objects.filter(name__icontains="Crime"))
        )


class ArticleSearchFormTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user2 = get_user_model().objects.create_user(
            username="admin_test22",
            password="test123"
        )
        self.client.force_login(self.user2)

    def test_search_article_by_title(self):
        response = self.client.get(NEWSPAPER_LIST_URL + "?title=Artificial")

        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(Newspaper.objects.filter(title__icontains="Artificial"))
        )


class PublisherSearchFormTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user3 = get_user_model().objects.create_user(
            username="admin_test333",
            password="test123"
        )
        self.client.force_login(self.user3)

    def test_search_publisher_by_username(self):
        response = self.client.get(PUBLISHER_LIST_URL + "?Username=admin")

        self.assertEqual(
            list(response.context["publisher_list"]),
            list(Publisher.objects.filter(username__icontains="admin"))
        )
        