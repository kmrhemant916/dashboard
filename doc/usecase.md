# API requirement for dashboard

## Get and process events form github/gitlab

### Build count by author

POST /gitlab/events

PAYLOAD

```json
{
    "object_kind": "push",
    "event_name": "push",
    "before": "f3cbf788332dc3d0216d9c228868367eca33f9fc",
    "after": "85c31889b5180da8ab3078194e9a0d84dff6f8ab",
    "ref": "refs/heads/develop",
    "checkout_sha": "85c31889b5180da8ab3078194e9a0d84dff6f8ab",
    "message": null,
    "user_id": 12251527,
    "user_name": "Sanjeev Batni",
    "user_username": "sanjb1",
    "user_email": "",
    "user_avatar": "https://secure.gravatar.com/avatar/3cda730673d8a67b20d9f1b49d5ef8ac?s=80&d=identicon",
    "project_id": 39216643,
    "project": {
        "id": 39216643,
        "name": "server",
        "description": "Repository for a1 objectstore server",
        "web_url": "https://gitlab.com/altairengineering/altair365/platform/object-store/server",
        "avatar_url": null,
        "git_ssh_url": "git@gitlab.com:altairengineering/altair365/platform/object-store/server.git",
        "git_http_url": "https://gitlab.com/altairengineering/altair365/platform/object-store/server.git",
        "namespace": "object-store",
        "visibility_level": 0,
        "path_with_namespace": "altairengineering/altair365/platform/object-store/server",
        "default_branch": "develop",
        "ci_config_path": "",
        "homepage": "https://gitlab.com/altairengineering/altair365/platform/object-store/server",
        "url": "git@gitlab.com:altairengineering/altair365/platform/object-store/server.git",
        "ssh_url": "git@gitlab.com:altairengineering/altair365/platform/object-store/server.git",
        "http_url": "https://gitlab.com/altairengineering/altair365/platform/object-store/server.git"
    },
    "commits": [
        {
            "id": "55aa6ed6a3b50202b8c4eaf3b40f184050597f03",
            "message": "Updates\n",
            "title": "Updates",
            "timestamp": "2022-12-12T17:29:17+03:00",
            "url": "https://gitlab.com/altairengineering/altair365/platform/object-store/server/-/commit/55aa6ed6a3b50202b8c4eaf3b40f184050597f03",
            "author": {
                "name": "Tejaswy Muralikrishna",
                "email": "tejaswy.muralikrishna@altair.com"
            },
            "added": [],
            "modified": [
                "services/common/src/main/java/aone/services/common/ActionUtils.java",
                "services/common/src/main/java/aone/services/common/RemoteDispatcher.java"
            ],
            "removed": []
        },
        {
            "id": "e6b842226351eceb3771c6c6802019c6e1700800",
            "message": "Remove commented code\n",
            "title": "Remove commented code",
            "timestamp": "2022-12-12T19:49:24+03:00",
            "url": "https://gitlab.com/altairengineering/altair365/platform/object-store/server/-/commit/e6b842226351eceb3771c6c6802019c6e1700800",
            "author": {
                "name": "Tejaswy Muralikrishna",
                "email": "tejaswy.muralikrishna@altair.com"
            },
            "added": [],
            "modified": [
                "services/common/src/main/java/aone/services/common/ActionUtils.java"
            ],
            "removed": []
        },
        {
            "id": "85c31889b5180da8ab3078194e9a0d84dff6f8ab",
            "message": "Merge branch 'EventPublishResolveRef' into 'develop'\n\nEvent publish resolve ref\n\nSee merge request altairengineering/altair365/platform/object-store/server!233",
            "title": "Merge branch 'EventPublishResolveRef' into 'develop'",
            "timestamp": "2022-12-13T06:37:49+00:00",
            "url": "https://gitlab.com/altairengineering/altair365/platform/object-store/server/-/commit/85c31889b5180da8ab3078194e9a0d84dff6f8ab",
            "author": {
                "name": "Sanjeev Batni",
                "email": "sanjb@altair.com"
            },
            "added": [],
            "modified": [
                "services/common/src/main/java/aone/services/common/ActionUtils.java",
                "services/common/src/main/java/aone/services/common/RemoteDispatcher.java"
            ],
            "removed": []
        }
    ],
    "total_commits_count": 3,
    "push_options": {},
    "repository": {
        "name": "server",
        "url": "git@gitlab.com:altairengineering/altair365/platform/object-store/server.git",
        "description": "Repository for a1 objectstore server",
        "homepage": "https://gitlab.com/altairengineering/altair365/platform/object-store/server",
        "git_http_url": "https://gitlab.com/altairengineering/altair365/platform/object-store/server.git",
        "git_ssh_url": "git@gitlab.com:altairengineering/altair365/platform/object-store/server.git",
        "visibility_level": 0
    }
}
```

response

{ 12251527: {"user_name": "Sanjeev Batni", "repository_name": "server"} }

## Gitlab API

* <https://docs.gitlab.com/ee/user/project/integrations/webhook_events.html#push-events>

## Get and process events form CICD pipeline

## Get and process events form our alerting pipeline

## Get and process events form our cloud

## Get and process events form our k8s
