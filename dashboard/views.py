from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse    
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import cloudinary.uploader
from .models import *
from .forms import *


# ==================== HELPER FUNCTION FOR CLOUDINARY IMAGE DELETION ====================
def delete_cloudinary_image(image_field):
    """
    Helper function to delete an image from Cloudinary.
    Works with both CloudinaryField and regular ImageField using Cloudinary storage.
    """
    if not image_field:
        return
    
    try:
        # For CloudinaryField
        if hasattr(image_field, 'public_id') and image_field.public_id:
            cloudinary.uploader.destroy(image_field.public_id)
        # For ImageField with Cloudinary storage - extract public_id from URL
        elif hasattr(image_field, 'name') and image_field.name:
            public_id = image_field.name
            if '.' in public_id:
                public_id = public_id.rsplit('.', 1)[0]
            cloudinary.uploader.destroy(public_id)
    except Exception as e:
        print(f"Error deleting Cloudinary image: {e}")


# ==================== AUTHENTICATION ====================
def login_view(request):
    User = get_user_model()

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Your account is inactive.')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


@login_required(login_url='login')
def dashboard_view(request):
    context = {'user': request.user}
    return render(request, 'dashboard.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')


# ==================== HOME PAGE ====================
@login_required
def home(request):
    """Home Page Management - List All Content"""
    context = {
        'home_banners': HomeBanner.objects.all().order_by('-created_at'),
        'home_text1': HomeText1.objects.all().order_by('-created_at'),
        'home_banner2': HomeBanner2.objects.all().order_by('-created_at'),
        'home_text2': HomeText2.objects.all().order_by('-created_at'),
        'concepts': Conncepts.objects.all().order_by('-created_at'),
        'home_banner3': HomeBanner3.objects.all().order_by('-created_at'),
        'home_text3': HomeText3.objects.all().order_by('-created_at'),
        'home_available_works': HomeAvailableWorks.objects.all().order_by('-created_at'),
        'home_banner4': HomeBanner4.objects.all().order_by('-created_at'),
        'home_about_us': HomeAboutUs.objects.all().order_by('-created_at'),
        'home_questions': HomeQuestions.objects.all().order_by('-created_at'),
        'footer': Footer.objects.all().order_by('-created_at'),
        'home_digital_marketing': HomeDigitalMarketing.objects.first(),
        'home_banners_count': HomeBanner.objects.count(),
        'home_text1_count': HomeText1.objects.count(),
        'home_banner2_count': HomeBanner2.objects.count(),
        'concepts_count': Conncepts.objects.count(),
        'home_banner3_count': HomeBanner3.objects.count(),
        'home_available_works_count': HomeAvailableWorks.objects.count(),
        'home_banner4_count': HomeBanner4.objects.count(),
        'home_about_us_count': HomeAboutUs.objects.count(),
        'home_questions_count': HomeQuestions.objects.count(),
    }
    return render(request, 'home.html', context)


# ==================== HOME BANNER CRUD ====================
@login_required
def home_banner(request):
    banners = HomeBanner.objects.all().order_by('-created_at')
    context = {'banners': banners, 'banners_count': banners.count()}
    return render(request, 'banner.html', context)


@login_required
def home_banner_create(request):
    if request.method == 'POST':
        form = HomeBannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Home banner created successfully!')
            return redirect('home_banner')
    else:
        form = HomeBannerForm()
    return render(request, 'home_banner_form.html', {'form': form, 'action': 'Create'})


@login_required
def home_banner_edit(request, pk):
    banner = get_object_or_404(HomeBanner, pk=pk)
    old_image = banner.image
    
    if request.method == 'POST':
        form = HomeBannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Home banner updated successfully!')
            return redirect('home_banner')
    else:
        form = HomeBannerForm(instance=banner)
    return render(request, 'home_banner_form.html', {'form': form, 'action': 'Edit'})


@login_required
def home_banner_delete(request, pk):
    banner = get_object_or_404(HomeBanner, pk=pk)
    if banner.image:
        delete_cloudinary_image(banner.image)
    banner.delete()
    messages.success(request, 'Home banner deleted successfully!')
    return redirect('home_banner')


# ==================== HOME TEXT 1 CRUD ====================
@login_required
def home_text1(request):
    text_sections = HomeText1.objects.all().order_by('-created_at')
    context = {'text_sections': text_sections, 'text_count': text_sections.count()}
    return render(request, 'text1.html', context)


@login_required
def home_text1_create(request):
    if request.method == 'POST':
        form = HomeText1Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section created successfully!')
            return redirect('home_text1')
    else:
        form = HomeText1Form()
    return render(request, 'home_text_form.html', {'form': form, 'action': 'Create', 'section': 'Text Section 1'})


@login_required
def home_text1_edit(request, pk):
    text = get_object_or_404(HomeText1, pk=pk)
    if request.method == 'POST':
        form = HomeText1Form(request.POST, instance=text)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section updated successfully!')
            return redirect('home_text1')
    else:
        form = HomeText1Form(instance=text)
    return render(request, 'home_text_form.html', {'form': form, 'action': 'Edit', 'section': 'Text Section 1'})


@login_required
def home_text1_delete(request, pk):
    text = get_object_or_404(HomeText1, pk=pk)
    text.delete()
    messages.success(request, 'Text section deleted successfully!')
    return redirect('home_text1')


# ==================== HOME BANNER 2 CRUD ====================
@login_required
def home_banner2(request):
    banners = HomeBanner2.objects.all().order_by('-created_at')
    context = {'banners': banners, 'banners_count': banners.count()}
    return render(request, 'secondarybanner.html', context)


@login_required
def home_banner2_create(request):
    if request.method == 'POST':
        form = HomeBanner2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Secondary banner created successfully!')
            return redirect('home_banner2')
    else:
        form = HomeBanner2Form()
    return render(request, 'home_banner_form.html', {'form': form, 'action': 'Create', 'banner_type': 'Secondary'})


@login_required
def home_banner2_edit(request, pk):
    banner = get_object_or_404(HomeBanner2, pk=pk)
    old_image = banner.image
    
    if request.method == 'POST':
        form = HomeBanner2Form(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Secondary banner updated successfully!')
            return redirect('home_banner2')
    else:
        form = HomeBanner2Form(instance=banner)
    return render(request, 'home_banner_form.html', {'form': form, 'action': 'Edit', 'banner_type': 'Secondary'})


@login_required
def home_banner2_delete(request, pk):
    banner = get_object_or_404(HomeBanner2, pk=pk)
    if banner.image:
        delete_cloudinary_image(banner.image)
    banner.delete()
    messages.success(request, 'Secondary banner deleted successfully!')
    return redirect('home_banner2')


# ==================== HOME TEXT 2 CRUD ====================
@login_required
def home_text2(request):
    text_sections = HomeText2.objects.all().order_by('-created_at')
    context = {'text_sections': text_sections, 'text_count': text_sections.count()}
    return render(request, 'text2.html', context)


@login_required
def home_text2_create(request):
    if request.method == 'POST':
        form = HomeText2Form(request.POST)
        if form.is_valid():
            new_text = form.save(commit=False)
            if new_text.is_active:
                HomeText2.objects.all().update(is_active=False)
            new_text.save()
            messages.success(request, 'Text section 2 created successfully!')
            return redirect('home_text2')
    else:
        form = HomeText2Form()
    return render(request, 'home_text_form.html', {'form': form, 'action': 'Create', 'section': 'Text Section 2'})


@login_required
def home_text2_edit(request, pk):
    text = get_object_or_404(HomeText2, pk=pk)
    if request.method == 'POST':
        form = HomeText2Form(request.POST, instance=text)
        if form.is_valid():
            updated_text = form.save(commit=False)
            if updated_text.is_active:
                HomeText2.objects.exclude(pk=pk).update(is_active=False)
            updated_text.save()
            messages.success(request, 'Text section 2 updated successfully!')
            return redirect('home_text2')
    else:
        form = HomeText2Form(instance=text)
    return render(request, 'home_text_form.html', {'form': form, 'action': 'Edit', 'section': 'Text Section 2'})


@login_required
def home_text2_delete(request, pk):
    text = get_object_or_404(HomeText2, pk=pk)
    text.delete()
    messages.success(request, 'Text section 2 deleted successfully!')
    return redirect('home_text2')


# ==================== CONCEPTS CRUD ====================
@login_required
def home_concepts(request):
    concepts = Conncepts.objects.all().order_by('-created_at')
    context = {'concepts': concepts, 'concepts_count': concepts.count()}
    return render(request, 'concepts.html', context)


@login_required
def concepts_create(request):
    if request.method == 'POST':
        form = ConnceptsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concept created successfully!')
            return redirect('home_concepts')
    else:
        form = ConnceptsForm()
    return render(request, 'concepts_form.html', {'form': form, 'action': 'Create'})


@login_required
def concepts_edit(request, pk):
    concept = get_object_or_404(Conncepts, pk=pk)
    old_image = concept.image
    
    if request.method == 'POST':
        form = ConnceptsForm(request.POST, request.FILES, instance=concept)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Concept updated successfully!')
            return redirect('home_concepts')
    else:
        form = ConnceptsForm(instance=concept)
    return render(request, 'concepts_form.html', {'form': form, 'action': 'Edit'})


@login_required
def concepts_delete(request, pk):
    concept = get_object_or_404(Conncepts, pk=pk)
    if concept.image:
        delete_cloudinary_image(concept.image)
    concept.delete()
    messages.success(request, 'Concept deleted successfully!')
    return redirect('home_concepts')


# ==================== HOME BANNER 3 CRUD ====================
@login_required
def home_banner3_page(request):
    banners = HomeBanner3.objects.all().order_by('-created_at')
    context = {'banners': banners, 'banners_count': banners.count()}
    return render(request, 'homebanner3.html', context)


@login_required
def home_banner3_create(request):
    if request.method == 'POST':
        form = HomeBanner3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Home banner 3 created successfully!')
    return redirect('home_banner3_page')


@login_required
def home_banner3_edit(request, pk):
    banner = get_object_or_404(HomeBanner3, pk=pk)
    old_image = banner.image
    
    if request.method == 'POST':
        form = HomeBanner3Form(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Home banner 3 updated successfully!')
    return redirect('home_banner3_page')


@login_required
def home_banner3_delete(request, pk):
    banner = get_object_or_404(HomeBanner3, pk=pk)
    if banner.image:
        delete_cloudinary_image(banner.image)
    banner.delete()
    messages.success(request, 'Home banner 3 deleted successfully!')
    return redirect('home_banner3_page')


# ==================== HOME TEXT 3 CRUD ====================
@login_required
def home_text3_page(request):
    text_sections = HomeText3.objects.all().order_by('-created_at')
    context = {'text_sections': text_sections, 'text_count': text_sections.count()}
    return render(request, 'text3.html', context)


@login_required
def home_text3_create(request):
    if request.method == 'POST':
        form = HomeText3Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section 3 created successfully!')
    return redirect('home_text3_page')


@login_required
def home_text3_edit(request, pk):
    text = get_object_or_404(HomeText3, pk=pk)
    if request.method == 'POST':
        form = HomeText3Form(request.POST, instance=text)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section 3 updated successfully!')
    return redirect('home_text3_page')


@login_required
def home_text3_delete(request, pk):
    text = get_object_or_404(HomeText3, pk=pk)
    text.delete()
    messages.success(request, 'Text section 3 deleted successfully!')
    return redirect('home_text3_page')


# ==================== HOME AVAILABLE WORKS CRUD ====================
@login_required
def home_available_works_page(request):
    works = HomeAvailableWorks.objects.all().order_by('-created_at')
    context = {'works': works, 'works_count': works.count()}
    return render(request, 'availableworks.html', context)


@login_required
def home_available_works_create(request):
    if request.method == 'POST':
        form = HomeAvailableWorksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Available work created successfully!')
    return redirect('home_available_works_page')


@login_required
def home_available_works_edit(request, pk):
    work = get_object_or_404(HomeAvailableWorks, pk=pk)
    old_image = work.image
    
    if request.method == 'POST':
        form = HomeAvailableWorksForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Available work updated successfully!')
    return redirect('home_available_works_page')


@login_required
def home_available_works_delete(request, pk):
    work = get_object_or_404(HomeAvailableWorks, pk=pk)
    if work.image:
        delete_cloudinary_image(work.image)
    work.delete()
    messages.success(request, 'Available work deleted successfully!')
    return redirect('home_available_works_page')


# ==================== HOME BANNER 4 CRUD ====================
@login_required
def home_banner4_page(request):
    banners = HomeBanner4.objects.all().order_by('-created_at')
    context = {'banners': banners, 'banners_count': banners.count()}
    return render(request, 'homebanner4.html', context)


@login_required
def home_banner4_create(request):
    if request.method == 'POST':
        form = HomeBanner4Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Home banner 4 created successfully!')
    return redirect('home_banner4_page')


@login_required
def home_banner4_edit(request, pk):
    banner = get_object_or_404(HomeBanner4, pk=pk)
    old_image = banner.image
    
    if request.method == 'POST':
        form = HomeBanner4Form(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Home banner 4 updated successfully!')
    return redirect('home_banner4_page')


@login_required
def home_banner4_delete(request, pk):
    banner = get_object_or_404(HomeBanner4, pk=pk)
    if banner.image:
        delete_cloudinary_image(banner.image)
    banner.delete()
    messages.success(request, 'Home banner 4 deleted successfully!')
    return redirect('home_banner4_page')


# ==================== CONTENTS CRUD ====================
@login_required
def contents_create(request):
    if request.method == 'POST':
        form = ContentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Content created successfully!')
    return redirect('home')


@login_required
def contents_edit(request, pk):
    content = get_object_or_404(Contents, pk=pk)
    if request.method == 'POST':
        form = ContentsForm(request.POST, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Content updated successfully!')
    return redirect('home')


@login_required
def contents_delete(request, pk):
    content = get_object_or_404(Contents, pk=pk)
    content.delete()
    messages.success(request, 'Content deleted successfully!')
    return redirect('home')


# ==================== HOME ABOUT US CRUD ====================
@login_required
def home_about_us_page(request):
    about_us_items = HomeAboutUs.objects.all().order_by('-created_at')
    context = {'about_us_items': about_us_items, 'about_us_count': about_us_items.count()}
    return render(request, 'homeaboutus.html', context)


@login_required
def home_about_us_create(request):
    if request.method == 'POST':
        form = HomeAboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            new_about = form.save(commit=False)
            if new_about.is_active:
                HomeAboutUs.objects.all().update(is_active=False)
            new_about.save()
            messages.success(request, 'About Us section created successfully!')
    return redirect('home_about_us_page')


@login_required
def home_about_us_edit(request, pk):
    about_us = get_object_or_404(HomeAboutUs, pk=pk)
    old_image = about_us.image
    
    if request.method == 'POST':
        form = HomeAboutUsForm(request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            updated_about = form.save(commit=False)
            if updated_about.is_active:
                HomeAboutUs.objects.exclude(pk=pk).update(is_active=False)
            if 'image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            updated_about.save()
            messages.success(request, 'About Us section updated successfully!')
    return redirect('home_about_us_page')


@login_required
def home_about_us_delete(request, pk):
    about_us = get_object_or_404(HomeAboutUs, pk=pk)
    if about_us.image:
        delete_cloudinary_image(about_us.image)
    about_us.delete()
    messages.success(request, 'About Us section deleted successfully!')
    return redirect('home_about_us_page')


# ==================== HOME QUESTIONS CRUD ====================
@login_required
def home_faq_page(request):
    faqs = HomeQuestions.objects.all().order_by('-created_at')
    context = {'faqs': faqs, 'faqs_count': faqs.count()}
    return render(request, 'homefaq.html', context)


@login_required
def home_questions_create(request):
    if request.method == 'POST':
        form = HomeQuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ section created successfully!')
    return redirect('home_faq_page')


@login_required
def home_questions_edit(request, pk):
    questions = get_object_or_404(HomeQuestions, pk=pk)
    if request.method == 'POST':
        form = HomeQuestionsForm(request.POST, instance=questions)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ section updated successfully!')
    return redirect('home_faq_page')


@login_required
def home_questions_delete(request, pk):
    questions = get_object_or_404(HomeQuestions, pk=pk)
    questions.delete()
    messages.success(request, 'FAQ section deleted successfully!')
    return redirect('home_faq_page')


# ==================== QUESTION CRUD ====================
@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question created successfully!')
    return redirect('home')


@login_required
def question_edit(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated successfully!')
    return redirect('home')


@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    messages.success(request, 'Question deleted successfully!')
    return redirect('home')


# ==================== FOOTER CRUD ====================
@login_required
def home_footer_page(request):
    footers = Footer.objects.all().order_by('-created_at')
    context = {'footers': footers, 'footers_count': footers.count()}
    return render(request, 'homefooter.html', context)


@login_required
def footer_create(request):
    if request.method == 'POST':
        form = FooterForm(request.POST)
        if form.is_valid():
            new_footer = form.save(commit=False)
            if new_footer.is_active:
                Footer.objects.all().update(is_active=False)
            new_footer.save()
            messages.success(request, 'Footer created successfully!')
    return redirect('home_footer_page')


@login_required
def footer_edit(request, pk):
    footer = get_object_or_404(Footer, pk=pk)
    if request.method == 'POST':
        form = FooterForm(request.POST, instance=footer)
        if form.is_valid():
            updated_footer = form.save(commit=False)
            if updated_footer.is_active:
                Footer.objects.exclude(pk=pk).update(is_active=False)
            updated_footer.save()
            messages.success(request, 'Footer updated successfully!')
    return redirect('home_footer_page')


@login_required
def footer_delete(request, pk):
    footer = get_object_or_404(Footer, pk=pk)
    footer.delete()
    messages.success(request, 'Footer deleted successfully!')
    return redirect('home_footer_page')


# ==================== HOME DIGITAL MARKETING ====================
@login_required
def home_digital_marketing_page(request):
    digital_marketing = HomeDigitalMarketing.objects.first()
    context = {'digital_marketing': digital_marketing}
    return render(request, 'homedigitalmarketing.html', context)


@login_required
def home_digital_marketing_update(request):
    marketing = HomeDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        old_image = marketing.banner_image if marketing else None
        
        if marketing:
            form = HomeDigitalMarketingForm(request.POST, request.FILES, instance=marketing)
        else:
            form = HomeDigitalMarketingForm(request.POST, request.FILES)
        
        if form.is_valid():
            if 'banner_image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'SEO / Digital Marketing settings updated successfully!')
    
    return redirect('home_digital_marketing_page')


# ==================== HOME VISION ====================
@login_required
def home_vision_list(request):
    visions = HomeVision.objects.all().order_by('-created_at')
    context = {'visions': visions, 'visions_count': visions.count()}
    return render(request, 'vision.html', context)


@login_required
def home_vision_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_active = request.POST.get('is_active') == 'on'
        
        if is_active:
            HomeVision.objects.all().update(is_active=False)
        
        HomeVision.objects.create(title=title, description=description, is_active=is_active)
        messages.success(request, 'Vision created successfully!')
    return redirect('home_vision_list')


@login_required
def home_vision_edit(request, pk):
    vision = get_object_or_404(HomeVision, pk=pk)
    
    if request.method == 'POST':
        vision.title = request.POST.get('title')
        vision.description = request.POST.get('description')
        is_active = request.POST.get('is_active') == 'on'
        
        if is_active:
            HomeVision.objects.exclude(pk=pk).update(is_active=False)
        
        vision.is_active = is_active
        vision.save()
        messages.success(request, 'Vision updated successfully!')
    return redirect('home_vision_list')


@login_required
def home_vision_delete(request, pk):
    vision = get_object_or_404(HomeVision, pk=pk)
    vision.delete()
    messages.success(request, 'Vision deleted successfully!')
    return redirect('home_vision_list')


# ==================== HOME FEATURES ====================
@login_required
def home_features_list(request):
    features = HomeFeatures.objects.all().order_by('-created_at')
    context = {'features': features, 'features_count': features.count()}
    return render(request, 'homefeatures.html', context)


@login_required
def home_features_add(request):
    if request.method == 'POST':
        is_active = request.POST.get('is_active') == 'on'
        if is_active:
            HomeFeatures.objects.all().update(is_active=False)
        
        HomeFeatures.objects.create(
            image=request.FILES.get('image'),
            main_feature=request.POST.get('main_feature'),
            text1=request.POST.get('text1'),
            text1_description=request.POST.get('text1_description'),
            text2=request.POST.get('text2'),
            text2_description=request.POST.get('text2_description'),
            text3=request.POST.get('text3'),
            text3_description=request.POST.get('text3_description'),
            text4=request.POST.get('text4'),
            text4_description=request.POST.get('text4_description'),
            text5=request.POST.get('text5'),
            text5_description=request.POST.get('text5_description'),
            text6=request.POST.get('text6'),
            text6_description=request.POST.get('text6_description'),
            is_active=is_active
        )
        messages.success(request, 'Home feature created successfully!')
    return redirect('home_features_list')


@login_required
def home_features_edit(request, pk):
    feature = get_object_or_404(HomeFeatures, pk=pk)
    old_image = feature.image
    
    if request.method == 'POST':
        feature.main_feature = request.POST.get('main_feature')
        feature.text1 = request.POST.get('text1')
        feature.text1_description = request.POST.get('text1_description')
        feature.text2 = request.POST.get('text2')
        feature.text2_description = request.POST.get('text2_description')
        feature.text3 = request.POST.get('text3')
        feature.text3_description = request.POST.get('text3_description')
        feature.text4 = request.POST.get('text4')
        feature.text4_description = request.POST.get('text4_description')
        feature.text5 = request.POST.get('text5')
        feature.text5_description = request.POST.get('text5_description')
        feature.text6 = request.POST.get('text6')
        feature.text6_description = request.POST.get('text6_description')
        is_active = request.POST.get('is_active') == 'on'
        
        if is_active:
            HomeFeatures.objects.exclude(pk=pk).update(is_active=False)
        feature.is_active = is_active
        
        if request.FILES.get('image'):
            if old_image:
                delete_cloudinary_image(old_image)
            feature.image = request.FILES.get('image')
        
        feature.save()
        messages.success(request, 'Home feature updated successfully!')
    return redirect('home_features_list')


@login_required
def home_features_delete(request, pk):
    feature = get_object_or_404(HomeFeatures, pk=pk)
    if feature.image:
        delete_cloudinary_image(feature.image)
    feature.delete()
    messages.success(request, 'Home feature deleted successfully!')
    return redirect('home_features_list')
# ==================== CONTACTS SECTION ====================

@login_required
def contacts_page(request):
    contact_sa = ContactSA.objects.all()
    leads = Leads.objects.all()
    contact_digital_marketing = ContactDigitalMarketing.objects.first()
    
    context = {
        'contact_sa': contact_sa,
        'contact_sa_count': contact_sa.count(),
        'leads': leads,
        'leads_count': leads.count(),
        'contact_digital_marketing': contact_digital_marketing,
    }
    return render(request, 'contacts.html', context)


@login_required
def contact_sa_create(request):
    if request.method == 'POST':
        ContactSA.objects.create(
            title=request.POST.get('title'),
            icon=request.POST.get('icon'),
            text=request.POST.get('text')
        )
        messages.success(request, 'Contact information created successfully!')
    return redirect('contacts_page')


@login_required
def contact_sa_edit(request, pk):
    contact = get_object_or_404(ContactSA, pk=pk)
    
    if request.method == 'POST':
        contact.title = request.POST.get('title')
        contact.icon = request.POST.get('icon')
        contact.text = request.POST.get('text')
        contact.save()
        messages.success(request, 'Contact information updated successfully!')
    return redirect('contacts_page')


@login_required
def contact_sa_delete(request, pk):
    contact = get_object_or_404(ContactSA, pk=pk)
    contact.delete()
    messages.success(request, 'Contact information deleted successfully!')
    return redirect('contacts_page')


@login_required
def contact_digital_marketing_update(request):
    contact_dm = ContactDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')
        meta_keywords = request.POST.get('meta_keywords')
        is_active = request.POST.get('is_active') == 'on'
        banner_image = request.FILES.get('banner_image')
        
        if contact_dm:
            old_image = contact_dm.banner_image
            contact_dm.meta_title = meta_title
            contact_dm.meta_description = meta_description
            contact_dm.meta_keywords = meta_keywords
            contact_dm.is_active = is_active
            if banner_image:
                if old_image:
                    delete_cloudinary_image(old_image)
                contact_dm.banner_image = banner_image
            contact_dm.save()
            messages.success(request, 'Contact SEO settings updated successfully!')
        else:
            ContactDigitalMarketing.objects.create(
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keywords=meta_keywords,
                is_active=is_active,
                banner_image=banner_image
            )
            messages.success(request, 'Contact SEO settings created successfully!')
    
    return redirect('contacts_page')


@login_required
def leads_create(request):
    if request.method == 'POST':
        Leads.objects.create(
            fullname=request.POST.get('fullname'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        messages.success(request, 'Lead created successfully!')
    return redirect('contacts_page')


@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Leads, pk=pk)
    
    if request.method == 'POST':
        lead.fullname = request.POST.get('fullname')
        lead.email = request.POST.get('email')
        lead.message = request.POST.get('message')
        lead.save()
        messages.success(request, 'Lead updated successfully!')
    return redirect('contacts_page')


@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Leads, pk=pk)
    lead.delete()
    messages.success(request, 'Lead deleted successfully!')
    return redirect('contacts_page')


# ==================== ABOUT US SECTION ====================

@login_required
def aboutus_page(request):
    context = {
        'aboutus_banner1': AboutUsBanner1.objects.all(),
        'aboutus_banner1_count': AboutUsBanner1.objects.count(),
        'aboutus_text1': AboutUsText1.objects.all(),
        'aboutus_text1_count': AboutUsText1.objects.count(),
        'aboutus_mission': AboutUsMission.objects.all(),
        'aboutus_mission_count': AboutUsMission.objects.count(),
        'aboutus_text2': AboutUsText2.objects.all(),
        'aboutus_text2_count': AboutUsText2.objects.count(),
        'aboutus_digital_marketing': AboutUsDigitalMarketing.objects.first(),
    }
    return render(request, 'aboutus.html', context)


@login_required
def aboutus_banner1_create(request):
    if request.method == 'POST':
        is_active = request.POST.get('is_active') == 'on'
        if is_active:
            AboutUsBanner1.objects.all().update(is_active=False)
        
        AboutUsBanner1.objects.create(
            title=request.POST.get('title'),
            subtitle=request.POST.get('subtitle'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            is_active=is_active
        )
        messages.success(request, 'About Us banner created successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_banner1_edit(request, pk):
    banner = get_object_or_404(AboutUsBanner1, pk=pk)
    
    if request.method == 'POST':
        banner.title = request.POST.get('title')
        banner.subtitle = request.POST.get('subtitle')
        banner.description = request.POST.get('description')
        is_active = request.POST.get('is_active') == 'on'
        
        if is_active:
            AboutUsBanner1.objects.exclude(pk=pk).update(is_active=False)
        banner.is_active = is_active
        
        if request.FILES.get('image'):
            if banner.image:
                delete_cloudinary_image(banner.image)
            banner.image = request.FILES.get('image')
        
        banner.save()
        messages.success(request, 'About Us banner updated successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_banner1_delete(request, pk):
    banner = get_object_or_404(AboutUsBanner1, pk=pk)
    if banner.image:
        delete_cloudinary_image(banner.image)
    banner.delete()
    messages.success(request, 'About Us banner deleted successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_text1_create(request):
    if request.method == 'POST':
        is_active = request.POST.get('is_active') == 'on'
        if is_active:
            AboutUsText1.objects.all().update(is_active=False)
        
        AboutUsText1.objects.create(
            heading=request.POST.get('heading'),
            content=request.POST.get('content'),
            is_active=is_active
        )
        messages.success(request, 'About Us text 1 created successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_text1_edit(request, pk):
    text = get_object_or_404(AboutUsText1, pk=pk)
    
    if request.method == 'POST':
        text.heading = request.POST.get('heading')
        text.content = request.POST.get('content')
        is_active = request.POST.get('is_active') == 'on'
        
        if is_active:
            AboutUsText1.objects.exclude(pk=pk).update(is_active=False)
        text.is_active = is_active
        text.save()
        messages.success(request, 'About Us text 1 updated successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_text1_delete(request, pk):
    text = get_object_or_404(AboutUsText1, pk=pk)
    text.delete()
    messages.success(request, 'About Us text 1 deleted successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_mission_create(request):
    if request.method == 'POST':
        AboutUsMission.objects.create(
            title=request.POST.get('title'),
            mission_text=request.POST.get('mission_text'),
            icon=request.FILES.get('icon'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'About Us mission created successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_mission_edit(request, pk):
    mission = get_object_or_404(AboutUsMission, pk=pk)
    
    if request.method == 'POST':
        mission.title = request.POST.get('title')
        mission.mission_text = request.POST.get('mission_text')
        mission.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('icon'):
            if mission.icon:
                delete_cloudinary_image(mission.icon)
            mission.icon = request.FILES.get('icon')
        
        mission.save()
        messages.success(request, 'About Us mission updated successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_mission_delete(request, pk):
    mission = get_object_or_404(AboutUsMission, pk=pk)
    if mission.icon:
        delete_cloudinary_image(mission.icon)
    mission.delete()
    messages.success(request, 'About Us mission deleted successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_text2_create(request):
    if request.method == 'POST':
        is_active = request.POST.get('is_active') == 'on'
        if is_active:
            AboutUsText2.objects.all().update(is_active=False)
        
        AboutUsText2.objects.create(
            heading=request.POST.get('heading'),
            content=request.POST.get('content'),
            is_active=is_active
        )
        messages.success(request, 'About Us text 2 created successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_text2_edit(request, pk):
    text = get_object_or_404(AboutUsText2, pk=pk)
    
    if request.method == 'POST':
        text.heading = request.POST.get('heading')
        text.content = request.POST.get('content')
        is_active = request.POST.get('is_active') == 'on'
        
        if is_active:
            AboutUsText2.objects.exclude(pk=pk).update(is_active=False)
        text.is_active = is_active
        text.save()
        messages.success(request, 'About Us text 2 updated successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_text2_delete(request, pk):
    text = get_object_or_404(AboutUsText2, pk=pk)
    text.delete()
    messages.success(request, 'About Us text 2 deleted successfully!')
    return redirect('aboutus_page')


@login_required
def aboutus_digital_marketing_update(request):
    aboutus_dm = AboutUsDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')
        meta_keywords = request.POST.get('meta_keywords')
        is_active = request.POST.get('is_active') == 'on'
        banner_image = request.FILES.get('banner_image')
        
        if aboutus_dm:
            old_image = aboutus_dm.banner_image
            aboutus_dm.meta_title = meta_title
            aboutus_dm.meta_description = meta_description
            aboutus_dm.meta_keywords = meta_keywords
            aboutus_dm.is_active = is_active
            if banner_image:
                if old_image:
                    delete_cloudinary_image(old_image)
                aboutus_dm.banner_image = banner_image
            aboutus_dm.save()
            messages.success(request, 'About Us SEO settings updated successfully!')
        else:
            AboutUsDigitalMarketing.objects.create(
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keywords=meta_keywords,
                is_active=is_active,
                banner_image=banner_image
            )
            messages.success(request, 'About Us SEO settings created successfully!')
    
    return redirect('aboutus_page')


# ==================== SERVICES SECTION ====================

@login_required
def service_management(request):
    services = Service.objects.all()
    service_names = ServiceName.objects.all().prefetch_related('subservices')
    digital_marketing_list = ServiceDigitalMarketing.objects.order_by('-created_at').all()
    
    context = {
        'services': services,
        'service_names': service_names,
        'service_count': services.count(),
        'service_name_count': service_names.count(),
        'subservice_count': Subservice.objects.count(),
        'digital_marketing_list': digital_marketing_list,
        'digital_marketing_count': digital_marketing_list.count(),
    }
    return render(request, 'service_management.html', context)


@login_required
def service_create(request):
    if request.method == 'POST':
        Service.objects.create(
            banner_description_title=request.POST.get('banner_description_title'),
            banner_description=request.POST.get('banner_description'),
            image=request.FILES.get('image')
        )
        messages.success(request, 'Service banner created successfully!')
    return redirect('service_management')


@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    
    if request.method == 'POST':
        service.banner_description_title = request.POST.get('banner_description_title')
        service.banner_description = request.POST.get('banner_description')
        
        if request.FILES.get('image'):
            if service.image:
                delete_cloudinary_image(service.image)
            service.image = request.FILES.get('image')
        
        service.save()
        messages.success(request, 'Service banner updated successfully!')
    return redirect('service_management')


@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if service.image:
        delete_cloudinary_image(service.image)
    service.delete()
    messages.success(request, 'Service banner deleted successfully!')
    return redirect('service_management')


@login_required
def service_name_create(request):
    if request.method == 'POST':
        ServiceName.objects.create(
            service_name=request.POST.get('service_name'),
            service_description=request.POST.get('service_description'),
            service_image=request.FILES.get('service_image')
        )
        messages.success(request, 'Service created successfully!')
    return redirect('service_management')


@login_required
def service_name_edit(request, pk):
    service_name = get_object_or_404(ServiceName, pk=pk)
    
    if request.method == 'POST':
        service_name.service_name = request.POST.get('service_name')
        service_name.service_description = request.POST.get('service_description')
        
        if request.FILES.get('service_image'):
            if service_name.service_image:
                delete_cloudinary_image(service_name.service_image)
            service_name.service_image = request.FILES.get('service_image')
        
        service_name.save()
        messages.success(request, 'Service updated successfully!')
    return redirect('service_management')


@login_required
def service_name_delete(request, pk):
    service_name = get_object_or_404(ServiceName, pk=pk)
    if service_name.service_image:
        delete_cloudinary_image(service_name.service_image)
    service_name.delete()
    messages.success(request, 'Service deleted successfully!')
    return redirect('service_management')


@login_required
def subservice_create(request):
    if request.method == 'POST':
        service_heading = get_object_or_404(ServiceName, pk=request.POST.get('service_heading'))
        Subservice.objects.create(
            service_heading=service_heading,
            subservice_name=request.POST.get('subservice_name'),
            subservice_title=request.POST.get('subservice_title'),
            subservice_description=request.POST.get('subservice_description'),
            sub_service_image=request.FILES.get('sub_service_image')
        )
        messages.success(request, 'Subservice created successfully!')
    return redirect('service_management')


@login_required
def subservice_edit(request, pk):
    subservice = get_object_or_404(Subservice, pk=pk)
    
    if request.method == 'POST':
        subservice.service_heading = get_object_or_404(ServiceName, pk=request.POST.get('service_heading'))
        subservice.subservice_name = request.POST.get('subservice_name')
        subservice.subservice_title = request.POST.get('subservice_title')
        subservice.subservice_description = request.POST.get('subservice_description')
        
        if request.FILES.get('sub_service_image'):
            if subservice.sub_service_image:
                delete_cloudinary_image(subservice.sub_service_image)
            subservice.sub_service_image = request.FILES.get('sub_service_image')
        
        subservice.save()
        messages.success(request, 'Subservice updated successfully!')
    return redirect('service_management')


@login_required
def subservice_delete(request, pk):
    subservice = get_object_or_404(Subservice, pk=pk)
    if subservice.sub_service_image:
        delete_cloudinary_image(subservice.sub_service_image)
    subservice.delete()
    messages.success(request, 'Subservice deleted successfully!')
    return redirect('service_management')


@login_required
def service_digital_marketing_create(request):
    if request.method == 'POST':
        ServiceDigitalMarketing.objects.create(
            meta_title=request.POST.get('meta_title'),
            meta_description=request.POST.get('meta_description'),
            meta_keywords=request.POST.get('meta_keywords'),
            banner_image=request.FILES.get('banner_image'),
            is_active=request.POST.get('is_active') == "on"
        )
        messages.success(request, "Digital Marketing section created!")
    return redirect('service_management')


@login_required
def service_digital_marketing_edit(request, pk):
    dm = get_object_or_404(ServiceDigitalMarketing, pk=pk)

    if request.method == 'POST':
        dm.meta_title = request.POST.get('meta_title')
        dm.meta_description = request.POST.get('meta_description')
        dm.meta_keywords = request.POST.get('meta_keywords')
        dm.is_active = request.POST.get('is_active') == "on"

        if request.FILES.get('banner_image'):
            if dm.banner_image:
                delete_cloudinary_image(dm.banner_image)
            dm.banner_image = request.FILES.get('banner_image')

        dm.save()
        messages.success(request, "Digital Marketing section updated!")
    return redirect('service_management')


@login_required
def service_digital_marketing_delete(request, pk):
    dm = get_object_or_404(ServiceDigitalMarketing, pk=pk)
    if dm.banner_image:
        delete_cloudinary_image(dm.banner_image)
    dm.delete()
    messages.success(request, "Digital Marketing section deleted!")
    return redirect('service_management')


# ==================== SOLUTIONS SECTION ====================

@login_required
def solutions_management(request):
    solutions = Solutions.objects.all()
    solutions_names = SolutionsName.objects.all().prefetch_related('solutions')
    digital_marketing_list = solutionsDigitalMarketing.objects.order_by('-created_at').all()
    
    context = {
        'solutions': solutions,
        'solutions_names': solutions_names,
        'solutions_count': solutions.count(),
        'solutions_name_count': solutions_names.count(),
        'subsolutions_count': Subsolutions.objects.count(),
        'digital_marketing_list': digital_marketing_list,
        'digital_marketing_count': digital_marketing_list.count(),
    }
    return render(request, 'solutions_management.html', context)


@login_required
def solutions_create(request):
    if request.method == 'POST':
        Solutions.objects.create(
            banner_description_title=request.POST.get('banner_description_title'),
            banner_description=request.POST.get('banner_description'),
            image=request.FILES.get('image')
        )
        messages.success(request, 'Solutions banner created successfully!')
    return redirect('solutions_management')


@login_required
def solutions_edit(request, pk):
    solution = get_object_or_404(Solutions, pk=pk)
    
    if request.method == 'POST':
        solution.banner_description_title = request.POST.get('banner_description_title')
        solution.banner_description = request.POST.get('banner_description')
        
        if request.FILES.get('image'):
            if solution.image:
                delete_cloudinary_image(solution.image)
            solution.image = request.FILES.get('image')
        
        solution.save()
        messages.success(request, 'Solutions banner updated successfully!')
    return redirect('solutions_management')


@login_required
def solutions_delete(request, pk):
    solution = get_object_or_404(Solutions, pk=pk)
    if solution.image:
        delete_cloudinary_image(solution.image)
    solution.delete()
    messages.success(request, 'Solutions banner deleted successfully!')
    return redirect('solutions_management')


@login_required
def solutions_name_create(request):
    if request.method == 'POST':
        SolutionsName.objects.create(
            solutions_name=request.POST.get('solutions_name'),
            solutions_description=request.POST.get('solutions_description'),
            solutions_image=request.FILES.get('solutions_image')
        )
        messages.success(request, 'Solution created successfully!')
    return redirect('solutions_management')


@login_required
def solutions_name_edit(request, pk):
    solutions_name = get_object_or_404(SolutionsName, pk=pk)
    
    if request.method == 'POST':
        solutions_name.solutions_name = request.POST.get('solutions_name')
        solutions_name.solutions_description = request.POST.get('solutions_description')
        
        if request.FILES.get('solutions_image'):
            if solutions_name.solutions_image:
                delete_cloudinary_image(solutions_name.solutions_image)
            solutions_name.solutions_image = request.FILES.get('solutions_image')
        
        solutions_name.save()
        messages.success(request, 'Solution updated successfully!')
    return redirect('solutions_management')


@login_required
def solutions_name_delete(request, pk):
    solutions_name = get_object_or_404(SolutionsName, pk=pk)
    if solutions_name.solutions_image:
        delete_cloudinary_image(solutions_name.solutions_image)
    solutions_name.delete()
    messages.success(request, 'Solution deleted successfully!')
    return redirect('solutions_management')


@login_required
def subsolutions_create(request):
    if request.method == 'POST':
        solutions_heading = get_object_or_404(SolutionsName, pk=request.POST.get('solutions_heading'))
        Subsolutions.objects.create(
            solutions_heading=solutions_heading,
            solutions_name=request.POST.get('solutions_name'),
            solutions_title=request.POST.get('solutions_title'),
            solutions_description=request.POST.get('solutions_description'),
            solutions_image=request.FILES.get('solutions_image')
        )
        messages.success(request, 'Subsolution created successfully!')
    return redirect('solutions_management')


@login_required
def subsolutions_edit(request, pk):
    subsolution = get_object_or_404(Subsolutions, pk=pk)
    
    if request.method == 'POST':
        subsolution.solutions_heading = get_object_or_404(SolutionsName, pk=request.POST.get('solutions_heading'))
        subsolution.solutions_name = request.POST.get('solutions_name')
        subsolution.solutions_title = request.POST.get('solutions_title')
        subsolution.solutions_description = request.POST.get('solutions_description')
        
        if request.FILES.get('solutions_image'):
            if subsolution.solutions_image:
                delete_cloudinary_image(subsolution.solutions_image)
            subsolution.solutions_image = request.FILES.get('solutions_image')
        
        subsolution.save()
        messages.success(request, 'Subsolution updated successfully!')
    return redirect('solutions_management')


@login_required
def subsolutions_delete(request, pk):
    subsolution = get_object_or_404(Subsolutions, pk=pk)
    if subsolution.solutions_image:
        delete_cloudinary_image(subsolution.solutions_image)
    subsolution.delete()
    messages.success(request, 'Subsolution deleted successfully!')
    return redirect('solutions_management')


@login_required
def solutions_digital_marketing_create(request):
    if request.method == 'POST':
        solutionsDigitalMarketing.objects.create(
            meta_title=request.POST.get('meta_title'),
            meta_description=request.POST.get('meta_description'),
            meta_keywords=request.POST.get('meta_keywords'),
            banner_image=request.FILES.get('banner_image'),
            is_active=request.POST.get('is_active') == "on"
        )
        messages.success(request, "Solutions Digital Marketing section created!")
    return redirect('solutions_management')


@login_required
def solutions_digital_marketing_edit(request, pk):
    dm = get_object_or_404(solutionsDigitalMarketing, pk=pk)

    if request.method == 'POST':
        dm.meta_title = request.POST.get('meta_title')
        dm.meta_description = request.POST.get('meta_description')
        dm.meta_keywords = request.POST.get('meta_keywords')
        dm.is_active = request.POST.get('is_active') == "on"

        if request.FILES.get('banner_image'):
            if dm.banner_image:
                delete_cloudinary_image(dm.banner_image)
            dm.banner_image = request.FILES.get('banner_image')

        dm.save()
        messages.success(request, "Solutions Digital Marketing section updated!")
    return redirect('solutions_management')


@login_required
def solutions_digital_marketing_delete(request, pk):
    dm = get_object_or_404(solutionsDigitalMarketing, pk=pk)
    if dm.banner_image:
        delete_cloudinary_image(dm.banner_image)
    dm.delete()
    messages.success(request, "Solutions Digital Marketing section deleted!")
    return redirect('solutions_management')
# ==================== OUR WORKS SECTION ====================

@login_required
def ourwork_page(request):
    ourworks = OurWorks.objects.all().order_by('-created_at')
    industries = Industry.objects.all().order_by('name')
    expertise = Expertise.objects.all().order_by('name')
    
    context = {
        'ourworks': ourworks,
        'ourworks_count': ourworks.count(),
        'industries': industries,
        'industries_count': industries.count(),
        'expertise': expertise,
        'expertise_count': expertise.count(),
    }
    return render(request, 'ourworks.html', context)


@login_required
def ourwork_create(request):
    if request.method == 'POST':
        industry_id = request.POST.get('industry')
        expertise_id = request.POST.get('expertise')
        
        OurWorks.objects.create(
            banner_image=request.FILES.get('banner_image'),
            banner_heading=request.POST.get('banner_heading'),
            banner_description=request.POST.get('banner_description'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            image=request.FILES.get('image'),
            industry=get_object_or_404(Industry, pk=industry_id) if industry_id else None,
            expertise=get_object_or_404(Expertise, pk=expertise_id) if expertise_id else None,
            language=request.POST.get('language'),
            time_scale=request.POST.get('time_scale'),
            launch_date=request.POST.get('launch_date'),
            system=request.POST.get('system'),
            banner2_image=request.FILES.get('banner2_image'),
            banner2_title=request.POST.get('banner2_title'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Our Work created successfully!')
    return redirect('ourwork_page')


@login_required
def ourwork_edit(request, pk):
    work = get_object_or_404(OurWorks, pk=pk)
    old_work_image = work.image
    old_banner_image = work.banner_image
    old_banner2_image = work.banner2_image

    if request.method == 'POST':
        work.banner_heading = request.POST.get('banner_heading')
        work.banner_description = request.POST.get('banner_description')
        work.title = request.POST.get('title')
        work.description = request.POST.get('description')
        work.is_active = request.POST.get('is_active') == 'on'
        
        industry_id = request.POST.get('industry')
        expertise_id = request.POST.get('expertise')
        work.industry = get_object_or_404(Industry, pk=industry_id) if industry_id else None
        work.expertise = get_object_or_404(Expertise, pk=expertise_id) if expertise_id else None
        
        work.language = request.POST.get('language')
        work.time_scale = request.POST.get('time_scale')
        work.launch_date = request.POST.get('launch_date')
        work.system = request.POST.get('system')
        work.banner2_title = request.POST.get('banner2_title')

        if request.FILES.get('banner_image'):
            if old_banner_image:
                delete_cloudinary_image(old_banner_image)
            work.banner_image = request.FILES.get('banner_image')

        if request.FILES.get('image'):
            if old_work_image:
                delete_cloudinary_image(old_work_image)
            work.image = request.FILES.get('image')

        if request.FILES.get('banner2_image'):
            if old_banner2_image:
                delete_cloudinary_image(old_banner2_image)
            work.banner2_image = request.FILES.get('banner2_image')

        work.save()
        messages.success(request, 'Our Work updated successfully!')
    return redirect('ourwork_page')


@login_required
def ourwork_delete(request, pk):
    work = get_object_or_404(OurWorks, pk=pk)
    
    if work.image:
        delete_cloudinary_image(work.image)
    if work.banner_image:
        delete_cloudinary_image(work.banner_image)
    if work.banner2_image:
        delete_cloudinary_image(work.banner2_image)
    
    work.delete()
    messages.success(request, 'Our Work deleted successfully!')
    return redirect('ourwork_page')
# ==================== OUR WORK SECTION 2 CRUD ====================

@login_required
def ourwork_section2_page(request):
    """Main page to manage all Section 2 entries"""
    sections = OurWorkSection2.objects.all().select_related('ourwork').order_by('-created_at')
    ourworks = OurWorks.objects.all().order_by('title')
    
    context = {
        'sections': sections,
        'sections_count': sections.count(),
        'ourworks': ourworks,
    }
    return render(request, 'ourwork_section2.html', context)


@login_required
def ourwork_section2_create(request):
    """Create Section 2"""
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        work = get_object_or_404(OurWorks, pk=work_id)
        
        OurWorkSection2.objects.create(
            ourwork=work,
            image=request.FILES.get('image'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            corporate_clients=request.POST.get('corporate_clients', '100+'),
            custom_designs=request.POST.get('custom_designs', '500+'),
            years_experience=request.POST.get('years_experience', '10+'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Section 2 created successfully!')
    return redirect('ourwork_section2_page')


@login_required
def ourwork_section2_edit(request, pk):
    """Edit Section 2"""
    section = get_object_or_404(OurWorkSection2, pk=pk)
    old_image = section.image
    
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        section.ourwork = get_object_or_404(OurWorks, pk=work_id)
        section.title = request.POST.get('title')
        section.description = request.POST.get('description')
        section.corporate_clients = request.POST.get('corporate_clients', '100+')
        section.custom_designs = request.POST.get('custom_designs', '500+')
        section.years_experience = request.POST.get('years_experience', '10+')
        section.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('image'):
            if old_image:
                delete_cloudinary_image(old_image)
            section.image = request.FILES.get('image')
        
        section.save()
        messages.success(request, 'Section 2 updated successfully!')
    return redirect('ourwork_section2_page')


@login_required
def ourwork_section2_delete(request, pk):
    """Delete Section 2"""
    section = get_object_or_404(OurWorkSection2, pk=pk)
    
    if section.image:
        delete_cloudinary_image(section.image)
    
    section.delete()
    messages.success(request, 'Section 2 deleted successfully!')
    return redirect('ourwork_section2_page')


# ==================== PROJECT GOALS CRUD ====================

@login_required
def project_goals_page(request):
    """Main page to manage all Project Goals"""
    sections = ProjectGoalsSection.objects.all().select_related('ourwork').prefetch_related('goals').order_by('-created_at')
    ourworks = OurWorks.objects.all().order_by('title')
    
    context = {
        'sections': sections,
        'sections_count': sections.count(),
        'ourworks': ourworks,
    }
    return render(request, 'project_goals.html', context)


@login_required
def project_goals_section_create(request):
    """Create Project Goals Section"""
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        work = get_object_or_404(OurWorks, pk=work_id)
        
        ProjectGoalsSection.objects.create(
            ourwork=work,
            main_heading=request.POST.get('main_heading', 'PROJECT GOALS'),
            main_title=request.POST.get('main_title', 'Objectives'),
            main_description=request.POST.get('main_description'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Project Goals Section created successfully!')
    return redirect('project_goals_page')


@login_required
def project_goals_section_edit(request, pk):
    """Edit Project Goals Section"""
    section = get_object_or_404(ProjectGoalsSection, pk=pk)
    
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        section.ourwork = get_object_or_404(OurWorks, pk=work_id)
        section.main_heading = request.POST.get('main_heading', 'PROJECT GOALS')
        section.main_title = request.POST.get('main_title', 'Objectives')
        section.main_description = request.POST.get('main_description')
        section.is_active = request.POST.get('is_active') == 'on'
        section.save()
        messages.success(request, 'Project Goals Section updated successfully!')
    return redirect('project_goals_page')


@login_required
def project_goals_section_delete(request, pk):
    """Delete Project Goals Section"""
    section = get_object_or_404(ProjectGoalsSection, pk=pk)
    section.delete()
    messages.success(request, 'Project Goals Section deleted successfully!')
    return redirect('project_goals_page')


# ==================== INDIVIDUAL GOALS CRUD ====================

@login_required
def project_goal_create(request):
    """Create Individual Goal"""
    if request.method == 'POST':
        section_id = request.POST.get('section')
        section = get_object_or_404(ProjectGoalsSection, pk=section_id)
        
        ProjectGoal.objects.create(
            section=section,
            heading=request.POST.get('heading'),
            description=request.POST.get('description'),
            display_order=request.POST.get('display_order', 0),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Goal added successfully!')
    return redirect('project_goals_page')


@login_required
def project_goal_edit(request, pk):
    """Edit Individual Goal"""
    goal = get_object_or_404(ProjectGoal, pk=pk)
    
    if request.method == 'POST':
        goal.heading = request.POST.get('heading')
        goal.description = request.POST.get('description')
        goal.display_order = request.POST.get('display_order', 0)
        goal.is_active = request.POST.get('is_active') == 'on'
        goal.save()
        messages.success(request, 'Goal updated successfully!')
    return redirect('project_goals_page')


@login_required
def project_goal_delete(request, pk):
    """Delete Individual Goal"""
    goal = get_object_or_404(ProjectGoal, pk=pk)
    goal.delete()
    messages.success(request, 'Goal deleted successfully!')
    return redirect('project_goals_page')    


# ==================== CHALLENGES / WHAT WE SOLVED CRUD ====================

@login_required
def challenges_page(request):
    """Main page to manage all Challenges"""
    sections = ChallengesSection.objects.all().select_related('ourwork').prefetch_related('challenges').order_by('-created_at')
    ourworks = OurWorks.objects.all().order_by('title')
    
    context = {
        'sections': sections,
        'sections_count': sections.count(),
        'ourworks': ourworks,
    }
    return render(request, 'challenges.html', context)


@login_required
def challenges_section_create(request):
    """Create Challenges Section"""
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        work = get_object_or_404(OurWorks, pk=work_id)
        
        ChallengesSection.objects.create(
            ourwork=work,
            banner_image=request.FILES.get('banner_image'),
            main_heading=request.POST.get('main_heading', 'WHAT WE SOLVED'),
            main_title=request.POST.get('main_title', 'Challenges'),
            main_description=request.POST.get('main_description'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Challenges Section created successfully!')
    return redirect('challenges_page')


@login_required
def challenges_section_edit(request, pk):
    """Edit Challenges Section"""
    section = get_object_or_404(ChallengesSection, pk=pk)
    old_image = section.banner_image
    
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        section.ourwork = get_object_or_404(OurWorks, pk=work_id)
        section.main_heading = request.POST.get('main_heading', 'WHAT WE SOLVED')
        section.main_title = request.POST.get('main_title', 'Challenges')
        section.main_description = request.POST.get('main_description')
        section.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('banner_image'):
            if old_image:
                delete_cloudinary_image(old_image)
            section.banner_image = request.FILES.get('banner_image')
        
        section.save()
        messages.success(request, 'Challenges Section updated successfully!')
    return redirect('challenges_page')


@login_required
def challenges_section_delete(request, pk):
    """Delete Challenges Section"""
    section = get_object_or_404(ChallengesSection, pk=pk)
    
    if section.banner_image:
        delete_cloudinary_image(section.banner_image)
    
    section.delete()
    messages.success(request, 'Challenges Section deleted successfully!')
    return redirect('challenges_page')


# ==================== INDIVIDUAL CHALLENGES CRUD ====================

@login_required
def challenge_create(request):
    """Create Individual Challenge"""
    if request.method == 'POST':
        section_id = request.POST.get('section')
        section = get_object_or_404(ChallengesSection, pk=section_id)
        
        Challenge.objects.create(
            section=section,
            heading=request.POST.get('heading'),
            description=request.POST.get('description'),
            display_order=request.POST.get('display_order', 0),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Challenge added successfully!')
    return redirect('challenges_page')


@login_required
def challenge_edit(request, pk):
    """Edit Individual Challenge"""
    challenge = get_object_or_404(Challenge, pk=pk)
    
    if request.method == 'POST':
        challenge.heading = request.POST.get('heading')
        challenge.description = request.POST.get('description')
        challenge.display_order = request.POST.get('display_order', 0)
        challenge.is_active = request.POST.get('is_active') == 'on'
        
        challenge.save()
        messages.success(request, 'Challenge updated successfully!')
    return redirect('challenges_page')


@login_required
def challenge_delete(request, pk):
    """Delete Individual Challenge"""
    challenge = get_object_or_404(Challenge, pk=pk)
    
    if challenge.image:
        delete_cloudinary_image(challenge.image)
    
    challenge.delete()
    messages.success(request, 'Challenge deleted successfully!')
    return redirect('challenges_page')

# ==================== CREATIVE DIRECTION CRUD ====================

@login_required
def creative_direction_page(request):
    """Main page to manage all Creative Direction sections"""
    sections = CreativeDirectionSection.objects.all().select_related('ourwork').prefetch_related('creative_items').order_by('-created_at')
    ourworks = OurWorks.objects.all().order_by('title')
    
    context = {
        'sections': sections,
        'sections_count': sections.count(),
        'ourworks': ourworks,
    }
    return render(request, 'creative_direction.html', context)


@login_required
def creative_direction_section_create(request):
    """Create Creative Direction Section"""
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        work = get_object_or_404(OurWorks, pk=work_id)
        
        CreativeDirectionSection.objects.create(
            ourwork=work,
            main_title=request.POST.get('main_title'),
            main_description=request.POST.get('main_description'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Creative Direction Section created successfully!')
    return redirect('creative_direction_page')


@login_required
def creative_direction_section_edit(request, pk):
    """Edit Creative Direction Section"""
    section = get_object_or_404(CreativeDirectionSection, pk=pk)
    
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        section.ourwork = get_object_or_404(OurWorks, pk=work_id)
        section.main_title = request.POST.get('main_title')
        section.main_description = request.POST.get('main_description')
        section.is_active = request.POST.get('is_active') == 'on'
        section.save()
        messages.success(request, 'Creative Direction Section updated successfully!')
    return redirect('creative_direction_page')


@login_required
def creative_direction_section_delete(request, pk):
    """Delete Creative Direction Section"""
    section = get_object_or_404(CreativeDirectionSection, pk=pk)
    section.delete()
    messages.success(request, 'Creative Direction Section deleted successfully!')
    return redirect('creative_direction_page')


# ==================== INDIVIDUAL CREATIVE ITEMS CRUD ====================

@login_required
def creative_item_create(request):
    """Create Individual Creative Item"""
    if request.method == 'POST':
        section_id = request.POST.get('section')
        section = get_object_or_404(CreativeDirectionSection, pk=section_id)
        
        CreativeItem.objects.create(
            section=section,
            image=request.FILES.get('image'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            display_order=request.POST.get('display_order', 0),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Creative Item added successfully!')
    return redirect('creative_direction_page')


@login_required
def creative_item_edit(request, pk):
    """Edit Individual Creative Item"""
    item = get_object_or_404(CreativeItem, pk=pk)
    old_image = item.image
    
    if request.method == 'POST':
        item.title = request.POST.get('title')
        item.description = request.POST.get('description')
        item.display_order = request.POST.get('display_order', 0)
        item.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('image'):
            if old_image:
                delete_cloudinary_image(old_image)
            item.image = request.FILES.get('image')
        
        item.save()
        messages.success(request, 'Creative Item updated successfully!')
    return redirect('creative_direction_page')


@login_required
def creative_item_delete(request, pk):
    """Delete Individual Creative Item"""
    item = get_object_or_404(CreativeItem, pk=pk)
    
    if item.image:
        delete_cloudinary_image(item.image)
    
    item.delete()
    messages.success(request, 'Creative Item deleted successfully!')
    return redirect('creative_direction_page')    



# ==================== MOBILE SECTION CRUD ====================

@login_required
def mobile_section_page(request):
    """Main page to manage all Mobile Sections"""
    sections = MobileSection.objects.all().select_related('ourwork').order_by('-created_at')
    ourworks = OurWorks.objects.all().order_by('title')
    
    context = {
        'sections': sections,
        'sections_count': sections.count(),
        'ourworks': ourworks,
    }
    return render(request, 'mobile_section.html', context)


@login_required
def mobile_section_create(request):
    """Create Mobile Section"""
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        work = get_object_or_404(OurWorks, pk=work_id)
        
        MobileSection.objects.create(
            ourwork=work,
            label=request.POST.get('label', 'INTERACTIVE EXPERIENCE'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            mobile_image_1=request.FILES.get('mobile_image_1'),
            mobile_image_2=request.FILES.get('mobile_image_2'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Mobile Section created successfully!')
    return redirect('mobile_section_page')


@login_required
def mobile_section_edit(request, pk):
    """Edit Mobile Section"""
    section = get_object_or_404(MobileSection, pk=pk)
    old_image_1 = section.mobile_image_1
    old_image_2 = section.mobile_image_2
    
    if request.method == 'POST':
        work_id = request.POST.get('ourwork')
        section.ourwork = get_object_or_404(OurWorks, pk=work_id)
        section.label = request.POST.get('label', 'INTERACTIVE EXPERIENCE')
        section.title = request.POST.get('title')
        section.description = request.POST.get('description')
        section.is_active = request.POST.get('is_active') == 'on'
        
        # Handle mobile_image_1
        if request.FILES.get('mobile_image_1'):
            if old_image_1:
                delete_cloudinary_image(old_image_1)
            section.mobile_image_1 = request.FILES.get('mobile_image_1')
        
        # Handle mobile_image_2
        if request.FILES.get('mobile_image_2'):
            if old_image_2:
                delete_cloudinary_image(old_image_2)
            section.mobile_image_2 = request.FILES.get('mobile_image_2')
        
        section.save()
        messages.success(request, 'Mobile Section updated successfully!')
    return redirect('mobile_section_page')


@login_required
def mobile_section_delete(request, pk):
    """Delete Mobile Section"""
    section = get_object_or_404(MobileSection, pk=pk)
    
    if section.mobile_image_1:
        delete_cloudinary_image(section.mobile_image_1)
    if section.mobile_image_2:
        delete_cloudinary_image(section.mobile_image_2)
    
    section.delete()
    messages.success(request, 'Mobile Section deleted successfully!')
    return redirect('mobile_section_page')    
# ==================== OUR WORKS DIGITAL MARKETING SECTION ====================    

@login_required
def ourworks_digital_marketing_page(request):
    digital_marketing = OurWorksDigitalMarketing.objects.first()
    context = {'digital_marketing': digital_marketing}
    return render(request, 'ourworksdigitalmarketing.html', context)


@login_required
def ourworks_digital_marketing_update(request):
    marketing = OurWorksDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        old_image = marketing.banner_image if marketing else None
        
        if marketing:
            form = OurWorksDigitalMarketingForm(request.POST, request.FILES, instance=marketing)
        else:
            form = OurWorksDigitalMarketingForm(request.POST, request.FILES)
        
        if form.is_valid():
            if 'banner_image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Our Works SEO / Digital Marketing settings updated successfully!')
    
    return redirect('ourworks_digital_marketing_page')


@login_required
def industry_create(request):
    if request.method == 'POST':
        Industry.objects.create(
            name=request.POST.get('name'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Industry created successfully!')
    return redirect('ourwork_page')


@login_required
def industry_edit(request, pk):
    industry = get_object_or_404(Industry, pk=pk)
    
    if request.method == 'POST':
        industry.name = request.POST.get('name')
        industry.is_active = request.POST.get('is_active') == 'on'
        industry.save()
        messages.success(request, 'Industry updated successfully!')
    return redirect('ourwork_page')


@login_required
def industry_delete(request, pk):
    industry = get_object_or_404(Industry, pk=pk)
    industry.delete()
    messages.success(request, 'Industry deleted successfully!')
    return redirect('ourwork_page')


@login_required
def expertise_create(request):
    if request.method == 'POST':
        Expertise.objects.create(
            name=request.POST.get('name'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Expertise created successfully!')
    return redirect('ourwork_page')


@login_required
def expertise_edit(request, pk):
    expertise = get_object_or_404(Expertise, pk=pk)
    
    if request.method == 'POST':
        expertise.name = request.POST.get('name')
        expertise.is_active = request.POST.get('is_active') == 'on'
        expertise.save()
        messages.success(request, 'Expertise updated successfully!')
    return redirect('ourwork_page')


@login_required
def expertise_delete(request, pk):
    expertise = get_object_or_404(Expertise, pk=pk)
    expertise.delete()
    messages.success(request, 'Expertise deleted successfully!')
    return redirect('ourwork_page')


# ==================== INSIGHTS SECTION ====================

@login_required
def insights_page(request):
    insights = Insights.objects.all().order_by('-created_at')
    context = {'insights': insights, 'insights_count': insights.count()}
    return render(request, 'insights.html', context)


@login_required
def insights_create(request):
    if request.method == 'POST':
        OurInsights.objects.create(
            category=request.POST.get('category') or None,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            services=request.POST.get('services'),
            insight_date=request.POST.get('insight_date'),
            image=request.FILES.get('image'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Insight created successfully!')
    return redirect('insights_page')


@login_required
def insights_edit(request, pk):
    insight = get_object_or_404(Insights, pk=pk)
    old_image = insight.banner_image
    
    if request.method == 'POST':
        insight.title = request.POST.get('title')
        insight.subtitle = request.POST.get('subtitle')
        insight.description = request.POST.get('description')
        is_active = request.POST.get('is_active') == 'on'
        
        if is_active:
            Insights.objects.exclude(pk=pk).update(is_active=False)
        insight.is_active = is_active
        
        if request.FILES.get('banner_image'):
            if old_image:
                delete_cloudinary_image(old_image)
            insight.banner_image = request.FILES.get('banner_image')
        
        insight.save()
        messages.success(request, 'Insight updated successfully!')
    return redirect('insights_page')


@login_required
def insights_delete(request, pk):
    insight = get_object_or_404(Insights, pk=pk)
    if insight.banner_image:
        delete_cloudinary_image(insight.banner_image)
    insight.delete()
    messages.success(request, 'Insight deleted successfully!')
    return redirect('insights_page')


@login_required
def insights_digital_marketing_page(request):
    digital_marketing = InsightsDigitalMarketing.objects.first()
    context = {'digital_marketing': digital_marketing}
    return render(request, 'insightsdigitalmarketing.html', context)


@login_required
def insights_digital_marketing_update(request):
    marketing = InsightsDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        old_image = marketing.banner_image if marketing else None
        
        if marketing:
            form = InsightsDigitalMarketingForm(request.POST, request.FILES, instance=marketing)
        else:
            form = InsightsDigitalMarketingForm(request.POST, request.FILES)
        
        if form.is_valid():
            if 'banner_image' in request.FILES and old_image:
                delete_cloudinary_image(old_image)
            form.save()
            messages.success(request, 'Insights SEO / Digital Marketing settings updated successfully!')
    
    return redirect('insights_digital_marketing_page')


# ==================== OUR INSIGHTS SECTION ====================

@login_required
def our_insights_page(request):
    our_insights = OurInsights.objects.all().order_by('-created_at')
    context = {'our_insights': our_insights, 'our_insights_count': our_insights.count()}
    return render(request, 'ourinsights.html', context)


@login_required
def our_insights_create(request):
    if request.method == 'POST':
        OurInsights.objects.create(
            category=request.POST.get('category'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            services=request.POST.get('services'),
            image=request.FILES.get('image'),
            insight_date=request.POST.get('insight_date'),
            is_active=request.POST.get('is_active') == 'on'
        )
        messages.success(request, 'Our Insight created successfully!')
    return redirect('our_insights_page')


@login_required
def our_insights_edit(request, pk):
    insight = get_object_or_404(OurInsights, pk=pk)
    old_image = insight.image
    
    if request.method == 'POST':
        insight.category = request.POST.get('category')
        insight.title = request.POST.get('title')
        insight.description = request.POST.get('description')
        insight.services = request.POST.get('services')
        insight.insight_date = request.POST.get('insight_date')
        insight.is_active = request.POST.get('is_active') == 'on'
        
        if request.FILES.get('image'):
            if old_image:
                delete_cloudinary_image(old_image)
            insight.image = request.FILES.get('image')
        
        insight.save()
        messages.success(request, 'Our Insight updated successfully!')
    return redirect('our_insights_page')


@login_required
def our_insights_delete(request, pk):
    insight = get_object_or_404(OurInsights, pk=pk)
    if insight.image:
        delete_cloudinary_image(insight.image)
    insight.delete()
    messages.success(request, 'Our Insight deleted successfully!')
    return redirect('our_insights_page')


# ==================== CHALLENGE SECTION ====================

@login_required
def get_challenge_section(request, insight_id):
    section = InsightChallengeSection.objects.filter(insight_id=insight_id).first()

    if not section:
        return JsonResponse({"exists": False})

    return JsonResponse({
        "exists": True,
        "id": section.id,
        "title": section.title,
        "description": section.description,
        "challenges": list(section.items.values_list("text", flat=True))
    })


@login_required
def save_challenge_section(request, insight_id):
    insight = get_object_or_404(OurInsights, id=insight_id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        challenges = request.POST.getlist("challenges[]")

        # Delete old section
        InsightChallengeSection.objects.filter(insight=insight).delete()

        # Create new section
        section = InsightChallengeSection.objects.create(
            insight=insight,
            title=title,
            description=description
        )

        # Save each challenge
        for ch in challenges:
            if ch.strip():
                InsightChallengeItem.objects.create(section=section, text=ch)

        return redirect('our_insights_page')
    
    return redirect('our_insights_page')