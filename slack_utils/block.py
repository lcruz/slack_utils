import json

class TextBlock():

    def __init__(self, text):
        self.type = "section"
        self.text = text

    def render(self):
        return {
            "type": "section",
            "text": {
                "type": "plain_text",
                "emoji": True,
                "text": self.text
            }
        }

class DivderBlock():

    def __init__(self):
        self.type = "divider"

    def render(self):
        return {
            "type": "divider",
        }

class InputBlock():

    def __init__(self, text, id=None, action_id=None, accesory=None, placeholder=None):
        self.type = "mrkdwn"
        self.text = text
        self.accesory = accesory
        self.id = id
        self.action_id = action_id
        self.placeholder = placeholder

    def render(self):
        data = {
			"type": "input",
			"element": {
				"type": "plain_text_input",
			},
			"label": {
				"type": "plain_text",
				"text": self.text,
				"emoji": True
			}
		}

        if self.id:
            data.update({"block_id" : self.id})

        if self.action_id:
            data.get("element").update({"action_id": self.action_id})

        if self.placeholder:
            data.get("element").update(
                {
                    "placeholder" : {
                        "type": "plain_text",
                        "text": self.placeholder
                    }
                })

        return data
class ActionButton():

    def __init__(self, text, style=None, id=None, value=None, url=None):
        self.text = text
        self.style = style
        self.url = url
        self.value = value
        self.id = id

    def render(self):
        data = {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": self.text
            }
        }
        if self.style:
            data.update({ "style": self.style})

        if self.value:
            data.update({ "value" : self.value})
        elif self.url:
            data.update({ "url" : self.url})

        if self.id:
            data.update({ "action_id" : self.id})

        return data

class ActionButtonBlock():

    def __init__(self, actions, id=None):
        self.type = "actions"
        self.actions = actions
        self.id = id

    def render(self):
        elements = [action.render() for action in self.actions]
        data = {
            "type": "actions",
            "elements": elements
        }
        if self.id:
            data.update({ "block_id": self.id })
        return data

class MarkdownBlock():

    def __init__(self, text, accesory=None):
        self.type = "mrkdwn"
        self.text = text
        self.accesory = accesory

    def render(self):
        data = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": self.text
            }
        }

        if self.accesory:
            data.update({ "accessory" : self.accesory.render() })

        return data

class ImageElement():

    def __init__(self, image_url, alt_text=""):
        self.image_url = image_url
        self.alt_text = alt_text

    def render(self):
        return {
            "type": "image",
            "image_url": self.image_url,
            "alt_text": self.alt_text
        }


class MarkdownElement():

    def __init__(self, text):
        self.text = text

    def render(self):
        return {
            "type": "mrkdwn",
            "text": self.text,
        }


class ContextBlock():

    def __init__(self, elements):
        self.elements = elements

    def render_elements(self):
        return list(map(lambda x: x.render(), self.elements))

    def render(self):
        return {
            "type": "context",
            "elements": self.render_elements()
        }


def render(blocks):
    return list(map(lambda x: x.render(), blocks))
