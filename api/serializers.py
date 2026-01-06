# serializers.py
from rest_framework import serializers
from dashboard.models import (
    HomeBanner, HomeText1, HomeBanner2, HomeText2, Conncepts,
    HomeBanner3, HomeText3, HomeAvailableWorks, HomeBanner4,
    Contents, HomeAboutUs, HomeQuestions, Question, Footer,
    HomeDigitalMarketing,  ContactSA, Leads, ContactDigitalMarketing,
    HomeVision,HomeFeatures,

    #  SERVICES
    Service, ServiceName, Subservice, ServiceDigitalMarketing,

    # solution
    Solutions, Subsolutions, SolutionsName, solutionsDigitalMarketing,

      # OUR WORKS
    Industry,
    Expertise,
    OurWorks,

    # INSIGHTS
    Insights,
)


class HomeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner
        fields = '__all__'


class HomeText1Serializer(serializers.ModelSerializer):
    class Meta:
        model = HomeText1
        fields = '__all__'


class HomeBanner2Serializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner2
        fields = '__all__'


class HomeText2Serializer(serializers.ModelSerializer):
    class Meta:
        model = HomeText2
        fields = '__all__'


class ConnceptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conncepts
        fields = '__all__'


class HomeBanner3Serializer(serializers.ModelSerializer):
    class Meta:
        model = HomeBanner3
        fields = '__all__'


class HomeText3Serializer(serializers.ModelSerializer):
    class Meta:
        model = HomeText3
        fields = '__all__'


class HomeAvailableWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAvailableWorks
        fields = '__all__'


class ContentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = '__all__'


class HomeBanner4Serializer(serializers.ModelSerializer):
    contents = ContentsSerializer(many=True, read_only=True)
    
    class Meta:
        model = HomeBanner4
        fields = '__all__'


class HomeAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAboutUs
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class HomeQuestionsSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = HomeQuestions
        fields = '__all__'


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class HomeDigitalMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeDigitalMarketing
        fields = '__all__'

class HomeVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeVision
        fields = '__all__'

class HomeFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeFeatures
        fields = '__all__'





# ========== contacts ======================>




class ContactSASerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSA
        fields = '__all__'


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'


class ContactDigitalMarketingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDigitalMarketing
        fields = '__all__'




# SERVICES =======================

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        fields = ('id', 'subservice_name', 'subservice_description', 'sub_service_image')
        # optionally: read_only_fields = ('id',)

class ServiceNameSerializer(serializers.ModelSerializer):
    # include nested subservices
    subservices = SubserviceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceName
        fields = ('id', 'service_name', 'service_description', 'service_image', 'subservices')

class ServiceDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDigitalMarketing
        fields = '__all__'



# SOLUTIONS =======================

class SolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solutions
        fields = '__all__'


class SubsolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsolutions
        fields = ('id', 'solutions_name', 'solutions_description', 'solutions_image')


class SolutionsNameSerializer(serializers.ModelSerializer):
    # include nested subsolutions
    solutions = SubsolutionsSerializer(many=True, read_only=True)

    class Meta:
        model = SolutionsName
        fields = ('id', 'solutions_name', 'solutions_description', 'solutions_image', 'solutions')


class SolutionsDigitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = solutionsDigitalMarketing
        fields = '__all__'



# navbar  =================

class SubsolutionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subsolutions
        fields = "__all__"


class SolutionsNameSerializer(serializers.ModelSerializer):
    solutions = SubsolutionsSerializer(many=True, read_only=True)

    class Meta:
        model = SolutionsName
        fields = "__all__"


# ===================== OUR WORKS SERIALIZERS ===========================>

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'


class OurWorksSerializer(serializers.ModelSerializer):
    industry_name = serializers.CharField(source='industry.name', read_only=True)
    expertise_name = serializers.CharField(source='expertise.name', read_only=True)
    
    class Meta:
        model = OurWorks
        fields = '__all__'    

class InsightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insights
        fields = '__all__'            