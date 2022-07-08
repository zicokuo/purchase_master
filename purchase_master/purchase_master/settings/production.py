from .base import *

DEBUG = False

try:
    from .local import *

    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn="https://9f367463d7254f96b00a0a0711a7a6c9@o1280570.ingest.sentry.io/6555945",
        integrations=[
            DjangoIntegration(),
        ],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
        release=True,
    )
except ImportError:
    pass
