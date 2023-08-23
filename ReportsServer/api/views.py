"""
api/views.py

Created by: Gabriel Menezes de Antonio
"""
from hashlib import md5, sha512
from typing import Any, Optional, TypeAlias
from uuid import uuid4
from random import randint

import coreapi  # type: ignore

from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.schemas.coreapi import AutoSchema
from rest_framework.views import APIView

from api.tools.api_tools import description_generator, generate_version


User = get_user_model()


# =================== Base API Class =================== #
class Base(APIView):
    """Base API class"""
    __api_token__: TypeAlias = Optional[str]
    __response_data__: TypeAlias = dict[str, Any]

    def generate_basic_response(self, status_code: int, message: str) -> Response:
        """Generates a basic response"""
        data = self.generate_basic_response_data(status_code, message)
        return Response(data=data, status=data.get('status'))

    def generate_basic_response_data(self, status_code: int, message: str) -> __response_data__:
        """Generates a basic response data"""
        return {
            'status': status_code,
            'message': message
        }


# =================== API Built-In Info =================== #
class StatusSchema(AutoSchema):
    """Schema for status endpoint"""
    def get_description(self, path: str, method: str) -> str:
        match method:
            case 'GET':
                responses = {
                    "200": {
                        'description': 'OK',
                        'reason': 'API reachable and responsive'
                    }
                }
                return description_generator(title="Check API reachability",
                                             description="",
                                             responses=responses)
            case _:
                return ''

    def get_path_fields(self, path: str, method: str) -> list[coreapi.Field]:
        match method:
            case _:
                return []


class ApiStatus(Base):
    """Checks API reachability."""

    schema = StatusSchema()

    def get(self, request):
        """Get request"""
        return self.generate_basic_response(status.HTTP_200_OK, 'API running')


class VersionSchema(AutoSchema):
    """Schema for version endpoint"""
    def get_description(self, path: str, method: str) -> str:
        match method:
            case 'GET':
                responses = {
                    "200": {
                        'description': 'OK',
                        'reason': 'API Version and environment fetched successfully'
                    },
                }
                return description_generator(title="Fetches API version and environment",
                                             description='',
                                             responses=responses)
            case _:
                return ''

    def get_path_fields(self, path: str, method: str) -> list[coreapi.Field]:
        match method:
            case _:
                return []


class ApiVersion(Base):
    """Returns API version and its environment"""

    schema = VersionSchema()

    def get(self, request):
        """Get request"""
        data = self.generate_basic_response_data(status.HTTP_200_OK, 'API version')
        data['version'] = generate_version()
        return Response(data=data, status=data.get('status'))
