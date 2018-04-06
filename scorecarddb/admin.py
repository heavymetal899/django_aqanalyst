from django.contrib import admin

# Register your models here.

from .models import Practitioner, Location, ReasonNoSale, ReferralSource, Scorecard

admin.site.register(Practitioner)
admin.site.register(Location)
admin.site.register(ReasonNoSale)
admin.site.register(ReferralSource)
#admin.site.register(Scorecard)

@admin.register(Scorecard)
class scorecardAdmin(admin.ModelAdmin):
    list_display = ('id', 'practitioner', 'location', 'date', 'time')
    fields = [('practitioner', 'location'), ('date', 'time'), ('patient_name', 'third_party'), 
    ('sale_made', 'reason'), ('referral', 'total_score'), 'reviewer', 'summary', 
    ('open_state_score', 'open_state_comment'),
    ('pain_points_score', 'pain_points_comment'),
    ('verb_COSI_score', 'verb_COSI_comment'),
    ('sum_val_score', 'sum_val_comment'),
    ('commitment_score', 'commitment_comment'),
    ('last_test_score', 'last_test_comment'),
    ('causes_score', 'causes_comment'),
    ('anatomy_score', 'anatomy_comment'),
    ('clinical_study_score', 'clinical_study_comment'),
    ('progressive_score', 'progressive_comment'),
    ('maintain_score', 'maintain_comment'),
    ('story_score', 'story_comment'),
    ('otoscope_score', 'otoscope_comment'),
    ('FVT_exp_score', 'FVT_exp_comment'),
    ('FVT_results_score', 'FVT_results_comment'),
    ('FVT_third_score', 'FVT_third_comment'),
    ('explain_audio_score', 'explain_audio_comment'),
    ('normal_hearing_score', 'normal_hearing_comment'),
    ('ask_chart_score', 'ask_chart_comment'),
    ('recommit_score', 'recommit_comment'),
    ('bad_good_score', 'bad_good_comment'),
    ('notions_score', 'notions_comment'),
    ('objections_score', 'objections_comment'),
    ('pick_two_score', 'pick_two_comment'),
    ('style_cost_score', 'style_cost_comment'),
    ('style_fitting_score', 'style_fitting_comment'),
    ('backup_score', 'backup_comment'),
    ('tech_fitting_score', 'tech_fitting_comment'),
    ('tech_levels_score', 'tech_levels_comment'),
    ('appropriate_score', 'appropriate_comment'),
    ('sep_rec_score', 'sep_rec_comment'),
    ('fight_score', 'fight_comment'),
    ('questions_score', 'questions_comment'),
    ('restate_score', 'restate_comment'),
    ('validation_score', 'validation_comment'),
    ('body_score', 'body_comment'),
    ('tone_score', 'tone_comment'),
    ('words_score', 'words_comment'),
    ('transitions_score', 'transitions_comment'),
    ('involvement_score', 'involvement_comment'),
    ('authority_score', 'authority_comment'),
    ('rapport_score', 'rapport_comment'),
    ('cred_score', 'cred_comment'),
    ('COSI_score', 'COSI_comment'),
    ('impact_score', 'impact_comment'),
    ('urgency_score', 'urgency_comment'),
    ('third_party_score', 'third_party_comment')]