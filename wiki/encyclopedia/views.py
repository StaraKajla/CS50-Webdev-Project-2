from django.shortcuts import redirect, render
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request):
    return render(request, "encyclopedia/wiki.html", {
        "entries": util.list_entries()
    })

def title(request, name):
    if not util.get_entry(name):
        return render(request, "encyclopedia/notfound.html", {
            "title": name.capitalize(),
            "missingPage": name
        })
        
    return render(request, "encyclopedia/titleSearch.html", {
        "entry": util.get_entry(name),
        "title": name.capitalize()
    })

def query(request):
    q = request.GET.get('q')
    match = util.get_entry(q)
    if match:
        return render(request, "encyclopedia/titleSearch.html", {
            "entry": match,
            "title": q.capitalize()
        })

    else:
        similarEntries = []
        for entry in util.list_entries():
            if q.lower() in entry.lower():
                similarEntries.append(entry)

        return render(request, "encyclopedia/searchresults.html", {
            "entries": similarEntries,
            "searchParam": q
    })
    
def newPage(request):
    return render(request, "encyclopedia/newpage.html")

def save(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

    match = util.get_entry(title)
    if match:
        return render(request, "encyclopedia/page_exists.html", {
            "title": title.capitalize()
        })

    util.save_entry(title, content)

    return render(request, "encyclopedia/titleSearch.html", {
        "entry": util.get_entry(title),
        "title": title.capitalize()
    })

def edit(request, name):

    currentContent = util.get_entry(name)

    if request.method == "POST":
        title = name
        content = request.POST.get("content")

        util.save_entry(title, content)

        return redirect(f"/wiki/{title}", {
            "title": name,
            "entry": currentContent            
        })

    return render(request, "encyclopedia/edit.html", {
        "editTitle": name,
        "currentContent": currentContent
    })

def randomSite(request):
    entries = util.list_entries()
    allEntries = len(entries) - 1
    x = random.randint(0, allEntries)

    return render(request, "encyclopedia/titleSearch.html", {
        "entry": util.get_entry(entries[x]),
        "title": entries[x]
    })
