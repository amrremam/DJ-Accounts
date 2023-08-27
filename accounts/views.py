from django.shortcuts import render, redirect
from .forms import signupForm, userform, profileForm
from django.contrib.auth import authenticate, login
from .models import profile



def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password=  form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/accounts/profile')
            
    else:
        form = signupForm()
    return render(request, 'registration/signup.html',{})



def profile(request):
    profile = profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile':profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = userform(request.POST, instance=request.user)
        profileForm = profileForm(request.POST, instance=profile)
        if userform.is_valid() and profileForm.is_valid():
            userform.save()
            myform = profileForm.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')

    else:
        userform = userform(indstance=request.user)
        profileForm = profileForm(instance=request.profile)


    return render(request, 'profile/profile_edit.html', {
        'userform' : userform,
        'profileform' : profileForm,
    })