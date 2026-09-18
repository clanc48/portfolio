from django.shortcuts import render

SERVICES = [
    ("Leaks & fixtures","Faucets, toilets, shutoffs, supply lines, and visible leaks."),
    ("Water heaters","No-hot-water diagnostics, replacement planning, and efficiency issues."),
    ("Drain & sewer","Slow drains, backups, recurring blockages, and next-step options."),
    ("Pressure problems","Low pressure, high pressure, regulators, and fixture flow issues."),
    ("Repiping","Targeted or whole-home replacement when aging piping is the root problem."),
    ("Emergency response","Priority triage for active leaks, loss of water, and urgent failures."),
]

def page(template_name, **context):
    def view(request):
        return render(request, template_name, context)
    return view

def services(request):
    return render(request, "services.html", {"services": SERVICES})

def request_service(request):
    submitted = request.method == "POST"
    return render(request, "request-service.html", {"submitted": submitted})
