from django.db import models
from cloudinary.models import CloudinaryField

# Note: If you have a base.py with BaseModel, keep that import
# from .base import BaseModel


class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order_number = models.PositiveIntegerField()
    image = CloudinaryField('image', folder='home_images', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Controls the display order on the homepage.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.order_number} - {self.title}"


# ==================== HOME SECTION ====================

class HomeBanner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='banners')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeText1(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeBanner2(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='banners2')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeText2(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Conncepts(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='concepts')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeBanner3(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='banners3')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeText3(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeAvailableWorks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='home_available_works')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeBanner4(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='banners4')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contents(models.Model):
    banner = models.ForeignKey(HomeBanner4, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=200)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeAboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', folder='home_about_us', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeQuestions(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    home_questions = models.ForeignKey(HomeQuestions, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=300)
    answer_text = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question_text
    

class Footer(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class HomeDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = CloudinaryField('image', folder='home_digital_marketing', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Home Page SEO / Marketing"


class HomeVision(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
   

class HomeFeatures(models.Model):
    """Home Features Section"""
    image = CloudinaryField('image', folder='home_features', blank=True, null=True)
    main_feature = models.TextField(blank=True, null=True)
    
    text1 = models.CharField(max_length=200, blank=True, null=True)
    text1_description = models.TextField(blank=True, null=True)
    
    text2 = models.CharField(max_length=200, blank=True, null=True)
    text2_description = models.TextField(blank=True, null=True)
    
    text3 = models.CharField(max_length=200, blank=True, null=True)
    text3_description = models.TextField(blank=True, null=True)
    
    text4 = models.CharField(max_length=200, blank=True, null=True)
    text4_description = models.TextField(blank=True, null=True)
    
    text5 = models.CharField(max_length=200, blank=True, null=True)
    text5_description = models.TextField(blank=True, null=True)
    
    text6 = models.CharField(max_length=200, blank=True, null=True)
    text6_description = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Home Features - {self.id}"


# ==================== CONTACTS SECTION ====================

class ContactSA(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)  
    text = models.TextField()

    def __str__(self):
        return self.title
    

class Leads(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    solution = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
    

class ContactDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = CloudinaryField('image', folder='contact_digital_marketing', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Contact Page SEO / Marketing"


# ==================== ABOUT US SECTION ====================

class AboutUsBanner1(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='about_us/banners')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class AboutUsText1(models.Model):
    heading = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
    

class AboutUsMission(models.Model):
    title = models.CharField(max_length=255)
    mission_text = models.TextField()
    icon = CloudinaryField('image', folder='about_us/mission', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AboutUsText2(models.Model):
    heading = models.CharField(max_length=255)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
    

class AboutUsDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = CloudinaryField('image', folder='about_digital_marketing', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Us Page SEO / Marketing"


# ==================== SERVICES SECTION ====================

class Service(models.Model):
    banner_description_title = models.CharField(max_length=255, blank=True, null=True)
    banner_description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='service_images', blank=True, null=True)

    def __str__(self):
        return self.banner_description_title or "Service"


class ServiceName(models.Model):
    service_name = models.CharField(max_length=255)
    service_description = models.TextField()
    service_image = CloudinaryField('image', folder='service_images')

    def __str__(self):
        return self.service_name


class Subservice(models.Model):
    service_heading = models.ForeignKey(ServiceName, on_delete=models.CASCADE, related_name='subservices')
    subservice_name = models.CharField(max_length=255)
    subservice_title = models.CharField(max_length=255, blank=True, null=True)
    subservice_description = models.TextField(blank=True, null=True)
    sub_service_image = CloudinaryField('image', folder='sub_service_images')

    def __str__(self):
        return self.subservice_name
    
    
class ServiceDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = CloudinaryField('image', folder='service_digital_marketing', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Service Page SEO / Marketing"


# ==================== SOLUTIONS SECTION ====================

class Solutions(models.Model):
    banner_description_title = models.CharField(max_length=255, blank=True, null=True)
    banner_description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', folder='solutions', blank=True, null=True)

    def __str__(self):
        return self.banner_description_title or "Solutions"


class SolutionsName(models.Model):
    solutions_name = models.CharField(max_length=255)
    solutions_description = models.TextField()
    solutions_image = CloudinaryField('image', folder='solutions_name')

    def __str__(self):
        return self.solutions_name


class Subsolutions(models.Model):
    solutions_heading = models.ForeignKey(SolutionsName, on_delete=models.CASCADE, related_name='solutions')
    solutions_name = models.CharField(max_length=255)
    solutions_title = models.CharField(max_length=255, blank=True, null=True)
    solutions_description = models.TextField(blank=True, null=True)
    solutions_image = CloudinaryField('image', folder='subsolutions')

    def __str__(self):
        return self.solutions_name
    
    
class solutionsDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = CloudinaryField('image', folder='solution_digital_marketing', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Solutions Page SEO / Marketing"


# ==================== OUR WORKS SECTION ====================

class Industry(models.Model):
    """Industries for Our Works"""
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Industry"
        verbose_name_plural = "Industries"

    def __str__(self):
        return self.name


class Expertise(models.Model):
    """Expertise for Our Works"""
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Expertise"
        verbose_name_plural = "Expertise"

    def __str__(self):
        return self.name


class OurWorks(models.Model):
    """Our Works Portfolio"""

    # Banner Section
    banner_image = CloudinaryField('image', folder='our_works/banners', null=True, blank=True)
    banner_heading = models.CharField(max_length=255, null=True, blank=True)
    banner_description = models.TextField(null=True, blank=True)

    # Work Details
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', folder='our_works')

    industry = models.ForeignKey(
        'Industry',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='works'
    )
    expertise = models.ForeignKey(
        'Expertise',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='works'
    )

    language = models.CharField(max_length=100, null=True, blank=True)
    time_scale = models.CharField(max_length=100, null=True, blank=True)
    launch_date = models.CharField(max_length=100, null=True, blank=True)
    system = models.CharField(max_length=150, null=True, blank=True)

    # Banner 2
    banner2_image = CloudinaryField('image', folder='our_works/banners', null=True, blank=True)
    banner2_title = models.CharField(max_length=255, null=True, blank=True)

    # Status & Timestamps
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Our Work"
        verbose_name_plural = "Our Works"

    def __str__(self):
        return self.title
# ==================== OUR WORK SECTION 2 ====================

class OurWorkSection2(models.Model):
    """Statistics section for Our Works"""
    ourwork = models.ForeignKey(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='section2_stats'
    )
    image = CloudinaryField('image', folder='our_works/section2', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    corporate_clients = models.CharField(max_length=50, default="100+", help_text="e.g., 100+")
    custom_designs = models.CharField(max_length=50, default="500+", help_text="e.g., 500+")
    years_experience = models.CharField(max_length=50, default="10+", help_text="e.g., 10+")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Our Work Section 2"
        verbose_name_plural = "Our Work Section 2"

    def __str__(self):
        return f"Section 2 - {self.title}"



class OurWorksDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = CloudinaryField('image', folder='ourworks_digital_marketing', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Our Works Page SEO / Marketing"         


# ==================== INSIGHTS SECTION ====================

class Insights(models.Model):
    """Insights/Blog Section"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    banner_image = CloudinaryField('image', folder='insights')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Insight"
        verbose_name_plural = "Insights"

    def __str__(self):
        return self.title    


class InsightsDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = CloudinaryField('image', folder='insights_digital_marketing', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Insights Page SEO / Marketing"      


class OurInsights(models.Model):
    """Our Insights Model"""
    category = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        help_text="e.g., Technology, Business, Marketing"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    services = models.TextField(
        null=True,
        blank=True,
        help_text="Comma separated values. Example: Web Development, SEO, UI/UX Design"
    )
    image = CloudinaryField('image', folder='our_insights')
    insight_date = models.CharField(
        max_length=100,
        help_text="e.g., 6 months, 1 week, 1 year"
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Our Insight"
        verbose_name_plural = "Our Insights"
        ordering = ['-created_at']

    def __str__(self):
        return self.title  


# ==================== CHALLENGE SECTION FOR INSIGHTS ====================

class InsightChallengeSection(models.Model):
    insight = models.ForeignKey(
        OurInsights,
        on_delete=models.CASCADE,
        related_name="challenge_sections"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   

class InsightChallengeItem(models.Model):
    section = models.ForeignKey(
        InsightChallengeSection,
        on_delete=models.CASCADE,
        related_name="items"
    )
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text