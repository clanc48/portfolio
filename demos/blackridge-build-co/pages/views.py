from django.shortcuts import render

PROJECTS = [
    {"name":"Ridge House","type":"Custom home","detail":"4,800 sq ft · mountain site","note":"Stone, blackened timber, and long western views."},
    {"name":"Pine Hollow","type":"Custom home","detail":"3,650 sq ft · wooded site","note":"Low-profile forms organized around an interior courtyard."},
    {"name":"Mill Creek Addition","type":"Renovation","detail":"1,900 sq ft addition","note":"A contemporary expansion tied carefully into an older masonry home."},
]

def page(template_name, **context):
    def view(request):
        return render(request, template_name, context)
    return view

def contact(request):
    submitted = request.method == "POST"
    return render(request, "contact.html", {"submitted": submitted})

def projects(request):
    return render(request, "projects.html", {"projects": PROJECTS})
