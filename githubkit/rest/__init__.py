"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

    python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import TYPE_CHECKING
from functools import cached_property

from .models import *
from .git import GitClient
from .apps import AppsClient
from .meta import MetaClient
from .oidc import OidcClient
from .orgs import OrgsClient
from .gists import GistsClient
from .pulls import PullsClient
from .repos import ReposClient
from .teams import TeamsClient
from .users import UsersClient
from .checks import ChecksClient
from .emojis import EmojisClient
from .issues import IssuesClient
from .search import SearchClient
from .actions import ActionsClient
from .billing import BillingClient
from .copilot import CopilotClient
from .activity import ActivityClient
from .licenses import LicensesClient
from .markdown import MarkdownClient
from .packages import PackagesClient
from .projects import ProjectsClient
from .classroom import ClassroomClient
from .gitignore import GitignoreClient
from .reactions import ReactionsClient
from .rate_limit import RateLimitClient
from .codespaces import CodespacesClient
from .dependabot import DependabotClient
from .migrations import MigrationsClient
from .interactions import InteractionsClient
from .code_scanning import CodeScanningClient
from .secret_scanning import SecretScanningClient
from .codes_of_conduct import CodesOfConductClient
from .dependency_graph import DependencyGraphClient
from .security_advisories import SecurityAdvisoriesClient

if TYPE_CHECKING:
    from githubkit import GitHubCore


class RestNamespace:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    @cached_property
    def meta(self) -> MetaClient:
        return MetaClient(self._github)

    @cached_property
    def security_advisories(self) -> SecurityAdvisoriesClient:
        return SecurityAdvisoriesClient(self._github)

    @cached_property
    def apps(self) -> AppsClient:
        return AppsClient(self._github)

    @cached_property
    def classroom(self) -> ClassroomClient:
        return ClassroomClient(self._github)

    @cached_property
    def codes_of_conduct(self) -> CodesOfConductClient:
        return CodesOfConductClient(self._github)

    @cached_property
    def emojis(self) -> EmojisClient:
        return EmojisClient(self._github)

    @cached_property
    def dependabot(self) -> DependabotClient:
        return DependabotClient(self._github)

    @cached_property
    def secret_scanning(self) -> SecretScanningClient:
        return SecretScanningClient(self._github)

    @cached_property
    def activity(self) -> ActivityClient:
        return ActivityClient(self._github)

    @cached_property
    def gists(self) -> GistsClient:
        return GistsClient(self._github)

    @cached_property
    def gitignore(self) -> GitignoreClient:
        return GitignoreClient(self._github)

    @cached_property
    def issues(self) -> IssuesClient:
        return IssuesClient(self._github)

    @cached_property
    def licenses(self) -> LicensesClient:
        return LicensesClient(self._github)

    @cached_property
    def markdown(self) -> MarkdownClient:
        return MarkdownClient(self._github)

    @cached_property
    def orgs(self) -> OrgsClient:
        return OrgsClient(self._github)

    @cached_property
    def actions(self) -> ActionsClient:
        return ActionsClient(self._github)

    @cached_property
    def oidc(self) -> OidcClient:
        return OidcClient(self._github)

    @cached_property
    def code_scanning(self) -> CodeScanningClient:
        return CodeScanningClient(self._github)

    @cached_property
    def codespaces(self) -> CodespacesClient:
        return CodespacesClient(self._github)

    @cached_property
    def copilot(self) -> CopilotClient:
        return CopilotClient(self._github)

    @cached_property
    def packages(self) -> PackagesClient:
        return PackagesClient(self._github)

    @cached_property
    def interactions(self) -> InteractionsClient:
        return InteractionsClient(self._github)

    @cached_property
    def migrations(self) -> MigrationsClient:
        return MigrationsClient(self._github)

    @cached_property
    def projects(self) -> ProjectsClient:
        return ProjectsClient(self._github)

    @cached_property
    def repos(self) -> ReposClient:
        return ReposClient(self._github)

    @cached_property
    def billing(self) -> BillingClient:
        return BillingClient(self._github)

    @cached_property
    def teams(self) -> TeamsClient:
        return TeamsClient(self._github)

    @cached_property
    def reactions(self) -> ReactionsClient:
        return ReactionsClient(self._github)

    @cached_property
    def rate_limit(self) -> RateLimitClient:
        return RateLimitClient(self._github)

    @cached_property
    def checks(self) -> ChecksClient:
        return ChecksClient(self._github)

    @cached_property
    def dependency_graph(self) -> DependencyGraphClient:
        return DependencyGraphClient(self._github)

    @cached_property
    def git(self) -> GitClient:
        return GitClient(self._github)

    @cached_property
    def pulls(self) -> PullsClient:
        return PullsClient(self._github)

    @cached_property
    def search(self) -> SearchClient:
        return SearchClient(self._github)

    @cached_property
    def users(self) -> UsersClient:
        return UsersClient(self._github)
