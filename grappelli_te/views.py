
import os

import json

from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, Http404
from django.shortcuts import render


is_staff = user_passes_test(lambda u: u.is_staff, login_url='admin:login')


@is_staff
def index(request):
    return render(request, 'grappelli_te/index.html')


@is_staff
def template_list(request):
    '''Return a list of templates'''
    path = settings.TEMPLATE_DIRS[0]

    data = []
    for root, dirs, files in os.walk(path):
        rel = root[len(path):]

        data.extend([
            {
                'kids': [],
                'path': os.path.join(rel, name),
            }
            for name in files
        ])

    return HttpResponse(
        json.dumps(data),
        content_type='text/json',
    )


@is_staff
def template_detail(request):
    root = settings.TEMPLATE_DIRS[0]

    if request.method == 'POST':
        try:
            path = request.POST['path']
        except KeyError:
            raise Http404

        full_path = os.path.abspath(os.path.join(root, path))

        if not full_path.startswith(root):
            raise Http404
        # Saving
        with open(full_path, 'w') as fout:
            fout.write(request.POST['data'])

        return HttpResponse(status=201)

    elif request.method == 'GET':
        try:
            path = request.GET['path']
        except KeyError:
            raise Http404

        full_path = os.path.abspath(os.path.join(root, path))

        if not full_path.startswith(root):
            raise Http404
        return HttpResponse(open(full_path, 'r'), content_type='text/plain')
