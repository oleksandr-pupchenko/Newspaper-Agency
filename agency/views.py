from django.shortcuts import render
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
