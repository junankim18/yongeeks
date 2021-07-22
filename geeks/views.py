from django.shortcuts import render


def main(request):
    ctx = {}
    return render(request, 'start.html', ctx)
