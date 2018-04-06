from django.shortcuts import render
from .models import Scorecard, Practitioner
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Scorecard
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from scorecarddb.forms import ReasonValForm
from django.db.models import Avg, Sum, IntegerField

# Create your views here.

@login_required
def index(request):
    """
    View function for home page of site.
    """
    cards = Scorecard.objects.all()
    
    num_reviews = Scorecard.objects.all().count()
    
    return render (
        request,
        'index.html',
        context={'num_reviews':num_reviews, 'cards':cards})

class NewScorecard(LoginRequiredMixin, CreateView):
    form_class = ReasonValForm
    template_name='scorecard_form.html'
    success_url = reverse_lazy('index')
   
class UpdateScorecard(LoginRequiredMixin, UpdateView):
    form_class = ReasonValForm
    template_name = 'scorecard_update_form.html'
    success_url = reverse_lazy('index')
    
    def get_queryset(self):
        return Scorecard.objects.all()
  
class DeleteScorecard(LoginRequiredMixin, DeleteView):
    model = Scorecard
    success_url = reverse_lazy('index')
    
# Company Stats View
@login_required
def CompStats(request):
    #Company wide average DE score
    avg_total_score = int(round(Scorecard.objects.all().aggregate(Avg('total_score'))['total_score__avg']))
    
    #Top 5 practitioners w/average scores
    topFive = Practitioner.objects.values('practitioner_first_name', 'practitioner_last_name').annotate(Average_Score=Avg('scorecard__total_score', output_field=IntegerField())).order_by('-Average_Score')[:5]
    
    #Bottom 5 practitioners w/average scores
    bottomFive = Practitioner.objects.values('practitioner_first_name', 'practitioner_last_name').annotate(Average_Score=Avg('scorecard__total_score', output_field=IntegerField())).order_by('Average_Score')[:5]
    
    #Average scores for each section of the DE process
    avg_intro_score = int(round(Scorecard.objects.all().aggregate(Avg('intro_score'))['intro_score__avg']))
    avg_ce_score = int(round(Scorecard.objects.all().aggregate(Avg('ce_score'))['ce_score__avg']))
    avg_fvt_score = int(round(Scorecard.objects.all().aggregate(Avg('fvt_score'))['fvt_score__avg']))
    avg_audio_score = int(round(Scorecard.objects.all().aggregate(Avg('audio_score'))['audio_score__avg']))
    avg_pr_score = int(round(Scorecard.objects.all().aggregate(Avg('pr_score'))['pr_score__avg']))
    avg_comm_score = int(round(Scorecard.objects.all().aggregate(Avg('comm_score'))['comm_score__avg']))
    avg_pro_score = int(round(Scorecard.objects.all().aggregate(Avg('pro_score'))['pro_score__avg']))
    avg_emo_score = int(round(Scorecard.objects.all().aggregate(Avg('emo_score'))['emo_score__avg']))
    
    #Scores their average close rate, percentage of practitioners that reach it
    
    #Geochart for DE scores
    
    return render (
        request,
        'comp_stats.html',
        context={'avg_total_score':avg_total_score, 'topFive':topFive, 'bottomFive':bottomFive, 'avg_intro_score':avg_intro_score, 'avg_ce_score':avg_ce_score, 'avg_fvt_score':avg_fvt_score, 'avg_audio_score':avg_audio_score, 'avg_pr_score':avg_pr_score, 'avg_comm_score':avg_comm_score, 'avg_pro_score':avg_pro_score, 'avg_emo_score':avg_emo_score})

# Practitioners List View
@login_required
def PractitionerList(request):
    # List of Trainees
    trainees = Practitioner.objects.all().filter(employment_status='Trainee')
    
    # List of Current Employees
    currents = Practitioner.objects.all().filter(employment_status='Current')
    
    # List of Terminated Employees
    terminates = Practitioner.objects.all().filter(employment_status='Terminated')

    return render (
        request,
        'practitioner_list.html',
        context={'trainees':trainees, 'currents':currents, 'terminates':terminates})

# Practitioner Stats View
@login_required
def PractitionerStats(request, pk):
    # Practitioner Name
    name = Practitioner.objects.get(pk=pk)
    
    # Average DE Score
    avg_total_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('total_score'))['total_score__avg']))
    
    # Average Scores Per Section
    avg_intro_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('intro_score'))['intro_score__avg']))
    avg_ce_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('ce_score'))['ce_score__avg']))
    avg_fvt_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('fvt_score'))['fvt_score__avg']))
    avg_audio_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('audio_score'))['audio_score__avg']))
    avg_pr_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('pr_score'))['pr_score__avg']))
    avg_comm_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('comm_score'))['comm_score__avg']))
    avg_pro_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('pro_score'))['pro_score__avg']))
    avg_emo_score = int(round(Scorecard.objects.filter(practitioner=pk).aggregate(Avg('emo_score'))['emo_score__avg']))
    
    # List of each DE w/Score and Date
    cards = Scorecard.objects.filter(practitioner=pk).order_by('date')

    return render (
        request,
        'practitioner_stats.html',
        context={'name':name, 'avg_total_score':avg_total_score, 'avg_intro_score':avg_intro_score, 'avg_ce_score':avg_ce_score, 'avg_fvt_score':avg_fvt_score, 'avg_audio_score':avg_audio_score, 'avg_pr_score':avg_pr_score, 'avg_comm_score':avg_comm_score, 'avg_pro_score':avg_pro_score, 'avg_emo_score':avg_emo_score, 'cards':cards})
    
# Marketing Stats View