
# urls.py
from django.urls import path
from .views import (
    HomeBannerListView, HomeText1ListView, HomeBanner2ListView,
    HomeText2ListView, ConnceptsListView, HomeBanner3ListView,
    HomeText3ListView, HomeAvailableWorksListView, HomeBanner4ListView,
    HomeAboutUsListView, HomeQuestionsListView, FooterListView,
    HomeDigitalMarketingListView,

    ContactSAListView, LeadsListCreateView, ContactDigitalMarketingListView
)

urlpatterns = [
    # Home prefixed URLs
    path('home/banners/', HomeBannerListView.as_view(), name='home-banners'),
    path('home/text1/', HomeText1ListView.as_view(), name='home-text1'),
    path('home/banners2/', HomeBanner2ListView.as_view(), name='home-banners2'),
    path('home/text2/', HomeText2ListView.as_view(), name='home-text2'),
    path('home/banners3/', HomeBanner3ListView.as_view(), name='home-banners3'),
    path('home/text3/', HomeText3ListView.as_view(), name='home-text3'),
    path('home/available-works/', HomeAvailableWorksListView.as_view(), name='home-available-works'),
    path('home/banners4/', HomeBanner4ListView.as_view(), name='home-banners4'),
    path('home/about-us/', HomeAboutUsListView.as_view(), name='home-about-us'),
    path('home/questions/', HomeQuestionsListView.as_view(), name='home-questions'),
    path('home/digital-marketing/', HomeDigitalMarketingListView.as_view(), name='home-digital-marketing'),
    
    # Non-home prefixed URLs
    path('concepts/', ConnceptsListView.as_view(), name='concepts'),
    path('footer/', FooterListView.as_view(), name='footer'),


    # contacts 

     path('contact/sa/', ContactSAListView.as_view(), name='contact-sa'),
    path('contact/leads/', LeadsListCreateView.as_view(), name='contact-leads'),
    path('contact/digital-marketing/', ContactDigitalMarketingListView.as_view(), name='contact-digital-marketing'),
]