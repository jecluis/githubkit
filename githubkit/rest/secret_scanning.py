"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Missing, exclude_unset

from .types import ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
from .models import (
    BasicError,
    SecretScanningAlert,
    SecretScanningLocation,
    OrganizationSecretScanningAlert,
    ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody,
    EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class SecretScanningClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        direction: Missing[Literal["asc", "desc"]] = "desc",
        per_page: Missing[int] = 30,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_enterprise(
        self,
        enterprise: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        direction: Missing[Literal["asc", "desc"]] = "desc",
        per_page: Missing[int] = 30,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/enterprises/{enterprise}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_org(
        self,
        org: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        direction: Missing[Literal["asc", "desc"]] = "desc",
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_org(
        self,
        org: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        direction: Missing[Literal["asc", "desc"]] = "desc",
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
    ) -> "Response[List[OrganizationSecretScanningAlert]]":
        url = f"/orgs/{org}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[OrganizationSecretScanningAlert],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        direction: Missing[Literal["asc", "desc"]] = "desc",
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
    ) -> "Response[List[SecretScanningAlert]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        state: Missing[Literal["open", "resolved"]] = UNSET,
        secret_type: Missing[str] = UNSET,
        resolution: Missing[str] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        direction: Missing[Literal["asc", "desc"]] = "desc",
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
    ) -> "Response[List[SecretScanningAlert]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts"

        params = {
            "state": state,
            "secret_type": secret_type,
            "resolution": resolution,
            "sort": sort,
            "direction": direction,
            "page": page,
            "per_page": per_page,
            "before": before,
            "after": after,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningAlert],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[SecretScanningAlert]":
        ...

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Literal[UNSET] = UNSET,
        state: Literal["open", "resolved"],
        resolution: Missing[
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ]
        ] = UNSET,
        resolution_comment: Missing[Union[str, None]] = UNSET,
    ) -> "Response[SecretScanningAlert]":
        ...

    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Missing[
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[SecretScanningAlert]":
        ...

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Literal[UNSET] = UNSET,
        state: Literal["open", "resolved"],
        resolution: Missing[
            Union[
                None, Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]
            ]
        ] = UNSET,
        resolution_comment: Missing[Union[str, None]] = UNSET,
    ) -> "Response[SecretScanningAlert]":
        ...

    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Missing[
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBodyType
        ] = UNSET,
        **kwargs,
    ) -> "Response[SecretScanningAlert]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            ReposOwnerRepoSecretScanningAlertsAlertNumberPatchBody, json
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=SecretScanningAlert,
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
    ) -> "Response[List[SecretScanningLocation]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_locations_for_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
    ) -> "Response[List[SecretScanningLocation]]":
        url = f"/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations"

        params = {
            "page": page,
            "per_page": per_page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[SecretScanningLocation],
            error_models={
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )
