from django.shortcuts import render, HttpResponse, redirect

from .forms import MyForm

from .util import list_entries

from random import randint

import markdown2

import os

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def test(request):
    entry = "CS"

    return redirect(entrypage, entry=entry)


def entry(request):
    return render(request, "encyclopedia/test.html", )



def entrypage(request, entry):

    try:
        return render(request, "encyclopedia/entrypage.html", {
            "title":entry,
            "var":markdown2.markdown(util.get_entry(entry))
        })
    except TypeError:
        return redirect(error_page)

    


def random(request):
    entries_list = util.list_entries()
    entry = entries_list[randint(0,(len(entries_list) - 1))]
    return redirect(entrypage, entry=entry)

def search(request):
    query = request.GET.get('q')
    entries = list_entries()
    partial_query = []

    for entry in entries:
        if query.lower() == entry.lower():
            return redirect(entrypage, entry=query)
        
    for string in entries:
        if query.lower() in string.lower():
            print("the string", string)
            partial_query.append(string)
    
    if len(partial_query) > 0:
        return render(request, 'encyclopedia/search.html', {'partial_query':partial_query})
    else:
        return redirect(error_page)


def error_page(request):

    return render(request, 'encyclopedia/error_page.html')

def new_page(request):

    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            entries = []
            for entry in list_entries():
                entries.append(entry.lower())
            title = form.cleaned_data['title']

            if title in entries:
                return redirect(title_exists)
            else:
                content = form.cleaned_data['content']
                util.save_entry(title, content)
                return redirect(entrypage, entry=title)
                
        else:
            return render(request, 'encyclopedia/new_page.html',{
                'form':form
            })
            
    elif request.method == 'GET':
        return render(request, 'encyclopedia/new_page.html')
    else:
        form = MyForm()

def edit_page(request, entry):
    if request.method == 'POST':
        content = request.POST['content']
        util.save_entry(entry, content)
        return redirect('entrypage', entry=entry)
    else:
        content = util.get_entry(entry)
        return render(request, 'encyclopedia/edit_page.html', {
                "title":entry,
                "content":content
            })




def title_exists(request):

    return render(request, 'encyclopedia/title_exists.html')


