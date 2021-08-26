# django-metabase

Atualize o seu arquivo de requirements com a versão que quiser do django-metabase
```requirements.txt
git+https://github.com/MaisTodos/django-metabase@v1.1
```

Depois, você precisa configurar o seu settings, com o setup básico do metabase
```settings.py
INSTALLED_APPS = [
   "metabase",
]

METABASE_SECRECT_KEY = os.environ.get("METABASE_SECRECT_KEY", "1")
METABASE_SITE_URL = os.environ.get("METABASE_SITE_URL", "url_base_do_dash")

# optionals
METABASE_DEFAULT_HEIGHT = "800px"  # default
METABASE_DEFAULT_WIDTH = "100%"  # default
METABASE_DEFAULT_EXPIRATION = (60 * 60 * 6)  # default

# filtros
METABASE_PARAMS_KEYS = ["filtro_a", "filtro_b"]
```

Como utilizar, no template
```template.html
{% load metabase_tags %}

{% render_metabase_dashboard request <matabase_id> height='2000px' width='2000px' filtro_a=valor filtro_b=valor %}

```
