
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from dashboard.models import (
    HomeBanner, HomeText1, HomeBanner2, HomeText2, Conncepts,
    HomeBanner3, HomeText3, HomeAvailableWorks, HomeBanner4,
    Contents, HomeAboutUs, HomeQuestions, Question, Footer,HomeVision,
    HomeFeatures,

    # ABOUT US
    AboutUsBanner1,
    AboutUsText1,
    AboutUsMission,
    AboutUsText2,
    AboutUsDigitalMarketing,

    
    # contacts
    HomeDigitalMarketing, ContactSA, Leads, ContactDigitalMarketing,
    #  services 

    Service, ServiceName, Subservice, ServiceDigitalMarketing,
    #  solution 
    Subsolutions, Solutions, SolutionsName, solutionsDigitalMarketing,
    # OUR WORKS
    Industry,
    Expertise,
    OurWorks,
    OurWorksDigitalMarketing,
    # INSIGHTS
    Insights,
    InsightsDigitalMarketing,
    OurInsights,
    Blog,Career,Location
)
from .serializers import (
    HomeBannerSerializer, HomeText1Serializer, HomeBanner2Serializer,
    HomeText2Serializer, ConnceptsSerializer, HomeBanner3Serializer,
    HomeText3Serializer, HomeAvailableWorksSerializer, HomeBanner4Serializer,
    ContentsSerializer, HomeAboutUsSerializer, HomeQuestionsSerializer,
    QuestionSerializer, FooterSerializer, HomeDigitalMarketingSerializer,
    HomeVisionSerializer,
    HomeFeaturesSerializer,


      ContactSASerializer, 
    LeadsSerializer, 
    ContactDigitalMarketingSerializer,
    # ABOUT US
    AboutUsBanner1Serializer,
    AboutUsText1Serializer,
    AboutUsMissionSerializer,
    AboutUsText2Serializer,
    AboutUsDigitalMarketingSerializer,
    # SERVICES

    ServiceSerializer, ServiceNameSerializer, SubserviceSerializer, ServiceDigitalSerializer,

    # solution 
    SubsolutionsSerializer, SolutionsSerializer, SolutionsNameSerializer, SolutionsDigitalSerializer,

    # OUR WORKS
    IndustrySerializer,
    ExpertiseSerializer,
    OurWorksSerializer,
    OurWorksDigitalMarketingSerializer,

    # INSIGHTS
    InsightsSerializer,
    InsightsDigitalMarketingSerializer,
    OurInsightsSerializer,
    BlogSerializer,
    CareerSerializer,
    LocationSerializer,

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

class HomeVisionListView(APIView):
    """GET: Retrieve all active Home Vision records"""
    def get(self, request):
        try:
            visions = HomeVision.objects.filter(is_active=True)
            serializer = HomeVisionSerializer(visions, many=True)
            return custom_response(
                success=True,
                message="Home visions retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home visions: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeFeaturesListView(APIView):
    """GET: Retrieve all active Home Features records"""
    def get(self, request):
        try:
            features = HomeFeatures.objects.filter(is_active=True)
            serializer = HomeFeaturesSerializer(features, many=True)
            return custom_response(
                success=True,
                message="Home features retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving home features: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# ==================== ABOUT US SECTION ====================

class AboutUsBanner1ListView(APIView):
    """GET: Retrieve all active About Us Banner 1 records"""
    def get(self, request):
        try:
            banners = AboutUsBanner1.objects.filter(is_active=True)
            serializer = AboutUsBanner1Serializer(banners, many=True)
            return custom_response(
                success=True,
                message="About us banners retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us banners: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsBanner1DetailView(APIView):
    """GET: Retrieve a single About Us Banner by ID"""
    def get(self, request, pk):
        try:
            banner = AboutUsBanner1.objects.get(pk=pk, is_active=True)
            serializer = AboutUsBanner1Serializer(banner)
            return custom_response(
                success=True,
                message="About us banner retrieved successfully",
                data=serializer.data
            )
        except AboutUsBanner1.DoesNotExist:
            return custom_response(
                success=False,
                message="About us banner not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us banner: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsText1ListView(APIView):
    """GET: Retrieve all active About Us Text 1 records"""
    def get(self, request):
        try:
            texts = AboutUsText1.objects.filter(is_active=True)
            serializer = AboutUsText1Serializer(texts, many=True)
            return custom_response(
                success=True,
                message="About us text 1 retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us text 1: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsText1DetailView(APIView):
    """GET: Retrieve a single About Us Text 1 by ID"""
    def get(self, request, pk):
        try:
            text = AboutUsText1.objects.get(pk=pk, is_active=True)
            serializer = AboutUsText1Serializer(text)
            return custom_response(
                success=True,
                message="About us text 1 retrieved successfully",
                data=serializer.data
            )
        except AboutUsText1.DoesNotExist:
            return custom_response(
                success=False,
                message="About us text 1 not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us text 1: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsMissionListView(APIView):
    """GET: Retrieve all active About Us Mission records"""
    def get(self, request):
        try:
            missions = AboutUsMission.objects.filter(is_active=True)
            serializer = AboutUsMissionSerializer(missions, many=True)
            return custom_response(
                success=True,
                message="About us missions retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us missions: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsMissionDetailView(APIView):
    """GET: Retrieve a single About Us Mission by ID"""
    def get(self, request, pk):
        try:
            mission = AboutUsMission.objects.get(pk=pk, is_active=True)
            serializer = AboutUsMissionSerializer(mission)
            return custom_response(
                success=True,
                message="About us mission retrieved successfully",
                data=serializer.data
            )
        except AboutUsMission.DoesNotExist:
            return custom_response(
                success=False,
                message="About us mission not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us mission: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsText2ListView(APIView):
    """GET: Retrieve all active About Us Text 2 records"""
    def get(self, request):
        try:
            texts = AboutUsText2.objects.filter(is_active=True)
            serializer = AboutUsText2Serializer(texts, many=True)
            return custom_response(
                success=True,
                message="About us text 2 retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us text 2: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsText2DetailView(APIView):
    """GET: Retrieve a single About Us Text 2 by ID"""
    def get(self, request, pk):
        try:
            text = AboutUsText2.objects.get(pk=pk, is_active=True)
            serializer = AboutUsText2Serializer(text)
            return custom_response(
                success=True,
                message="About us text 2 retrieved successfully",
                data=serializer.data
            )
        except AboutUsText2.DoesNotExist:
            return custom_response(
                success=False,
                message="About us text 2 not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us text 2: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AboutUsDigitalMarketingView(APIView):
    """GET: Retrieve About Us Digital Marketing settings"""
    def get(self, request):
        try:
            digital_marketing = AboutUsDigitalMarketing.objects.filter(is_active=True).first()
            if digital_marketing:
                serializer = AboutUsDigitalMarketingSerializer(digital_marketing)
                return custom_response(
                    success=True,
                    message="About us digital marketing retrieved successfully",
                    data=serializer.data
                )
            return custom_response(
                success=False,
                message="About us digital marketing not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving about us digital marketing: {str(e)}",
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
        


# ===================== services ========================>


class ServiceListView(APIView):
    """GET: Retrieve all Service records"""

    def get(self, request):
        try:
            services = Service.objects.all()   # or filter(is_active=True) if needed
            serializer = ServiceSerializer(services, many=True)
            
            return custom_response(
                success=True,
                message="Services retrieved successfully",
                data=serializer.data
            )

        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving services: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )





# ================== names under the services like for   branding  ========
class ServiceNameListView(APIView):
    """GET: Retrieve all ServiceName records, each with its subservices"""

    def get(self, request):
        try:
            services = ServiceName.objects.all().prefetch_related('subservices')

            # Generate slug if missing
            for service in services:
                for subservice in service.subservices.all():
                    if not subservice.slug:
                        subservice.slug = slugify(subservice.subservice_name)
                        subservice.save(update_fields=["slug"])

            serializer = ServiceNameSerializer(services, many=True)

            return custom_response(
                success=True,
                message="Service names and their subservices retrieved successfully",
                data=serializer.data
            )

        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving service names: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


# =================== single subservice get ================>

class SubserviceDetailView(APIView):
    """GET: Retrieve a single Subservice by ID"""

    def get(self, request, pk):
        try:
            subservice = Subservice.objects.get(pk=pk)
            serializer = SubserviceSerializer(subservice)

            return custom_response(
                success=True,
                message="Subservice retrieved successfully",
                data=serializer.data
            )
        
        except Subservice.DoesNotExist:
            return custom_response(
                success=False,
                message="Subservice not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving subservice: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class NavbarServiceListView(APIView):
    """GET: Retrieve all services & solutions with their nested items for navbar"""

    def get(self, request):
        try:
            # Get all services + nested subservices
            services = ServiceName.objects.all().prefetch_related('subservices')
            service_serializer = ServiceNameSerializer(services, many=True)

            # Get all solutions + nested subsolutions
            solutions = SolutionsName.objects.all().prefetch_related('solutions')
            solution_serializer = SolutionsNameSerializer(solutions, many=True)

            # Combined response
            response_data = {
                "services": service_serializer.data,
                "solutions": solution_serializer.data
            }

            return custom_response(
                success=True,
                message="Navbar services & solutions retrieved successfully",
                data=response_data
            )

        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving navbar navbar data: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class serviceDigitalMarket(APIView):


    def get(self, request):
        try:
            subservicedigital = ServiceDigitalMarketing.objects.first()
            serializerDigital = ServiceDigitalSerializer(subservicedigital)

            return custom_response(
                success=True,
                message="service Digital market retrieved successfully",
                data=serializerDigital.data
            )
        
        except Subservice.DoesNotExist:
            return custom_response(
                success=False,
                message="Subservice not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving subservice: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        


# ----------------- solution --------------->

class SolutionsListView(APIView):
    """GET: Retrieve all Solutions records"""

    def get(self, request):
        try:
            solutions = Solutions.objects.all()
            serializer = SolutionsSerializer(solutions, many=True)
            
            return custom_response(
                success=True,
                message="Solutions retrieved successfully",
                data=serializer.data
            )

        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving solutions: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# ================== names under the solutions ========
class SolutionsNameListView(APIView):
    """GET: Retrieve all SolutionsName records, each with its subsolutions"""

    def get(self, request):
        try:
            solutions = SolutionsName.objects.all().prefetch_related('solutions')
            serializer = SolutionsNameSerializer(solutions, many=True)

            return custom_response(
                success=True,
                message="Solution names and their subsolutions retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving solution names: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# =================== single subsolution get ================>


class SubsolutionsDetailView(APIView):
    """GET: Retrieve a single Subsolution by ID"""

    def get(self, request, pk):
        try:
            subsolution = Subsolutions.objects.get(pk=pk)
            serializer = SubsolutionsSerializer(subsolution)

            return custom_response(
                success=True,
                message="Subsolution retrieved successfully",
                data=serializer.data
            )
        
        except Subsolutions.DoesNotExist:
            return custom_response(
                success=False,
                message="Subsolution not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving subsolution: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class solutionDigitalMarket_view(APIView):


    def get(self, request):
        try:
            subservicedigital = solutionsDigitalMarketing.objects.first()
            serializerDigital = SolutionsDigitalSerializer(subservicedigital)

            return custom_response(
                success=True,
                message="service Digital market retrieved successfully",
                data=serializerDigital.data
            )
        
        except Subservice.DoesNotExist:
            return custom_response(
                success=False,
                message="Subservice not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving subservice: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

# ==================== OUR WORKS SECTION ====================

class IndustryListView(APIView):
    """GET: Retrieve all active Industries"""
    def get(self, request):
        try:
            industries = Industry.objects.filter(is_active=True)
            serializer = IndustrySerializer(industries, many=True)
            return custom_response(
                success=True,
                message="Industries retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving industries: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ExpertiseListView(APIView):
    """GET: Retrieve all active Expertise"""
    def get(self, request):
        try:
            expertise = Expertise.objects.filter(is_active=True)
            serializer = ExpertiseSerializer(expertise, many=True)
            return custom_response(
                success=True,
                message="Expertise retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving expertise: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class OurWorksListView(APIView):
    """GET: Retrieve all active Our Works"""
    def get(self, request):
        try:
            ourworks = OurWorks.objects.filter(is_active=True).select_related('industry', 'expertise')
            serializer = OurWorksSerializer(ourworks, many=True)
            return custom_response(
                success=True,
                message="Our works retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving our works: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class OurWorkDetailView(APIView):
    """GET: Retrieve single Our Work with all related sections"""
    def get(self, request, pk):
        try:
            our_work = OurWorks.objects.get(pk=pk, is_active=True)
            serializer = OurWorksSerializer(our_work)
            return custom_response(
                success=True,
                message="Our Work detail retrieved successfully",
                data=serializer.data
            )
        except OurWorks.DoesNotExist:
            return custom_response(
                success=False,
                message="Our Work not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving Our Work detail: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



class OurWorksDigitalMarketingView(APIView):
    """GET: Retrieve Our Works Digital Marketing settings"""
    def get(self, request):
        try:
            digital_marketing = OurWorksDigitalMarketing.objects.filter(is_active=True).first()
            if digital_marketing:
                serializer = OurWorksDigitalMarketingSerializer(digital_marketing)
                return custom_response(
                    success=True,
                    message="Our works digital marketing retrieved successfully",
                    data=serializer.data
                )
            return custom_response(
                success=False,
                message="Our works digital marketing not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving our works digital marketing: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


# ==================== INSIGHTS SECTION ====================

class InsightsListView(APIView):
    """GET: Retrieve all active Insights (Banners)"""
    def get(self, request):
        try:
            insights = Insights.objects.filter(is_active=True).order_by('-created_at')
            serializer = InsightsSerializer(insights, many=True)
            return custom_response(
                success=True,
                message="Insights retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving insights: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




class OurInsightsListView(APIView):
    """GET: Retrieve all active Our Insights"""
    def get(self, request):
        try:
            our_insights = OurInsights.objects.filter(is_active=True).order_by('-created_at')
            serializer = OurInsightsSerializer(our_insights, many=True)
            return custom_response(
                success=True,
                message="Our insights retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving our insights: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class OurInsightsDetailView(APIView):
    """GET: Retrieve a single Our Insight by ID"""
    def get(self, request, pk):
        try:
            insight = OurInsights.objects.get(pk=pk, is_active=True)
            serializer = OurInsightsSerializer(insight)
            return custom_response(
                success=True,
                message="Our insight retrieved successfully",
                data=serializer.data
            )
        except OurInsights.DoesNotExist:
            return custom_response(
                success=False,
                message="Our insight not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving our insight: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class InsightsDigitalMarketingView(APIView):
    """GET: Retrieve Insights Digital Marketing settings"""
    def get(self, request):
        try:
            digital_marketing = InsightsDigitalMarketing.objects.filter(is_active=True).first()
            if digital_marketing:
                serializer = InsightsDigitalMarketingSerializer(digital_marketing)
                return custom_response(
                    success=True,
                    message="Insights digital marketing retrieved successfully",
                    data=serializer.data
                )
            return custom_response(
                success=False,
                message="Insights digital marketing not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving insights digital marketing: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )        
#blog section
class BlogListView(APIView):
    """GET: Retrieve all active Blog posts"""
    def get(self, request):
        try:
            blogs = Blog.objects.order_by('-created_at')
            serializer = BlogSerializer(blogs, many=True)
            return custom_response(
                success=True,
                message="Blog posts retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving blog posts: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class BlogDetailView(APIView):
    """GET: Retrieve a single Blog post by ID"""

    def get(self, request, id):
        try:
            blog = get_object_or_404(Blog, id=id)
            serializer = BlogSerializer(blog)

            return custom_response(
                success=True,
                message="Blog post retrieved successfully",
                data=serializer.data
            )

        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving blog post: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

            
#Career
class CareerListView(APIView):
    """GET: Retrieve all active Career posts"""
    def get(self, request):
        try:
            careers = Career.objects.order_by('-created_at')
            serializer = CareerSerializer(careers, many=True)
            return custom_response(
                success=True,
                message="Career posts retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving career posts: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
#Location
class LocationListView(APIView):
    """GET: Retrieve all active Locations"""
    def get(self, request):
        try:
            locations = Location.objects.order_by('heading')
            serializer = LocationSerializer(locations, many=True)
            return custom_response(
                success=True,
                message="Locations retrieved successfully",
                data=serializer.data
            )
        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving locations: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class LocationDetailView(APIView):
    """GET: Retrieve a single Location by ID"""

    def get(self, request, id):
        try:
            location = get_object_or_404(Location, id=id)
            serializer = LocationSerializer(location)

            return custom_response(
                success=True,
                message="Location retrieved successfully",
                data=serializer.data
            )

        except Exception as e:
            return custom_response(
                success=False,
                message=f"Error retrieving location: {str(e)}",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )