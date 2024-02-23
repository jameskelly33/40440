from django.shortcuts import render, get_object_or_404, redirect
from home.models import Goal, Objective
from .forms import ObjectiveForm

def details(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id)
    objectives = Objective.objects.filter(goal=goal)
    objective_total = objectives.count()
    num_objective_completed= objectives.filter(completed=True).count()
    categories_colors = {
        'language':'--owl-pink',
        'otter':'--midnight-blue',
        'music':'--charcoal-gray' ,
        'hamburger':'--burgundy',
        'martini-glass-citrus':'--forest-green',
        'computer':'--plum',
        'heart-pulse':'--slate-blue',
        'location-dot':'--olive-green',
        'briefcase':'--deep-indigo',
        'palette':'--steel-gray',
        'list-ol':'--aubergine'
        
    }
    if objective_total > 0:
        completion_percentage= (num_objective_completed/objective_total)*100
        if num_objective_completed == objective_total:
            goal.completed = True
            goal.save()
        else:
            goal.completed= False
            goal.save()    
    else:
        completion_percentage =0 
        goal.completed = False
    

    if request.method == 'POST':
        # Adding a new objective
        if 'add_objective' in request.POST:
            form = ObjectiveForm(request.POST)
            if form.is_valid():
                objective = form.save(commit=False)
                objective.goal = goal
                objective.save()
        # Deleting an existing objective
        elif 'delete_objective' in request.POST:
            objective_id = request.POST.get('delete_objective')
            Objective.objects.filter(id=objective_id).delete()
            
        # Changing the completed status of objectives
        elif 'update_objectives' in request.POST:
            all_objective_ids = Objective.objects.values_list('id', flat=True).filter(goal=goal_id)
            completed_objective_ids = request.POST.getlist('completed')
    
    # Mark objectives as completed based on the form submission
            Objective.objects.filter(id__in=all_objective_ids).update(completed=False)
            Objective.objects.filter(id__in=completed_objective_ids).update(completed=True)
        print(goal.completed)    
        return redirect('details', goal_id=goal_id )
                

  

    form = ObjectiveForm()  # Create a new form for adding objectives
    

    context = {
        'goal': goal,
        'objectives': objectives,
        'form': form,
        'objective_total':objective_total,
        'num_objective_completed':num_objective_completed,
        'completion_percentage':completion_percentage,
        'categories_colors': categories_colors
        
        
    }

    return render(request, 'details/details.html', context)
