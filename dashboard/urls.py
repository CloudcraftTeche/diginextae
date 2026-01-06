from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    # -------------------- home ---------------------------------------->

  path('home/', views.home, name='home'),

    # ==================== HOME BANNER CRUD ====================
    path('home/banner/', views.home_banner, name='home_banner'),
    path('home/banner/create/', views.home_banner_create, name='home_banner_create'),
    path('home/banner/<int:pk>/edit/', views.home_banner_edit, name='home_banner_edit'),
    path('home/banner/<int:pk>/delete/', views.home_banner_delete, name='home_banner_delete'),
    
    # ==================== HOME TEXT 1 CRUD ====================
    path('home/text1/', views.home_text1, name='home_text1'),
    path('home/text1/create/', views.home_text1_create, name='home_text1_create'),
    path('home/text1/<int:pk>/edit/', views.home_text1_edit, name='home_text1_edit'),
    path('home/text1/<int:pk>/delete/', views.home_text1_delete, name='home_text1_delete'),
    
    # ==================== HOME BANNER 2 CRUD ====================
    path('home/banner2/', views.home_banner2, name='home_banner2'),
    path('home/banner2/create/', views.home_banner2_create, name='home_banner2_create'),
    path('home/banner2/<int:pk>/edit/', views.home_banner2_edit, name='home_banner2_edit'),
    path('home/banner2/<int:pk>/delete/', views.home_banner2_delete, name='home_banner2_delete'),
    
    # ==================== HOME TEXT 2 CRUD ====================
    path('home/text2/', views.home_text2, name='home_text2'),
    path('home/text2/create/', views.home_text2_create, name='home_text2_create'),
    path('home/text2/<int:pk>/edit/', views.home_text2_edit, name='home_text2_edit'),
    path('home/text2/<int:pk>/delete/', views.home_text2_delete, name='home_text2_delete'),
    
    # ==================== CONCEPTS CRUD ====================
    path('home/concepts/', views.home_concepts, name='home_concepts'),
    path('home/concepts/create/', views.concepts_create, name='concepts_create'),
    path('home/concepts/<int:pk>/edit/', views.concepts_edit, name='concepts_edit'),
    path('home/concepts/<int:pk>/delete/', views.concepts_delete, name='concepts_delete'),

    # ==================== HOME BANNER 3 CRUD ====================
    path('home/banner3/', views.home_banner3_page, name='home_banner3_page'),
    path('home/banner3/create/', views.home_banner3_create, name='home_banner3_create'),
    path('home/banner3/<int:pk>/edit/', views.home_banner3_edit, name='home_banner3_edit'),
    path('home/banner3/<int:pk>/delete/', views.home_banner3_delete, name='home_banner3_delete'),

    # ==================== HOME TEXT 3 CRUD ====================
    path('home/text3/', views.home_text3_page, name='home_text3_page'),
    path('home/text3/create/', views.home_text3_create, name='home_text3_create'),
    path('home/text3/<int:pk>/edit/', views.home_text3_edit, name='home_text3_edit'),
    path('home/text3/<int:pk>/delete/', views.home_text3_delete, name='home_text3_delete'),

    # ==================== HOME AVAILABLE WORKS CRUD ====================
    path('home/available-works/', views.home_available_works_page, name='home_available_works_page'),
    path('home/available-works/create/', views.home_available_works_create, name='home_available_works_create'),
    path('home/available-works/<int:pk>/edit/', views.home_available_works_edit, name='home_available_works_edit'),
    path('home/available-works/<int:pk>/delete/', views.home_available_works_delete, name='home_available_works_delete'),

    # ==================== HOME BANNER 4 CRUD ====================
    path('home/banner4/', views.home_banner4_page, name='home_banner4_page'),
    path('home/banner4/create/', views.home_banner4_create, name='home_banner4_create'),
    path('home/banner4/<int:pk>/edit/', views.home_banner4_edit, name='home_banner4_edit'),
    path('home/banner4/<int:pk>/delete/', views.home_banner4_delete, name='home_banner4_delete'),

    # ==================== CONTENTS CRUD ====================
    path('home/contents/create/', views.contents_create, name='contents_create'),
    path('home/contents/<int:pk>/edit/', views.contents_edit, name='contents_edit'),
    path('home/contents/<int:pk>/delete/', views.contents_delete, name='contents_delete'),

    # ==================== HOME ABOUT US CRUD ====================
    path('home/about-us/', views.home_about_us_page, name='home_about_us_page'),
    path('home/about-us/create/', views.home_about_us_create, name='home_about_us_create'),
    path('home/about-us/<int:pk>/edit/', views.home_about_us_edit, name='home_about_us_edit'),
    path('home/about-us/<int:pk>/delete/', views.home_about_us_delete, name='home_about_us_delete'),

    # ==================== HOME QUESTIONS CRUD ====================
    path('home/faq/', views.home_faq_page, name='home_faq_page'),
    path('home/questions/create/', views.home_questions_create, name='home_questions_create'),
    path('home/questions/<int:pk>/edit/', views.home_questions_edit, name='home_questions_edit'),
    path('home/questions/<int:pk>/delete/', views.home_questions_delete, name='home_questions_delete'),

    # ==================== QUESTION CRUD ====================
    path('home/question/create/', views.question_create, name='question_create'),
    path('home/question/<int:pk>/edit/', views.question_edit, name='question_edit'),
    path('home/question/<int:pk>/delete/', views.question_delete, name='question_delete'),

    # ==================== FOOTER CRUD ====================
    path('home/footer/', views.home_footer_page, name='home_footer_page'),
    path('home/footer/create/', views.footer_create, name='footer_create'),
    path('home/footer/<int:pk>/edit/', views.footer_edit, name='footer_edit'),
    path('home/footer/<int:pk>/delete/', views.footer_delete, name='footer_delete'),

    # ==================== HOME DIGITAL MARKETING ====================
    path('home/digital-marketing/', views.home_digital_marketing_page, name='home_digital_marketing_page'),
    path('home/digital-marketing/update/', views.home_digital_marketing_update, name='home_digital_marketing_update'),


   #===================== Vision Section =======================
    path('home/vision/', views.home_vision_list, name='home_vision_list'),
    path('home/vision/create/', views.home_vision_add, name='home_vision_add'),
    path('home/vision/<int:pk>/edit/', views.home_vision_edit, name='home_vision_edit'),
    path('home/vision/<int:pk>/delete/', views.home_vision_delete, name='home_vision_delete'),

   #===================== Features Section =======================
    path('home/features/', views.home_features_list, name='home_features_list'),
    path('home/features/create/', views.home_features_add, name='home_features_add'),
    path('home/features/<int:pk>/edit/', views.home_features_edit, name='home_features_edit'),
    path('home/features/<int:pk>/delete/', views.home_features_delete, name='home_features_delete'),



   # ==================== CONTACTS SECTION ====================
    # Main contacts page
    path('contacts/', views.contacts_page, name='contacts_page'),
    
    # ContactSA URLs
    path('contacts/contact-sa/create/', views.contact_sa_create, name='contact_sa_create'),
    path('contacts/contact-sa/edit/<int:pk>/', views.contact_sa_edit, name='contact_sa_edit'),
    path('contacts/contact-sa/delete/<int:pk>/', views.contact_sa_delete, name='contact_sa_delete'),
    
    # Contact Digital Marketing
    path('contacts/digital-marketing/update/', views.contact_digital_marketing_update, name='contact_digital_marketing_update'),
    
    # Leads URLs
    path('contacts/leads/create/', views.leads_create, name='leads_create'),
    path('contacts/leads/edit/<int:pk>/', views.leads_edit, name='leads_edit'),
    path('contacts/leads/delete/<int:pk>/', views.leads_delete, name='leads_delete'),







    
    # Main about us page
    path('aboutus/', views.aboutus_page, name='aboutus_page'),
    
    # About Us Banner1 URLs
    path('aboutus/banner1/create/', views.aboutus_banner1_create, name='aboutus_banner1_create'),
    path('aboutus/banner1/edit/<int:pk>/', views.aboutus_banner1_edit, name='aboutus_banner1_edit'),
    path('aboutus/banner1/delete/<int:pk>/', views.aboutus_banner1_delete, name='aboutus_banner1_delete'),
    
    # About Us Text1 URLs
    path('aboutus/text1/create/', views.aboutus_text1_create, name='aboutus_text1_create'),
    path('aboutus/text1/edit/<int:pk>/', views.aboutus_text1_edit, name='aboutus_text1_edit'),
    path('aboutus/text1/delete/<int:pk>/', views.aboutus_text1_delete, name='aboutus_text1_delete'),
    
    # About Us Mission URLs
    path('aboutus/mission/create/', views.aboutus_mission_create, name='aboutus_mission_create'),
    path('aboutus/mission/edit/<int:pk>/', views.aboutus_mission_edit, name='aboutus_mission_edit'),
    path('aboutus/mission/delete/<int:pk>/', views.aboutus_mission_delete, name='aboutus_mission_delete'),
    
    # About Us Text2 URLs
    path('aboutus/text2/create/', views.aboutus_text2_create, name='aboutus_text2_create'),
    path('aboutus/text2/edit/<int:pk>/', views.aboutus_text2_edit, name='aboutus_text2_edit'),
    path('aboutus/text2/delete/<int:pk>/', views.aboutus_text2_delete, name='aboutus_text2_delete'),
    
    # About Us Digital Marketing
    path('aboutus/digital-marketing/update/', views.aboutus_digital_marketing_update, name='aboutus_digital_marketing_update'),




        # ============= SERVICE MANAGEMENT =============
    # Service Management Main Page
    path('service-management/', views.service_management, name='service_management'),
    
    # Service Banner URLs
    path('service-banner/create/', views.service_create, name='service_create'),
    path('service-banner/edit/<int:pk>/', views.service_edit, name='service_edit'),
    path('service-banner/delete/<int:pk>/', views.service_delete, name='service_delete'),
    
    # Service Name (Category) URLs
    path('service-category/create/', views.service_name_create, name='service_name_create'),
    path('service-category/edit/<int:pk>/', views.service_name_edit, name='service_name_edit'),
    path('service-category/delete/<int:pk>/', views.service_name_delete, name='service_name_delete'),
    
    # Subservice URLs
    path('subservice/create/', views.subservice_create, name='subservice_create'),
    path('subservice/edit/<int:pk>/', views.subservice_edit, name='subservice_edit'),
    path('subservice/delete/<int:pk>/', views.subservice_delete, name='subservice_delete'),

      path('digital-marketing/create/', views.service_digital_marketing_create, name='digital_marketing_create'),
    path('digital-marketing/edit/<int:pk>/', views.service_digital_marketing_edit, name='digital_marketing_edit'),
    path('digital-marketing/delete/<int:pk>/', views.service_digital_marketing_delete, name='digital_marketing_delete'),



    # solutions ==========================

      path('solutions-management/', views.solutions_management, name='solutions_management'),
    
    # Solutions Banner CRUD
    path('solutions/create/', views.solutions_create, name='solutions_create'),
    path('solutions/edit/<int:pk>/', views.solutions_edit, name='solutions_edit'),
    path('solutions/delete/<int:pk>/', views.solutions_delete, name='solutions_delete'),
    
    # Solutions Name CRUD
    path('solutions-name/create/', views.solutions_name_create, name='solutions_name_create'),
    path('solutions-name/edit/<int:pk>/', views.solutions_name_edit, name='solutions_name_edit'),
    path('solutions-name/delete/<int:pk>/', views.solutions_name_delete, name='solutions_name_delete'),
    
    # Subsolutions CRUD
    path('subsolutions/create/', views.subsolutions_create, name='subsolutions_create'),
    path('subsolutions/edit/<int:pk>/', views.subsolutions_edit, name='subsolutions_edit'),
    path('subsolutions/delete/<int:pk>/', views.subsolutions_delete, name='subsolutions_delete'),
    
    # Solutions Digital Marketing CRUD
    path('solutions-digital-marketing/create/', views.solutions_digital_marketing_create, name='solutions_digital_marketing_create'),
    path('solutions-digital-marketing/edit/<int:pk>/', views.solutions_digital_marketing_edit, name='solutions_digital_marketing_edit'),
    path('solutions-digital-marketing/delete/<int:pk>/', views.solutions_digital_marketing_delete, name='solutions_digital_marketing_delete'),




# ==================== OUR WORKS SECTION ====================
path('ourworks/', views.ourwork_page, name='ourwork_page'),
path('ourworks/create/', views.ourwork_create, name='ourwork_create'),
path('ourworks/<int:pk>/edit/', views.ourwork_edit, name='ourwork_edit'),
path('ourworks/<int:pk>/delete/', views.ourwork_delete, name='ourwork_delete'),

# Industries Management
path('ourworks/industry/create/', views.industry_create, name='industry_create'),
path('ourworks/industry/<int:pk>/edit/', views.industry_edit, name='industry_edit'),
path('ourworks/industry/<int:pk>/delete/', views.industry_delete, name='industry_delete'),

# Expertise Management
path('ourworks/expertise/create/', views.expertise_create, name='expertise_create'),
path('ourworks/expertise/<int:pk>/edit/', views.expertise_edit, name='expertise_edit'),
path('ourworks/expertise/<int:pk>/delete/', views.expertise_delete, name='expertise_delete'),


]