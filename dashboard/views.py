from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from .models import *
from .forms import *



def login_view(request):
    User = get_user_model()

    # Create superuser "aldi" only if it doesn't already exist
    # if not User.objects.filter(username='aldi', is_superuser=True).exists():
    #     username = 'aldi'
    #     email = 'aldi@example.com'
    #     password = 'Admin@123'
    #     User.objects.create_superuser(username=username, email=email, password=password)
    #     print(f"Superuser created -> username: {username}, password: {password}")
    #     print(f"Superuser created -> username: {username}, password: {password}")
    #     print(f"Superuser created -> username: {username}, password: {password}")
    # print(f"already has aldi named super user")
    

    # If user is already logged in, redirect
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
    context = {
        'user': request.user,
    }
    return render(request, 'dashboard.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully')
    return redirect('login')











# ---------------- from claud  ------------------->


# ==================== HOME PAGE ====================
@login_required
def home(request):
    """Home Page Management - List All Content"""
    context = {
        # Existing sections
        'home_banners': HomeBanner.objects.all().order_by('-created_at'),
        'home_text1': HomeText1.objects.all().order_by('-created_at'),
        'home_banner2': HomeBanner2.objects.all().order_by('-created_at'),
        'home_text2': HomeText2.objects.all().order_by('-created_at'),
        'concepts': Conncepts.objects.all().order_by('-created_at'),
        
        # New sections
        'home_banner3': HomeBanner3.objects.all().order_by('-created_at'),
        'home_text3': HomeText3.objects.all().order_by('-created_at'),
        'home_available_works': HomeAvailableWorks.objects.all().order_by('-created_at'),
        'home_banner4': HomeBanner4.objects.all().order_by('-created_at'),
        'home_about_us': HomeAboutUs.objects.all().order_by('-created_at'),
        'home_questions': HomeQuestions.objects.all().order_by('-created_at'),
        'footer': Footer.objects.all().order_by('-created_at'),
        'home_digital_marketing': HomeDigitalMarketing.objects.first(),
        
        # Counts
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
def home_banner_create(request):
    if request.method == 'POST':
        form = HomeBannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Home banner created successfully!')
            return redirect('home')
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
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'Home banner updated successfully!')
            return redirect('home')
    else:
        form = HomeBannerForm(instance=banner)
    return render(request, 'home_banner_form.html', {'form': form, 'action': 'Edit'})


@login_required
def home_banner_delete(request, pk):
    banner = get_object_or_404(HomeBanner, pk=pk)
    
    if banner.image:
        if os.path.isfile(banner.image.path):
            try:
                os.remove(banner.image.path)
            except Exception as e:
                print(f"Error deleting image: {e}")
    
    banner.delete()
    messages.success(request, 'Home banner deleted successfully!')
    return redirect('home')


# ==================== HOME TEXT 1 CRUD ====================
@login_required
def home_text1_create(request):
    if request.method == 'POST':
        form = HomeText1Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section created successfully!')
            return redirect('home')
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
            return redirect('home')
    else:
        form = HomeText1Form(instance=text)
    return render(request, 'home_text_form.html', {'form': form, 'action': 'Edit', 'section': 'Text Section 1'})


@login_required
def home_text1_delete(request, pk):
    text = get_object_or_404(HomeText1, pk=pk)
    text.delete()
    messages.success(request, 'Text section deleted successfully!')
    return redirect('home')


# ==================== HOME BANNER 2 CRUD ====================
@login_required
def home_banner2_create(request):
    if request.method == 'POST':
        form = HomeBanner2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Secondary banner created successfully!')
            return redirect('home')
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
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'Secondary banner updated successfully!')
            return redirect('home')
    else:
        form = HomeBanner2Form(instance=banner)
    return render(request, 'home_banner_form.html', {'form': form, 'action': 'Edit', 'banner_type': 'Secondary'})


@login_required
def home_banner2_delete(request, pk):
    banner = get_object_or_404(HomeBanner2, pk=pk)
    
    if banner.image:
        if os.path.isfile(banner.image.path):
            try:
                os.remove(banner.image.path)
            except Exception as e:
                print(f"Error deleting image: {e}")
    
    banner.delete()
    messages.success(request, 'Secondary banner deleted successfully!')
    return redirect('home')


# ==================== HOME TEXT 2 CRUD ====================
@login_required
def home_text2_create(request):
    if request.method == 'POST':
        form = HomeText2Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section 2 created successfully!')
            return redirect('home')
    else:
        form = HomeText2Form()
    return render(request, 'home_text_form.html', {'form': form, 'action': 'Create', 'section': 'Text Section 2'})


@login_required
def home_text2_edit(request, pk):
    text = get_object_or_404(HomeText2, pk=pk)
    if request.method == 'POST':
        form = HomeText2Form(request.POST, instance=text)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section 2 updated successfully!')
            return redirect('home')
    else:
        form = HomeText2Form(instance=text)
    return render(request, 'home_text_form.html', {'form': form, 'action': 'Edit', 'section': 'Text Section 2'})


@login_required
def home_text2_delete(request, pk):
    text = get_object_or_404(HomeText2, pk=pk)
    text.delete()
    messages.success(request, 'Text section 2 deleted successfully!')
    return redirect('home')


# ==================== CONCEPTS CRUD ====================
@login_required
def concepts_create(request):
    if request.method == 'POST':
        form = ConnceptsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concept created successfully!')
            return redirect('home')
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
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'Concept updated successfully!')
            return redirect('home')
    else:
        form = ConnceptsForm(instance=concept)
    return render(request, 'concepts_form.html', {'form': form, 'action': 'Edit'})


@login_required
def concepts_delete(request, pk):
    concept = get_object_or_404(Conncepts, pk=pk)
    
    if concept.image:
        if os.path.isfile(concept.image.path):
            try:
                os.remove(concept.image.path)
            except Exception as e:
                print(f"Error deleting image: {e}")
    
    concept.delete()
    messages.success(request, 'Concept deleted successfully!')
    return redirect('home')


# ==================== HOME BANNER 3 CRUD ====================
@login_required
def home_banner3_create(request):
    if request.method == 'POST':
        form = HomeBanner3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Home banner 3 created successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_banner3_edit(request, pk):
    banner = get_object_or_404(HomeBanner3, pk=pk)
    old_image = banner.image
    
    if request.method == 'POST':
        form = HomeBanner3Form(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'Home banner 3 updated successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_banner3_delete(request, pk):
    banner = get_object_or_404(HomeBanner3, pk=pk)
    
    if banner.image:
        if os.path.isfile(banner.image.path):
            try:
                os.remove(banner.image.path)
            except Exception as e:
                print(f"Error deleting image: {e}")
    
    banner.delete()
    messages.success(request, 'Home banner 3 deleted successfully!')
    return redirect('home')


# ==================== HOME TEXT 3 CRUD ====================
@login_required
def home_text3_create(request):
    if request.method == 'POST':
        form = HomeText3Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section 3 created successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_text3_edit(request, pk):
    text = get_object_or_404(HomeText3, pk=pk)
    if request.method == 'POST':
        form = HomeText3Form(request.POST, instance=text)
        if form.is_valid():
            form.save()
            messages.success(request, 'Text section 3 updated successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_text3_delete(request, pk):
    text = get_object_or_404(HomeText3, pk=pk)
    text.delete()
    messages.success(request, 'Text section 3 deleted successfully!')
    return redirect('home')


# ==================== HOME AVAILABLE WORKS CRUD ====================
@login_required
def home_available_works_create(request):
    if request.method == 'POST':
        form = HomeAvailableWorksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Available work created successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_available_works_edit(request, pk):
    work = get_object_or_404(HomeAvailableWorks, pk=pk)
    old_image = work.image
    
    if request.method == 'POST':
        form = HomeAvailableWorksForm(request.POST, request.FILES, instance=work)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'Available work updated successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_available_works_delete(request, pk):
    work = get_object_or_404(HomeAvailableWorks, pk=pk)
    
    if work.image:
        if os.path.isfile(work.image.path):
            try:
                os.remove(work.image.path)
            except Exception as e:
                print(f"Error deleting image: {e}")
    
    work.delete()
    messages.success(request, 'Available work deleted successfully!')
    return redirect('home')


# ==================== HOME BANNER 4 CRUD ====================
@login_required
def home_banner4_create(request):
    if request.method == 'POST':
        form = HomeBanner4Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Home banner 4 created successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_banner4_edit(request, pk):
    banner = get_object_or_404(HomeBanner4, pk=pk)
    old_image = banner.image
    
    if request.method == 'POST':
        form = HomeBanner4Form(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'Home banner 4 updated successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_banner4_delete(request, pk):
    banner = get_object_or_404(HomeBanner4, pk=pk)
    
    if banner.image:
        if os.path.isfile(banner.image.path):
            try:
                os.remove(banner.image.path)
            except Exception as e:
                print(f"Error deleting image: {e}")
    
    banner.delete()
    messages.success(request, 'Home banner 4 deleted successfully!')
    return redirect('home')


# ==================== CONTENTS CRUD ====================
@login_required
def contents_create(request):
    if request.method == 'POST':
        form = ContentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Content created successfully!')
            return redirect('home')
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
    return redirect('home')


@login_required
def contents_delete(request, pk):
    content = get_object_or_404(Contents, pk=pk)
    content.delete()
    messages.success(request, 'Content deleted successfully!')
    return redirect('home')


# ==================== HOME ABOUT US CRUD ====================
@login_required
def home_about_us_create(request):
    if request.method == 'POST':
        form = HomeAboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'About Us section created successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_about_us_edit(request, pk):
    about_us = get_object_or_404(HomeAboutUs, pk=pk)
    old_image = about_us.image
    
    if request.method == 'POST':
        form = HomeAboutUsForm(request.POST, request.FILES, instance=about_us)
        if form.is_valid():
            if 'image' in request.FILES and old_image:
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'About Us section updated successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_about_us_delete(request, pk):
    about_us = get_object_or_404(HomeAboutUs, pk=pk)
    
    if about_us.image:
        if os.path.isfile(about_us.image.path):
            try:
                os.remove(about_us.image.path)
            except Exception as e:
                print(f"Error deleting image: {e}")
    
    about_us.delete()
    messages.success(request, 'About Us section deleted successfully!')
    return redirect('home')


# ==================== HOME QUESTIONS CRUD ====================
@login_required
def home_questions_create(request):
    if request.method == 'POST':
        form = HomeQuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ section created successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_questions_edit(request, pk):
    questions = get_object_or_404(HomeQuestions, pk=pk)
    if request.method == 'POST':
        form = HomeQuestionsForm(request.POST, instance=questions)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ section updated successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def home_questions_delete(request, pk):
    questions = get_object_or_404(HomeQuestions, pk=pk)
    questions.delete()
    messages.success(request, 'FAQ section deleted successfully!')
    return redirect('home')


# ==================== QUESTION CRUD ====================
@login_required
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question created successfully!')
            return redirect('home')
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
    return redirect('home')


@login_required
def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    messages.success(request, 'Question deleted successfully!')
    return redirect('home')


# ==================== FOOTER CRUD ====================
@login_required
def footer_create(request):
    if request.method == 'POST':
        form = FooterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Footer created successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def footer_edit(request, pk):
    footer = get_object_or_404(Footer, pk=pk)
    if request.method == 'POST':
        form = FooterForm(request.POST, instance=footer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Footer updated successfully!')
            return redirect('home')
    return redirect('home')


@login_required
def footer_delete(request, pk):
    footer = get_object_or_404(Footer, pk=pk)
    footer.delete()
    messages.success(request, 'Footer deleted successfully!')
    return redirect('home')


# ==================== HOME DIGITAL MARKETING ====================
@login_required
def home_digital_marketing_update(request):
    marketing = HomeDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        if marketing:
            old_image = marketing.banner_image
            form = HomeDigitalMarketingForm(request.POST, request.FILES, instance=marketing)
        else:
            old_image = None
            form = HomeDigitalMarketingForm(request.POST, request.FILES)
        
        if form.is_valid():
            if 'banner_image' in request.FILES and old_image:
                if os.path.isfile(old_image.path):
                    try:
                        os.remove(old_image.path)
                    except Exception as e:
                        print(f"Error deleting old image: {e}")
            
            form.save()
            messages.success(request, 'SEO / Digital Marketing settings updated successfully!')
            return redirect('home')
    
    return redirect('home')






# ======================  contacts ==========================>


# ==================== MAIN CONTACTS PAGE ====================
@login_required
def contacts_page(request):
    """Display all contacts and leads"""
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

# ==================== CONTACTSA CRUD OPERATIONS ====================
@login_required
def contact_sa_create(request):
    """Create new ContactSA"""
    if request.method == 'POST':
        title = request.POST.get('title')
        icon = request.POST.get('icon')
        text = request.POST.get('text')
        
        ContactSA.objects.create(
            title=title,
            icon=icon,
            text=text
        )
        messages.success(request, 'Contact information created successfully!')
        return redirect('contacts_page')
    return redirect('contacts_page')

@login_required
def contact_sa_edit(request, pk):
    """Edit existing ContactSA"""
    contact = get_object_or_404(ContactSA, pk=pk)
    
    if request.method == 'POST':
        contact.title = request.POST.get('title')
        contact.icon = request.POST.get('icon')
        contact.text = request.POST.get('text')
        contact.save()
        
        messages.success(request, 'Contact information updated successfully!')
        return redirect('contacts_page')
    return redirect('contacts_page')

@login_required
def contact_sa_delete(request, pk):
    """Delete ContactSA"""
    contact = get_object_or_404(ContactSA, pk=pk)
    contact.delete()
    messages.success(request, 'Contact information deleted successfully!')
    return redirect('contacts_page')

# ==================== CONTACT DIGITAL MARKETING ====================
@login_required
def contact_digital_marketing_update(request):
    """Create or Update Contact Digital Marketing settings"""
    contact_dm = ContactDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')
        meta_keywords = request.POST.get('meta_keywords')
        is_active = request.POST.get('is_active') == 'on'
        banner_image = request.FILES.get('banner_image')
        
        if contact_dm:
            # Update existing
            contact_dm.meta_title = meta_title
            contact_dm.meta_description = meta_description
            contact_dm.meta_keywords = meta_keywords
            contact_dm.is_active = is_active
            if banner_image:
                contact_dm.banner_image = banner_image
            contact_dm.save()
            messages.success(request, 'Contact SEO settings updated successfully!')
        else:
            # Create new
            ContactDigitalMarketing.objects.create(
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keywords=meta_keywords,
                is_active=is_active,
                banner_image=banner_image
            )
            messages.success(request, 'Contact SEO settings created successfully!')
        
        return redirect('contacts_page')
    return redirect('contacts_page')

# ==================== LEADS CRUD OPERATIONS ====================
@login_required
def leads_create(request):
    """Create new Lead"""
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Leads.objects.create(
            fullname=fullname,
            email=email,
            message=message
        )
        messages.success(request, 'Lead created successfully!')
        return redirect('contacts_page')
    return redirect('contacts_page')

@login_required
def leads_edit(request, pk):
    """Edit existing Lead"""
    lead = get_object_or_404(Leads, pk=pk)
    
    if request.method == 'POST':
        lead.fullname = request.POST.get('fullname')
        lead.email = request.POST.get('email')
        lead.message = request.POST.get('message')
        lead.save()
        
        messages.success(request, 'Lead updated successfully!')
        return redirect('contacts_page')
    return redirect('contacts_page')

@login_required
def leads_delete(request, pk):
    """Delete Lead"""
    lead = get_object_or_404(Leads, pk=pk)
    lead.delete()
    messages.success(request, 'Lead deleted successfully!')
    return redirect('contacts_page')












# ======================  ABOUT US ==========================>

# ==================== MAIN ABOUT US PAGE ====================
@login_required
def aboutus_page(request):
    """Display all about us content"""
    aboutus_banner1 = AboutUsBanner1.objects.all()
    aboutus_text1 = AboutUsText1.objects.all()
    aboutus_mission = AboutUsMission.objects.all()
    aboutus_text2 = AboutUsText2.objects.all()
    aboutus_digital_marketing = AboutUsDigitalMarketing.objects.first()
    
    context = {
        'aboutus_banner1': aboutus_banner1,
        'aboutus_banner1_count': aboutus_banner1.count(),
        'aboutus_text1': aboutus_text1,
        'aboutus_text1_count': aboutus_text1.count(),
        'aboutus_mission': aboutus_mission,
        'aboutus_mission_count': aboutus_mission.count(),
        'aboutus_text2': aboutus_text2,
        'aboutus_text2_count': aboutus_text2.count(),
        'aboutus_digital_marketing': aboutus_digital_marketing,
    }
    return render(request, 'aboutus.html', context)

# ==================== ABOUT US BANNER1 CRUD ====================
@login_required
def aboutus_banner1_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        is_active = request.POST.get('is_active') == 'on'
        
        AboutUsBanner1.objects.create(
            title=title,
            subtitle=subtitle,
            description=description,
            image=image,
            is_active=is_active
        )
        messages.success(request, 'About Us banner created successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_banner1_edit(request, pk):
    banner = get_object_or_404(AboutUsBanner1, pk=pk)
    
    if request.method == 'POST':
        banner.title = request.POST.get('title')
        banner.subtitle = request.POST.get('subtitle')
        banner.description = request.POST.get('description')
        banner.is_active = request.POST.get('is_active') == 'on'
        
        image = request.FILES.get('image')
        if image:
            banner.image = image
        
        banner.save()
        messages.success(request, 'About Us banner updated successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_banner1_delete(request, pk):
    banner = get_object_or_404(AboutUsBanner1, pk=pk)
    banner.delete()
    messages.success(request, 'About Us banner deleted successfully!')
    return redirect('aboutus_page')

# ==================== ABOUT US TEXT1 CRUD ====================
@login_required
def aboutus_text1_create(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        content = request.POST.get('content')
        is_active = request.POST.get('is_active') == 'on'
        
        AboutUsText1.objects.create(
            heading=heading,
            content=content,
            is_active=is_active
        )
        messages.success(request, 'About Us text 1 created successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_text1_edit(request, pk):
    text = get_object_or_404(AboutUsText1, pk=pk)
    
    if request.method == 'POST':
        text.heading = request.POST.get('heading')
        text.content = request.POST.get('content')
        text.is_active = request.POST.get('is_active') == 'on'
        text.save()
        
        messages.success(request, 'About Us text 1 updated successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_text1_delete(request, pk):
    text = get_object_or_404(AboutUsText1, pk=pk)
    text.delete()
    messages.success(request, 'About Us text 1 deleted successfully!')
    return redirect('aboutus_page')

# ==================== ABOUT US MISSION CRUD ====================
@login_required
def aboutus_mission_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        mission_text = request.POST.get('mission_text')
        icon = request.FILES.get('icon')
        is_active = request.POST.get('is_active') == 'on'
        
        AboutUsMission.objects.create(
            title=title,
            mission_text=mission_text,
            icon=icon,
            is_active=is_active
        )
        messages.success(request, 'About Us mission created successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_mission_edit(request, pk):
    mission = get_object_or_404(AboutUsMission, pk=pk)
    
    if request.method == 'POST':
        mission.title = request.POST.get('title')
        mission.mission_text = request.POST.get('mission_text')
        mission.is_active = request.POST.get('is_active') == 'on'
        
        icon = request.FILES.get('icon')
        if icon:
            mission.icon = icon
        
        mission.save()
        messages.success(request, 'About Us mission updated successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_mission_delete(request, pk):
    mission = get_object_or_404(AboutUsMission, pk=pk)
    mission.delete()
    messages.success(request, 'About Us mission deleted successfully!')
    return redirect('aboutus_page')

# ==================== ABOUT US TEXT2 CRUD ====================
@login_required
def aboutus_text2_create(request):
    if request.method == 'POST':
        heading = request.POST.get('heading')
        content = request.POST.get('content')
        is_active = request.POST.get('is_active') == 'on'
        
        AboutUsText2.objects.create(
            heading=heading,
            content=content,
            is_active=is_active
        )
        messages.success(request, 'About Us text 2 created successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_text2_edit(request, pk):
    text = get_object_or_404(AboutUsText2, pk=pk)
    
    if request.method == 'POST':
        text.heading = request.POST.get('heading')
        text.content = request.POST.get('content')
        text.is_active = request.POST.get('is_active') == 'on'
        text.save()
        
        messages.success(request, 'About Us text 2 updated successfully!')
        return redirect('aboutus_page')
    return redirect('aboutus_page')

@login_required
def aboutus_text2_delete(request, pk):
    text = get_object_or_404(AboutUsText2, pk=pk)
    text.delete()
    messages.success(request, 'About Us text 2 deleted successfully!')
    return redirect('aboutus_page')

# ==================== ABOUT US DIGITAL MARKETING ====================
@login_required
def aboutus_digital_marketing_update(request):
    """Create or Update About Us Digital Marketing settings"""
    aboutus_dm = AboutUsDigitalMarketing.objects.first()
    
    if request.method == 'POST':
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')
        meta_keywords = request.POST.get('meta_keywords')
        is_active = request.POST.get('is_active') == 'on'
        banner_image = request.FILES.get('banner_image')
        
        if aboutus_dm:
            # Update existing
            aboutus_dm.meta_title = meta_title
            aboutus_dm.meta_description = meta_description
            aboutus_dm.meta_keywords = meta_keywords
            aboutus_dm.is_active = is_active
            if banner_image:
                aboutus_dm.banner_image = banner_image
            aboutus_dm.save()
            messages.success(request, 'About Us SEO settings updated successfully!')
        else:
            # Create new
            AboutUsDigitalMarketing.objects.create(
                meta_title=meta_title,
                meta_description=meta_description,
                meta_keywords=meta_keywords,
                is_active=is_active,
                banner_image=banner_image
            )
            messages.success(request, 'About Us SEO settings created successfully!')
        
        return redirect('aboutus_page')
    return redirect('aboutus_page')



# ------------------- services-------------------------->

@login_required
def service_management(request):
    """Main service management page"""
    services = Service.objects.all()
    service_names = ServiceName.objects.all().prefetch_related('subservices')
    digital_marketing_list = ServiceDigitalMarketing.objects.order_by('-created_at').all()
    digital_marketing_count = digital_marketing_list.count()
    
    # Count statistics
    service_count = services.count()
    service_name_count = service_names.count()
    subservice_count = Subservice.objects.all().count()
    
    context = {
        'services': services,
        'service_names': service_names,
        'service_count': service_count,
        'service_name_count': service_name_count,
        'subservice_count': subservice_count,
        'digital_marketing_list': digital_marketing_list,
        'digital_marketing_count': digital_marketing_count,
    }
    return render(request, 'service_management.html', context)

# ============= SERVICE BANNER CRUD =============
@login_required
def service_create(request):
    """Create service banner"""
    if request.method == 'POST':
        banner_description_title = request.POST.get('banner_description_title')
        banner_description = request.POST.get('banner_description')
        image = request.FILES.get('image')
        
        Service.objects.create(
            banner_description_title=banner_description_title,
            banner_description=banner_description,
            image=image
        )
        messages.success(request, 'Service banner created successfully!')
        return redirect('service_management')
    return redirect('service_management')

@login_required
def service_edit(request, pk):
    """Edit service banner"""
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.banner_description_title = request.POST.get('banner_description_title')
        service.banner_description = request.POST.get('banner_description')
        
        if request.FILES.get('image'):
            service.image = request.FILES.get('image')
        
        service.save()
        messages.success(request, 'Service banner updated successfully!')
        return redirect('service_management')
    return redirect('service_management')

@login_required
def service_delete(request, pk):
    """Delete service banner"""
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    messages.success(request, 'Service banner deleted successfully!')
    return redirect('service_management')

# ============= SERVICE NAME CRUD =============
@login_required
def service_name_create(request):
    """Create service name"""
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        service_description = request.POST.get('service_description')
        service_image = request.FILES.get('service_image')
        
        ServiceName.objects.create(
            service_name=service_name,
            service_description=service_description,
            service_image=service_image
        )
        messages.success(request, 'Service created successfully!')
        return redirect('service_management')
    return redirect('service_management')

@login_required
def service_name_edit(request, pk):
    """Edit service name"""
    service_name = get_object_or_404(ServiceName, pk=pk)
    if request.method == 'POST':
        service_name.service_name = request.POST.get('service_name')
        service_name.service_description = request.POST.get('service_description')
        
        if request.FILES.get('service_image'):
            service_name.service_image = request.FILES.get('service_image')
        
        service_name.save()
        messages.success(request, 'Service updated successfully!')
        return redirect('service_management')
    return redirect('service_management')

@login_required
def service_name_delete(request, pk):
    """Delete service name"""
    service_name = get_object_or_404(ServiceName, pk=pk)
    service_name.delete()
    messages.success(request, 'Service deleted successfully!')
    return redirect('service_management')

# ============= SUBSERVICE CRUD =============
@login_required
def subservice_create(request):
    """Create subservice"""
    if request.method == 'POST':
        service_heading_id = request.POST.get('service_heading')
        subservice_name = request.POST.get('subservice_name')
        subservice_description = request.POST.get('subservice_description')
        sub_service_image = request.FILES.get('sub_service_image')
        
        service_heading = get_object_or_404(ServiceName, pk=service_heading_id)
        
        Subservice.objects.create(
            service_heading=service_heading,
            subservice_name=subservice_name,
            subservice_description=subservice_description,
            sub_service_image=sub_service_image
        )
        messages.success(request, 'Subservice created successfully!')
        return redirect('service_management')
    return redirect('service_management')

@login_required
def subservice_edit(request, pk):
    """Edit subservice"""
    subservice = get_object_or_404(Subservice, pk=pk)
    if request.method == 'POST':
        service_heading_id = request.POST.get('service_heading')
        subservice.service_heading = get_object_or_404(ServiceName, pk=service_heading_id)
        subservice.subservice_name = request.POST.get('subservice_name')
        subservice.subservice_description = request.POST.get('subservice_description')
        
        if request.FILES.get('sub_service_image'):
            subservice.sub_service_image = request.FILES.get('sub_service_image')
        
        subservice.save()
        messages.success(request, 'Subservice updated successfully!')
        return redirect('service_management')
    return redirect('service_management')

@login_required
def subservice_delete(request, pk):
    """Delete subservice"""
    subservice = get_object_or_404(Subservice, pk=pk)
    subservice.delete()
    messages.success(request, 'Subservice deleted successfully!')
    return redirect('service_management')


@login_required
def digital_marketing_create(request):
    if request.method == 'POST':
        meta_title = request.POST.get('meta_title')
        meta_description = request.POST.get('meta_description')
        meta_keywords = request.POST.get('meta_keywords')
        banner_image = request.FILES.get('banner_image')
        is_active = request.POST.get('is_active') == "on"

        ServiceDigitalMarketing.objects.create(
            meta_title=meta_title,
            meta_description=meta_description,
            meta_keywords=meta_keywords,
            banner_image=banner_image,
            is_active=is_active
        )
        messages.success(request, "Digital Marketing section created!")
        return redirect('service_management')

    return redirect('service_management')

@login_required
def digital_marketing_edit(request, pk):
    dm = get_object_or_404(ServiceDigitalMarketing, pk=pk)

    if request.method == 'POST':
        dm.meta_title = request.POST.get('meta_title')
        dm.meta_description = request.POST.get('meta_description')
        dm.meta_keywords = request.POST.get('meta_keywords')
        dm.is_active = request.POST.get('is_active') == "on"

        if request.FILES.get('banner_image'):
            dm.banner_image = request.FILES.get('banner_image')

        dm.save()
        messages.success(request, "Digital Marketing section updated!")
        return redirect('service_management')

    return redirect('service_management')



@login_required
def digital_marketing_delete(request, pk):
    dm = get_object_or_404(ServiceDigitalMarketing, pk=pk)
    dm.delete()
    messages.success(request, "Digital Marketing section deleted!")
    return redirect('service_management')
