from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def on_enter_user(self, event):
        print("I'm entering user")

        reply_token = event.reply_token
        send_text_message(reply_token, " start game \n please enter start")
    def is_going_to_q1(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_q2(self, event):
        text = event.message.text
        return text.lower() == "yes"

    def on_enter_q1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, " 1.去年至少看過一次美術展覽，家中書櫃裏至少有一本和美術相關的書籍？\nenter yes or no")

    def on_exit_q1(self,event):
        print("Leaving state1")

    def on_enter_q2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "2.你的地理國文成績比數學理化好？\nenter yes or no")
        self.go_back()

    def on_exit_q2(self):
        print("Leaving state2")
