from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Topic, Newspaper, Publisher

TOPIC_LIST_URL = reverse("agency:topic-list")
NEWSPAPER_LIST_URL = reverse("agency:newspaper-list")
PUBLISHER_LIST_URL = reverse("agency:publisher-list")


class PublicTopicTests(TestCase):
    def test_login_required(self):
        response = self.client.get(TOPIC_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateTopicTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_topics(self):
        Topic.objects.create(name="Crime")
        Topic.objects.create(name="Fashion")

        response = self.client.get(TOPIC_LIST_URL)
        topics = Topic.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "agency/topic_list.html")


class PublicNewspaperTests(TestCase):
    def test_login_required_for_list(self):
        response = self.client.get(NEWSPAPER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateNewspaperTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_newspaper_list(self):
        topic_ = Topic.objects.create(name="Crime")
        Newspaper.objects.create(title="Serial Killer was found", topic=topic_)
        Newspaper.objects.create(title="NYFW is about to start", topic=topic_)

        response = self.client.get(NEWSPAPER_LIST_URL)
        newspapers = Newspaper.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(newspapers)
        )
        self.assertTemplateUsed(response, "agency/newspaper_list.html")


class PublicPublisherTests(TestCase):
    def test_login_required_for_list(self):
        response = self.client.get(PUBLISHER_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivatePublisherTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
         )
        self.client.force_login(self.user)

    def test_retrieve_driver_list(self):
        Publisher.objects.create(username="TestAdmin")

        response = self.client.get(PUBLISHER_LIST_URL)
        publishers = Publisher.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["publisher_list"]),
            list(publishers)
        )
        self.assertTemplateUsed(response, "agency/publisher_list.html")
