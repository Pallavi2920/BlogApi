from mongoengine import Document ,fields,connect
connect('blogApidb')
import datetime
class Blog(Document):
    title = fields.StringField(max_length=50)
    content = fields.StringField()
    created_at = fields.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = fields.DateTimeField(default=datetime.datetime.utcnow)
