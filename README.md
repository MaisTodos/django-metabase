# django-metabase

```
INSTALLED_APPS = [
   "metabase",
]
```

```settings.py
METABASE_SECRECT_KEY = os.environ.get("METABASE_SECRECT_KEY", "1")
METABASE_SITE_URL = os.environ.get("METABASE_SITE_URL", "url_base_do_dash")

# optionals
METABASE_DEFAULT_HEIGHT = "800px"  # default
METABASE_DEFAULT_WIDTH = "100%"  # default
METABASE_DEFAULT_EXPIRATION = (60 * 60 * 6)  # default
```
