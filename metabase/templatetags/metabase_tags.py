
import time

import jwt
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


METABASE_SECRECT_KEY = getattr(settings, "METABASE_SECRECT_KEY", "")
METABASE_SITE_URL = getattr(settings, "METABASE_SITE_URL", "")
METABASE_DEFAULT_HEIGHT = getattr(settings, "METABASE_DEFAULT_HEIGHT", "800px")
METABASE_DEFAULT_WIDTH = getattr(settings, "METABASE_DEFAULT_WIDTH", "100%")
METABASE_DEFAULT_EXPIRATION = getattr(settings, "METABASE_DEFAULT_EXPIRATION", (60 * 60 * 6))


METABASE_IFRAME = """<iframe
    src="{{ iframeUrl }}"
    frameborder="0"
    width="{{ width }}"
    height="{{ height }}"
    allowtransparency
></iframe>"""


@register.simple_tag
def render_metabase_dashboard(context, dashboard, *args, **kwargs):

    payload = {
        "resource": {"dashboard": int(dashboard)},
        "params": {},
        "exp": round(time.time()) + METABASE_DEFAULT_EXPIRATION,
    }

    width = kwargs.get("width", METABASE_DEFAULT_WIDTH)
    height = kwargs.get("height", METABASE_DEFAULT_HEIGHT)

    token = jwt.encode(payload, METABASE_SECRECT_KEY, algorithm="HS256")
    iframeUrl = (
        METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=false"
    )

    data = {
        "iframeUrl": iframeUrl,
        "width": width,
        "height": height,
    }

    template = Template(METABASE_IFRAME)
    context = Context(data)
    iframe = template.render(context)
    return mark_safe(iframe)
