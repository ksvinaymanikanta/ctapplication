# from django.shortcuts import render, redirect
# from .form import CreditCardApplicationForm




# def credit_card_application(request):
#     if request.method == "POST":
#         form = CreditCardApplicationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success_page')  # Redirect to a success page
#     else:
#         form = CreditCardApplicationForm()
#     return render(request, 'creditcard/application_form.html', {'form': form})

# def home(request):
#     return render(request, 'home.html')  # ✅ Make sure this template exists

from django.shortcuts import render, redirect
from .form import CreditCardApplicationForm
from .models import CreditCardApplication

# def credit_card_application(request):
#     # if request.method == "POST":
#     #     form = CreditCardApplicationForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()  # Save data to the database
#     #         return redirect('success')  # Redirect to a success page
#     # else:
#     #     form = CreditCardApplicationForm()

#     return render(request, "credit_card_form.html", {"form": form})

def home(request):
    if request.method == "POST":
        form = CreditCardApplicationForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database
            return redirect('success')  # Redirect to a success page
    else:
        form = CreditCardApplicationForm()

    return render(request, "home.html", {"form": form})
# def home(request):
#      return render(request, 'home.html')
def success(request):
    return render(request, "success.html")
def forms(request):
    return render(request, "forms.html")
def tc(request):
    return render(request, "t&c.html")
def details(request):
    data= CreditCardApplication.objects.all()
    print('USER DETAILS',data)
    content={
        'data':data
    }
    return render(request, "user_details.html", context=content)
