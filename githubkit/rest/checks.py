"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from datetime import datetime
from typing import TYPE_CHECKING, List, Union, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Missing, exclude_unset

from .models import (
    CheckRun,
    BasicError,
    CheckSuite,
    EmptyObject,
    CheckAnnotation,
    CheckSuitePreference,
    ReposOwnerRepoCheckSuitesPostBody,
    ReposOwnerRepoCheckRunsPostBodyOneof0,
    ReposOwnerRepoCheckRunsPostBodyOneof1,
    ReposOwnerRepoCheckSuitesPreferencesPatchBody,
    ReposOwnerRepoCommitsRefCheckRunsGetResponse200,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1,
    ReposOwnerRepoCommitsRefCheckSuitesGetResponse200,
    ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
)
from .types import (
    ReposOwnerRepoCheckSuitesPostBodyType,
    ReposOwnerRepoCheckRunsPostBodyOneof0Type,
    ReposOwnerRepoCheckRunsPostBodyOneof1Type,
    ReposOwnerRepoCheckRunsPostBodyPropOutputType,
    ReposOwnerRepoCheckSuitesPreferencesPatchBodyType,
    ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType,
    ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType,
    ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class ChecksClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    @overload
    def create(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[
            ReposOwnerRepoCheckRunsPostBodyOneof0Type,
            ReposOwnerRepoCheckRunsPostBodyOneof1Type,
        ],
    ) -> "Response[CheckRun]":
        ...

    @overload
    def create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Literal["completed"],
        started_at: Missing[datetime] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    @overload
    def create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        started_at: Missing[datetime] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    def create(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0Type,
                ReposOwnerRepoCheckRunsPostBodyOneof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> "Response[CheckRun]":
        url = f"/repos/{owner}/{repo}/check-runs"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0,
                ReposOwnerRepoCheckRunsPostBodyOneof1,
            ],
            json,
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    @overload
    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        data: Union[
            ReposOwnerRepoCheckRunsPostBodyOneof0Type,
            ReposOwnerRepoCheckRunsPostBodyOneof1Type,
        ],
    ) -> "Response[CheckRun]":
        ...

    @overload
    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Literal["completed"],
        started_at: Missing[datetime] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    @overload
    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        started_at: Missing[datetime] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0Type,
                ReposOwnerRepoCheckRunsPostBodyOneof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> "Response[CheckRun]":
        url = f"/repos/{owner}/{repo}/check-runs"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0,
                ReposOwnerRepoCheckRunsPostBodyOneof1,
            ],
            json,
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    def get(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
    ) -> "Response[CheckRun]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    async def async_get(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
    ) -> "Response[CheckRun]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    @overload
    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Union[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
        ],
    ) -> "Response[CheckRun]":
        ...

    @overload
    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["completed"]] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    @overload
    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> "Response[CheckRun]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1,
            ],
            json,
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    @overload
    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Union[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
        ],
    ) -> "Response[CheckRun]":
        ...

    @overload
    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["completed"]] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    @overload
    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> "Response[CheckRun]":
        ...

    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> "Response[CheckRun]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1,
            ],
            json,
        )
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    def list_annotations(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
    ) -> "Response[List[CheckAnnotation]]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations"

        params = {
            "per_page": per_page,
            "page": page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CheckAnnotation],
        )

    async def async_list_annotations(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
    ) -> "Response[List[CheckAnnotation]]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations"

        params = {
            "per_page": per_page,
            "page": page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CheckAnnotation],
        )

    def rerequest_run(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "403": BasicError,
                "422": BasicError,
                "404": BasicError,
            },
        )

    async def async_rerequest_run(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "403": BasicError,
                "422": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def create_suite(
        self, owner: str, repo: str, *, data: ReposOwnerRepoCheckSuitesPostBodyType
    ) -> "Response[CheckSuite]":
        ...

    @overload
    def create_suite(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        head_sha: str,
    ) -> "Response[CheckSuite]":
        ...

    def create_suite(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[ReposOwnerRepoCheckSuitesPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CheckSuite]":
        url = f"/repos/{owner}/{repo}/check-suites"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCheckSuitesPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    @overload
    async def async_create_suite(
        self, owner: str, repo: str, *, data: ReposOwnerRepoCheckSuitesPostBodyType
    ) -> "Response[CheckSuite]":
        ...

    @overload
    async def async_create_suite(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        head_sha: str,
    ) -> "Response[CheckSuite]":
        ...

    async def async_create_suite(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[ReposOwnerRepoCheckSuitesPostBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CheckSuite]":
        url = f"/repos/{owner}/{repo}/check-suites"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCheckSuitesPostBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    @overload
    def set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: ReposOwnerRepoCheckSuitesPreferencesPatchBodyType,
    ) -> "Response[CheckSuitePreference]":
        ...

    @overload
    def set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        auto_trigger_checks: Missing[
            List[
                ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType
            ]
        ] = UNSET,
    ) -> "Response[CheckSuitePreference]":
        ...

    def set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[ReposOwnerRepoCheckSuitesPreferencesPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CheckSuitePreference]":
        url = f"/repos/{owner}/{repo}/check-suites/preferences"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCheckSuitesPreferencesPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuitePreference,
        )

    @overload
    async def async_set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: ReposOwnerRepoCheckSuitesPreferencesPatchBodyType,
    ) -> "Response[CheckSuitePreference]":
        ...

    @overload
    async def async_set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        auto_trigger_checks: Missing[
            List[
                ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType
            ]
        ] = UNSET,
    ) -> "Response[CheckSuitePreference]":
        ...

    async def async_set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: Missing[ReposOwnerRepoCheckSuitesPreferencesPatchBodyType] = UNSET,
        **kwargs,
    ) -> "Response[CheckSuitePreference]":
        url = f"/repos/{owner}/{repo}/check-suites/preferences"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(ReposOwnerRepoCheckSuitesPreferencesPatchBody, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuitePreference,
        )

    def get_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
    ) -> "Response[CheckSuite]":
        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    async def async_get_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
    ) -> "Response[CheckSuite]":
        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    def list_for_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = "latest",
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
    ) -> "Response[ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200]":
        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
        )

    async def async_list_for_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = "latest",
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
    ) -> "Response[ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200]":
        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
        )

    def rerequest_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
        )

    async def async_rerequest_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
        )

    def list_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = "latest",
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
        app_id: Missing[int] = UNSET,
    ) -> "Response[ReposOwnerRepoCommitsRefCheckRunsGetResponse200]":
        url = f"/repos/{owner}/{repo}/commits/{ref}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
            "app_id": app_id,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckRunsGetResponse200,
        )

    async def async_list_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = "latest",
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
        app_id: Missing[int] = UNSET,
    ) -> "Response[ReposOwnerRepoCommitsRefCheckRunsGetResponse200]":
        url = f"/repos/{owner}/{repo}/commits/{ref}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
            "app_id": app_id,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckRunsGetResponse200,
        )

    def list_suites_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        app_id: Missing[int] = UNSET,
        check_name: Missing[str] = UNSET,
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
    ) -> "Response[ReposOwnerRepoCommitsRefCheckSuitesGetResponse200]":
        url = f"/repos/{owner}/{repo}/commits/{ref}/check-suites"

        params = {
            "app_id": app_id,
            "check_name": check_name,
            "per_page": per_page,
            "page": page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckSuitesGetResponse200,
        )

    async def async_list_suites_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        app_id: Missing[int] = UNSET,
        check_name: Missing[str] = UNSET,
        per_page: Missing[int] = 30,
        page: Missing[int] = 1,
    ) -> "Response[ReposOwnerRepoCommitsRefCheckSuitesGetResponse200]":
        url = f"/repos/{owner}/{repo}/commits/{ref}/check-suites"

        params = {
            "app_id": app_id,
            "check_name": check_name,
            "per_page": per_page,
            "page": page,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckSuitesGetResponse200,
        )
