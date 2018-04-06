from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Practitioner(models.Model):
    """
    This is a model for the practitioners
    """
	
	# Fields
    STATUS = (
        ('Trainee', 'Trainee'),
        ('Current', 'Current'),
        ('Terminated', 'Terminated'),
    )
    
    practitioner_first_name = models.CharField(max_length=30)
    practitioner_last_name = models.CharField(max_length=30)
    employment_status = models.CharField(max_length=10, choices=STATUS, null=True)
	
    # Metadata
    class Meta:
        ordering = ["practitioner_last_name", "practitioner_first_name"]
	
	# Methods
    def __str__(self):
        """
        Returns string of the full name
        """
        return '%s, %s' % (self.practitioner_last_name, self.practitioner_first_name)
    
    def get_absolute_url(self):
        """
        Returns the url for a single practitioner
        """
        return reverse('practitioner_stats', args=[str(self.id)])
		
# Model for locations
class Location(models.Model):
    """
    This is a model for the locations
    """
    
    # Fields
    STATES = (
        ('AK', 'AK'),
        ('AL', 'AL'),
        ('AR', 'AR'),
        ('AZ', 'AZ'),
        ('CA', 'CA'),
        ('CO', 'CO'),
        ('CT', 'CT'),
        ('DC', 'DC'),
        ('DE', 'DE'),
        ('FL', 'FL'),
        ('GA', 'GA'),
        ('HI', 'HI'),
        ('IA', 'IA'),
        ('ID', 'ID'),
        ('IL', 'IL'),
        ('IN', 'IN'),
        ('KS', 'KS'),
        ('KY', 'KY'),
        ('LA', 'LA'),
        ('MA', 'MA'),
        ('MD', 'MD'),
        ('ME', 'ME'),
        ('MI', 'MI'),
        ('MN', 'MN'),
        ('MO', 'MO'),
        ('MS', 'MS'),
        ('MT', 'MT'),
        ('NC', 'NC'),
        ('ND', 'ND'),
        ('NE', 'NE'),
        ('NH', 'NH'),
        ('NJ', 'NJ'),
        ('NM', 'NM'),
        ('NV', 'NV'),
        ('NY', 'NY'),
        ('OH', 'OH'),
        ('OK', 'OK'),
        ('OR', 'OR'),
        ('PA', 'PA'),
        ('RI', 'RI'),
        ('SC', 'SC'),
        ('SD', 'SD'),
        ('TN', 'TN'),
        ('TX', 'TX'),
        ('UT', 'UT'),
        ('VA', 'VA'),
        ('VT', 'VT'),
        ('WA', 'WA'),
        ('WI', 'WI'),
        ('WV', 'WV'),
        ('WY', 'WY'),
    )
    
    location_city = models.CharField(max_length=30)
    location_state = models.CharField(max_length=2, choices=STATES)
    
    # Metadata
    class Meta:
        ordering = ["location_state", "location_city"]
        
    # Methods
    def __str__(self):
        """
        Returns string of the full location
        """
        return '%s, %s' % (self.location_city, self.location_state)

# Model for reasons
class ReasonNoSale(models.Model):
    """
    This is a model for the reasons a sale fell through
    """
    
    # Fields
    reason_name = models.CharField(max_length=40)
    
    # Metadata
    
    # Methods
    def __str__(self):
        """
        Returns string of the reason
        """
        return self.reason_name
    
# Model for referrals
class ReferralSource(models.Model):
    """
    This is a model for the referral sources
    """
    
    # Fields
    referral_source = models.CharField(max_length=30)
    
    # Metadata
    
    # Methods
    def __str__(self):
        """
        Returns string of the referral source
        """
        return self.referral_source
    
# Model for scorecards
class Scorecard(models.Model):
    """
    This is a model for the scorecards
    """
    
    # Fields
    YESNO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    SCORES = (
        (0, 0),
        (1, 1),
		(2, 2),
		(3, 3),
    )
    
    SCORES2 = (
        (0, 0),
        (2, 2),
    )

    practitioner = models.ForeignKey('Practitioner', on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    patient_name = models.CharField(max_length=30, null=True)
    third_party = models.CharField(max_length=3, choices=YESNO, default='Yes')
    sale_made = models.CharField(max_length=3, choices=YESNO, default='Yes')
    reason = models.ForeignKey('ReasonNoSale', on_delete=models.PROTECT, null=True, blank=True)
    referral = models.ForeignKey('ReferralSource', verbose_name='Referral source', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(blank=True)
    reviewer = models.CharField(max_length=30, null=True)
    total_score = models.PositiveSmallIntegerField(default=0)
    intro_score = models.PositiveSmallIntegerField(default=0)
    ce_score = models.PositiveSmallIntegerField(default=0)
    fvt_score = models.PositiveSmallIntegerField(default=0)
    audio_score = models.PositiveSmallIntegerField(default=0)
    pr_score = models.PositiveSmallIntegerField(default=0)
    comm_score = models.PositiveSmallIntegerField(default=0)
    pro_score = models.PositiveSmallIntegerField(default=0)
    emo_score = models.PositiveSmallIntegerField(default=0)
    
    open_state_score = models.PositiveSmallIntegerField("Opening Statement", choices=SCORES, default=0,
    help_text="3) Direct Questions, Anatomy, Test, Recommendation, Seeks Acknowledgement")
    open_state_comment = models.TextField(blank=True)
    pain_points_score = models.PositiveSmallIntegerField("Discovery of Pain Points", choices=SCORES, default=0,
    help_text="1) Asks 2) Identifies multiple lifestyle pain points 3) Discovers related emotional markers")
    pain_points_comment = models.TextField(blank=True)
    verb_COSI_score = models.PositiveSmallIntegerField("Verbalizes Pain Points as COSI Goals", choices=SCORES2, default=0,
    help_text="Explicitly explains that the pain points will be used as verifiable goals")
    verb_COSI_comment = models.TextField(blank=True)
    sum_val_score = models.PositiveSmallIntegerField("Gives a Summary Validation of COSI Goals", choices=SCORES2, default=0)
    sum_val_comment = models.TextField(blank=True)
    commitment_score = models.PositiveSmallIntegerField("Commitment", choices=SCORES, default=0,
    help_text="1) Asks a commitment question 2) Addresses objections 3) Recommits")
    commitment_comment = models.TextField(blank=True)
    last_test_score = models.PositiveSmallIntegerField("Last Hearing Test", choices=SCORES, default=0,
    help_text="1) Finds out date 2) What were the results? 3) Recommends an annual exam")
    last_test_comment = models.TextField(blank=True)
    causes_score = models.PositiveSmallIntegerField("Discuss Possible Causes for Loss", choices=SCORES, default=0,
    help_text="3) Age, Noise Exposure, Medical History, Genetics")
    causes_comment = models.TextField(blank=True)
    anatomy_score = models.PositiveSmallIntegerField("Anatomy of the Ear", choices=SCORES, default=0,
    help_text="1) Verbal description 2) Uses diagram 3) Specific reference to otoscope AND audiogram")
    anatomy_comment = models.TextField(blank=True)
    clinical_study_score = models.PositiveSmallIntegerField("Referenced a Clinical Study", choices=SCORES2, default=0,
    help_text="Names an institutional study")
    clinical_study_comment = models.TextField(blank=True)
    progressive_score = models.PositiveSmallIntegerField("Described hearing loss as Progressive, Permanent, and Irreversible", 
    choices=SCORES, default=0, 
    help_text="3) States/defines all three words and creates urgency by explaining how each relates to HL")
    progressive_comment = models.TextField(blank=True)
    maintain_score = models.PositiveSmallIntegerField("Discussed need to maintain what is left", choices=SCORES, default=0,
    help_text="3) Explains speech understanding and how HA maintain it, uses an analogy")
    maintain_comment = models.TextField(blank=True)
    story_score = models.PositiveSmallIntegerField("Personal story", choices=SCORES, default=0,
    help_text="3) Practitioner relates an emotionally impactful personal story that describes the effects of untreated HL")
    story_comment = models.TextField(blank=True)
    otoscope_score = models.PositiveSmallIntegerField("Otoscope", choices=SCORES, default=0,
    help_text="1) Uses otoscope 3) Sets proper expectations prior and gives thorough explanation after")
    otoscope_comment = models.TextField(blank=True)
    FVT_exp_score = models.PositiveSmallIntegerField("Expectations", choices=SCORES, default=0,
    help_text="3) Expect 100% correct, missing 1-2 is a red flag, any more will be a cause for concern")
    FVT_exp_comment = models.TextField(blank=True)
    FVT_results_score = models.PositiveSmallIntegerField("Results", choices=SCORES, default=0,
    help_text="3) Refers back to expectations, reviews response examples, realization of PT loss is impactful")
    FVT_results_comment = models.TextField(blank=True)
    FVT_third_score = models.PositiveSmallIntegerField("Discussed results with the third party", choices=SCORES, default=0,
    help_text="1) Asks a single direct question, 2) Asks multiple follow-up questions 3) draws out emotion, gets perspective")
    FVT_third_comment = models.TextField(blank=True)
    explain_audio_score = models.PositiveSmallIntegerField("Explained audiogram", choices=SCORES, default=0,
    help_text="1) Explains volume and frequency axis, 3) explains speech recognition test")
    explain_audio_comment = models.TextField(blank=True)
    normal_hearing_score = models.PositiveSmallIntegerField("Normal hearing vs. hearing loss", choices=SCORES, default=0,
    help_text="1) Explains normal hearing 2) Explains HL is any hearing below 20db 3) Specifies anything below 20db will require corrective treatment")
    normal_hearing_comment = models.TextField(blank=True)
    ask_chart_score = models.PositiveSmallIntegerField("Asked where patient expected to be on the chart", 
    choices=SCORES2, default=0)
    ask_chart_comment = models.TextField(blank=True)
    recommit_score = models.PositiveSmallIntegerField("Recommitment", choices=SCORES, default=0,
    help_text="References 1st commitment and/or FVT results, confirms willingness, seeks acknowledgement")
    recommit_comment = models.TextField(blank=True)
    bad_good_score = models.PositiveSmallIntegerField("Bad News/Good News", choices=SCORES, default=0,
    help_text="1) Separates Bad News/Good News, 2) Insert COSI, 3) Discuss Proper Amplification")
    bad_good_comment = models.TextField(blank=True)
    notions_score = models.PositiveSmallIntegerField("Discover if patient has preconceived notions of hearing aids", 
    choices=SCORES2, default=0, help_text="\"What have you heard good or not so good about HA?\"")
    notions_comment = models.TextField(blank=True)
    objections_score = models.PositiveSmallIntegerField("How well did they overcome objections?", choices=SCORES, default=0,
    help_text="1) Acknowledges concern 2) Addresses concerns 3) Moves forward without creating more objections")
    objections_comment = models.TextField(blank=True)
    pick_two_score = models.PositiveSmallIntegerField("5 most important things", choices=SCORES, default=0,
    help_text="3) Presents choices, has PT pick, references BOTH choices during the P&R")
    pick_two_comment = models.TextField(blank=True)
    style_cost_score = models.PositiveSmallIntegerField("States style has no bearing on cost", choices=SCORES, default=0,
    help_text="1) Says that style has no bearing on cost 3) Explains that style is based on looks and comfort")
    style_cost_comment = models.TextField(blank=True)
    style_fitting_score = models.PositiveSmallIntegerField("Used Audiogram Style Fitting Guide", choices=SCORES, default=0,
    help_text="Uses style guide to show WHY certain styles are appropriate, narrows down to 2-3, thoroughly explains differences between remaining styles")
    style_fitting_comment = models.TextField(blank=True)
    backup_score = models.PositiveSmallIntegerField("Get backup hearing aid", choices=SCORES2, default=0)
    backup_comment = models.TextField(blank=True)
    tech_fitting_score = models.PositiveSmallIntegerField("Used Technology Fitting Guide (Triangle or similar)", 
    choices=SCORES, default=0, help_text="Uses tech fitting guide, based on lifestyle and budget")
    tech_fitting_comment = models.TextField(blank=True)
    tech_levels_score = models.PositiveSmallIntegerField("Explanation of Technology Levels w/COSI references", 
    choices=SCORES, default=0, help_text="Inserts specific COSI goals to explain the levels of technology and helps PT visualize where they fall on the triangle (don't just list off COSI)")
    tech_levels_comment = models.TextField(blank=True)
    appropriate_score = models.PositiveSmallIntegerField("State that all recommendations are appropriate", 
    choices=SCORES2, default=0, help_text="Explains that a lower level of technology is NOT an inferior HA")
    appropriate_comment = models.TextField(blank=True)
    sep_rec_score = models.PositiveSmallIntegerField("Separate style and technology completely", choices=SCORES2, default=0,
    help_text="Settles on a specific style before moving on to technology, does not bounce back and forth")
    sep_rec_comment = models.TextField(blank=True)
    fight_score = models.PositiveSmallIntegerField("Fight for the sale?", choices=SCORES, default=0,
    help_text="References COSI and Auditory Deprivation")
    fight_comment = models.TextField(blank=True)
    questions_score = models.PositiveSmallIntegerField("Open Ended Questions", choices=SCORES, default=0,
    help_text="Asks more open than closed ended questions, properly digs for details")
    questions_comment = models.TextField(blank=True)
    restate_score = models.PositiveSmallIntegerField("Restate", choices=SCORES, default=0,
    help_text="Consistently restates PT pain points so they feel heard/understood")
    restate_comment = models.TextField(blank=True)
    validation_score = models.PositiveSmallIntegerField("Validation", choices=SCORES, default=0,
    help_text="Validates each specific pain point, thorough summary validation, validates each objection")
    validation_comment = models.TextField(blank=True)
    body_score = models.PositiveSmallIntegerField("Body Language", choices=SCORES, default=0,
    help_text="Ex: Sits up straight, leans forward when appropriate to show engagement")
    body_comment = models.TextField(blank=True)
    tone_score = models.PositiveSmallIntegerField("Tone", choices=SCORES, default=0,
    help_text="Tone demonstrates concern and consideration especially during the FVT results and bad news/good news")
    tone_comment = models.TextField(blank=True)
    words_score = models.PositiveSmallIntegerField("Words", choices=SCORES, default=0,
    help_text="Conveys confidence through clarity and conciseness with ALL explanations, no weak verbiage (maybe, I think, a little), does not mispronounce clinical terms")
    words_comment = models.TextField(blank=True)
    transitions_score = models.PositiveSmallIntegerField("Transitions", choices=SCORES, default=0,
    help_text="Smoothly moves from one DE section to the next, all necessary items take place before or after the audiogram")
    transitions_comment = models.TextField(blank=True)
    involvement_score = models.PositiveSmallIntegerField("Patient Involvement", choices=SCORES, default=0,
    help_text="Follows 70/30 Rule, PT opens up with hearing struggle, seeks acknowledgement throughout recommendation")
    involvement_comment = models.TextField(blank=True)
    authority_score = models.PositiveSmallIntegerField("Authority", choices=SCORES, default=0,
    help_text="Utilizes strong parent/child relationship to maintain control and direction")
    authority_comment = models.TextField(blank=True)
    rapport_score = models.PositiveSmallIntegerField("Rapport", choices=SCORES, default=0,
    help_text="PT trusts practitioner, practitioner shows interest and concern")
    rapport_comment = models.TextField(blank=True)
    cred_score = models.PositiveSmallIntegerField("Credibility", choices=SCORES, default=0,
    help_text="Establishes themselves as a medical professional")
    cred_comment = models.TextField(blank=True)
    COSI_score = models.PositiveSmallIntegerField("Use of COSI", choices=SCORES, default=0,
    help_text="Implements PT COSI goals during the anatomy, FVT, audiogram, prescription & recommendation")
    COSI_comment = models.TextField(blank=True)
    impact_score = models.PositiveSmallIntegerField("Impact", choices=SCORES, default=0,
    help_text="Helps PT internalize their loss and realize its severity (personal story, FVT, bad news/good news)")
    impact_comment = models.TextField(blank=True)
    urgency_score = models.PositiveSmallIntegerField("Urgency", choices=SCORES, default=0,
    help_text="Throughout the entire DE, PT understands how HL is a \"ticking clock,\" and that they are much worse off leaving their HL untreated")
    urgency_comment = models.TextField(blank=True)
    third_party_score = models.PositiveSmallIntegerField("3rd Party Interaction", choices=SCORES, default=0,
    help_text="Involves 3rd party at every level of the DE")
    third_party_comment = models.TextField(blank=True)
    
    # Metadata
    class Meta:
        ordering = ["-id"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a scorecard instance.
        """
        return reverse('scorecard_update_form', args=[str(self.id)])
    
    def get_another_absolute_url(self):
        """
        Returns the url to access a scorecard instance.
        """
        return reverse('scorecard_confirm_delete', args=[str(self.id)])
    
    def __str__(self):
        """
        Returns string of the referral source
        """
        return '%s/%s/%s/%s/%s' % (self.id, self.practitioner, self.location, self.date, self.time)