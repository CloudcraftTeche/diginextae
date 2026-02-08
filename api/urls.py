
# urls.py
from django.urls import path
from .views import (
    HomeBannerListView, HomeText1ListView, HomeBanner2ListView,
    HomeText2ListView, ConnceptsListView, HomeBanner3ListView,
    HomeText3ListView, HomeAvailableWorksListView, HomeBanner4ListView,
    HomeAboutUsListView, HomeQuestionsListView, FooterListView,
    HomeDigitalMarketingListView,  HomeVisionListView,
    HomeFeaturesListView,BlogDetailView,

    # CONTACTS SECTION
    ContactSAListView, LeadsListCreateView, ContactDigitalMarketingListView,
    subscribe,

    # ABOUT US SECTION
    AboutUsBanner1ListView, AboutUsBanner1DetailView,
    AboutUsText1ListView, AboutUsText1DetailView,
    AboutUsMissionListView, AboutUsMissionDetailView,
    AboutUsText2ListView, AboutUsText2DetailView,
    AboutUsDigitalMarketingView,

    # service 
    ServiceListView, ServiceNameListView, SubserviceDetailView, NavbarServiceListView, serviceDigitalMarket,

    # sotion
    SolutionsListView, SolutionsNameListView, SubsolutionsDetailView, solutionDigitalMarket_view,

    # OUR WORKS SECTION
    IndustryListView, ExpertiseListView, OurWorksListView, 
    OurWorkDetailView, OurWorksDigitalMarketingView,

    # INSIGHTS SECTION
    InsightsListView, OurInsightsListView,
    OurInsightsDetailView, InsightsDigitalMarketingView,
    BlogListView, CareerListView, LocationListView,LocationDetailView
)

urlpatterns = [
    # Home prefixed URLs
    path('home/banners/', HomeBannerListView.as_view(), name='home-banners'),
    # path('home/text1/', HomeText1ListView.as_view(), name='home-text1'),
    path('home/banner-secondary/', HomeBanner2ListView.as_view(), name='home-banners2'),
    path('home/text2/', HomeText2ListView.as_view(), name='home-text2'),
    # path('home/banners3/', HomeBanner3ListView.as_view(), name='home-banners3'),
    # path('home/text3/', HomeText3ListView.as_view(), name='home-text3'),
    # path('home/available-works/', HomeAvailableWorksListView.as_view(), name='home-available-works'),
    # path('home/banners4/', HomeBanner4ListView.as_view(), name='home-banners4'),
    path('home/about-us/', HomeAboutUsListView.as_view(), name='home-about-us'),
    path('home/faq/', HomeQuestionsListView.as_view(), name='home-questions'),
    path('home/digital-marketing/', HomeDigitalMarketingListView.as_view(), name='home-digital-marketing'),
    path('home/visions/', HomeVisionListView.as_view(), name='home-visions'),
    path('home/features/', HomeFeaturesListView.as_view(), name='home-features'),
    # Non-home prefixed URLs
    path('concepts/', ConnceptsListView.as_view(), name='concepts'),
    path('footer/', FooterListView.as_view(), name='footer'),

    # ============= ABOUT US SECTION =============
    path('aboutus/banners/', AboutUsBanner1ListView.as_view(), name='aboutus-banners'),
    path('aboutus/banners/<int:pk>/', AboutUsBanner1DetailView.as_view(), name='aboutus-banner-detail'),
    path('aboutus/text1/', AboutUsText1ListView.as_view(), name='aboutus-text1'),
    path('aboutus/text1/<int:pk>/', AboutUsText1DetailView.as_view(), name='aboutus-text1-detail'),
    path('aboutus/missions/', AboutUsMissionListView.as_view(), name='aboutus-missions'),
    path('aboutus/missions/<int:pk>/', AboutUsMissionDetailView.as_view(), name='aboutus-mission-detail'),
    path('aboutus/text2/', AboutUsText2ListView.as_view(), name='aboutus-text2'),
    path('aboutus/text2/<int:pk>/', AboutUsText2DetailView.as_view(), name='aboutus-text2-detail'),
    path('aboutus/digital-marketing/', AboutUsDigitalMarketingView.as_view(), name='aboutus-digital-marketing'),

    # contacts 
    path('contact/sa/', ContactSAListView.as_view(), name='contact-sa'),
    path('contact/leads/', LeadsListCreateView.as_view(), name='contact-leads'),
    path('contact/digital-marketing/', ContactDigitalMarketingListView.as_view(), name='contact-digital-marketing'),


    # ============= services ==============>

    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/service-names/', ServiceNameListView.as_view(), name='service-name-list'),
    path('services/subservice/<int:pk>/', SubserviceDetailView.as_view(), name='subservice-detail'),
    path('services/serviceDigitalMarket', serviceDigitalMarket.as_view(), name='service-DigitalMarket'),

    # ============= solutions ==============

    path('solutions/', SolutionsListView.as_view(), name='solutions-list'),
    path('solutions/solutions-names/', SolutionsNameListView.as_view(), name='solutions-names-list'),
    path('solutions/subsolutions/<int:pk>/', SubsolutionsDetailView.as_view(), name='subsolution-detail'),
    path('solutions/solutioinDigitalMarket', solutionDigitalMarket_view.as_view(), name='solution-DigitalMarket'),

    # ============= OUR WORKS SECTION =============
    path('ourworks/', OurWorksListView.as_view(), name='ourworks-list'),
    path('ourworks/<int:pk>/', OurWorkDetailView.as_view(), name='ourworks-detail'),
    path('ourworks/industries/', IndustryListView.as_view(), name='industries-list'),
    path('ourworks/expertise/', ExpertiseListView.as_view(), name='expertise-list'),
    path('ourworks/digital-marketing/', OurWorksDigitalMarketingView.as_view(), name='ourworks-digital-marketing'),

    # ============= INSIGHTS SECTION =============
    path('insights/banner', InsightsListView.as_view(), name='insights-list'),
    path('insights/our-insights/', OurInsightsListView.as_view(), name='our-insights-list'),
    path('insights/our-insights/<int:pk>/', OurInsightsDetailView.as_view(), name='our-insights-detail'),
    path('insights/digital-marketing/', InsightsDigitalMarketingView.as_view(), name='insights-digital-marketing'),
    

    # navbar 
    path('navbar-data/', NavbarServiceListView.as_view(), name='navbar-services'),

    # subscribe 
    path('api/subscribe/', subscribe, name='subscribe'),
    
    # blog
    path('blog/', BlogListView.as_view(), name='blog-list'),
    path('blog/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),

    
    #Career
    path('career/', CareerListView.as_view(), name='career-list'),
    
    
    #Location
    path('locations/', LocationListView.as_view(), name='location-list'),
    path('locations/<int:id>/', LocationDetailView.as_view(), name='location-detail'),
    
]