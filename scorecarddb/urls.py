from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newscorecard/$', views.NewScorecard.as_view(), name='scorecard_form'),
    url(r'^updatescorecard/(?P<pk>\d+)$', views.UpdateScorecard.as_view(), name='scorecard_update_form'),
    url(r'^deletescorecard/(?P<pk>\d+)$', views.DeleteScorecard.as_view(), name='scorecard_confirm_delete'),
    url(r'^companystats/$', views.CompStats, name='comp_stats'),
    url(r'^practitioners/$', views.PractitionerList, name='practitioner_list'),
    url(r'^practitioner/(?P<pk>\d+)$', views.PractitionerStats, name='practitioner_stats'),
]