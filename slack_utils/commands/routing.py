from django.utils.module_loading import import_string
from rest_framework.response import Response

def handle(routes, payload):
    if payload.get('type') in ("block_actions", "dialog_submission", "dialog_cancellation"):
        return route(routes, payload)

def route(routes, payload):
    print(payload)
    if payload.get("type") == "block_actions":
        for route in routes.get("block_actions"):
            for  action in payload.get("actions"):
                if action.get("block_id") == route.get("block_id") and  \
                    action.get("action_id") == route.get("action_id"):
                    command = import_string(route.get("command"))
                    instance = command(payload, action)
                    return instance.execute()

    if payload.get("type") == "dialog_submission":
        for route in routes.get("dialog_submission"):
            if route.get("callback_id") == payload.get("callback_id"):
                command = import_string(route.get("command"))
                instance = command(payload)
                return instance.execute()

    return Response("No asingado")
