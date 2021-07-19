class SlackCommand():

    def __init__(self, payload, action=None):
        self.payload = payload
        self.action = action
        self.channel = self.payload.get("channel").get('id')

    def get_state(self):
        return {
            "id": self.action.get('value'),
            "ts": self.payload.get("message").get("ts"),
            "channel": self.payload.get("channel").get('id')
        }


class DialogSubmission(SlackCommand):

    def __init__(self, payload):
        super(DialogSubmission, self).__init__(payload)
        self.submission = payload.get('submission')
