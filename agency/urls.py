from django.urls import path
from agency.views import (
    index,
    TopicListView,
    NewspaperListView,
    PublisherListView,
    NewspaperDetailView,
    PublisherDetailView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "topics/",
        TopicListView.as_view(),
        name="topic-list",
    ),
    path(
        "topics/create/",
        TopicCreateView.as_view(),
        name="topic-create",
    ),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update",
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),
    path(
        "articles/",
        NewspaperListView.as_view(),
        name="newspaper-list",
    ),
    path(
        "articles/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="article-detail",
    ),
    path(
        "publishers/",
        PublisherListView.as_view(),
        name="publisher-list",
    ),
    path(
        "publishers/<int:pk>/",
        PublisherDetailView.as_view(),
        name="publisher-detail",
    ),
]

app_name = "agency"
