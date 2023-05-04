from django.shortcuts import render


def page_not_found_view(request, exception=None):
    return render(request, 'bases/404.html')
