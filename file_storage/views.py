import string
from os import path as os_path

from django.http import HttpResponse

from sendfile import sendfile

valid_chars = "-_.()%s%s" % (string.ascii_letters, string.digits)


def sanatize_file_name(name):
    """
    docstring for sanatize_file_name
    """
    return ''.join(c for c in name if c in valid_chars)


def index(request, path):
    """
    docstring for index
    """
    if request.method == "POST":
        for file_name, file in request.FILES.iteritems():
            file_name = sanatize_file_name(file.name)
            file_path = os_path.join('uploads', path, file_name)
            f = open(file_path, "w")
            f.write(file.file.read())
            f.close()
        return HttpResponse("Uploaded")
    return sendfile(request, os_path.join('uploads', path))
