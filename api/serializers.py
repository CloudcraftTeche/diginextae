# serializers.py
from rest_framework import serializers
from dashboard.models import (
    HomeBanner, HomeText1, HomeBanner2, HomeText2, Conncepts,
    HomeBanner3, HomeText3, HomeAvailableWorks, HomeBanner4,
    Contents, HomeAboutUs, HomeQuestions, Question, Footer,
    HomeDigitalMarketing,  ContactSA, Leads, ContactDigitalMarketing
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

