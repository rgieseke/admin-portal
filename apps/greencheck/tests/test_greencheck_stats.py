import pytest
import logging

from apps.greencheck.legacy_workers import LegacySiteCheckLogger, SiteCheck
from apps.greencheck.models import Greencheck, GreenDomain
from apps.accounts.models import Hostingprovider


console = logging.StreamHandler()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(console)


# (1) number of checks past 24 hours
# (2) number of those checks labeled as green
# (3) number of checks per TLD
# (4) number of checks green per TLD
# (5) number of checks for each listed green hoster (link to ID)
# (6) number of checks for each domain
