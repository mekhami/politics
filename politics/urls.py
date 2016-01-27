"""politics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from legislators.models import Legislator
from bills.models import Bill

class LegislatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Legislator
        fields = (
                'url',
                'full_name',
                'title',
                'first_name',
                'middle_name',
                'last_name',
                'name_suffix',
                'party',
                'chamber',
                'state',
                'district',
                'in_office',
                'gender',
                'phone',
                'fax',
                'website',
                'bioguide_id',
            )

class LegislatorViewSet(viewsets.ModelViewSet):
    queryset = Legislator.objects.all()
    serializer_class = LegislatorSerializer

class BillSerializer(serializers.HyperlinkedModelSerializer):
    sponsor = serializers.HyperlinkedRelatedField(view_name='legislator-detail', read_only=True)

    class Meta:
        model = Bill
        fields = (
            'url',
            'bill_id',
            'bill_type',
            'chamber',
            'congress',
            'cosponsors_count',
            'enacted_as',
            'introduced_on',
            'last_action_at',
            'last_version_on',
            'last_vote_at',
            'number',
            'official_title',
            'popular_title',
            'short_title',
            'sponsor',
        )

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


router = routers.DefaultRouter()
router.register(r'legislators', LegislatorViewSet)
router.register(r'bills', BillViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
