from django.db import models
from django.utils.text import slugify
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
    
    # New fields - slug without unique constraint initially
    slug = models.SlugField(max_length=255, blank=True, null=True)  # Remove unique=True
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.subservice_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.subservice_name)
            slug = base_slug
            counter = 1
            while Subservice.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    
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
    
    
class ServiceSection1(models.Model):
    service_heading = models.ForeignKey(
        'Subservice',
        on_delete=models.CASCADE,
        related_name='service_section1'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ServiceSection2(models.Model):
    service_heading = models.ForeignKey(
        'Subservice',
        on_delete=models.CASCADE,
        related_name='service_section2'
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



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
    solutions_heading = models.ForeignKey(
        SolutionsName,
        on_delete=models.CASCADE,
        related_name='solutions'
    )
    solutions_name = models.CharField(max_length=255)
    solutions_title = models.CharField(max_length=255, blank=True, null=True)
    solutions_description = models.TextField(blank=True, null=True)
    solutions_image = CloudinaryField('image', folder='subsolutions')

    # SEO fields
    slug = models.SlugField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.solutions_name

    def save(self, *args, **kwargs):
        # Generate slug only if empty
        if not self.slug and self.solutions_name:
            base_slug = slugify(self.solutions_name)
            slug = base_slug
            counter = 1

            # Ensure slug is unique
            while Subsolutions.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)
    
    
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


class SolutionsSection1(models.Model):
    solutions_heading = models.ForeignKey(
        Subsolutions,
        on_delete=models.CASCADE,
        related_name='section1_items'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Solution Section 1'
        verbose_name_plural = 'Solution Section 1'
    
    def __str__(self):
        return f"{self.title} - {self.solutions_heading.solutions_name}"


class SolutionsSection2(models.Model):
    solutions_heading = models.ForeignKey(
        Subsolutions,
        on_delete=models.CASCADE,
        related_name='section2_items'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Solution Section 2'
        verbose_name_plural = 'Solution Section 2'
    
    def __str__(self):
        return f"{self.title} - {self.solutions_heading.solutions_name}"
    
    
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

    # ✅ SEO fields (nullable)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    
    
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
    """Section 2 for Our Works - Image, Title, Description, and 3 customizable statistics"""

    ourwork = models.ForeignKey(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='section2_stats'
    )

    # Main content
    image = CloudinaryField('image', folder='our_works/section2', blank=True, null=True)

    title = models.CharField(
        max_length=200,
        default="Section Title",
        help_text="e.g., Building Trust Through Clear Communication"
    )

    description = models.TextField(
        default="Section description goes here.",
        help_text="e.g., Strong visuals and messaging helped position the brand..."
    )


    # Statistic 1
    stat1_count = models.CharField(max_length=50, default="1000+")
    stat1_text = models.CharField(max_length=100, default="Students Guided")

    # Statistic 2
    stat2_count = models.CharField(max_length=50, default="15+")
    stat2_text = models.CharField(max_length=100, default="Partner Universities")

    # Statistic 3
    stat3_count = models.CharField(max_length=50, default="95%")
    stat3_text = models.CharField(max_length=100, default="Application Success Rate")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Our Work Section 2"
        verbose_name_plural = "Our Work Section 2"
        ordering = ['-created_at']

    def __str__(self):
        return f"Section 2 - {self.ourwork.title}: {self.title}"

    # ✅ Auto generate slug
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while OurWorkSection2.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)
        
# ==================== PROJECT GOALS SECTION ====================

class ProjectGoalsSection(models.Model):
    """Main Project Goals Section"""
    ourwork = models.OneToOneField(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='project_goals_section'
    )
    main_heading = models.CharField(max_length=200, default="PROJECT GOALS")
    main_title = models.CharField(max_length=200, default="Objectives")
    main_description = models.TextField(help_text="e.g., To visually highlight customization quality and brand reliability.")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project Goals Section"
        verbose_name_plural = "Project Goals Sections"

    def __str__(self):
        return f"Project Goals - {self.ourwork.title}"


class ProjectGoal(models.Model):
    """Individual Goals within Project Goals Section"""
    section = models.ForeignKey(
        ProjectGoalsSection,
        on_delete=models.CASCADE,
        related_name='goals'
    )
    heading = models.CharField(max_length=200, help_text="e.g., Product Showcase, Brand Value, Market Reach")
    description = models.TextField(help_text="e.g., Highlight diary quality and finish.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which goals appear")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project Goal"
        verbose_name_plural = "Project Goals"
        ordering = ['display_order', 'created_at']

    def __str__(self):
        return f"{self.heading}"

# ==================== CHALLENGES / WHAT WE SOLVED SECTION ====================

class ChallengesSection(models.Model):
    """Main Challenges Section for Our Works"""
    ourwork = models.OneToOneField(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='challenges_section'
    )
    banner_image = CloudinaryField('image', folder='challenges/banners', blank=True, null=True, help_text="Large banner image showcasing multiple designs")
    main_heading = models.CharField(max_length=200, default="WHAT WE SOLVED")
    main_title = models.CharField(max_length=200, default="Challenges")
    main_description = models.TextField(help_text="e.g., Balancing informative content with engaging design.")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Challenges Section"
        verbose_name_plural = "Challenges Sections"

    def __str__(self):
        return f"Challenges - {self.ourwork.title}"


class Challenge(models.Model):
    """Individual Challenges within Challenges Section"""
    section = models.ForeignKey(
        ChallengesSection,
        on_delete=models.CASCADE,
        related_name='challenges'
    )
    heading = models.CharField(max_length=200, help_text="e.g., Information Density, Student Engagement")
    description = models.TextField(help_text="e.g., Presenting large amounts of data clearly.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which challenges appear")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Challenge"
        verbose_name_plural = "Challenges"
        ordering = ['display_order', 'created_at']

    def __str__(self):
        return f"{self.heading}"

# ==================== CREATIVE DIRECTION SECTION ====================

class CreativeDirectionSection(models.Model):
    """Main Creative Direction Section for Our Works"""
    ourwork = models.OneToOneField(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='creative_direction_section'
    )
    main_heading = models.CharField( max_length=200,default="Creative Direction",help_text="e.g., Creative Direction")
    main_title = models.CharField(max_length=200, help_text="e.g., Wellness-Focused Visual Identity")
    main_description = models.TextField(help_text="e.g., A clean, elegant design language that reflects peace and wellness.")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Creative Direction Section"
        verbose_name_plural = "Creative Direction Sections"

    def __str__(self):
        return f"Creative Direction - {self.ourwork.title}"


class CreativeItem(models.Model):
    """Individual Creative Items within Creative Direction Section"""
    section = models.ForeignKey(
        CreativeDirectionSection,
        on_delete=models.CASCADE,
        related_name='creative_items'
    )
    image = CloudinaryField('image', folder='creative_direction', help_text="Creative item image")
    title = models.CharField(max_length=200, help_text="e.g., SOCIAL MEDIA DESIGN, PROMOTIONAL CREATIVES")
    description = models.TextField(help_text="e.g., Minimal and calming social creatives.")
    display_order = models.PositiveIntegerField(default=0, help_text="Order in which items appear")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Creative Item"
        verbose_name_plural = "Creative Items"
        ordering = ['display_order', 'created_at']

    def __str__(self):
        return f"{self.title}"

# ==================== MOBILE SECTION ====================

class MobileSection(models.Model):
    """Mobile Section for Our Works - displays mobile app/experience with 2 images"""
    ourwork = models.OneToOneField(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='mobile_section'
    )
    label = models.CharField(max_length=100, default="INTERACTIVE EXPERIENCE", help_text="Small label above title")
    title = models.CharField(max_length=200, help_text="e.g., 3D Visualization & Virtual Tours")
    description = models.TextField(help_text="Long description about the mobile experience")
    
    # Two mobile images/screenshots
    mobile_image_1 = CloudinaryField('image', folder='mobile_sections', help_text="First mobile image/screenshot")
    mobile_image_2 = CloudinaryField('image', folder='mobile_sections', help_text="Second mobile image/screenshot")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Mobile Section"
        verbose_name_plural = "Mobile Sections"

    def __str__(self):
        return f"Mobile Section - {self.ourwork.title}"

# ==================== SECTION 4 - THREE IMAGES ====================

class Section4(models.Model):
    """Section 4 for Our Works - heading, description, and 3 images"""
    ourwork = models.OneToOneField(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='section4'
    )
    heading = models.CharField(max_length=200, help_text="Section heading")
    description = models.TextField(help_text="Section description")
    
    # Three images
    image_1 = CloudinaryField('image', folder='section4', help_text="First image")
    image_2 = CloudinaryField('image', folder='section4', help_text="Second image")
    image_3 = CloudinaryField('image', folder='section4', help_text="Third image")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Section 4"
        verbose_name_plural = "Section 4"

    def __str__(self):
        return f"Section 4 - {self.ourwork.title}"


# ==================== SECTION 5 - SINGLE IMAGE ====================

class Section5(models.Model):
    """Section 5 for Our Works - heading, description, and single image"""
    ourwork = models.OneToOneField(
        OurWorks,
        on_delete=models.CASCADE,
        related_name='section5'
    )
    heading = models.CharField(max_length=200, help_text="Section heading")
    description = models.TextField(help_text="Section description")
    image = CloudinaryField('image', folder='section5', help_text="Main section image")
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Section 5"
        verbose_name_plural = "Section 5"

    def __str__(self):
        return f"Section 5 - {self.ourwork.title}"
# ==================== OUR WORKS DIGITAL MARKETING SECTION ====================
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

    # ✅ Auto generate slug
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Insights.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)    


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
    # ✅ SEO fields (nullable)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
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
    
# ==================== Blog ====================
class Blog(models.Model):
    banner_image = CloudinaryField(
        'banner_image',
        blank=True,
        null=True
    )

    title = models.CharField(max_length=255)

    image = CloudinaryField(
        'image',
        blank=True,
        null=True
    )

    category = models.CharField(max_length=100)

    features = models.TextField(
        null=True,
        blank=True,
        help_text="Comma separated features"
    )

    description = models.TextField()

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Career(models.Model):
    icon = models.CharField(max_length=255, blank=True, null=True)
    heading = models.CharField(max_length=255)
    description = models.TextField()
    experience = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    job_type = models.CharField(max_length=50, blank=True, null=True)
    sections = models.JSONField(blank=True, null=True, help_text='JSON list of sections: [{"heading": "...", "points": ["p1","p2"]}]')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
    
class Location(models.Model):
    location = models.CharField(max_length=150)
    heading = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    slug = models.SlugField(blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.location)
            slug = base_slug
            counter = 1

            while Location.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.location

class Design(models.Model):
    banner_image = models.ImageField(upload_to="design/banner/")
    banner_heading = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Auto generate slug if not exists
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            # Ensure unique slug
            while Design.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class DesignImage(models.Model):
    design = models.ForeignKey(
        Design,
        related_name="images",
        on_delete=models.CASCADE
    )

    image = CloudinaryField("design_image")

    def __str__(self):
        return self.design.title
