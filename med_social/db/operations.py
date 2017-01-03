from django.db import migrations
from django.db.migrations.operations.base import Operation


class AddField(migrations.AddField):
    """
    Allow adding a field to a model from a different application.

    This enables us to add the field to contrib.admin.LogEntry that
    stores the schema for an aware object.
    """
    def __init__(self, *args, **kwargs):
        self.app_label = kwargs.pop('app_label')
        super(AddField, self).__init__(*args, **kwargs)

    def state_forwards(self, app_label, state):
        return super(AddField, self).state_forwards(self.app_label, state)

    def database_forwards(self, app_label, *args):
        return super(AddField, self).database_forwards(self.app_label, *args)

    def state_backwards(self, app_label, state):
        return super(AddField, self).state_backwards(self.app_label, state)

    def database_backwards(self, app_label, *args):
        return super(AddField, self).database_backwards(self.app_label, *args)


class LoadSQLFromScript(Operation):
    def __init__(self, filename):
        self.filename = filename

    reversible = False

    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        schema_editor.execute(open(self.filename).read().replace('%', '%%'))
