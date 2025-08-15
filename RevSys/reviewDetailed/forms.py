from django import forms
from django.contrib.auth.models import User
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'review-textarea',
                'rows': 8,
                'placeholder': 'Share your experience... What did you like or dislike?'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ensure required flags at form level
        self.fields['content'].required = True
        self.fields['rating'].required = True

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if not rating:
            raise forms.ValidationError('Please select a star rating.')
        if rating not in [1, 2, 3, 4, 5]:
            raise forms.ValidationError('Invalid rating value.')
        return rating
        