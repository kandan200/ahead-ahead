from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseServerError

def handler400(request, exception):
    #dont forget to reference the templates in docProject directory
    #also add an html button that returns the client to the homepage
    return HttpResponseBadRequest("The request cant be processed due to syntax error")

def handler403(request, exception):
    return HttpResponseNotAllowed("You dont have the permission to make this request")

def handler404(request, exception):
    return HttpResponseNotFound("Page not found on server")

def handler500(request):
    return HttpResponseServerError("Server error")
