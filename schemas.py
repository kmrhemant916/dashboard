from marshmallow import Schema, fields

class GitlabEventsSchema(Schema):
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
    project = fields.Dict(required=True)
    commits = fields.List(fields.Dict(), required=True)
    total_commits_count = fields.Int(required=True)
    push_options = fields.Dict(required=True)
    repository = fields.Dict(required=True)

