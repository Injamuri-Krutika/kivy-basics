from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Ellipse
import kivy
kivy.require("1.11.1")


class PaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode="hsv")
            d = 30.
            Ellipse(pos=(touch.x - d/2, touch.y-d/2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class PaintApp(App):

    def build(self):
        parent = Widget()

        self.painter = PaintWidget()
        parent.add_widget(self.painter)

        clear_btn = Button(text="Clear")
        clear_btn.bind(on_release=self.canvas_clear)
        parent.add_widget(clear_btn)

        return parent

    def canvas_clear(self, obj):
        self.painter.canvas.clear()


if __name__ == "__main__":
    PaintApp().run()
