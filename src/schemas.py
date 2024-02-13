from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, validate=validate.Regexp('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,20}$'))

class PlayerSchema(Schema):
    last_played = fields.Str(dump_only=True)
    user = fields.Str(dump_only=True)
    highscore = fields.Int(dump_only=True)
    login_status = fields.Str(dump_only=True)

class leaderboardSchema(Schema):
    date_time = fields.Str(dump_only=True)
    username = fields.Str(dump_only=True)
    highscore = fields.Int(dump_only=True)

class UsernameSchema(Schema):
    username = fields.Str(required=True)

class QuestionSchema(Schema):
    ques_id = fields.Int(load_only=True)
    question = fields.Str(required=True)
    option1 = fields.Str(required=True)
    option2 = fields.Str(required=True)
    option3 = fields.Str(required=True)
    option4 = fields.Str(required=True)
    correct = fields.Str(required=True)