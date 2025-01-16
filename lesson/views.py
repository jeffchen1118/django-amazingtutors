from django.http import HttpResponse

# Create your views here.
# class my_lesson(TemplateView):
#     """
#     Displays the home page.
#     """

#     template_name = 'index.html'


def my_lesson(request):
    return HttpResponse("Hello, world. You're at the lesson index.")
