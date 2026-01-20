from django.db import models
from .base import BaseModel

class Home(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='home_images/', blank=True, null=True)
    display_order = models.PositiveIntegerField(default=0, help_text="Controls the display order on the homepage.")

    def __str__(self):
        return f"{self.order_number} - {self.title}"


# --------------------- from her on use ------------------------>

# --------------------home ------------------------>


class HomeBanner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
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
    image = models.ImageField(upload_to='banners2/')
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
    image = models.ImageField(upload_to='concepts/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class HomeBanner3(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banners3/')
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
    image = models.ImageField(upload_to='home_available_works/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


  
    
class HomeBanner4(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='banners4/')
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
    image = models.ImageField(upload_to='home_about_us/', blank=True, null=True)
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
    banner_image = models.ImageField(upload_to='home_digital_marketing/', blank=True, null=True)
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
    
    image = models.ImageField(upload_to='home_features/', blank=True, null=True)
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
# ==================================  contacts ===============================>


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
    

class ContactDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = models.ImageField(upload_to='home_digital_marketing/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   

    def __str__(self):
        return "Home Page SEO / Marketing"
    






# =========================== abouts us ==========================>


class AboutUsBanner1(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about_us/banners/')
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
    icon = models.ImageField(upload_to='about_us/mission/', blank=True, null=True)
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
    banner_image = models.ImageField(upload_to='about_digital_marketing/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)








# ================================= services ===========================>



class Service(models.Model):

    banner_description_title = models.CharField(max_length=255, blank=True, null=True)
    banner_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)

    def __str__(self):
        return self.banner_description_title


class ServiceName(models.Model):
    service_name = models.CharField(max_length=255)
    service_description = models.TextField()
    service_image = models.ImageField(upload_to='service_images/')

    def __str__(self):
        return self.service_name



class Subservice(models.Model):
    service_heading = models.ForeignKey(ServiceName, on_delete=models.CASCADE, related_name='subservices')
    subservice_name = models.CharField(max_length=255)
    subservice_title = models.CharField(max_length=255, blank=True, null=True)
    subservice_description = models.TextField(blank=True, null=True)
    sub_service_image =models.ImageField(upload_to='sub_service_images/')


    def __str__(self):
        return self.subservice_name
    
    
class ServiceDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = models.ImageField(upload_to='home_digital_marketing/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# ===================== solution ===========================>


class Solutions(models.Model):

    banner_description_title = models.CharField(max_length=255, blank=True, null=True)
    banner_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Solutions/', blank=True, null=True)

    def __str__(self):
        return self.banner_description_title


class SolutionsName(models.Model):
    solutions_name = models.CharField(max_length=255)
    solutions_description = models.TextField()
    solutions_image = models.ImageField(upload_to='SolutionsName/')

    def __str__(self):
        return self.solutions_name

        



class Subsolutions(models.Model):
    solutions_heading = models.ForeignKey(SolutionsName, on_delete=models.CASCADE, related_name='solutions')
    solutions_name = models.CharField(max_length=255)
    solutions_title = models.CharField(max_length=255, blank=True, null=True)
    solutions_description = models.TextField(blank=True, null=True)
    solutions_image =models.ImageField(upload_to='Subsolutions/')


    def __str__(self):
        return self.solutions_name
    
    
class solutionsDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = models.ImageField(upload_to='solution_digital_marketing/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   

# ===================== OUR WORKS SECTION ===========================>

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

    # ================= Banner Section =================
    banner_image = models.ImageField(
        upload_to='our_works/banners/',
        null=True,
        blank=True
    )
    banner_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    banner_description = models.TextField(
        null=True,
        blank=True
    )

    # ================= Work Details =================
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='our_works/')

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

    language = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    time_scale = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    launch_date = models.CharField(   # text because form uses text
        max_length=100,
        null=True,
        blank=True
    )
    system = models.CharField(
        max_length=150,
        null=True,
        blank=True
    )

    # ================= Banner 2 =================
    banner2_image = models.ImageField(
        upload_to='our_works/banners/',
        null=True,
        blank=True
    )
    banner2_title = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    # ================= Status & Timestamps =================
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Our Work"
        verbose_name_plural = "Our Works"

    def __str__(self):
        return self.title

class OurWorksDigitalMarketing(models.Model):
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.CharField(max_length=500, blank=True, null=True)
    banner_image = models.ImageField(upload_to='ourworks_digital_marketing/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Our Works Page SEO / Marketing"         

# ===================== INSIGHTS SECTION ===========================>

class Insights(models.Model):
    """Insights/Blog Section"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='insights/')
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
    banner_image = models.ImageField(upload_to='insights_digital_marketing/', blank=True, null=True)
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

    image = models.ImageField(upload_to='our_insights/')

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


# ================= Challenge Section for Our Insights ===========================>

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
   
# ================= Challenge Items for Each Section ===========================>

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
