from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render_to_response
from django.shortcuts import *
from django.template import RequestContext
from django.template.defaultfilters import slugify
from forms import *
from models import *
from boto.s3.key import Key
from boto import connect_s3
import mimetypes

def upload(request):
    if request.method == "POST":
        form = ComicForm(request.POST, request.FILES)

        message = "Did not upload successfully"

        if form.is_valid():
            file = request.FILES['image']
            filename = datetime.now().strftime("%Y%m%d%H%M%S%f") + file.name

            conn = connect_s3()
            bucket = conn.create_bucket('developerrage')
            
            k = Key(bucket)
            k.key = filename
            k.content_type = mimetypes.guess_type(filename)[0]
            k.set_contents_from_string(file.read())
            k.set_acl('public-read')

            comic = Comic()
            comic.title = request.POST['title']
            comic.slug = slugify(request.POST['title'])
            comic.image = filename
            comic.approved = 0
            comic.votes = False
            comic.save()

            message = 'Thank you for your submission we will review it shortly'

            return render_to_response('comic/upload.html',
                { 'form': form , 'message': message},
                context_instance=RequestContext(request))
        return render_to_response('comic/upload.html',
                { 'form': form , 'message': message},
                context_instance=RequestContext(request))
    else:
        form = ComicForm()
        return render_to_response('comic/upload.html',
                { 'form': form },
                context_instance=RequestContext(request))

