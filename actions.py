# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import spacy


class ActionSetPart(Action):

    def name(self):
        return "action_set_part"

    def run(self, dispatcher, tracker, domain):
        message = tracker.latest_message.get('text')
        dispatcher.utter_message("Hello!")

        return [SlotSet('participants', message)]
