"""
URLConf for Cab.

Recommended usage is to use a call to ``include()`` in your project's
root URLConf to include this URLConf for any URL beginning with
'/snippets/'.

"""

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list
from django.contrib.auth.models import User
from django.contrib.syndication.views import feed
import feeds
from models import Language, Snippet, Tag
from views import bookmarks, popular, snippets

# Info for feeds.
feed_dict = {
    'author': feeds.SnippetsByAuthorFeed,
    'language': feeds.SnippetsByLanguageFeed,
    'latest': feeds.LatestSnippetsFeed,
    'tag': feeds.SnippetsByTagFeed,
    }

# Info for generic views.
base_generic_dict = {
    'paginate_by': 20,
    }

language_info_dict = dict(base_generic_dict,
                          queryset=Language.objects.all())

snippet_info_dict = dict(base_generic_dict,
                         queryset=Snippet.objects.all())

tag_info_dict = dict(base_generic_dict,
                     queryset=Tag.objects.all())

user_info_dict = dict(base_generic_dict,
                      queryset=User.objects.all(),
                      template_name='cab/user_list.html')

# General snippets views.
urlpatterns = patterns('',
                       url(r'^(?P<snippet_id>\d+)/$', snippets.snippet_detail, name='snippet_detail'),
                       url(r'^(?P<snippet_id>\d+)/download/$', snippets.download, name='snippet_download'),
                       url(r'^add/$', snippets.add_snippet, name='add_snippet'),
                       url(r'^edit/(?P<snippet_id>\d+)/$', snippets.edit_snippet, name='edit_snippet'),
                       url(r'^languages/(?P<slug>[\w-]+)$', snippets.snippets_by_language, name='snippets_by_language'),
                       url(r'^rate/(?P<snippet_id>\d+)/$', snippets.rate_snippet, name='rate_snippet'),
                       url(r'^tags/(?P<slug>[\w-]+)/$', snippets.snippets_by_tag, name='snippets_by_tag'),
                       url(r'^users/(?P<username>[^/]+)/$', snippets.snippets_by_author, name='snippets_by_author'),
                       )

# Views that work with bookmarks.
urlpatterns += patterns('',
                        url(r'^bookmarks/$', bookmarks.bookmarks, name='bookmarks'),
                        url(r'^bookmarks/add/(?P<snippet_id>\d+)/$', bookmarks.add_bookmark, name='add_bookmark'),
                        url(r'^bookmarks/author/(?P<author_username>[\w-]+)/$', bookmarks.bookmarks_by_author, name='bookmarks_by_author'),
                        url(r'^bookmarks/delete/(?P<bookmark_id>\d+)/$', bookmarks.delete_bookmark, name='delete_bookmark'),
                        url(r'^bookmarks/language/(?P<language_slug>[\w-]+)/$', bookmarks.bookmarks_by_language, name='bookmarks_by_language'),
                        url(r'^bookmarks/tag/(?P<tag_slug>[\w-]+)/$', bookmarks.bookmarks_by_tag, name='bookmarks_by_tag'),
                        )

# Views for popular items.
urlpatterns += patterns('',
                        # Need a better URL for this one. (r'^popular/authors/$', popular.top_authors),
                        url(r'^popular/bookmarks/$', popular.most_bookmarked, name='most_bookmarked'),
                        url(r'^popular/languages/$', popular.top_languages, name='top_languages'),
                        url(r'^popular/top-rated/$', popular.top_rated, name='top_rated'),
                        url(r'^popular/tags/$', popular.top_tags, name='top_tags'),
                        )

# Generic views.
urlpatterns += patterns('',
                        url(r'^$', object_list, snippet_info_dict, name='index'),
                        url(r'^feeds/(?P<url>.*)/$', feed, feed_dict, name='feed'),
                        url(r'^languages/$', object_list, language_info_dict, name='languages'),
                        url(r'^tags/$', object_list, tag_info_dict, name='tags'),
                        url(r'^users/$', object_list, user_info_dict, name='users'),
                        )
