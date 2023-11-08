from django.shortcuts import render
import random
# Create your views here.
def Adivina(request):
    return render(request, 'AdivinaApp/adivina.html')

def resultado(request):
    random_number = random.randint(1, 100)
    usuario = int(request.POST['repite'])

    if usuario == random_number:
        message = "Congratulations! Ypu guessed the correct number."
    elif usuario > random_number:
        message="Your guess is too high. Try again!"
    else:
        message="Your guess is too low. Try again!"
    
    return render(request, 'AdivinaApp/repitenum.html', {'message':message})