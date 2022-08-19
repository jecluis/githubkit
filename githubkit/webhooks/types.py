"""DO NOT EDIT THIS FILE!

This file is auto generated by github webhook schema.
See https://github.com/octokit/webhooks for more information.
"""

from typing import Any, Dict, Union
from typing_extensions import Annotated

from pydantic import Field

from .models import (
    ForkEvent,
    PingEvent,
    PushEvent,
    TeamEdited,
    CreateEvent,
    DeleteEvent,
    GollumEvent,
    LabelEdited,
    MemberAdded,
    MetaDeleted,
    PublicEvent,
    StarCreated,
    StarDeleted,
    StatusEvent,
    TeamCreated,
    TeamDeleted,
    IssuesClosed,
    IssuesEdited,
    IssuesLocked,
    IssuesOpened,
    IssuesPinned,
    LabelCreated,
    LabelDeleted,
    MemberEdited,
    TeamAddEvent,
    WatchStarted,
    IssuesDeleted,
    IssuesLabeled,
    MemberRemoved,
    ProjectClosed,
    ProjectEdited,
    ReleaseEdited,
    IssuesAssigned,
    IssuesReopened,
    IssuesUnlocked,
    IssuesUnpinned,
    PackageUpdated,
    PageBuildEvent,
    ProjectCreated,
    ProjectDeleted,
    ReleaseCreated,
    ReleaseDeleted,
    CheckRunCreated,
    IssuesUnlabeled,
    MembershipAdded,
    MilestoneClosed,
    MilestoneEdited,
    MilestoneOpened,
    OrgBlockBlocked,
    ProjectReopened,
    ReleaseReleased,
    DeployKeyCreated,
    DeployKeyDeleted,
    DiscussionEdited,
    DiscussionLocked,
    DiscussionPinned,
    IssuesMilestoned,
    IssuesUnassigned,
    MilestoneCreated,
    MilestoneDeleted,
    PackagePublished,
    ProjectCardMoved,
    ReleasePublished,
    RepositoryEdited,
    CheckRunCompleted,
    DeploymentCreated,
    DiscussionCreated,
    DiscussionDeleted,
    DiscussionLabeled,
    IssuesTransferred,
    MembershipRemoved,
    OrgBlockUnblocked,
    ProjectCardEdited,
    PullRequestClosed,
    PullRequestEdited,
    PullRequestLocked,
    PullRequestOpened,
    RepositoryCreated,
    RepositoryDeleted,
    RepositoryRenamed,
    SponsorshipEdited,
    WorkflowJobQueued,
    DiscussionAnswered,
    DiscussionUnlocked,
    DiscussionUnpinned,
    IssueCommentEdited,
    IssuesDemilestoned,
    ProjectCardCreated,
    ProjectCardDeleted,
    ProjectColumnMoved,
    PullRequestLabeled,
    ReleasePrereleased,
    ReleaseUnpublished,
    RepositoryArchived,
    SponsorshipCreated,
    CheckRunRerequested,
    CheckSuiteCompleted,
    CheckSuiteRequested,
    DiscussionUnlabeled,
    InstallationCreated,
    InstallationDeleted,
    InstallationSuspend,
    IssueCommentCreated,
    IssueCommentDeleted,
    OrganizationDeleted,
    OrganizationRenamed,
    ProjectColumnEdited,
    PullRequestAssigned,
    PullRequestReopened,
    PullRequestUnlocked,
    CommitCommentCreated,
    DiscussionUnanswered,
    ProjectCardConverted,
    ProjectColumnCreated,
    ProjectColumnDeleted,
    ProjectsV2ItemEdited,
    PullRequestUnlabeled,
    RepositoryPrivatized,
    RepositoryPublicized,
    RepositoryUnarchived,
    SponsorshipCancelled,
    WorkflowJobCompleted,
    WorkflowRunCompleted,
    WorkflowRunRequested,
    CheckSuiteRerequested,
    DiscussionTransferred,
    InstallationUnsuspend,
    ProjectsV2ItemCreated,
    ProjectsV2ItemDeleted,
    PullRequestUnassigned,
    RepositoryImportEvent,
    RepositoryTransferred,
    TeamAddedToRepository,
    WorkflowDispatchEvent,
    WorkflowJobInProgress,
    CodeScanningAlertFixed,
    ProjectsV2ItemArchived,
    ProjectsV2ItemRestored,
    PullRequestSynchronize,
    SponsorshipTierChanged,
    CheckRunRequestedAction,
    DeploymentStatusCreated,
    DiscussionCommentEdited,
    OrganizationMemberAdded,
    ProjectsV2ItemConverted,
    ProjectsV2ItemReordered,
    PullRequestReviewEdited,
    RepositoryDispatchEvent,
    SecurityAdvisoryUpdated,
    CodeScanningAlertCreated,
    DiscussionCommentCreated,
    DiscussionCommentDeleted,
    CodeScanningAlertReopened,
    DiscussionCategoryChanged,
    MergeGroupChecksRequested,
    OrganizationMemberInvited,
    OrganizationMemberRemoved,
    PullRequestReadyForReview,
    SecurityAdvisoryPerformed,
    SecurityAdvisoryPublished,
    SecurityAdvisoryWithdrawn,
    TeamRemovedFromRepository,
    BranchProtectionRuleEdited,
    MarketplacePurchaseChanged,
    PullRequestReviewDismissed,
    PullRequestReviewSubmitted,
    SecretScanningAlertCreated,
    BranchProtectionRuleCreated,
    BranchProtectionRuleDeleted,
    PullRequestAutoMergeEnabled,
    PullRequestConvertedToDraft,
    SecretScanningAlertReopened,
    SecretScanningAlertResolved,
    MarketplacePurchaseCancelled,
    MarketplacePurchasePurchased,
    PullRequestAutoMergeDisabled,
    SponsorshipPendingTierChange,
    CodeScanningAlertClosedByUser,
    GithubAppAuthorizationRevoked,
    InstallationRepositoriesAdded,
    PullRequestReviewCommentEdited,
    SponsorshipPendingCancellation,
    CodeScanningAlertReopenedByUser,
    InstallationRepositoriesRemoved,
    PullRequestReviewCommentCreated,
    PullRequestReviewCommentDeleted,
    PullRequestReviewThreadResolved,
    MarketplacePurchasePendingChange,
    PullRequestReviewRequestedOneof0,
    PullRequestReviewRequestedOneof1,
    CodeScanningAlertAppearedInBranch,
    PullRequestReviewThreadUnresolved,
    InstallationNewPermissionsAccepted,
    RepositoryVulnerabilityAlertCreate,
    RepositoryVulnerabilityAlertReopen,
    RepositoryVulnerabilityAlertDismiss,
    RepositoryVulnerabilityAlertResolve,
    PullRequestReviewRequestRemovedOneof0,
    PullRequestReviewRequestRemovedOneof1,
    MarketplacePurchasePendingChangeCancelled,
)

BranchProtectionRuleEvent = Annotated[
    Union[
        BranchProtectionRuleCreated,
        BranchProtectionRuleDeleted,
        BranchProtectionRuleEdited,
    ],
    Field(discriminator="action"),
]
CheckRunEvent = Annotated[
    Union[
        CheckRunCompleted,
        CheckRunCreated,
        CheckRunRequestedAction,
        CheckRunRerequested,
    ],
    Field(discriminator="action"),
]
CheckSuiteEvent = Annotated[
    Union[
        CheckSuiteCompleted,
        CheckSuiteRequested,
        CheckSuiteRerequested,
    ],
    Field(discriminator="action"),
]
CodeScanningAlertEvent = Annotated[
    Union[
        CodeScanningAlertAppearedInBranch,
        CodeScanningAlertClosedByUser,
        CodeScanningAlertCreated,
        CodeScanningAlertFixed,
        CodeScanningAlertReopened,
        CodeScanningAlertReopenedByUser,
    ],
    Field(discriminator="action"),
]
CommitCommentEvent = CommitCommentCreated
DeployKeyEvent = Annotated[
    Union[
        DeployKeyCreated,
        DeployKeyDeleted,
    ],
    Field(discriminator="action"),
]
DeploymentEvent = DeploymentCreated
DeploymentStatusEvent = DeploymentStatusCreated
DiscussionEvent = Annotated[
    Union[
        DiscussionAnswered,
        DiscussionCategoryChanged,
        DiscussionCreated,
        DiscussionDeleted,
        DiscussionEdited,
        DiscussionLabeled,
        DiscussionLocked,
        DiscussionPinned,
        DiscussionTransferred,
        DiscussionUnanswered,
        DiscussionUnlabeled,
        DiscussionUnlocked,
        DiscussionUnpinned,
    ],
    Field(discriminator="action"),
]
DiscussionCommentEvent = Annotated[
    Union[
        DiscussionCommentCreated,
        DiscussionCommentDeleted,
        DiscussionCommentEdited,
    ],
    Field(discriminator="action"),
]
GithubAppAuthorizationEvent = GithubAppAuthorizationRevoked
InstallationEvent = Annotated[
    Union[
        InstallationCreated,
        InstallationDeleted,
        InstallationNewPermissionsAccepted,
        InstallationSuspend,
        InstallationUnsuspend,
    ],
    Field(discriminator="action"),
]
InstallationRepositoriesEvent = Annotated[
    Union[
        InstallationRepositoriesAdded,
        InstallationRepositoriesRemoved,
    ],
    Field(discriminator="action"),
]
IssueCommentEvent = Annotated[
    Union[
        IssueCommentCreated,
        IssueCommentDeleted,
        IssueCommentEdited,
    ],
    Field(discriminator="action"),
]
IssuesEvent = Annotated[
    Union[
        IssuesAssigned,
        IssuesClosed,
        IssuesDeleted,
        IssuesDemilestoned,
        IssuesEdited,
        IssuesLabeled,
        IssuesLocked,
        IssuesMilestoned,
        IssuesOpened,
        IssuesPinned,
        IssuesReopened,
        IssuesTransferred,
        IssuesUnassigned,
        IssuesUnlabeled,
        IssuesUnlocked,
        IssuesUnpinned,
    ],
    Field(discriminator="action"),
]
LabelEvent = Annotated[
    Union[
        LabelCreated,
        LabelDeleted,
        LabelEdited,
    ],
    Field(discriminator="action"),
]
MarketplacePurchaseEvent = Annotated[
    Union[
        MarketplacePurchaseCancelled,
        MarketplacePurchaseChanged,
        MarketplacePurchasePendingChange,
        MarketplacePurchasePendingChangeCancelled,
        MarketplacePurchasePurchased,
    ],
    Field(discriminator="action"),
]
MemberEvent = Annotated[
    Union[
        MemberAdded,
        MemberEdited,
        MemberRemoved,
    ],
    Field(discriminator="action"),
]
MembershipEvent = Annotated[
    Union[
        MembershipAdded,
        MembershipRemoved,
    ],
    Field(discriminator="action"),
]
MergeGroupEvent = MergeGroupChecksRequested
MetaEvent = MetaDeleted
MilestoneEvent = Annotated[
    Union[
        MilestoneClosed,
        MilestoneCreated,
        MilestoneDeleted,
        MilestoneEdited,
        MilestoneOpened,
    ],
    Field(discriminator="action"),
]
OrgBlockEvent = Annotated[
    Union[
        OrgBlockBlocked,
        OrgBlockUnblocked,
    ],
    Field(discriminator="action"),
]
OrganizationEvent = Annotated[
    Union[
        OrganizationDeleted,
        OrganizationMemberAdded,
        OrganizationMemberInvited,
        OrganizationMemberRemoved,
        OrganizationRenamed,
    ],
    Field(discriminator="action"),
]
PackageEvent = Annotated[
    Union[
        PackagePublished,
        PackageUpdated,
    ],
    Field(discriminator="action"),
]
ProjectEvent = Annotated[
    Union[
        ProjectClosed,
        ProjectCreated,
        ProjectDeleted,
        ProjectEdited,
        ProjectReopened,
    ],
    Field(discriminator="action"),
]
ProjectCardEvent = Annotated[
    Union[
        ProjectCardConverted,
        ProjectCardCreated,
        ProjectCardDeleted,
        ProjectCardEdited,
        ProjectCardMoved,
    ],
    Field(discriminator="action"),
]
ProjectColumnEvent = Annotated[
    Union[
        ProjectColumnCreated,
        ProjectColumnDeleted,
        ProjectColumnEdited,
        ProjectColumnMoved,
    ],
    Field(discriminator="action"),
]
ProjectsV2ItemEvent = Annotated[
    Union[
        ProjectsV2ItemArchived,
        ProjectsV2ItemConverted,
        ProjectsV2ItemCreated,
        ProjectsV2ItemDeleted,
        ProjectsV2ItemEdited,
        ProjectsV2ItemReordered,
        ProjectsV2ItemRestored,
    ],
    Field(discriminator="action"),
]
PullRequestEvent = Annotated[
    Union[
        PullRequestAssigned,
        PullRequestAutoMergeDisabled,
        PullRequestAutoMergeEnabled,
        PullRequestClosed,
        PullRequestConvertedToDraft,
        PullRequestEdited,
        PullRequestLabeled,
        PullRequestLocked,
        PullRequestOpened,
        PullRequestReadyForReview,
        PullRequestReopened,
        Union[
            PullRequestReviewRequestRemovedOneof0, PullRequestReviewRequestRemovedOneof1
        ],
        Union[PullRequestReviewRequestedOneof0, PullRequestReviewRequestedOneof1],
        PullRequestSynchronize,
        PullRequestUnassigned,
        PullRequestUnlabeled,
        PullRequestUnlocked,
    ],
    Field(discriminator="action"),
]
PullRequestReviewEvent = Annotated[
    Union[
        PullRequestReviewDismissed,
        PullRequestReviewEdited,
        PullRequestReviewSubmitted,
    ],
    Field(discriminator="action"),
]
PullRequestReviewCommentEvent = Annotated[
    Union[
        PullRequestReviewCommentCreated,
        PullRequestReviewCommentDeleted,
        PullRequestReviewCommentEdited,
    ],
    Field(discriminator="action"),
]
PullRequestReviewThreadEvent = Annotated[
    Union[
        PullRequestReviewThreadResolved,
        PullRequestReviewThreadUnresolved,
    ],
    Field(discriminator="action"),
]
ReleaseEvent = Annotated[
    Union[
        ReleaseCreated,
        ReleaseDeleted,
        ReleaseEdited,
        ReleasePrereleased,
        ReleasePublished,
        ReleaseReleased,
        ReleaseUnpublished,
    ],
    Field(discriminator="action"),
]
RepositoryEvent = Annotated[
    Union[
        RepositoryArchived,
        RepositoryCreated,
        RepositoryDeleted,
        RepositoryEdited,
        RepositoryPrivatized,
        RepositoryPublicized,
        RepositoryRenamed,
        RepositoryTransferred,
        RepositoryUnarchived,
    ],
    Field(discriminator="action"),
]
RepositoryVulnerabilityAlertEvent = Annotated[
    Union[
        RepositoryVulnerabilityAlertCreate,
        RepositoryVulnerabilityAlertDismiss,
        RepositoryVulnerabilityAlertReopen,
        RepositoryVulnerabilityAlertResolve,
    ],
    Field(discriminator="action"),
]
SecretScanningAlertEvent = Annotated[
    Union[
        SecretScanningAlertCreated,
        SecretScanningAlertReopened,
        SecretScanningAlertResolved,
    ],
    Field(discriminator="action"),
]
SecurityAdvisoryEvent = Annotated[
    Union[
        SecurityAdvisoryPerformed,
        SecurityAdvisoryPublished,
        SecurityAdvisoryUpdated,
        SecurityAdvisoryWithdrawn,
    ],
    Field(discriminator="action"),
]
SponsorshipEvent = Annotated[
    Union[
        SponsorshipCancelled,
        SponsorshipCreated,
        SponsorshipEdited,
        SponsorshipPendingCancellation,
        SponsorshipPendingTierChange,
        SponsorshipTierChanged,
    ],
    Field(discriminator="action"),
]
StarEvent = Annotated[
    Union[
        StarCreated,
        StarDeleted,
    ],
    Field(discriminator="action"),
]
TeamEvent = Annotated[
    Union[
        TeamAddedToRepository,
        TeamCreated,
        TeamDeleted,
        TeamEdited,
        TeamRemovedFromRepository,
    ],
    Field(discriminator="action"),
]
WatchEvent = WatchStarted
WorkflowJobEvent = Annotated[
    Union[
        WorkflowJobCompleted,
        WorkflowJobInProgress,
        WorkflowJobQueued,
    ],
    Field(discriminator="action"),
]
WorkflowRunEvent = Annotated[
    Union[
        WorkflowRunCompleted,
        WorkflowRunRequested,
    ],
    Field(discriminator="action"),
]

WebhookEvent = Union[
    BranchProtectionRuleEvent,
    CheckRunEvent,
    CheckSuiteEvent,
    CodeScanningAlertEvent,
    CommitCommentEvent,
    CreateEvent,
    DeleteEvent,
    DeployKeyEvent,
    DeploymentEvent,
    DeploymentStatusEvent,
    DiscussionEvent,
    DiscussionCommentEvent,
    ForkEvent,
    GithubAppAuthorizationEvent,
    GollumEvent,
    InstallationEvent,
    InstallationRepositoriesEvent,
    IssueCommentEvent,
    IssuesEvent,
    LabelEvent,
    MarketplacePurchaseEvent,
    MemberEvent,
    MembershipEvent,
    MergeGroupEvent,
    MetaEvent,
    MilestoneEvent,
    OrgBlockEvent,
    OrganizationEvent,
    PackageEvent,
    PageBuildEvent,
    PingEvent,
    ProjectEvent,
    ProjectCardEvent,
    ProjectColumnEvent,
    ProjectsV2ItemEvent,
    PublicEvent,
    PullRequestEvent,
    PullRequestReviewEvent,
    PullRequestReviewCommentEvent,
    PullRequestReviewThreadEvent,
    PushEvent,
    ReleaseEvent,
    RepositoryEvent,
    RepositoryDispatchEvent,
    RepositoryImportEvent,
    RepositoryVulnerabilityAlertEvent,
    SecretScanningAlertEvent,
    SecurityAdvisoryEvent,
    SponsorshipEvent,
    StarEvent,
    StatusEvent,
    TeamEvent,
    TeamAddEvent,
    WatchEvent,
    WorkflowDispatchEvent,
    WorkflowJobEvent,
    WorkflowRunEvent,
]


webhook_action_types = {
    "create": CreateEvent,
    "delete": DeleteEvent,
    "fork": ForkEvent,
    "gollum": GollumEvent,
    "page_build": PageBuildEvent,
    "ping": PingEvent,
    "public": PublicEvent,
    "push": PushEvent,
    "repository_dispatch": RepositoryDispatchEvent,
    "repository_import": RepositoryImportEvent,
    "status": StatusEvent,
    "team_add": TeamAddEvent,
    "workflow_dispatch": WorkflowDispatchEvent,
    "branch_protection_rule": {
        "created": BranchProtectionRuleCreated,
        "deleted": BranchProtectionRuleDeleted,
        "edited": BranchProtectionRuleEdited,
    },
    "check_run": {
        "completed": CheckRunCompleted,
        "created": CheckRunCreated,
        "requested_action": CheckRunRequestedAction,
        "rerequested": CheckRunRerequested,
    },
    "check_suite": {
        "completed": CheckSuiteCompleted,
        "requested": CheckSuiteRequested,
        "rerequested": CheckSuiteRerequested,
    },
    "code_scanning_alert": {
        "appeared_in_branch": CodeScanningAlertAppearedInBranch,
        "closed_by_user": CodeScanningAlertClosedByUser,
        "created": CodeScanningAlertCreated,
        "fixed": CodeScanningAlertFixed,
        "reopened": CodeScanningAlertReopened,
        "reopened_by_user": CodeScanningAlertReopenedByUser,
    },
    "commit_comment": {
        "created": CommitCommentCreated,
    },
    "deploy_key": {
        "created": DeployKeyCreated,
        "deleted": DeployKeyDeleted,
    },
    "deployment": {
        "created": DeploymentCreated,
    },
    "deployment_status": {
        "created": DeploymentStatusCreated,
    },
    "discussion": {
        "answered": DiscussionAnswered,
        "category_changed": DiscussionCategoryChanged,
        "created": DiscussionCreated,
        "deleted": DiscussionDeleted,
        "edited": DiscussionEdited,
        "labeled": DiscussionLabeled,
        "locked": DiscussionLocked,
        "pinned": DiscussionPinned,
        "transferred": DiscussionTransferred,
        "unanswered": DiscussionUnanswered,
        "unlabeled": DiscussionUnlabeled,
        "unlocked": DiscussionUnlocked,
        "unpinned": DiscussionUnpinned,
    },
    "discussion_comment": {
        "created": DiscussionCommentCreated,
        "deleted": DiscussionCommentDeleted,
        "edited": DiscussionCommentEdited,
    },
    "github_app_authorization": {
        "revoked": GithubAppAuthorizationRevoked,
    },
    "installation": {
        "created": InstallationCreated,
        "deleted": InstallationDeleted,
        "new_permissions_accepted": InstallationNewPermissionsAccepted,
        "suspend": InstallationSuspend,
        "unsuspend": InstallationUnsuspend,
    },
    "installation_repositories": {
        "added": InstallationRepositoriesAdded,
        "removed": InstallationRepositoriesRemoved,
    },
    "issue_comment": {
        "created": IssueCommentCreated,
        "deleted": IssueCommentDeleted,
        "edited": IssueCommentEdited,
    },
    "issues": {
        "assigned": IssuesAssigned,
        "closed": IssuesClosed,
        "deleted": IssuesDeleted,
        "demilestoned": IssuesDemilestoned,
        "edited": IssuesEdited,
        "labeled": IssuesLabeled,
        "locked": IssuesLocked,
        "milestoned": IssuesMilestoned,
        "opened": IssuesOpened,
        "pinned": IssuesPinned,
        "reopened": IssuesReopened,
        "transferred": IssuesTransferred,
        "unassigned": IssuesUnassigned,
        "unlabeled": IssuesUnlabeled,
        "unlocked": IssuesUnlocked,
        "unpinned": IssuesUnpinned,
    },
    "label": {
        "created": LabelCreated,
        "deleted": LabelDeleted,
        "edited": LabelEdited,
    },
    "marketplace_purchase": {
        "cancelled": MarketplacePurchaseCancelled,
        "changed": MarketplacePurchaseChanged,
        "pending_change": MarketplacePurchasePendingChange,
        "pending_change_cancelled": MarketplacePurchasePendingChangeCancelled,
        "purchased": MarketplacePurchasePurchased,
    },
    "member": {
        "added": MemberAdded,
        "edited": MemberEdited,
        "removed": MemberRemoved,
    },
    "membership": {
        "added": MembershipAdded,
        "removed": MembershipRemoved,
    },
    "merge_group": {
        "checks_requested": MergeGroupChecksRequested,
    },
    "meta": {
        "deleted": MetaDeleted,
    },
    "milestone": {
        "closed": MilestoneClosed,
        "created": MilestoneCreated,
        "deleted": MilestoneDeleted,
        "edited": MilestoneEdited,
        "opened": MilestoneOpened,
    },
    "org_block": {
        "blocked": OrgBlockBlocked,
        "unblocked": OrgBlockUnblocked,
    },
    "organization": {
        "deleted": OrganizationDeleted,
        "member_added": OrganizationMemberAdded,
        "member_invited": OrganizationMemberInvited,
        "member_removed": OrganizationMemberRemoved,
        "renamed": OrganizationRenamed,
    },
    "package": {
        "published": PackagePublished,
        "updated": PackageUpdated,
    },
    "project": {
        "closed": ProjectClosed,
        "created": ProjectCreated,
        "deleted": ProjectDeleted,
        "edited": ProjectEdited,
        "reopened": ProjectReopened,
    },
    "project_card": {
        "converted": ProjectCardConverted,
        "created": ProjectCardCreated,
        "deleted": ProjectCardDeleted,
        "edited": ProjectCardEdited,
        "moved": ProjectCardMoved,
    },
    "project_column": {
        "created": ProjectColumnCreated,
        "deleted": ProjectColumnDeleted,
        "edited": ProjectColumnEdited,
        "moved": ProjectColumnMoved,
    },
    "projects_v2_item": {
        "archived": ProjectsV2ItemArchived,
        "converted": ProjectsV2ItemConverted,
        "created": ProjectsV2ItemCreated,
        "deleted": ProjectsV2ItemDeleted,
        "edited": ProjectsV2ItemEdited,
        "reordered": ProjectsV2ItemReordered,
        "restored": ProjectsV2ItemRestored,
    },
    "pull_request": {
        "assigned": PullRequestAssigned,
        "auto_merge_disabled": PullRequestAutoMergeDisabled,
        "auto_merge_enabled": PullRequestAutoMergeEnabled,
        "closed": PullRequestClosed,
        "converted_to_draft": PullRequestConvertedToDraft,
        "edited": PullRequestEdited,
        "labeled": PullRequestLabeled,
        "locked": PullRequestLocked,
        "opened": PullRequestOpened,
        "ready_for_review": PullRequestReadyForReview,
        "reopened": PullRequestReopened,
        "review_request_removed": Union[
            PullRequestReviewRequestRemovedOneof0, PullRequestReviewRequestRemovedOneof1
        ],
        "review_requested": Union[
            PullRequestReviewRequestedOneof0, PullRequestReviewRequestedOneof1
        ],
        "synchronize": PullRequestSynchronize,
        "unassigned": PullRequestUnassigned,
        "unlabeled": PullRequestUnlabeled,
        "unlocked": PullRequestUnlocked,
    },
    "pull_request_review": {
        "dismissed": PullRequestReviewDismissed,
        "edited": PullRequestReviewEdited,
        "submitted": PullRequestReviewSubmitted,
    },
    "pull_request_review_comment": {
        "created": PullRequestReviewCommentCreated,
        "deleted": PullRequestReviewCommentDeleted,
        "edited": PullRequestReviewCommentEdited,
    },
    "pull_request_review_thread": {
        "resolved": PullRequestReviewThreadResolved,
        "unresolved": PullRequestReviewThreadUnresolved,
    },
    "release": {
        "created": ReleaseCreated,
        "deleted": ReleaseDeleted,
        "edited": ReleaseEdited,
        "prereleased": ReleasePrereleased,
        "published": ReleasePublished,
        "released": ReleaseReleased,
        "unpublished": ReleaseUnpublished,
    },
    "repository": {
        "archived": RepositoryArchived,
        "created": RepositoryCreated,
        "deleted": RepositoryDeleted,
        "edited": RepositoryEdited,
        "privatized": RepositoryPrivatized,
        "publicized": RepositoryPublicized,
        "renamed": RepositoryRenamed,
        "transferred": RepositoryTransferred,
        "unarchived": RepositoryUnarchived,
    },
    "repository_vulnerability_alert": {
        "create": RepositoryVulnerabilityAlertCreate,
        "dismiss": RepositoryVulnerabilityAlertDismiss,
        "reopen": RepositoryVulnerabilityAlertReopen,
        "resolve": RepositoryVulnerabilityAlertResolve,
    },
    "secret_scanning_alert": {
        "created": SecretScanningAlertCreated,
        "reopened": SecretScanningAlertReopened,
        "resolved": SecretScanningAlertResolved,
    },
    "security_advisory": {
        "performed": SecurityAdvisoryPerformed,
        "published": SecurityAdvisoryPublished,
        "updated": SecurityAdvisoryUpdated,
        "withdrawn": SecurityAdvisoryWithdrawn,
    },
    "sponsorship": {
        "cancelled": SponsorshipCancelled,
        "created": SponsorshipCreated,
        "edited": SponsorshipEdited,
        "pending_cancellation": SponsorshipPendingCancellation,
        "pending_tier_change": SponsorshipPendingTierChange,
        "tier_changed": SponsorshipTierChanged,
    },
    "star": {
        "created": StarCreated,
        "deleted": StarDeleted,
    },
    "team": {
        "added_to_repository": TeamAddedToRepository,
        "created": TeamCreated,
        "deleted": TeamDeleted,
        "edited": TeamEdited,
        "removed_from_repository": TeamRemovedFromRepository,
    },
    "watch": {
        "started": WatchStarted,
    },
    "workflow_job": {
        "completed": WorkflowJobCompleted,
        "in_progress": WorkflowJobInProgress,
        "queued": WorkflowJobQueued,
    },
    "workflow_run": {
        "completed": WorkflowRunCompleted,
        "requested": WorkflowRunRequested,
    },
}

webhook_event_types = {
    "branch_protection_rule": BranchProtectionRuleEvent,
    "check_run": CheckRunEvent,
    "check_suite": CheckSuiteEvent,
    "code_scanning_alert": CodeScanningAlertEvent,
    "commit_comment": CommitCommentEvent,
    "create": CreateEvent,
    "delete": DeleteEvent,
    "deploy_key": DeployKeyEvent,
    "deployment": DeploymentEvent,
    "deployment_status": DeploymentStatusEvent,
    "discussion": DiscussionEvent,
    "discussion_comment": DiscussionCommentEvent,
    "fork": ForkEvent,
    "github_app_authorization": GithubAppAuthorizationEvent,
    "gollum": GollumEvent,
    "installation": InstallationEvent,
    "installation_repositories": InstallationRepositoriesEvent,
    "issue_comment": IssueCommentEvent,
    "issues": IssuesEvent,
    "label": LabelEvent,
    "marketplace_purchase": MarketplacePurchaseEvent,
    "member": MemberEvent,
    "membership": MembershipEvent,
    "merge_group": MergeGroupEvent,
    "meta": MetaEvent,
    "milestone": MilestoneEvent,
    "org_block": OrgBlockEvent,
    "organization": OrganizationEvent,
    "package": PackageEvent,
    "page_build": PageBuildEvent,
    "ping": PingEvent,
    "project": ProjectEvent,
    "project_card": ProjectCardEvent,
    "project_column": ProjectColumnEvent,
    "projects_v2_item": ProjectsV2ItemEvent,
    "public": PublicEvent,
    "pull_request": PullRequestEvent,
    "pull_request_review": PullRequestReviewEvent,
    "pull_request_review_comment": PullRequestReviewCommentEvent,
    "pull_request_review_thread": PullRequestReviewThreadEvent,
    "push": PushEvent,
    "release": ReleaseEvent,
    "repository": RepositoryEvent,
    "repository_dispatch": RepositoryDispatchEvent,
    "repository_import": RepositoryImportEvent,
    "repository_vulnerability_alert": RepositoryVulnerabilityAlertEvent,
    "secret_scanning_alert": SecretScanningAlertEvent,
    "security_advisory": SecurityAdvisoryEvent,
    "sponsorship": SponsorshipEvent,
    "star": StarEvent,
    "status": StatusEvent,
    "team": TeamEvent,
    "team_add": TeamAddEvent,
    "watch": WatchEvent,
    "workflow_dispatch": WorkflowDispatchEvent,
    "workflow_job": WorkflowJobEvent,
    "workflow_run": WorkflowRunEvent,
}

__all__ = [
    "BranchProtectionRuleEvent",
    "CheckRunEvent",
    "CheckSuiteEvent",
    "CodeScanningAlertEvent",
    "CommitCommentEvent",
    "CreateEvent",
    "DeleteEvent",
    "DeployKeyEvent",
    "DeploymentEvent",
    "DeploymentStatusEvent",
    "DiscussionEvent",
    "DiscussionCommentEvent",
    "ForkEvent",
    "GithubAppAuthorizationEvent",
    "GollumEvent",
    "InstallationEvent",
    "InstallationRepositoriesEvent",
    "IssueCommentEvent",
    "IssuesEvent",
    "LabelEvent",
    "MarketplacePurchaseEvent",
    "MemberEvent",
    "MembershipEvent",
    "MergeGroupEvent",
    "MetaEvent",
    "MilestoneEvent",
    "OrgBlockEvent",
    "OrganizationEvent",
    "PackageEvent",
    "PageBuildEvent",
    "PingEvent",
    "ProjectEvent",
    "ProjectCardEvent",
    "ProjectColumnEvent",
    "ProjectsV2ItemEvent",
    "PublicEvent",
    "PullRequestEvent",
    "PullRequestReviewEvent",
    "PullRequestReviewCommentEvent",
    "PullRequestReviewThreadEvent",
    "PushEvent",
    "ReleaseEvent",
    "RepositoryEvent",
    "RepositoryDispatchEvent",
    "RepositoryImportEvent",
    "RepositoryVulnerabilityAlertEvent",
    "SecretScanningAlertEvent",
    "SecurityAdvisoryEvent",
    "SponsorshipEvent",
    "StarEvent",
    "StatusEvent",
    "TeamEvent",
    "TeamAddEvent",
    "WatchEvent",
    "WorkflowDispatchEvent",
    "WorkflowJobEvent",
    "WorkflowRunEvent",
    "WebhookEvent",
    "webhook_action_types",
    "webhook_event_types",
]
