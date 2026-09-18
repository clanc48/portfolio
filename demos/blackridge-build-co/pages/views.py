from django.shortcuts import render

def render_page(template_name):
    def view(request):
        return render(request, template_name)
    return view
