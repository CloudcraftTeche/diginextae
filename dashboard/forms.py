from django import forms
from .models import (
    HomeBanner, HomeText1, HomeBanner2, HomeText2, Conncepts,
    HomeBanner3, HomeText3, HomeAvailableWorks, HomeBanner4, 
    Contents, HomeAboutUs, HomeQuestions, Question, Footer,
    HomeDigitalMarketing,  HomeVision,Insights,InsightsDigitalMarketing,OurWorksDigitalMarketing,OurInsights,
    Blog,Design,InsightStrategy, InsightStrategyBlock, InsightStrategyPoint,
    InsightResult, InsightResultBlock,
    InsightAchievement, InsightAchievementPoint

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


class OurInsightsForm(forms.ModelForm):
    class Meta:
        model = OurInsights
        fields = ['title', 'description', 'image', 'insight_date', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter description'}),
            'insight_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 6 months, 1 week, 2 years'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }     
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'banner_image',
            'title',
            'image',
            'category',
            'features',
            'description',
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_content'}),
        }
   
class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = "__all__"
        exclude = ["slug"]
        
class InsightStrategyForm(forms.ModelForm):
    class Meta:
        model  = InsightStrategy
        fields = ['heading', 'description']
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter main heading',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter main description',
            }),
        }


class InsightStrategyBlockForm(forms.ModelForm):
    class Meta:
        model  = InsightStrategyBlock
        fields = ['heading']
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter block heading',
            }),
        }


# ─────────────────────────────────────────────
# View helper – called from your strategy view
# ─────────────────────────────────────────────

def save_strategy(request, insight):
    """
    Parse the POST data sent by the Strategy tab form and
    save/update InsightStrategy + its blocks and points.

    Expected POST keys
    ------------------
    heading                          – common heading
    description                      – common description
    strategy_blocks[0][heading]      – block 0 heading
    strategy_blocks[0][points][]     – block 0 points (multiple values)
    strategy_blocks[1][heading]      – block 1 heading
    strategy_blocks[1][points][]     – block 1 points
    ...
    """

    # 1. Save / update the parent InsightStrategy row
    strategy, _ = InsightStrategy.objects.get_or_create(insight=insight)
    strategy.heading     = request.POST.get('heading', '').strip()
    strategy.description = request.POST.get('description', '').strip()
    strategy.save()

    # 2. Parse blocks from POST data
    #    Collect all block indices present in the POST dict
    block_indices = set()
    for key in request.POST:
        # keys look like:  strategy_blocks[0][heading]
        if key.startswith('strategy_blocks['):
            try:
                idx = int(key.split('[')[1].split(']')[0])
                block_indices.add(idx)
            except (IndexError, ValueError):
                pass

    # 3. Delete old blocks (easiest approach – re-create fresh each save)
    strategy.blocks.all().delete()

    # 4. Re-create blocks and points in order
    for order, idx in enumerate(sorted(block_indices)):

        heading_key = f'strategy_blocks[{idx}][heading]'
        points_key  = f'strategy_blocks[{idx}][points][]'

        block_heading = request.POST.get(heading_key, '').strip()

        # getlist handles multiple values for the same key
        points = [
            p.strip()
            for p in request.POST.getlist(points_key)
            if p.strip()
        ]

        # Skip completely empty blocks
        if not block_heading and not points:
            continue

        block = InsightStrategyBlock.objects.create(
            strategy=strategy,
            heading=block_heading,
            order=order,
        )

        for pt_order, pt_text in enumerate(points):
            InsightStrategyPoint.objects.create(
                block=block,
                text=pt_text,
                order=pt_order,
            )

    return strategy


# ─────────────────────────────────────────────
# JSON serialiser – used by the /content/get/ endpoint
# ─────────────────────────────────────────────

def strategy_to_dict(insight):
    """
    Return strategy data as a dict ready to be sent as JSON
    so the frontend can pre-populate the modal fields.
    """
    try:
        strategy = insight.strategy
    except InsightStrategy.DoesNotExist:
        return {}

    blocks = []
    for block in strategy.blocks.all():
        blocks.append({
            'heading': block.heading,
            'points':  list(block.points.values_list('text', flat=True)),
        })

    return {
        'heading':     strategy.heading,
        'description': strategy.description,
        'blocks':      blocks,
    }


# ─────────────────────────────────────────────
# Example Django view
# ─────────────────────────────────────────────

# urls.py  ── add these two lines:
#
#   path('dashboard/insights/<int:insight_id>/content/strategy/',
#        views.insight_strategy_save, name='insight_strategy_save'),
#
#   path('dashboard/insights/<int:insight_id>/content/get/',
#        views.insight_content_get,   name='insight_content_get'),


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import OurInsights   # adjust to your app


def insight_strategy_save(request, insight_id):
    if request.method != 'POST':
        return redirect('our_insights')

    insight = get_object_or_404(OurInsight, pk=insight_id)
    save_strategy(request, insight)
    messages.success(request, 'Strategy saved successfully.')
    return redirect('our_insights')


def insight_content_get(request, insight_id):
    """
    Returns all content tab data as JSON for pre-populating
    the Content modal.  Add the other tabs (results, achievements,
    growth) here in the same pattern.
    """
    insight = get_object_or_404(OurInsight, pk=insight_id)

    data = {
        'strategy': strategy_to_dict(insight),
        # 'results':      results_to_dict(insight),
        # 'achievements': achievements_to_dict(insight),
        # 'growth':       growth_to_dict(insight),
    }

    return JsonResponse(data)

class InsightResultForm(forms.ModelForm):
    class Meta:
        model  = InsightResult
        fields = ['heading', 'description']
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter main heading',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter main description',
            }),
        }


class InsightResultBlockForm(forms.ModelForm):
    class Meta:
        model  = InsightResultBlock
        fields = ['image', 'heading', 'title', 'description']
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter block heading',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-sm',
                'placeholder': 'Enter block title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 2,
                'placeholder': 'Enter block description',
            }),
        }


# ─────────────────────────────────────────────
# View helper
# ─────────────────────────────────────────────

def save_result(request, insight):
    """
    Parse the POST + FILES data sent by the Results tab form and
    save/update InsightResult + its blocks.

    Expected POST keys
    ------------------
    heading                              – common heading
    description                          – common description
    results_blocks[0][heading]           – block 0 heading
    results_blocks[0][title]             – block 0 title
    results_blocks[0][description]       – block 0 description

    Expected FILES keys
    -------------------
    results_blocks[0][image]             – block 0 image (optional)
    """

    # 1. Save / update the parent InsightResult row
    result, _ = InsightResult.objects.get_or_create(insight=insight)
    result.heading     = request.POST.get('heading', '').strip()
    result.description = request.POST.get('description', '').strip()
    result.save()

    # 2. Collect block indices from POST keys
    block_indices = set()
    for key in request.POST:
        if key.startswith('results_blocks['):
            try:
                idx = int(key.split('[')[1].split(']')[0])
                block_indices.add(idx)
            except (IndexError, ValueError):
                pass
    # Also check FILES for any image-only blocks
    for key in request.FILES:
        if key.startswith('results_blocks['):
            try:
                idx = int(key.split('[')[1].split(']')[0])
                block_indices.add(idx)
            except (IndexError, ValueError):
                pass

    # 3. Delete old blocks and re-create fresh
    result.blocks.all().delete()

    # 4. Re-create blocks in order
    for order, idx in enumerate(sorted(block_indices)):

        heading_key     = f'results_blocks[{idx}][heading]'
        title_key       = f'results_blocks[{idx}][title]'
        description_key = f'results_blocks[{idx}][description]'
        image_key       = f'results_blocks[{idx}][image]'

        heading     = request.POST.get(heading_key, '').strip()
        title       = request.POST.get(title_key, '').strip()
        description = request.POST.get(description_key, '').strip()
        image       = request.FILES.get(image_key)  # None if not uploaded

        # Skip completely empty blocks
        if not any([heading, title, description, image]):
            continue

        block = InsightResultBlock(
            result=result,
            heading=heading,
            title=title,
            description=description,
            order=order,
        )
        if image:
            block.image = image
        block.save()

    return result


# ─────────────────────────────────────────────
# JSON serialiser – used by /content/get/ endpoint
# ─────────────────────────────────────────────

def result_to_dict(insight):
    """
    Return result data as a dict ready to be sent as JSON
    so the frontend can pre-populate the modal fields.
    """
    try:
        result = insight.result
    except InsightResult.DoesNotExist:
        return {}

    blocks = []
    for block in result.blocks.all():
        blocks.append({
            'heading':     block.heading,
            'title':       block.title,
            'description': block.description,
            'image_url':   block.image.url if block.image else '',
        })

    return {
        'heading':     result.heading,
        'description': result.description,
        'blocks':      blocks,
    }


# ─────────────────────────────────────────────
# Example Django view
# ─────────────────────────────────────────────

# urls.py – add this line:
#
#   path('dashboard/insights/<int:insight_id>/content/results/',
#        views.insight_result_save, name='insight_result_save'),


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import OurInsights  # adjust to your app


def insight_result_save(request, insight_id):
    if request.method != 'POST':
        return redirect('our_insights')

    insight = get_object_or_404(OurInsight, pk=insight_id)
    save_result(request, insight)
    messages.success(request, 'Results saved successfully.')
    return redirect('our_insights')


class InsightAchievementForm(forms.ModelForm):
    class Meta:
        model  = InsightAchievement
        fields = ['heading']
        widgets = {
            'heading': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter heading',
            }),
        }


# ─────────────────────────────────────────────
# View helper
# ─────────────────────────────────────────────

def save_achievement(request, insight):
    """
    Parse the POST data sent by the Achievements tab form and
    save/update InsightAchievement + its points.

    Expected POST keys
    ------------------
    heading                  – single heading
    achievements_points[]    – multiple point values (getlist)
    """

    # 1. Save / update the parent InsightAchievement row
    achievement, _ = InsightAchievement.objects.get_or_create(insight=insight)
    achievement.heading = request.POST.get('heading', '').strip()
    achievement.save()

    # 2. Get all points from the form (filter out blank ones)
    points = [
        p.strip()
        for p in request.POST.getlist('achievements_points[]')
        if p.strip()
    ]

    # 3. Delete old points and re-create fresh
    achievement.points.all().delete()

    for order, text in enumerate(points):
        InsightAchievementPoint.objects.create(
            achievement=achievement,
            text=text,
            order=order,
        )

    return achievement


# ─────────────────────────────────────────────
# JSON serialiser – used by the /content/get/ endpoint
# ─────────────────────────────────────────────

def achievement_to_dict(insight):
    """
    Return achievement data as a dict ready to be sent as JSON
    so the frontend can pre-populate the modal fields.
    """
    try:
        achievement = insight.achievement
    except InsightAchievement.DoesNotExist:
        return {}

    return {
        'heading': achievement.heading,
        'points':  list(achievement.points.values_list('text', flat=True)),
    }


# ─────────────────────────────────────────────
# Example Django view
# ─────────────────────────────────────────────

# urls.py  ── add this line:
#
#   path('dashboard/insights/<int:insight_id>/content/achievements/',
#        views.insight_achievement_save, name='insight_achievement_save'),


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import OurInsights  # adjust to your app


def insight_achievement_save(request, insight_id):
    if request.method != 'POST':
        return redirect('our_insights')

    insight = get_object_or_404(OurInsights, pk=insight_id)
    save_achievement(request, insight)
    messages.success(request, 'Achievements saved successfully.')
    return redirect('our_insights')


# ─────────────────────────────────────────────
# Updated insight_content_get view
# (replace the one from result_forms_views.py)
# ─────────────────────────────────────────────

from django.http import JsonResponse
# from .strategy_forms_views import strategy_to_dict    # adjust import
# from .result_forms_views   import result_to_dict      # adjust import


def insight_content_get(request, insight_id):
    insight = get_object_or_404(OurInsights, pk=insight_id)

    data = {
        'strategy':     strategy_to_dict(insight),
        'results':      result_to_dict(insight),
        'achievements': achievement_to_dict(insight),
        # 'growth':    growth_to_dict(insight),
    }

    return JsonResponse(data)
