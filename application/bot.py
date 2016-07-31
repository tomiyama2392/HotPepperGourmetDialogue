# -*- coding: utf-8 -*-
from modules.DialogueManagement.manager import DialogueManager
from modules.LanguageGeneration.generator import LanguageGenerator
from modules.LanguageUnderstanding.language_understanding import LanguageUnderstanding


class Bot(object):

    def __init__(self):
        self.generator = LanguageGenerator()
        self.language_understanding = LanguageUnderstanding()
        self.manager = DialogueManager()

    def reply(self, sent):
        dialogue_act = self.language_understanding.execute(sent)

        # Update Dialogue state
        self.manager.update_dialogue_state(dialogue_act)
        sys_act_type = self.manager.select_action(dialogue_act)

        # Generate Sentence
        sent = self.generator.generate_sentence(sys_act_type)

        return sent