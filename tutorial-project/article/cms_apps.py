# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ArticleHook(CMSApp):
    name = _("Article")
    urls = ["article.urls"]
    app_name = "article"

apphook_pool.register(ArticleHook)
