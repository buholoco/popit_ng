"""popit_ng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/?$', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from popit.views import *
from popit_search.views import GenericSearchView
from popit_search.views import GenericRawSearchView
from rest_framework.authtoken import views as token_view


urlpatterns = [
    url(r'^admin/?', include(admin.site.urls)),
]

if "rosetta" in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'rosetta/?', include('rosetta.urls'))
    ]

# TODO: the parameter in url is wrong

api_urls = [
    url(r'^api-token-auth/?$', token_view.obtain_auth_token),
    url(r'^rawsearch/?$', GenericRawSearchView.as_view(), name="rawsearch"),
    url(r'^(?P<language>\w{2})/search/(?P<index_name>\w+)/?$', GenericSearchView.as_view(), name="search"),

    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/(?P<link_id>\w+)/?$',
        PostContactDetailCitationDetailView.as_view(), name="post-contact-detail-citation-detail-view"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        PostContactDetailCitationListView.as_view(), name="post-contact-detail-citation-list-views"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/?$',
        PostContactDetailFieldCitationView.as_view(), name="post-contact-detail-field-citation-views"),

    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        PostContactDetailLinkDetail.as_view(), name="post-contact-detail-link-detail"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/?$',
        PostContactDetailLinkList.as_view(), name="post-contact-detail-link-list"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/?$',
        PostContactDetailDetail.as_view(), name="post-contact-detail-detail"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/contact_details/?$', PostContactDetailList.as_view(),
        name="post-contact-detail-list"),

    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/other_labels/(?P<child_pk>[-\w]+)/citations/(?P<field>[-\w]+)/(?P<link_id>[-\w]+)/?$',
        PostOtherLabelsCitationDetailView.as_view(), name="post-other-labels-citation-detail-view"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/other_labels/(?P<child_pk>[-\w]+)/citations/(?P<field>[-\w]+)/?$',
        PostOtherLabelsCitationListView.as_view(), name="post-other-labels-citation-list-view"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/other_labels/(?P<child_pk>[-\w]+)/citations/?$',
        PostOtherLabelFieldCitationView.as_view(), name="post-other-labels-field-citation-view"),

    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/other_labels/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        PostOtherLabelsLinkDetail.as_view(), name="post-other-label-link-detail"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/other_labels/(?P<pk>[-\w]+)/links/?$', PostOtherLabelsLinkList.as_view(),
        name="posts-other-label-link-list"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/other_labels/(?P<pk>[-\w]+)/?$', PostOtherLabelsDetail.as_view(),
        name="post-other-label-detail"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/other_labels/?$', PostOtherLabelsList.as_view(), name="post-other-label-list"),

    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/links/(?P<pk>[-\w]+)/?$', PostLinkDetail.as_view(), name="posts-link-detail"),
    url(r'^(?P<language>\w{2})/posts/(?P<parent_pk>[-\w]+)/links/?$', PostLinkList.as_view(), name="post-link-list"),

    url(r'^(?P<language>\w{2})/posts/(?P<parent>[-\w]+)/citations/(?P<field>\w+)/(?P<pk>\w+)/?$',
        PostCitationDetailView.as_view(), name="post-citation-detail-view"),
    url(r'^(?P<language>\w{2})/posts/(?P<pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        PostCitationListCreateView.as_view(), name="post-citation-list-views"),
    url(r'^(?P<language>\w{2})/posts/(?P<pk>[-\w]+)/citations/?$', PostFieldCitationView.as_view(),
        name="post-citation-field-view"),

    url(r'^(?P<language>\w{2})/posts/(?P<pk>[-\w]+)/?$', PostDetail.as_view(), name="post-detail"),
    url(r'^(?P<language>\w{2})/posts/?$', PostList.as_view(), name="post-list"),

    url(r'^(?P<language>\w{2})/persons/(?P<pk>[-\w]+)/citations/?$', PersonFieldCitationView.as_view(),
        name="person-field-citations-views"),
    url(r'^(?P<language>\w{2})/persons/(?P<pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        PersonCitationListCreateView.as_view(),
        name="person-citation-list-view"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent>[-\w]+)/citations/(?P<field>\w+)/(?P<pk>[-\w]+)/?$',
        PersonCitationDetailView.as_view(), name="person-citation-detail"),

    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/(?P<link_id>[-\w]+)/?$',
        PersonContactDetailCitationDetailView.as_view(), name="person-contact-details-citations-detail-view"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        PersonContactDetailCitationListView.as_view(), name="person-contact-details-citations-view"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/?$',
        PersonContactDetailFieldCitationView.as_view(), name="person-contact-details-field-citations-view"),

    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        PersonContactDetailLinkDetail.as_view(), name="person-contact-detail-link-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/?$', PersonContactDetailLinkList.as_view(),
        name="person-contact-detail-link-list"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/?$', PersonContactDetailDetail.as_view(),
        name="person-contact-detail-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/contact_details/?$', PersonContactDetailList.as_view(),
        name="person-contact-detail-list"),

    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/links/(?P<pk>[-\w]+)/?$', PersonLinkDetail.as_view(),
        name="person-link-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/links/?$', PersonLinkList.as_view(), name="person-link-list"),

    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/othernames/(?P<child_pk>[-\w]+)/citations/(?P<field>[-\w]+)/(?P<link_id>[-\w]+)/?$',
        PersonOthernameCitationDetailView.as_view(), name="person-othername-citation-detail-view"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/othernames/(?P<child_pk>[-\w]+)/citations/(?P<field>[-\w]+)/?$',
        PersonOthernameCitationListView.as_view(), name="person-othername-citation-list-view"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/othernames/(?P<child_pk>[-\w]+)/citations/?$',
        PersonOtherNameFieldCitationView.as_view(), name="person-othername-citation-field-view"),

    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/othernames/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        PersonOtherNameLinkDetail.as_view(), name="person-othername-link-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/othernames/(?P<pk>[-\w]+)/links/?$',
        PersonOtherNameLinkList.as_view(), name="person-othername-link-list"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/othernames/(?P<pk>[-\w]+)/?$', PersonOtherNameDetail.as_view(),
        name="person-othername-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/othernames/?$', PersonOtherNameList.as_view(),
        name="person-othername-list"),

    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/identifiers/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/(?P<link_id>[-\w]+)/?$',
        PersonIdentifierCitationDetailView.as_view(), name="person-identifier-citation-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/identifiers/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        PersonIdentifierCitationListView.as_view(), name="person-identifier-citation-list"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/identifiers/(?P<child_pk>[-\w]+)/citations/?$',
        PersonIdentifierFieldCitationView.as_view(), name="person-identifier-citation-field-view"),

    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/identifiers/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        PersonIdentifierLinkDetail.as_view(), name="person-identifier-link-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/identifiers/(?P<pk>[-\w]+)/links/?$',
        PersonIdentifierLinkList.as_view(), name="person-identifier-link-list"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/identifiers/(?P<pk>[-\w]+)/?$', PersonIdentifierDetail.as_view(),
        name="person-identifier-detail"),
    url(r'^(?P<language>\w{2})/persons/(?P<parent_pk>[-\w]+)/identifiers/?$', PersonIdentifierList.as_view(),
        name="person-identifier-list"),

    url(r'^(?P<language>\w{2})/persons/(?P<pk>[-\w]+)/?$', PersonDetail.as_view(), name="person-detail"),
    url(r'^(?P<language>\w{2})/persons/?$', PersonList.as_view(), name="person-list"),

    url('^(?P<language>\w{2})/organizations/(?P<parent>[-\w]+)/citations/(?P<field>\w+)/(?P<pk>[-\w]+)/?$',
        OrganizationCitationDetailView.as_view(), name="organization-citation-detail-view"),
    url('^(?P<language>\w{2})/organizations/(?P<pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        OrganizationCitationListCreateView.as_view(), name="organization-citation-list-view"),
    url('^(?P<language>\w{2})/organizations/(?P<pk>[-\w]+)/citations/?$', OrganizationFieldCitationView.as_view(),
        name="organization-citation-field-view"),

    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/(?P<link_id>[-\w]+)/?$',
        OrganizationContactDetailCitationDetailView.as_view(), name="organization-contact-detail-ciitation-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        OrganizationContactDetailCitationListView.as_view(), name="organization-contact-details-citation-views"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/?$',
        OrganizationContactDetailFieldCitationView.as_view(), name="organization-contact-details-field-citation"),

    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        OrganizationContactDetailLinkDetail.as_view(), name="organization-contact-detail-link-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/?$', OrganizationContactDetailLinkList.as_view(),
        name="organization-contact-detail-link-list"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/?$', OrganizationContactDetailDetail.as_view(),
        name="organization-contact-detail-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/contact_details/?$', OrganizationContactDetailList.as_view(),
        name="organization-contact-detail-list"),

    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/links/(?P<pk>[-\w]+)/?$', OrganizationLinkDetail.as_view(),
        name="organization-link-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/links/?$', OrganizationLinkList.as_view(),
        name="organization-link-list"),

    url(r'(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/othernames/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/(?P<link_id>[-\w]+)/?$',
        OrganizationOthernameCitationDetailView.as_view(), name="person-othername-citation-detail"),
    url(r'(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/othernames/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        OrganizationOthernameCitationListView.as_view(), name="person-othername-citation-list"),
    url(r'(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/othernames/(?P<child_pk>[-\w]+)/citations/?$',
        OrganizationOtherNameFieldCitationView.as_view(), name="person-othername-field-citation-view"),

    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/othernames/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        OrganizationOtherNameLinkDetail.as_view(), name="organization-othername-link-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/othernames/(?P<pk>[-\w]+)/links/?$',
        OrganizationOtherNameLinkList.as_view(), name="organization-othername-link-list"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/othernames/(?P<pk>[-\w]+)/?$', OrganizationOtherNameDetail.as_view(),
        name="organization-othername-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/othernames/?$', OrganizationOtherNameList.as_view(),
        name="organization-othername-list"),

    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/identifiers/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/(?P<link_id>[-\w]+)/?$',
        OrganizationIdentifierCitationDetailView.as_view(), name="organization-identifier-citation-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/identifiers/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        OrganizationIdentifierCitationListView.as_view(), name="organization-identifier-citation-list"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/identifiers/(?P<child_pk>[-\w]+)/citations/?$',
        OrganizationIdentifierFieldCitationView.as_view(), name="organization-identifier-field-citation"),

    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/identifiers/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        OrganizationIdentifierLinkDetail.as_view(), name="organization-identifier-link-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/identifiers/(?P<pk>[-\w]+)/links/?$',
        OrganizationIdentifierLinkList.as_view(), name="organization-identifier-link-list"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/identifiers/(?P<pk>[-\w]+)/?$', OrganizationIdentifierDetail.as_view(),
        name="organization-identifier-detail"),
    url(r'^(?P<language>\w{2})/organizations/(?P<parent_pk>[-\w]+)/identifiers/?$', OrganizationIdentifierList.as_view(),
        name="organization-identifier-list"),

    url(r'^(?P<language>\w{2})/organizations/(?P<pk>[-\w]+)/?$', OrganizationDetail.as_view(), name="organization-detail"),
    url(r'^(?P<language>\w{2})/organizations/?$', OrganizationList.as_view(), name="organization-list"),

    url(r'^(?P<language>\w{2})/areas/(?P<parent_pk>[-\w]+)/links/(?P<pk>[-\w]+)/?$', AreaLinkDetail.as_view(),
        name="area-link-detail"),
    url(r'^(?P<language>\w{2})/areas/(?P<parent_pk>[-\w]+)/links/?$', AreaLinkList.as_view(), name="area-link-list"),
    url(r'^(?P<language>\w{2})/areas/(?P<pk>[-\w]+)/?$', AreaDetail.as_view(), name="area-detail"),
    url(r'^(?P<language>\w{2})/areas/?$', AreaList.as_view(), name="area-list"),

    url(r'^(?P<language>\w{2})/memberships/(?P<parent>[-\w]+)/citations/(?P<field>\w+)/(?P<pk>[-\w]+)/?$',
        MembershipCitationDetailView.as_view(), name="membership-citation-detail"),
    url(r'^(?P<language>\w{2})/memberships/(?P<pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        MembershipCitationListCreateView.as_view(), name="membership-citation-list"),
    url(r'^(?P<language>\w{2})/memberships/(?P<pk>[-\w]+)/citations/?$', MembershipFieldCitationView.as_view(),
        name="membership-field-citation-view"),

    url(
        r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/(?P<link_id>[-\w]+)/?$',
        MembershipContactDetailCitationDetailView.as_view(), name="membership-contact-detail-citation-detail"
    ),
    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/(?P<field>\w+)/?$',
        MembershipContactDetailCitationListView.as_view(), name="membership-contact-detaion-citation-list"),
    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/contact_details/(?P<child_pk>[-\w]+)/citations/?$',
        MembershipContactDetailFieldCitationView.as_view(), name="membership-contact-detail-field-citation"),

    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/(?P<link_pk>[-\w]+)/?$',
        MembershipContactDetailLinkDetail.as_view(), name="membership-contact-detail-link-detail"),
    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/links/?$', MembershipContactDetailLinkList.as_view(),
        name="membership-contact-detail-link-list"),
    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/contact_details/(?P<pk>[-\w]+)/?$', MembershipContactDetailDetail.as_view(),
        name="membership-contact-detail-detail"),
    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/contact_details/?$', MembershipContactDetailList.as_view(),
        name="membership-contact-detail-list"),

    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/links/(?P<pk>[-\w]+)/?$', MembershipLinkDetail.as_view(),
        name="membership-link-detail"),
    url(r'^(?P<language>\w{2})/memberships/(?P<parent_pk>[-\w]+)/links/?$', MembershipLinkList.as_view(),
        name="membership-link-list"),
    url(r'^(?P<language>\w{2})/memberships/(?P<pk>[-\w]+)/?$', MembershipDetail.as_view(),
        name="membership-detail"),
    url(r'^(?P<language>\w{2})/memberships/?$', MembershipList.as_view(), name="membership-list"),
    url(r'^(?P<language>\w{2})', api_root, name="api-root"),
    url(r'^$', api_root_all),
 ]

api_urls = format_suffix_patterns(api_urls)
urlpatterns += api_urls


