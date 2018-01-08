from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views import View
# from django.core.files.storage import FilesSystemStorage
from .forms import PicAddingForm
from mysite import models
from PIL import Image


class AddPicture(View):
    def get(self, request):
        form = PicAddingForm(request.POST, request.FILES)
        return render(request, 'mysite/add.html', {'form': form})

    def post(self, request):
        form = PicAddingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mysite:feed')
        else:
            return render(request, 'mysite/add.html', {'form': form})
