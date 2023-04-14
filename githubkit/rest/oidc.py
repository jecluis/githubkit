"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Missing, exclude_unset

from .types import OidcCustomSubType
from .models import BasicError, EmptyObject, OidcCustomSub

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class OidcClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def get_oidc_custom_sub_template_for_org(
        self,
        org: str,
    ) -> "Response[OidcCustomSub]":
        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OidcCustomSub,
        )

    async def async_get_oidc_custom_sub_template_for_org(
        self,
        org: str,
    ) -> "Response[OidcCustomSub]":
        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=OidcCustomSub,
        )

    @overload
    def update_oidc_custom_sub_template_for_org(
        self, org: str, *, data: OidcCustomSubType
    ) -> "Response[EmptyObject]":
        ...

    @overload
    def update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        include_claim_keys: List[str],
    ) -> "Response[EmptyObject]":
        ...

    def update_oidc_custom_sub_template_for_org(
        self, org: str, *, data: Missing[OidcCustomSubType] = UNSET, **kwargs
    ) -> "Response[EmptyObject]":
        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OidcCustomSub, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    @overload
    async def async_update_oidc_custom_sub_template_for_org(
        self, org: str, *, data: OidcCustomSubType
    ) -> "Response[EmptyObject]":
        ...

    @overload
    async def async_update_oidc_custom_sub_template_for_org(
        self,
        org: str,
        *,
        data: Literal[UNSET] = UNSET,
        include_claim_keys: List[str],
    ) -> "Response[EmptyObject]":
        ...

    async def async_update_oidc_custom_sub_template_for_org(
        self, org: str, *, data: Missing[OidcCustomSubType] = UNSET, **kwargs
    ) -> "Response[EmptyObject]":
        url = f"/orgs/{org}/actions/oidc/customization/sub"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(OidcCustomSub, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )
