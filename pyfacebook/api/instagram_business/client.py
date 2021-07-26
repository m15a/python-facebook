"""
    Client for Instagram Graph API.
"""

from pyfacebook.api.base_client import BaseApi
from pyfacebook.api.instagram_business import resource as rs


class IGBusinessApi(BaseApi):
    """
    Api class for Instagram Business
    """

    user = rs.IGBusinessUser()
