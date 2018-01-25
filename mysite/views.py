from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.views import View
# from django.core.files.storage import FilesSystemStorage
from .forms import PicAddingForm, CommentForm, Filters
from mysite import models
from PIL import Image
from mysite.customfilters import blue_line


def make_obj(picture):
    comments = []
    comment_set = picture.comment_set.all()
    for c in comment_set:
        comments.append(c.comment)
    return {
        'url': picture.photo.url.replace('mysite/static', ''),
        'description': picture.description,
        'id': picture.id,
        'comments': comments
    }


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


class PicView(View):
    def get(self, request):
        picture_objects = models.Picture.objects.all()
        pictures = []
        for picture in picture_objects:
            pictures.append(make_obj(picture))

        return render(request, 'mysite/feed.html',
                      {'pictures': pictures,
                       'post_comment': CommentForm()})


class DeletePic(View):
    def post(self, request, image_id):
        models.Picture.objects.get(id=image_id).delete()
        return redirect('mysite:feed')


class InsertComment(View):
    def post(self, request, image_id):
        pic = models.Picture.objects.get(id=image_id)
        form = CommentForm(pic, request.POST)
        if form.is_valid():
            form.saveComment()
            return redirect('mysite:feed')
        else:
            return redirect('mysite:feed')


class AddFilter(View):
    def get(self, request, image_id):
        form = Filters()
        path = 'mysite/static/' + models.Picture.objects.get(
            id=image_id).img_url()
        return render(request, 'mysite/feed.html', {'form': form})

    def post(self, request, image_id):
        form = Filters(request.POST)
        path = 'mysite/static/' + models.Picture.objects.get(
            id=image_id).img_url()
        image = Image.open(path)
        if form.is_valid():
            f = form.apply_filter()
            image.convert('RGB').filter(f).save(path)
            return redirect('mysite:feed')
        return render(request, 'mysite/filter.html', {'form': form})


def blue_filter(request, image_id):
    path = models.Picture.objects.get(id=image_id).photo.path
    blue_line(path)
    models.Picture.objects.get(id=image_id).save()
    return redirect('mysite:feed')