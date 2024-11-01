import matplotlib
from django.shortcuts import render


# Create your views here.
def projecthomepage(request):
    return render(request, 'adminapp/ProjectHomePage.html')


def printpagecall(request):
    return render(request, 'adminapp/printer.html')


def printpagelogic(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        print(f'User Input: {user_input}')
    a1 = {'user_input': user_input}
    return render(request, 'adminapp/printer.html', a1)


def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')


def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')


import random
import string


def randompagecall(request):
    return render(request, 'adminapp/RandomExample.html')


def randomlogic(request):
    if request.method == "POST":
        number1 = int(request.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1 = {'ran': ran}
    return render(request, 'adminapp/RandomExample.html', a1)


def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')

    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html', {'form': form, 'tasks': tasks})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')


# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.contrib.auth import logout
# from django.urls import reverse
#
# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm-password']
#
#         if password == confirm_password:
#             # Create the user and redirect to the homepage
#             user = User.objects.create_user(username=username, email=email, password=password)
#             login(request, user)
#             messages.success(request, f'Account created for {username}!')
#             return redirect('projecthomepage')
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')
#     else:
#         return render(request, 'adminapp/register.html')
#
#
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         # Authenticate the user
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             # Log the user in and redirect to homepage
#             login(request, user)
#             return redirect('projecthomepage')
#         else:
#             # Invalid credentials, show an error message
#             error_message = "Invalid username or password"
#             return render(request, 'adminapp/login.html', {'error_message': error_message})
#     else:
#         return render(request, 'adminapp/login.html')
#
#
# def log_out_view(request):
#     # Use Django's built-in logout function
#     logout(request)
#
#     # Redirect to a specific page after logging out (e.g., login page or homepage)
#     return redirect(reverse('projecthomepage'))


from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render


def UserRegisterPageCall(request):
    return render(request, 'adminapp/register.html')


def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/register.html')
    else:
        return render(request, 'adminapp/register.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def UserLoginPageCall(request):
    return render(request, 'adminapp/login.html')


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # Check the length of the username
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/login.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/login.html')
    else:
        return render(request, 'adminapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')


from django.shortcuts import render
from datetime import datetime
import pytz


def datetime_view(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    selected_country = request.GET.get('country', 'UTC')
    country_time = datetime.now(pytz.timezone(selected_country)).strftime('%Y-%m-%d %H:%M:%S')
    countries = [
        'UTC', 'America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney',
        'Europe/Paris', 'Europe/Berlin', 'Asia/Shanghai', 'Asia/Kolkata', 'America/Los_Angeles',
        'America/Chicago', 'Europe/Moscow', 'Asia/Dubai', 'Asia/Singapore', 'Africa/Johannesburg',
        'America/Toronto', 'America/Sao_Paulo', 'Asia/Seoul', 'Asia/Hong_Kong', 'Pacific/Auckland'
    ]

    context = {
        'current_time': current_time,
        'country_time': country_time,
        'countries': countries,
        'selected_country': selected_country,
    }
    return render(request, 'adminapp/DateTimeExample.html', context)


from .forms import StudentForm
from .models import StudentList


# def add_student(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')
#     else:
#         form = StudentForm()
#     return render(request, 'adminapp/add_student.html', {'form': form})


def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/student_list.html', {'students': students})


#  ============== CSV TASK ===============

import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.shortcuts import render
matplotlib.use('Agg')


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        # Read the CSV file
        df = pd.read_csv(file, parse_dates=['Date'], dayfirst=True)

        # Calculate total and average sales
        total_sales = df['Sales'].sum()
        average_sales = df['Sales'].mean()

        # Add a 'Month' column and calculate monthly sales
        df['Month'] = df['Date'].dt.month
        monthly_sales = df.groupby('Month')['Sales'].sum()

        # Month names for labels
        month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x: month_names[x - 1])

        # Plot the pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(monthly_sales, labels=monthly_sales.index, autopct='%1.1f%%', startangle=90)
        plt.title('Sales Distribution Per Month')

        # Save the plot to a buffer
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Convert to base64 to send to the template
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        plt.close()

        # Pass data to the template
        context = {
            'total_sales': total_sales,
            'average_sales': average_sales,
            'monthly_sales': monthly_sales.to_dict(),
            'chart': image_data,
        }
        return render(request, 'adminapp/chart.html', context)

    return render(request, 'adminapp/chart.html')

def contact_manager(request):
    return render(request, 'adminapp/contact_manager.html')


# contact_manager/views.py
from django.shortcuts import render, redirect
from .models import Contact  # Ensure you have a Contact model defined


def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']

        # Create and save the new contact
        Contact.objects.create(name=name, email=email, phone=phone, address=address)

        return redirect('contact_manager')  # Adjust this to your needs

    return render(request, 'adminapp/add_contact.html')
