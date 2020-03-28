from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, editProfileForm, changePasswordForm
import datetime

def home(request):
	return render (request, 'index.html', {})

def resume(request):
	return render (request, 'resume.html', {})

def countdown(request):
	now = datetime.date.today()
	scStart = datetime.date(2020, 8, 20)
	diff = scStart - now
	diffDay = diff.days
	return render (request, 'countdown.html', {'diff':diff, 'diffDay':diffDay} )

def add(request):
	from random import randint
	numOne = randint(0, 20)
	numTwo = randint(0, 20)
	if request.method == "POST":
		answer = request.POST['answer']
		oldNumOne = request.POST['oldNumOne']
		oldNumTwo = request.POST['oldNumTwo']
		correctAnswer = int(oldNumOne) + int(oldNumTwo)
		if int(answer) == correctAnswer:
			myAnswer = "Correct! " + oldNumOne + " + " + oldNumTwo + " = " + answer
			color = "success"
		else:
			myAnswer = "Incorrect! " + oldNumOne + " + " + oldNumTwo + " = " + str(correctAnswer) + ", it is not " + answer
			color = "danger"
		return render(request, 'add.html', {'answer':answer, 'numOne':numOne, 'numTwo':numTwo, 'myAnswer':myAnswer, 'color':color})
	return render (request, 'add.html', {'numOne':numOne, 'numTwo':numTwo})

def subtract(request):
	from random import randint
	numOne = randint(0, 20)
	numTwo = randint(0, 20)
	while (numOne - numTwo) < 0:
		numOne = randint(0, 10)
		numTwo = randint(0, 10)
	if request.method == "POST":
		answer = request.POST['answer']
		oldNumOne = request.POST['oldNumOne']
		oldNumTwo = request.POST['oldNumTwo']
		correctAnswer = int(oldNumOne) - int(oldNumTwo)
		if int(answer) == correctAnswer:
			myAnswer = "Correct! " + oldNumOne + " - " + oldNumTwo + " = " + answer
			color = "success"
		else:
			myAnswer = "Incorrect! " + oldNumOne + " - " + oldNumTwo + " = " + str(correctAnswer) + ", it is not " + answer
			color = "danger"
		return render(request, 'subtract.html', {'answer':answer, 'numOne':numOne, 'numTwo':numTwo, 'myAnswer':myAnswer, 'color':color})
	return render (request, 'subtract.html', {'numOne':numOne, 'numTwo':numTwo})

def multiplication(request):
	from random import randint
	numOne = randint(0, 20)
	numTwo = randint(0, 20)
	if request.method == "POST":
		answer = request.POST['answer']
		oldNumOne = request.POST['oldNumOne']
		oldNumTwo = request.POST['oldNumTwo']
		correctAnswer = int(oldNumOne) * int(oldNumTwo)
		if int(answer) == correctAnswer:
			myAnswer = "Correct! " + oldNumOne + " X " + oldNumTwo + " = " + answer
			color = "success"
		else:
			myAnswer = "Incorrect! " + oldNumOne + " X " + oldNumTwo + " = " + str(correctAnswer) + ", it is not " + answer
			color = "danger"
		return render(request, 'multiplication.html', {'answer':answer, 'numOne':numOne, 'numTwo':numTwo, 'myAnswer':myAnswer, 'color':color})
	return render (request, 'multiplication.html', {'numOne':numOne, 'numTwo':numTwo})

def division(request):
	from random import randint
	numOne = randint(0, 20)
	numTwo = randint(1, 20)
	while (numOne%numTwo) != 0:
		numOne = randint(0, 10)
		numTwo = randint(1, 10)
	if request.method == "POST":
		answer = request.POST['answer']
		oldNumOne = request.POST['oldNumOne']
		oldNumTwo = request.POST['oldNumTwo']
		correctAnswer = int(oldNumOne) / int(oldNumTwo)
		corrAnswer = int(correctAnswer)
		if int(answer) == correctAnswer:
			myAnswer = "Correct! " + oldNumOne + " / " + oldNumTwo + " = " + answer
			color = "success"
		else:
			myAnswer = "Incorrect! " + oldNumOne + " / " + oldNumTwo + " = " + str(corrAnswer) + ", it is not " + answer
			color = "danger"
		return render(request, 'division.html', {'answer':answer, 'numOne':numOne, 'numTwo':numTwo, 'myAnswer':myAnswer, 'color':color})
	return render (request, 'division.html', {'numOne':numOne, 'numTwo':numTwo})

def loginUser(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You have been logged in successfully!'))
			color = "success"
			return redirect('home')
		else:
			messages.success(request, ('Error logging in, check username and password!'))
			color="danger"
			return redirect('login')
	else:
		return render(request, 'login.html', {})

def logoutUser(request):
	logout(request)
	messages.success(request, ('You have been logged out successfully!'))
	color = "success"
	return redirect('home')

def registerUser(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ('You have been registered successfully!'))
			color = "success"
			return redirect('home')
	else:
		form = SignUpForm()
	context = {'form':form}
	return render(request, 'register.html', context)

def editProfile(request):
	if request.method == "POST":
		form = editProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile successfully!'))
			color = "success"
			return redirect('home')
	else:
		form = editProfileForm(instance=request.user)
	context = {'form':form}
	return render(request, 'editProfile.html', context)

def changePassword(request):
	if request.method == "POST":
		form = changePasswordForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have changed your password successfully!'))
			color = "success"
			return redirect('home')
	else:
		form = changePasswordForm(user=request.user)
	context = {'form':form}
	return render(request, 'changePassword.html', context)