from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.http import JsonResponse
from .models import CalendarEvent
from django.utils.timezone import now

@csrf_exempt
def register(request):
    register_form = None  # Initialize register_form to avoid UnboundLocalError
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, "Passwords do not match")
        else:
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Registration successful!")
                return redirect('login')  # Redirect to login page
            else:
                messages.error(request, "Password should contain special symbols(/;,&$)")
                for field, errors in register_form.errors.items():
                    for error in errors:
                        print(f"Error in {field}: {error}")  # Print form errors to the console for debugging
    else:
        register_form = RegisterForm()
    return render(request, 'register.html', {'register_form': register_form})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(username=User.objects.get(email=email).username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('calendar')  # Redirect to home page upon successful login
            else:
                messages.error(request, "Invalid credentials")
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})

def calendar(request):
    events = CalendarEvent.objects.filter(user=request.user)  # Filter events for the logged-in user
    return render(request, 'calendar.html', {'events': events})
def tables(request):
    return render(request,'tables.html')
def tables2(request):
    return render(request,'tables2.html')
def tables4(request):
    return render(request,'tables4.html')
def tables3(request):
    return render(request,'tables3.html')
# Define festival detail views
def christmas(request):
    return render(request, 'festivals/christmas.html')
def newyear(request):
    return render(request, 'festivals/jan/newyear.html')
def guru(request):
    return render(request,'festivals/jan/guru.html')
def bhogi(request):
    return render(request,'festivals/jan/bhogi.html')
def sankranti(request):
    return render(request,'festivals/jan/sankranti.html')
def kanuma(request):
    return render(request,'festivals/jan/kanuma.html')
def swami(request):
    return render(request,'festivals/jan/swami.html')
def bosee(request):
    return render(request,'festivals/jan/bosee.html')
def republic(request):
    return render(request,'festivals/jan/republic.html')
def valentine(request):
    return render(request,'festivals/feb/valentine.html')
def shivaji(request):
    return render(request,'festivals/feb/shivaji.html')
def shiva(request):
    return render(request,'festivals/feb/shiva.html')
def holi(request):
    return render(request,'festivals/march/holi.html')
def ugadi(request):
    return render(request,'festivals/march/ugadi.html')
def ramzan(request):
    return render(request,'festivals/march/ramzan.html')
def ram(request):
    return render(request,'festivals/april/ram.html')
def mahavir(request):
    return render(request,'festivals/april/mahavir.html')
def ambedkar(request):
    return render(request,'festivals/april/ambedkar.html')
def gfriday(request):
    return render(request,'festivals/april/gfriday.html')
def easter(request):
    return render(request,'festivals/april/easter.html')
def tagore(request):
    return render(request,'festivals/may/tagore.html')
def mother(request):
    return render(request,'festivals/may/mother.html')
def buddha(request):
    return render(request,'festivals/may/buddha.html')
def bakrid(request):
    return render(request,'festivals/june/bakrid.html')
def kabir(request):
    return render(request,'festivals/june/kabir.html')
def father(request):
    return render(request,'festivals/june/father.html')
def muharam(request):
    return render(request,'festivals/muharam.html')
def friend(request):
    return render(request,'festivals/august/friend.html')
def raksha(request):
    return render(request,'festivals/august/raksha.html')
def independance(request):
    return render(request,'festivals/august/independance.html')
def krishna(request):
    return render(request,'festivals/august/krishna.html')
def ganesh(request):
    return render(request,'festivals/august/ganesh.html')
def onam(request):
    return render(request,'festivals/sept/onam.html')
def teacher(request):
    return render(request,'festivals/sept/teacher.html')
def durga(request):
    return render(request,'festivals/sept/durga.html')
def vijaya(request):
    return render(request,'festivals/oct/vijaya.html')
def gandhi(request):
    return render(request,'festivals/oct/gandhi.html')
def diwali(request):
    return render(request,'festivals/oct/diwali.html')
def children(request):
    return render(request,'festivals/nov/children.html')
@login_required
def add_event(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title', '').strip()
            date = request.POST.get('date')
            description = request.POST.get('description', '').strip()
            event_type = request.POST.get('type', 'other').strip()
            
            if not all([title, date]):
                messages.error(request, 'Title and date are required')
                return redirect('calendar')

            event = CalendarEvent(
                title=title,
                date=date,
                event_type=event_type,
                description=description,
                user_email=request.user.email,
                user=request.user
            )
            event.save()

            try:
            from django.core.mail import send_mail
                    f'New Calendar Event: {title}',
                    f'''Event Details:
                    
Title: {title}
Date: {date}
Type: {event.get_event_type_display()}
Description: {description or "No description provided"}''',
                    settings.DEFAULT_FROM_EMAIL,
                    [request.user.email],
                    fail_silently=False,
                )
                messages.success(request, 'Event added successfully!')
            except Exception as e:
                messages.warning(request, f'Event saved but email failed: {str(e)}')

            return redirect('calendar')

        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('calendar')

    return redirect('calendar')

@login_required
def get_events(request):
    events = CalendarEvent.objects.filter(user=request.user).values(
        'id', 'title', 'date', 'event_type', 'description'
    )
    return JsonResponse(list(events), safe=False)


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CalendarEventForm  # You'll need to create this form

@login_required
def update_event(request, event_id):
    # Get the event or return 404 if not found or doesn't belong to user
    event = get_object_or_404(CalendarEvent, id=event_id, user=request.user)
    
    if request.method == 'POST':
        # Create form instance with POST data and the existing event
        form = CalendarEventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('calendar')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        # For GET requests, show the form with current event data
        form = CalendarEventForm(instance=event)
    
    return render(request, 'update_event.html', {
        'form': form,
        'event': event
    })

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(CalendarEvent, id=event_id, user=request.user)
    if request.method == "POST":
        event.delete()
        return redirect('calendar')
    return render(request, 'delete_confirmation.html', {'event': event})

@login_required
def event_details(request, event_id):
    event = get_object_or_404(CalendarEvent, id=event_id, user=request.user)
    return render(request, 'event_details.html', {'event': event})

@login_required
def categorized_events(request):
    date_param = request.GET.get('date')
    comparison_date = date_param if date_param else now().date()
    
    events = CalendarEvent.objects.filter(user=request.user)
    context = {
        'upcoming_events': events.filter(date__gt=comparison_date),
        'running_events': events.filter(date=comparison_date),
        'completed_events': events.filter(date__lt=comparison_date),
        'selected_date': comparison_date,
    }
    return render(request, 'categorized_events.html', context)
