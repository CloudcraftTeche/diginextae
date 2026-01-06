from django import forms
from .models import (
    HomeBanner, HomeText1, HomeBanner2, HomeText2, Conncepts,
    HomeBanner3, HomeText3, HomeAvailableWorks, HomeBanner4, 
    Contents, HomeAboutUs, HomeQuestions, Question, Footer,
    HomeDigitalMarketing,  HomeVision,Insights,InsightsDigitalMarketing,OurWorksDigitalMarketing,
)


class HomeBannerForm(forms.ModelForm):
    class Meta:
        model = HomeBanner
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner description',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeText1Form(forms.ModelForm):
    class Meta:
        model = HomeText1
        fields = ['title', 'content', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content',
                'rows': 6
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeBanner2Form(forms.ModelForm):
    class Meta:
        model = HomeBanner2
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner description',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeText2Form(forms.ModelForm):
    class Meta:
        model = HomeText2
        fields = ['title', 'content', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content',
                'rows': 6
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class ConnceptsForm(forms.ModelForm):
    class Meta:
        model = Conncepts
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter concept title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter concept description',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


# ==================== NEW FORMS ====================

class HomeBanner3Form(forms.ModelForm):
    class Meta:
        model = HomeBanner3
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner description',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeText3Form(forms.ModelForm):
    class Meta:
        model = HomeText3
        fields = ['title', 'content', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content',
                'rows': 6
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeAvailableWorksForm(forms.ModelForm):
    class Meta:
        model = HomeAvailableWorks
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter work title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter work description',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeBanner4Form(forms.ModelForm):
    class Meta:
        model = HomeBanner4
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter banner description',
                'rows': 4
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class ContentsForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ['banner', 'title', 'text', 'is_active']
        widgets = {
            'banner': forms.Select(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter content text',
                'rows': 5
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeAboutUsForm(forms.ModelForm):
    class Meta:
        model = HomeAboutUs
        fields = ['title', 'description', 'image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter about us title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter about us description',
                'rows': 6
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeQuestionsForm(forms.ModelForm):
    class Meta:
        model = HomeQuestions
        fields = ['title', 'description', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter FAQ section title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter FAQ section description',
                'rows': 4
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['home_questions', 'question_text', 'answer_text', 'is_active']
        widgets = {
            'home_questions': forms.Select(attrs={
                'class': 'form-control'
            }),
            'question_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter question'
            }),
            'answer_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter answer',
                'rows': 4
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ['title', 'description', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter footer title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter footer description',
                'rows': 5
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class HomeDigitalMarketingForm(forms.ModelForm):
    class Meta:
        model = HomeDigitalMarketing
        fields = ['meta_title', 'meta_description', 'meta_keywords', 'banner_image', 'is_active']
        widgets = {
            'meta_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter meta title'
            }),
            'meta_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter meta description',
                'rows': 3
            }),
            'meta_keywords': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter meta keywords (comma separated)'
            }),
            'banner_image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }

class HomeVisionForm(forms.ModelForm):
    class Meta:
        model = HomeVision
        fields = ['title', 'description', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vision title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter vision description'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }       

class InsightsForm(forms.ModelForm):
    class Meta:
        model = Insights
        fields = ['title', 'subtitle', 'description', 'banner_image', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter subtitle'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }        

class InsightsDigitalMarketingForm(forms.ModelForm):
    class Meta:
        model = InsightsDigitalMarketing
        fields = ['meta_title', 'meta_description', 'meta_keywords', 'banner_image', 'is_active']
        widgets = {
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter meta title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter meta description'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter meta keywords (comma separated)'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }        

class OurWorksDigitalMarketingForm(forms.ModelForm):
    class Meta:
        model = OurWorksDigitalMarketing
        fields = ['meta_title', 'meta_description', 'meta_keywords', 'banner_image', 'is_active']
        widgets = {
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter meta title'}),
            'meta_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter meta description'}),
            'meta_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter meta keywords (comma separated)'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }        