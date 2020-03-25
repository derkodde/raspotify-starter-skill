from mycroft import MycroftSkill, intent_file_handler
import subprocess

class ShellStarter(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    #sudo systemctl restart raspotify
    @intent_file_handler('start.raspotify.intent')
    def handle_start_raspotify(self, message):

        subprocess.call(["sudo","systemctl","restart","raspotify"])
        self.speak_dialog('start.raspotify')

    #sudo systemctl stop raspotify
    @intent_file_handler('stop.raspotify.intent')
    def handle_stop_raspotify(self, message):

        subprocess.call(["sudo","systemctl","stop","raspotify"])
        self.speak_dialog('stop.raspotify')


def create_skill():
    return ShellStarter()

