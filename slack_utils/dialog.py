class DialogText():

    def __init__(self, label, name, hint=None):
        self.label = label
        self.name = name
        self.hint = hint

    def render(self):
        return {
            "type": "text",
            "label": self.label,
            "name": self.name,
            "hint": self.hint
        }

class DialogSelect():

    def __init__(self, label, name, hint):
        self.label = label
        self.name = name
        self.hint = hint

    def render(self):
        return {
            "type": "select",
            "label": self.label,
            "name": self.name,
            "hint": self.hint
        }

class DialogTextArea():
    def __init__(self, label, name, data_source):
        self.label = label
        self.name = name
        self.data_source = data_source

    def render(self):
        return {
            "type": "select",
            "label": self.label,
            "name": self.name,
            "data_source": self.data_source
        }

class Dialog():

    def __init__(self, id, title, submit_label="Send", notify_on_cancel=False):
        self.id = id
        self.title = title
        self.submit_label = submit_label
        self.notify_on_cancel = notify_on_cancel
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def render(self):

        elements = [x.render() for x in self.elements]

        return {
            "callback_id": self.id,
            "title": self.title,
            "submit_label": self.submit_label,
            "notify_on_cancel": self.notify_on_cancel,
            "elements": elements
        }
