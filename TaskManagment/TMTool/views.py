from .models import Topic, Entry
from .forms import TopicForm
from .forms import EntryForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone


def index(request):
    if request.user.is_authenticated:
        return render(request, 'TMTool/home_page.html')
    return render(request, 'TMTool/index.html')

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'TMTool/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    topic.last_accessed = timezone.now()
    topic.save()
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'TMTool/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('TMTool:topics')

    context = {'form': form}
    return render(request, 'TMTool/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('TMTool:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'TMTool/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('TMTool:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'TMTool/edit_entry.html', context)

@login_required
def home_page(request):
    last_topics = Topic.objects.filter(owner=request.user).order_by('-last_accessed')[:3]
    context = {'last_topics': last_topics}
    return render(request, 'TMTool/home_page.html', context)

@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method == 'POST':
        entry.delete_entry()
        return redirect('TMTool:topic', topic_id=topic.id)
    context = {'entry': entry}
    return render(request, 'TMTool/topic.html', context)

@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method == 'POST':
        topic.delete_topic()
        return redirect('TMTool:topics')
    context = {'topic': topic}
    return render(request, 'TMTool/topics.html', context)
