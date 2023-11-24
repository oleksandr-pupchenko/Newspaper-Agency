from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic.base import ContextMixin

from agency.forms import TopicForm
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


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("agency:topic-list")

    def form_valid(self, form):
        if self.request.POST.get('action') == 'create':
            form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return HttpResponseRedirect(reverse("agency:topic-list"))
        else:
            return super().post(request, *args, **kwargs)


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    form_class = TopicForm
    success_url = reverse_lazy("agency:topic-list")

    def get_initial(self):
        initial = super().get_initial()
        if self.object.name:
            initial["cancel"] = True
        return initial

    def form_valid(self, form):
        if self.request.POST.get("action") == "update" and "cancel" in self.request.POST:
            return HttpResponseRedirect(self.get_success_url())
        return super().form_valid(form)


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView, ContextMixin):
    model = Topic
    success_url = reverse_lazy("agency:topic-list")


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    paginate_by = 5
    queryset = Newspaper.objects.all().select_related("topic")


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class PublisherListView(LoginRequiredMixin, generic.ListView):
    model = Publisher
    paginate_by = 5


class PublisherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Publisher
    queryset = Publisher.objects.all().prefetch_related("newspapers__topic")
