from django.shortcuts import render
from .models import Topic, Entry
from .forms import TopicForm
from .forms import EntryForm
from django.shortcuts import redirect


def index(request):
    return render(request, 'TMTool/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'TMTool/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'TMTool/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('TMTool:topics')

    context = {'form': form}
    return render(request, 'TMTool/new_topic.html', context)

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

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('TMTool:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'TMTool/edit_entry.html', context)