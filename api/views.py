
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dashboard.models import (
    HomeBanner, HomeText1, HomeBanner2, HomeText2, Conncepts,
    HomeBanner3, HomeText3, HomeAvailableWorks, HomeBanner4,
    Contents, HomeAboutUs, HomeQuestions, Question, Footer,
    
    # contacts
    HomeDigitalMarketing, ContactSA, Leads, ContactDigitalMarketing
)
from .serializers import (
    HomeBannerSerializer, HomeText1Serializer, HomeBanner2Serializer,
    HomeText2Serializer, ConnceptsSerializer, HomeBanner3Serializer,
    HomeText3Serializer, HomeAvailableWorksSerializer, HomeBanner4Serializer,
    ContentsSerializer, HomeAboutUsSerializer, HomeQuestionsSerializer,
    QuestionSerializer, FooterSerializer, HomeDigitalMarketingSerializer,


      ContactSASerializer, 
    LeadsSerializer, 
    ContactDigitalMarketingSerializer
)


def custom_response(success, message, data=None, status_code=status.HTTP_200_OK):
    """Helper function to create consistent API responses"""
    response_data = {
        'success': success,
        'message': message,
        'data': data
    }
    return Response(response_data, status=status_code)


class HomeBannerListView(APIView):
    def get(self, request):
        try:
            banners = HomeBanner.objects.filter(is_active=True)
            serializer = HomeBannerSerializer(banners, many=True)
            return custom_response(
                success=True,
                message="Home banners retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home banners: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeText1ListView(APIView):
    def get(self, request):
        try:
            texts = HomeText1.objects.filter(is_active=True)
            serializer = HomeText1Serializer(texts, many=True)
            return custom_response(
                success=True,
                message="Home text 1 retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home text 1: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeBanner2ListView(APIView):
    def get(self, request):
        try:
            banners = HomeBanner2.objects.filter(is_active=True)
            serializer = HomeBanner2Serializer(banners, many=True)
            return custom_response(
                success=True,
                message="Home banners 2 retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home banners 2: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeText2ListView(APIView):
    def get(self, request):
        try:
            texts = HomeText2.objects.filter(is_active=True)
            serializer = HomeText2Serializer(texts, many=True)
            return custom_response(
                success=True,
                message="Home text 2 retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home text 2: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ConnceptsListView(APIView):
    def get(self, request):
        try:
            concepts = Conncepts.objects.filter(is_active=True)
            serializer = ConnceptsSerializer(concepts, many=True)
            return custom_response(
                success=True,
                message="Concepts retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving concepts: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeBanner3ListView(APIView):
    def get(self, request):
        try:
            banners = HomeBanner3.objects.filter(is_active=True)
            serializer = HomeBanner3Serializer(banners, many=True)
            return custom_response(
                success=True,
                message="Home banners 3 retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home banners 3: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeText3ListView(APIView):
    def get(self, request):
        try:
            texts = HomeText3.objects.filter(is_active=True)
            serializer = HomeText3Serializer(texts, many=True)
            return custom_response(
                success=True,
                message="Home text 3 retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home text 3: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeAvailableWorksListView(APIView):
    def get(self, request):
        try:
            works = HomeAvailableWorks.objects.filter(is_active=True)
            serializer = HomeAvailableWorksSerializer(works, many=True)
            return custom_response(
                success=True,
                message="Home available works retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home available works: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeBanner4ListView(APIView):
    def get(self, request):
        try:
            banners = HomeBanner4.objects.filter(is_active=True).prefetch_related('contents')
            serializer = HomeBanner4Serializer(banners, many=True)
            return custom_response(
                success=True,
                message="Home banners 4 with contents retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home banners 4: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeAboutUsListView(APIView):
    def get(self, request):
        try:
            about_us = HomeAboutUs.objects.filter(is_active=True)
            serializer = HomeAboutUsSerializer(about_us, many=True)
            return custom_response(
                success=True,
                message="Home about us retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home about us: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeQuestionsListView(APIView):
    def get(self, request):
        try:
            questions = HomeQuestions.objects.filter(is_active=True).prefetch_related('questions')
            serializer = HomeQuestionsSerializer(questions, many=True)
            return custom_response(
                success=True,
                message="Home questions retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home questions: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FooterListView(APIView):
    def get(self, request):
        try:
            footer = Footer.objects.filter(is_active=True)
            serializer = FooterSerializer(footer, many=True)
            return custom_response(
                success=True,
                message="Footer retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving footer: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeDigitalMarketingListView(APIView):
    def get(self, request):
        try:
            marketing = HomeDigitalMarketing.objects.filter(is_active=True)
            serializer = HomeDigitalMarketingSerializer(marketing, many=True)
            return custom_response(
                success=True,
                message="Home digital marketing retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home digital marketing: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )











# ========================== contatcs ======================>


class ContactSAListView(APIView):
    """GET: Retrieve all active ContactSA records"""
    def get(self, request):
        try:
            contacts = ContactSA.objects.all()
            serializer = ContactSASerializer(contacts, many=True)
            return custom_response(
                success=True,
                message="Contact SA retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving contact SA: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




class ContactDigitalMarketingListView(APIView):
    """GET: Retrieve all active Contact Digital Marketing records"""
    def get(self, request):
        try:
            marketing = ContactDigitalMarketing.objects.filter(is_active=True)
            serializer = ContactDigitalMarketingSerializer(marketing, many=True)
            return custom_response(
                success=True,
                message="Contact digital marketing retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving contact digital marketing: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )





# ===================================================
# views.py

from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .utils.email_templates import (
    get_subscription_email_template, 
    get_subscription_confirmation_email_template,
    get_lead_notification_email_template,
    get_lead_confirmation_email_template
)

@api_view(['POST'])
def subscribe(request):
    """
    API endpoint to handle email subscription
    Expects JSON: {"email": "user@example.com"}
    """
    email = request.data.get('email')
    
    if not email:
        return Response(
            {'error': 'Email is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validate email format
    try:
        validate_email(email)
    except ValidationError:
        return Response(
            {'error': 'Invalid email format'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Send emails
    try:
        from_email = settings.EMAIL_HOST_USER
        
        # 1. Send notification to company
        subject_company, text_company, html_company = get_subscription_email_template(email)
        
        email_to_company = EmailMultiAlternatives(
            subject_company,
            text_company,
            from_email,
            ['hello@diginext.ae']
        )
        email_to_company.attach_alternative(html_company, "text/html")
        email_to_company.send(fail_silently=False)
        
        # 2. Send confirmation to subscriber
        subject_subscriber, text_subscriber, html_subscriber = get_subscription_confirmation_email_template(email)
        
        email_to_subscriber = EmailMultiAlternatives(
            subject_subscriber,
            text_subscriber,
            from_email,
            [email]
        )
        email_to_subscriber.attach_alternative(html_subscriber, "text/html")
        email_to_subscriber.send(fail_silently=False)
        
        return Response(
            {'message': 'Subscription successful! Confirmation email sent.'},
            status=status.HTTP_200_OK
        )
    
    except Exception as e:
        return Response(
            {'error': f'Failed to send email: {str(e)}'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


class LeadsListCreateView(APIView):
    """
    GET: Retrieve all leads
    POST: Create a new lead and send email notification
    """
    def get(self, request):
        try:
            leads = Leads.objects.all()
            serializer = LeadsSerializer(leads, many=True)
            return custom_response(
                success=True,
                message="Leads retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving leads: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def post(self, request):
        try:
            serializer = LeadsSerializer(data=request.data)
            if serializer.is_valid():
                # Save the lead
                lead = serializer.save()
                
                # Send emails
                try:
                    from_email = settings.EMAIL_HOST_USER
                    
                    # 1. Send notification to company
                    subject_company, text_company, html_company = get_lead_notification_email_template(
                        fullname=lead.fullname,
                        email=lead.email,
                        phone_number=lead.phone_number,
                        company_name=lead.company_name,
                        solution=lead.solution,
                        message=lead.message
                    )
                    
                    email_to_company = EmailMultiAlternatives(
                        subject_company,
                        text_company,
                        from_email,
                        ['hello@diginext.ae']
                    )
                    email_to_company.attach_alternative(html_company, "text/html")
                    email_to_company.send(fail_silently=False)
                    
                    # 2. Send confirmation to lead sender
                    subject_lead, text_lead, html_lead = get_lead_confirmation_email_template(
                        fullname=lead.fullname,
                        solution=lead.solution
                    )
                    
                    email_to_lead = EmailMultiAlternatives(
                        subject_lead,
                        text_lead,
                        from_email,
                        [lead.email]
                    )
                    email_to_lead.attach_alternative(html_lead, "text/html")
                    email_to_lead.send(fail_silently=False)
                    
                except Exception as email_error:
                    # Log the email error but don't fail the request
                    print(f"Email notification failed: {str(email_error)}")
                
                return custom_response(
                    success=True,
                    message="Lead created successfully",
                    data=serializer.data,
                    status_code=status.HTTP_201_CREATED
                )
            
            return custom_response(
                success=False,
                message="Validation error",
                data=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error creating lead: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )