from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.properties import StringProperty

class Timer(Label):
    text = StringProperty("00:00")

    def start(self):
        self.seconds = 0
        self.timer = Clock.schedule_interval(self.update, 1)

    def update(self, dt=None):
        self.seconds += 1
        self.text = "{:02d}:{:02d}".format(*divmod(self.seconds, 60))

    def stop(self):
        Clock.unschedule(self.timer)

    def reset(self):
        self.seconds = 0
        self.text = "00:00"


Factory.register('Timer', module='widgets')
Builder.load_file('widgets/timer.kv')
