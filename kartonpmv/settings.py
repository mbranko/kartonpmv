import logging
import os

log = logging.getLogger()

if 'DJANGO_SETTINGS' in os.environ:
    cfg = os.environ['DJANGO_SETTINGS']
    if cfg == "dev":
        log.info('Configuration: dev')
        from kartonpmv.app_settings.dev import *
    elif cfg == "prod":
        log.info('Configuration: prod')
        from kartonpmv.app_settings.prod import *
    elif cfg == "test":
        log.info('Configuration: test')
        from kartonpmv.app_settings.test import *
    else:
        log.fatal('Unknown configuration')
else:
    log.info('Configuration not set, defaulting to: dev')
    from kartonpmv.app_settings.dev import *
