import abc
import requests
import logging

from apps.greencheck.management.commands.importer_interface import BaseImporter, Importer

from django.core.management.base import BaseCommand
from django.conf import settings

logger = logging.getLogger(__name__)

class EquinixImporter(BaseImporter):
    def __init__(cls):
        cls.hosting_provider_id = settings.EQUINIX_PROVIDER_ID

    def fetch_data_from_source(cls) -> list:
        try:
            response = requests.get(settings.EQUINIX_DATASET_ENDPOINT)
            return cls.parse_to_list(response.text)
        except requests.RequestException:
            logger.warning("Unable to fetch text file. Aborting early.")

    def parse_to_list(cls, raw_data) -> list:
        try:
            list_of_ips = []
            for line in raw_data.splitlines():
                # Filter out the lines with network information
                # (i.e. ip with subnet or AS numbers)
                if line.startswith("AS") or line[0].isdigit():
                    list_of_ips.append(
                        line.split(" ", 1)[0]
                    )  # Format as follows: IP range/ASN, Naming

            return list_of_ips
        except Exception as e:
            logger.exception("Something really unexpected happened. Aborting")

class Command(BaseCommand):
    help = "Update IP ranges for cloud providers that publish them"

    def handle(self, *args, **options):
        importer = EquinixImporter()
        data = importer.fetch_data_from_source()
        importer.process_addresses(data)

        # TODO: Implement output