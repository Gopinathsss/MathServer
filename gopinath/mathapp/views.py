from django.shortcuts import render
from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    category = None
    if request.method == 'POST':
        try:
            height = float(request.POST.get('height')) / 100
            weight = float(request.POST.get('weight'))
            bmi = round(weight / (height ** 2), 2)
            print(f" Height: {height * 100} cm \n Weight: {weight} kg \n BMI: {bmi}")
        except (ValueError, ZeroDivisionError):
            print("Invalid input received.")
            bmi = "Invalid input"
            category = None
    return render(request, 'mathapp/math.html', {'bmi': bmi, 'category': category})


# Create your views here.
