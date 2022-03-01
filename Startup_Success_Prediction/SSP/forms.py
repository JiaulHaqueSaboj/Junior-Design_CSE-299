from attr import attr
from django import forms

from .models import Startup


class StartupModelForm(forms.ModelForm):

    class Meta:
        model = Startup
        fields = '__all__'
        labels = {
            'name': 'Startup Name ',
            'start': 'Startup Founded ',
            'category': 'Category ',
            'relationship_num': 'No. of Relationship ',
            'milestone_num': 'No. of Milestone ',
            'first_milestone': 'First Milestone Date ',
            'last_milestone': "Last Milestone Date ",
            'total_fund': 'Total Funding (USD) ',
            'first_funding': 'First Funding Date ',
            'last_funding': 'Last Funding Date ',
            'funding_round_num': 'No. of Funding Round ',
            'has_angel': "Angel Investor ",
            'has_vc': 'Venture Capital',
            'has_A': 'Series A ',
            'has_B': 'Series B ',
            'has_C': 'Series C ',
            'has_D': 'Series D ',

        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Startup name'
            }
            ),
            'start': forms.DateInput(
                format=('%d%m%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'category': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Choose Category'
            }),
            'relationship_num': forms.NumberInput(
                attrs={'step': 1,
                       "min_value": 0,
                       "max_value": 1000,
                       'class': 'form-control', 'placeholder': 'Enter the value', }),
            'milestone_num': forms.NumberInput(
                attrs={'step': 1,
                       "min_value": 0,
                       "max_value": 1000,
                       'class': 'form-control', 'placeholder': 'Enter the value', }),
            'first_milestone': forms.DateInput(
                format=('%d%m%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'last_milestone': forms.DateInput(
                format=('%d%m%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),



            'total_fund': forms.NumberInput(
                attrs={'step': 1,
                       "min_value": 0,
                       'class': 'form-control', 'placeholder': 'Enter the value', }),

            'first_funding': forms.DateInput(
                format=('%d%m%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'last_funding': forms.DateInput(
                format=('%d%m%Y'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            'funding_round_num': forms.NumberInput(
                attrs={'step': 1,
                       "min_value": 0,
                       "max_value": 1000,
                       'class': 'form-control', 'placeholder': 'Enter the value', }),
            'has_angel': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': "padding : 9px"}),
            'has_vc': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': "padding : 9px"}),

            'has_A': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': "padding : 9px"}),
            'has_B': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': "padding : 9px"}),
            'has_C': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': "padding : 9px"}),
            'has_D': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': "padding : 9px"}),





        }
