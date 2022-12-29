from marshmallow import Schema, fields

class GitlabProjectSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    web_url = fields.Str(required=True)
    avatar_url = fields.Str(allow_none=True)
    git_ssh_url = fields.Str(required=True)
    git_http_url = fields.Str(required=True)
    namespace = fields.Str(required=True)
    visibility_level = fields.Int(required=True)
    path_with_namespace = fields.Str(required=True)
    default_branch = fields.Str(required=True)
    homepage = fields.Str(required=True)
    url = fields.Str(required=True)
    ssh_url = fields.Str(required=True)
    http_url = fields.Str(required=True)
    ci_config_path = fields.Str(required=True)

class GitlabPushEventSchema(Schema):
    object_kind = fields.Str(required=True)
    event_name = fields.Str(required=True)
    before = fields.Str(required=True)
    after = fields.Str(required=True)
    ref = fields.Str(required=True)
    checkout_sha = fields.Str(required=True)
    message = fields.Str(allow_none=True)
    user_id = fields.Int(required=True)
    user_name = fields.Str(required=True)
    user_username = fields.Str(required=True)
    user_email = fields.Str(required=True)
    user_avatar =fields.Str(required=True)
    project_id = fields.Int(required=True)
    project = fields.Nested(GitlabProjectSchema(), required=True)
    commits = fields.List(fields.Dict(), required=True)
    total_commits_count = fields.Int(required=True)
    push_options = fields.Dict(required=True)
    repository = fields.Dict(required=True)

