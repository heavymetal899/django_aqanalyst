# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-12 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorecarddb', '0029_auto_20171111_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorecard',
            name='COSI_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Use of COSI'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='FVT_exp_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Expectations'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='FVT_results_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Results'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='FVT_third_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Discussed results with the third party'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='appropriate_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='State that all recommendations are appropriate'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='ask_chart_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Asked where patient expected to be on the chart'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='authority_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Authority'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='backup_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Get backup hearing aid'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='bad_good_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Bad News/Good News'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='body_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Body Language'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='cred_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Credibility'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='explain_audio_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Explained audiogram'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='fight_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Fight for the sale?'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='impact_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Impact'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='involvement_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Patient Involvement'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='maintain_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Discussed need to maintain what is left'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='normal_hearing_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Normal hearing vs. hearing loss'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='notions_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Discover if patient has preconceived notions of hearing aids'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='objections_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='How well did they overcome objections?'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='otoscope_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Otoscope'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='pick_two_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='5 most important things'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='questions_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Open Ended Questions'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='rapport_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Rapport'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='recommit_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Recommitment'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='restate_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Restate'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='sep_rec_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Separate style and technology completely'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='story_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Personal story'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='style_cost_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='States style has no bearing on cost'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='style_fitting_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Used Audiogram Style Fitting Guide'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='tech_fitting_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Used Technology Fitting Guide (Triangle or similar)'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='tech_levels_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Explanation of Technology Levels w/COSI references'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='third_party_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='3rd Party Interaction'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='tone_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Tone'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='transitions_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Transitions'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='urgency_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Urgency'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='validation_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Validation'),
        ),
        migrations.AlterField(
            model_name='scorecard',
            name='words_score',
            field=models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, verbose_name='Words'),
        ),
    ]
