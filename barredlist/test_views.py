from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def test_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"LOGIN ATTEMPT: {username} / {password}")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(f"LOGIN SUCCESS: {user}")
            return redirect('/')
        else:
            print("LOGIN FAILED: Invalid credentials")
            return render(request, 'test_login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'test_login.html')