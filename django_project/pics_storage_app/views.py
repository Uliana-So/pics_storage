from django.shortcuts import render
from django.views.generic import View

from .form import UploadImageForm
from .models import Album


class IndexView(View):
    template_name = 'index.html'

    def get(self, req):
        data = Album.objects.all().order_by('-id')
        context = {'form': UploadImageForm(), 'img_obj': data}
        return render(req, self.template_name, context=context)

    def post(self, req):
        form = UploadImageForm(req.POST, req.FILES)
        if form.is_valid():
            model = Album(title=form.cleaned_data['title'],
                          image=req.FILES['image'])
            model.save()

        data = Album.objects.all().order_by('-id')
        context = {'form': UploadImageForm(), 'img_obj': data}
        return render(req, self.template_name, context=context)
