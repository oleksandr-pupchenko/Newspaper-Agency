from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from agency.models import Topic, Newspaper, Publisher


def index(request):
    """View function for the home page of the site."""

    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_publishers = Publisher.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
        "num_publishers": num_publishers,
        "num_visits": num_visits + 1,
    }

    return render(request, "agency/index.html", context=context)


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "agency/topic_list.html"
    paginate_by = 5


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5
    queryset = Newspaper.objects.all().select_related("topic")


class PublisherListView(LoginRequiredMixin, generic.ListView):
    model = Publisher
    paginate_by = 5
