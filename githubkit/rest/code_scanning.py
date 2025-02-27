"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Union, Literal, Optional, overload

from pydantic import BaseModel, TypeAdapter

from githubkit.utils import UNSET, Missing, exclude_unset

from .types import (
    CodeScanningDefaultSetupUpdateType,
    ReposOwnerRepoCodeScanningSarifsPostBodyType,
    ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType,
)
from .models import (
    BasicError,
    EmptyObject,
    CodeScanningAlert,
    CodeScanningAnalysis,
    CodeScanningAlertItems,
    CodeScanningDefaultSetup,
    CodeScanningSarifsStatus,
    CodeScanningAlertInstance,
    CodeScanningSarifsReceipt,
    CodeScanningCodeqlDatabase,
    CodeScanningAnalysisDeletion,
    CodeScanningDefaultSetupUpdate,
    CodeScanningOrganizationAlertItems,
    ReposOwnerRepoCodeScanningSarifsPostBody,
    ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody,
    EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class CodeScanningClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_alerts_for_org(
        self,
        org: str,
        tool_name: Missing[str] = UNSET,
        tool_guid: Missing[Union[str, None]] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        state: Missing[Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        severity: Missing[
            Literal["critical", "high", "medium", "low", "warning", "note", "error"]
        ] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningOrganizationAlertItems]]":
        url = f"/orgs/{org}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "before": before,
            "after": after,
            "page": page,
            "per_page": per_page,
            "direction": direction,
            "state": state,
            "sort": sort,
            "severity": severity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningOrganizationAlertItems],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_org(
        self,
        org: str,
        tool_name: Missing[str] = UNSET,
        tool_guid: Missing[Union[str, None]] = UNSET,
        before: Missing[str] = UNSET,
        after: Missing[str] = UNSET,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        state: Missing[Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        sort: Missing[Literal["created", "updated"]] = "created",
        severity: Missing[
            Literal["critical", "high", "medium", "low", "warning", "note", "error"]
        ] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningOrganizationAlertItems]]":
        url = f"/orgs/{org}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "before": before,
            "after": after,
            "page": page,
            "per_page": per_page,
            "direction": direction,
            "state": state,
            "sort": sort,
            "severity": severity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningOrganizationAlertItems],
            error_models={
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        tool_name: Missing[str] = UNSET,
        tool_guid: Missing[Union[str, None]] = UNSET,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        ref: Missing[str] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        sort: Missing[Literal["created", "updated"]] = "created",
        state: Missing[Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        severity: Missing[
            Literal["critical", "high", "medium", "low", "warning", "note", "error"]
        ] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningAlertItems]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "direction": direction,
            "sort": sort,
            "state": state,
            "severity": severity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alerts_for_repo(
        self,
        owner: str,
        repo: str,
        tool_name: Missing[str] = UNSET,
        tool_guid: Missing[Union[str, None]] = UNSET,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        ref: Missing[str] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        sort: Missing[Literal["created", "updated"]] = "created",
        state: Missing[Literal["open", "closed", "dismissed", "fixed"]] = UNSET,
        severity: Missing[
            Literal["critical", "high", "medium", "low", "warning", "note", "error"]
        ] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningAlertItems]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "direction": direction,
            "sort": sort,
            "state": state,
            "severity": severity,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningAlertItems],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
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
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[CodeScanningAlert]":
        ...

    @overload
    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        state: Literal["open", "dismissed"],
        dismissed_reason: Missing[
            Union[None, Literal["false positive", "won't fix", "used in tests"]]
        ] = UNSET,
        dismissed_comment: Missing[Union[str, None]] = UNSET,
    ) -> "Response[CodeScanningAlert]":
        ...

    def update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(
            ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody
        ).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
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
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType,
    ) -> "Response[CodeScanningAlert]":
        ...

    @overload
    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        state: Literal["open", "dismissed"],
        dismissed_reason: Missing[
            Union[None, Literal["false positive", "won't fix", "used in tests"]]
        ] = UNSET,
        dismissed_comment: Missing[Union[str, None]] = UNSET,
    ) -> "Response[CodeScanningAlert]":
        ...

    async def async_update_alert(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningAlert]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(
            ReposOwnerRepoCodeScanningAlertsAlertNumberPatchBody
        ).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeScanningAlert,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_alert_instances(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        ref: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningAlertInstance]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances"

        params = {
            "page": page,
            "per_page": per_page,
            "ref": ref,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningAlertInstance],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_alert_instances(
        self,
        owner: str,
        repo: str,
        alert_number: int,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        ref: Missing[str] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningAlertInstance]]":
        url = f"/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances"

        params = {
            "page": page,
            "per_page": per_page,
            "ref": ref,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningAlertInstance],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_recent_analyses(
        self,
        owner: str,
        repo: str,
        tool_name: Missing[str] = UNSET,
        tool_guid: Missing[Union[str, None]] = UNSET,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        ref: Missing[str] = UNSET,
        sarif_id: Missing[str] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        sort: Missing[Literal["created"]] = "created",
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningAnalysis]]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "sarif_id": sarif_id,
            "direction": direction,
            "sort": sort,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningAnalysis],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_recent_analyses(
        self,
        owner: str,
        repo: str,
        tool_name: Missing[str] = UNSET,
        tool_guid: Missing[Union[str, None]] = UNSET,
        page: Missing[int] = 1,
        per_page: Missing[int] = 30,
        ref: Missing[str] = UNSET,
        sarif_id: Missing[str] = UNSET,
        direction: Missing[Literal["asc", "desc"]] = "desc",
        sort: Missing[Literal["created"]] = "created",
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningAnalysis]]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses"

        params = {
            "tool_name": tool_name,
            "tool_guid": tool_guid,
            "page": page,
            "per_page": per_page,
            "ref": ref,
            "sarif_id": sarif_id,
            "direction": direction,
            "sort": sort,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CodeScanningAnalysis],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningAnalysis]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningAnalysis,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningAnalysis]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningAnalysis,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def delete_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
        confirm_delete: Missing[Union[str, None]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningAnalysisDeletion]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        params = {
            "confirm_delete": confirm_delete,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "DELETE",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=CodeScanningAnalysisDeletion,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_delete_analysis(
        self,
        owner: str,
        repo: str,
        analysis_id: int,
        confirm_delete: Missing[Union[str, None]] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningAnalysisDeletion]":
        url = f"/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}"

        params = {
            "confirm_delete": confirm_delete,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "DELETE",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=CodeScanningAnalysisDeletion,
            error_models={
                "400": BasicError,
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def list_codeql_databases(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningCodeqlDatabase]]":
        url = f"/repos/{owner}/{repo}/code-scanning/codeql/databases"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeScanningCodeqlDatabase],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_list_codeql_databases(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[List[CodeScanningCodeqlDatabase]]":
        url = f"/repos/{owner}/{repo}/code-scanning/codeql/databases"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=List[CodeScanningCodeqlDatabase],
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_codeql_database(
        self,
        owner: str,
        repo: str,
        language: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningCodeqlDatabase]":
        url = f"/repos/{owner}/{repo}/code-scanning/codeql/databases/{language}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningCodeqlDatabase,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_codeql_database(
        self,
        owner: str,
        repo: str,
        language: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningCodeqlDatabase]":
        url = f"/repos/{owner}/{repo}/code-scanning/codeql/databases/{language}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningCodeqlDatabase,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningDefaultSetup]":
        url = f"/repos/{owner}/{repo}/code-scanning/default-setup"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningDefaultSetup,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningDefaultSetup]":
        url = f"/repos/{owner}/{repo}/code-scanning/default-setup"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningDefaultSetup,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    def update_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: CodeScanningDefaultSetupUpdateType,
    ) -> "Response[EmptyObject]":
        ...

    @overload
    def update_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        state: Literal["configured", "not-configured"],
        query_suite: Missing[Literal["default", "extended"]] = UNSET,
        languages: Missing[
            List[
                Literal[
                    "c-cpp",
                    "csharp",
                    "go",
                    "java-kotlin",
                    "javascript-typescript",
                    "python",
                    "ruby",
                    "swift",
                ]
            ]
        ] = UNSET,
    ) -> "Response[EmptyObject]":
        ...

    def update_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[CodeScanningDefaultSetupUpdateType] = UNSET,
        **kwargs,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/code-scanning/default-setup"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(CodeScanningDefaultSetupUpdate).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_update_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: CodeScanningDefaultSetupUpdateType,
    ) -> "Response[EmptyObject]":
        ...

    @overload
    async def async_update_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        state: Literal["configured", "not-configured"],
        query_suite: Missing[Literal["default", "extended"]] = UNSET,
        languages: Missing[
            List[
                Literal[
                    "c-cpp",
                    "csharp",
                    "go",
                    "java-kotlin",
                    "javascript-typescript",
                    "python",
                    "ruby",
                    "swift",
                ]
            ]
        ] = UNSET,
    ) -> "Response[EmptyObject]":
        ...

    async def async_update_default_setup(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[CodeScanningDefaultSetupUpdateType] = UNSET,
        **kwargs,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/code-scanning/default-setup"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(CodeScanningDefaultSetupUpdate).validate_python(json)
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "409": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    def upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCodeScanningSarifsPostBodyType,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    @overload
    def upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        commit_sha: str,
        ref: str,
        sarif: str,
        checkout_uri: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        tool_name: Missing[str] = UNSET,
        validate_: Missing[bool] = UNSET,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    def upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCodeScanningSarifsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningSarifsReceipt]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoCodeScanningSarifsPostBody).validate_python(
            json
        )
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeScanningSarifsReceipt,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    @overload
    async def async_upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCodeScanningSarifsPostBodyType,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    @overload
    async def async_upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        commit_sha: str,
        ref: str,
        sarif: str,
        checkout_uri: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        tool_name: Missing[str] = UNSET,
        validate_: Missing[bool] = UNSET,
    ) -> "Response[CodeScanningSarifsReceipt]":
        ...

    async def async_upload_sarif(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCodeScanningSarifsPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CodeScanningSarifsReceipt]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = TypeAdapter(ReposOwnerRepoCodeScanningSarifsPostBody).validate_python(
            json
        )
        json = json.model_dump(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CodeScanningSarifsReceipt,
            error_models={
                "403": BasicError,
                "404": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    def get_sarif(
        self,
        owner: str,
        repo: str,
        sarif_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningSarifsStatus]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningSarifsStatus,
            error_models={
                "403": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )

    async def async_get_sarif(
        self,
        owner: str,
        repo: str,
        sarif_id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> "Response[CodeScanningSarifsStatus]":
        url = f"/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CodeScanningSarifsStatus,
            error_models={
                "403": BasicError,
                "503": EnterprisesEnterpriseSecretScanningAlertsGetResponse503,
            },
        )
