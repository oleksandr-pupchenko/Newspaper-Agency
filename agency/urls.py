from django.urls import path
from agency.views import (
    index,
    TopicListView,
    NewspaperListView,
    PublisherListView
)

urlpatterns = [
    path("", index, name="index"),
path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "articles/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
    path(
        "publishers/",
        PublisherListView.as_view(),
        name="publisher-list",
    ),
]

app_name = "agency"
