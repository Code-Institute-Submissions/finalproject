from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Packages
from django.contrib.auth.decorators import login_required
from .forms import PackageForm

# Create your views here.
def get_packages(request):
    packages = Packages.objects.all()
    return render(request, "packages.html", {'packages': packages})

@login_required
def package_details(request, id):
    this_package = get_object_or_404(Packages, pk=id)
    form = PackageForm
    subform = DynamicSub
    return render(request, "package_details.html", {'package' : this_package, 'form':form, 'subform':subform})
    