from django.shortcuts import render

# Create your views here.

def home(request):
    if request.method == 'POST':
        image = request.FILES['image']
        output = predict(image)
        return render(request, 'home.html', {'output': output})
    return render(request, 'home.html')
