from django.shortcuts import render, redirect
from .models import Goal, Objective
from. forms import GoalForm

# Create your views here.
def home(request, category=None):
    if category:
        goals = Goal.objects.filter(categories=category)
        goals_completed_total = goals.filter(completed=True).count()
    else:
        goals = Goal.objects.all()
        goals_completed_total = Goal.objects.filter(completed=True).count()

    categories_queryset = Goal.objects.values_list('categories', flat=True).distinct()
    category_list = list(categories_queryset)
    
    categories_colors = {
        'language': '--owl-pink',
        'otter': '--midnight-blue',
        'music': '--charcoal-gray',
        'hamburger': '--burgundy',
        'martini-glass-citrus': '--forest-green',
        'computer': '--plum',
        'heart-pulse': '--slate-blue',
        'location-dot': '--olive-green',
        'briefcase': '--deep-indigo',
        'palette': '--steel-gray',
        'list-ol': '--aubergine'
    }
   
    goal_total = len(goals)

    
    goals_by_category = {cat: Goal.objects.filter(categories=cat) for cat in category_list}
    
    context = {
        'category_list': category_list,
        'goals_by_category': goals_by_category if not category else {category: goals},
        'categories_colors': categories_colors,
        'goals_total': goal_total,
        'goals_completed_total': goals_completed_total 
    }
    
    return render(request, 'home/index.html', context)

def add_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GoalForm()

    return render(request, 'home/add_goal.html', {'form': form})
    
    
