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
    TopicDeleteView,
    NewspaperCreateView,
    NewspaperUpdateView,
    NewspaperDeleteView
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
        "articles/create/",
        NewspaperCreateView.as_view(),
        name="newspaper-create",
    ),
    path(
        "articles/<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "articles/<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path(
        "articles/<int:pk>/",
        NewspaperDetailView.as_view(),
        name="newspaper-detail",
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
