from django.shortcuts import render
from django.views import generic
from .models import File
from .forms import SignUpForm, UploadFileForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import get_object_or_404
from PyPDF2 import PdfFileReader

class FileDetailView(generic.DetailView):
    model=File

class FileListView(generic.ListView):
    model=File

from django.contrib.auth.decorators import login_required

@login_required
def fileList(request):
    file_list = File.objects.all()
    count = rate(request)
    return render(request, 'print/file_list.html', {'file_list': file_list,'count':count})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('file_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class FileCreate(CreateView):
    model = File
    fields = ['name','mainFile','user']
    success_url = reverse_lazy('file_list')

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             u = form.cleaned_data.get('username')
#             t = form.cleaned_data.get('title')
#             q = File(FileOwner= u, name= t, mainFile=request.FILES['file'])
#             q.save()
#             return HttpResponseRedirect('/happy/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

from django.http import JsonResponse

def markPrinted(request, pk):
    f = get_object_or_404(File, pk=pk)
    f.isPrinted = True
    var = PdfFileReader(open('./'+ f.mainFile.url,'rb'))
    f.noOfPages = var.getNumPages()
    f.save()
    return JsonResponse({'status':'success'})

def forgot(request):
    return HttpResponse("<h1>please contact us</h1>")

def profile(request):
    u = request.user
    return render(request, 'profile.html', {'user': u})


def rate(request):
    count=0

   # count=sum([file.noOfPages for file in request.user.files.all() if file.isPrinted])

    for file in request.user.files.all():
        if file.isPrinted:
            count=count+file.noOfPages
            print(file.noOfPages)
            
    return count