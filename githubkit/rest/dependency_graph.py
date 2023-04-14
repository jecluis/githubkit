"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from datetime import datetime
from typing import TYPE_CHECKING, List, Literal, overload

from pydantic import BaseModel, parse_obj_as

from githubkit.utils import UNSET, Missing, exclude_unset

from .types import (
    MetadataType,
    SnapshotType,
    SnapshotPropJobType,
    SnapshotPropDetectorType,
    SnapshotPropManifestsType,
)
from .models import (
    Snapshot,
    BasicError,
    DependencyGraphSpdxSbom,
    DependencyGraphDiffItems,
    ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
)

if TYPE_CHECKING:
    from githubkit import GitHubCore
    from githubkit.response import Response


class DependencyGraphClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: "GitHubCore"):
        self._github = github

    def diff_range(
        self,
        owner: str,
        repo: str,
        basehead: str,
        name: Missing[str] = UNSET,
    ) -> "Response[List[DependencyGraphDiffItems]]":
        url = f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}"

        params = {
            "name": name,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[DependencyGraphDiffItems],
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    async def async_diff_range(
        self,
        owner: str,
        repo: str,
        basehead: str,
        name: Missing[str] = UNSET,
    ) -> "Response[List[DependencyGraphDiffItems]]":
        url = f"/repos/{owner}/{repo}/dependency-graph/compare/{basehead}"

        params = {
            "name": name,
        }

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[DependencyGraphDiffItems],
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    def export_sbom(
        self,
        owner: str,
        repo: str,
    ) -> "Response[DependencyGraphSpdxSbom]":
        url = f"/repos/{owner}/{repo}/dependency-graph/sbom"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=DependencyGraphSpdxSbom,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    async def async_export_sbom(
        self,
        owner: str,
        repo: str,
    ) -> "Response[DependencyGraphSpdxSbom]":
        url = f"/repos/{owner}/{repo}/dependency-graph/sbom"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=DependencyGraphSpdxSbom,
            error_models={
                "404": BasicError,
                "403": BasicError,
            },
        )

    @overload
    def create_repository_snapshot(
        self, owner: str, repo: str, *, data: SnapshotType
    ) -> "Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]":
        ...

    @overload
    def create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        version: int,
        job: SnapshotPropJobType,
        sha: str,
        ref: str,
        detector: SnapshotPropDetectorType,
        metadata: Missing[MetadataType] = UNSET,
        manifests: Missing[SnapshotPropManifestsType] = UNSET,
        scanned: datetime,
    ) -> "Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]":
        ...

    def create_repository_snapshot(
        self, owner: str, repo: str, *, data: Missing[SnapshotType] = UNSET, **kwargs
    ) -> "Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]":
        url = f"/repos/{owner}/{repo}/dependency-graph/snapshots"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(Snapshot, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        )

    @overload
    async def async_create_repository_snapshot(
        self, owner: str, repo: str, *, data: SnapshotType
    ) -> "Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]":
        ...

    @overload
    async def async_create_repository_snapshot(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        version: int,
        job: SnapshotPropJobType,
        sha: str,
        ref: str,
        detector: SnapshotPropDetectorType,
        metadata: Missing[MetadataType] = UNSET,
        manifests: Missing[SnapshotPropManifestsType] = UNSET,
        scanned: datetime,
    ) -> "Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]":
        ...

    async def async_create_repository_snapshot(
        self, owner: str, repo: str, *, data: Missing[SnapshotType] = UNSET, **kwargs
    ) -> "Response[ReposOwnerRepoDependencyGraphSnapshotsPostResponse201]":
        url = f"/repos/{owner}/{repo}/dependency-graph/snapshots"

        headers = {
            "X-GitHub-Api-Version": self._REST_API_VERSION,
        }

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = parse_obj_as(Snapshot, json)
        json = json.dict(by_alias=True) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoDependencyGraphSnapshotsPostResponse201,
        )
