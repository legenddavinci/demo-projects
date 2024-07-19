from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    text = ''
    counter = 0
    if request.method == 'POST':
        text = request.POST['text']
        counter = len(text.split())
        return render(request, 'wordcounter.html', {'text':text, 'counter': counter} )

    else:
        return render(request, 'wordcounter.html')
