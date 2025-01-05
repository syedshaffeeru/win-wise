import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time

# ==============================================================
# HTTPSessionManager with Rate-Limiting and Retry Capabilities
# --------------------------------------------------------------
# Purpose:
# This module provides a robust session manager for making HTTP
# requests, with built-in support for:
# 1. Rate-limiting: Automatically handles 429 Too Many Requests
#    responses by respecting the Retry-After header.
# 2. Retry logic: Configurable retries for transient errors (e.g.,
#    500, 502, 503, 504) with backoff.
#
# Components:
# 1. RateLimitedAdapter:
#    - Extends HTTPAdapter to handle rate-limiting scenarios.
#    - Sleeps for the duration specified in the Retry-After header.
# 2. HTTPSessionManager:
#    - Configures a session with rate-limiting and retry behavior.
#    - Provides reusable sessions with connection pooling.
#
# Usage:
# 1. Import HTTPSessionManager.
# 2. Create an instance with custom retry policies.
# 3. Use the session to send GET, POST, or other HTTP requests.
# ==============================================================

class RateLimitedAdapter(HTTPAdapter):
    """An HTTPAdapter that handles rate-limiting via Retry-After header."""
    
    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        retry_after = self.get_retry_after(response)
        if response.status_code == 429 and retry_after:
            time.sleep(retry_after)  # Sleep as advised by Retry-After
            return super().send(request, **kwargs)
        return response

    @staticmethod
    def get_retry_after(response):
        """Extract Retry-After header value (if present)."""
        retry_after = response.headers.get('Retry-After')
        return int(retry_after) if retry_after and retry_after.isdigit() else None

class HTTPSessionManager:
    """Manages an HTTP session with retry and rate-limiting support."""
    
    def __init__(self, total_retries=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]):
        """
        Initialize the session manager.
        
        Args:
            total_retries (int): Maximum number of retries.
            backoff_factor (float): Delay multiplier for retries.
            status_forcelist (list): HTTP status codes to retry.
        """
        self.total_retries = total_retries
        self.backoff_factor = backoff_factor
        self.status_forcelist = status_forcelist
        self.session = None

    def setup_session(self):
        """Set up a session with rate-limiting and retry configuration."""
        self.session = requests.Session()
        retries = Retry(
            total=self.total_retries,
            backoff_factor=self.backoff_factor,
            status_forcelist=self.status_forcelist,
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        adapter = RateLimitedAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        return self.session

    def get_session(self):
        """Return an existing session or create a new one if none exists."""
        if not self.session:
            return self.setup_session()
        return self.session
