from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Topic, Newspaper, Publisher


class TopicModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Topic.objects.create(name="Crime")

    def test_name_label(self):
        topic = Topic.objects.get(id=1)
        field_label = topic._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        topic = Topic.objects.get(id=1)
        max_length = topic._meta.get_field("name").max_length
        self.assertEqual(max_length, 255)

    def test_topic_str(self):
        topic = Topic.objects.get(id=1)
        expected_object_name = topic.name
        self.assertEqual(str(topic), expected_object_name)


class PublisherModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="Test first",
            last_name="Test last",
            years_of_experience=1
        )

    def test_publisher_str(self):
        publisher = Publisher.objects.get(id=1)
        expected_object_name = f"{publisher.username}" \
                               f" ({publisher.first_name}" \
                               f" {publisher.last_name})"
        self.assertEqual(str(publisher), expected_object_name)

    def test_years_of_experience_label(self):
        publisher = Publisher.objects.get(id=1)
        field_label = publisher._meta.get_field("years_of_experience").verbose_name
        self.assertEqual(field_label, "years of experience")

    def test_get_absolute_url(self):
        publisher = Publisher.objects.get(id=1)
        self.assertEqual(publisher.get_absolute_url(), '/publishers/1/')


class NewspaperModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        topic = Topic.objects.create(name="Crime")
        Newspaper.objects.create(
            title="Test",
            content="testtesttest",
            topic=topic,
        )

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.get(id=1)
        expected_object_name = newspaper.title
        self.assertEqual(str(newspaper), expected_object_name)
