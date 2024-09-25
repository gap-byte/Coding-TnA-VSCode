from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyApp(App):
    def build(self):
        return Label(text='Hello, Kivy!')
    
class MyApp(App):
    def build(self):
        return Button(text='Click Me')
    
class MyApp(App):
    def build(self):
        btn = Button(text='Click Me')
        btn.bind(on_press=self.button_clicked)
        return btn

    def button_clicked(self, instance):
        print('Button clicked!')



class Ball(Widget):
    pass

class MyApp(App):
    def build(self):
        layout = BoxLayout()
        ball = Ball()
        layout.add_widget(ball)
        return layout
    
class Ball(Widget):
    def update(self):
        self.x += 1

class MyApp(App):
    def build(self):
        # ...
        Clock.schedule_interval(self.update_ball, 1/60)
        return layout

    def update_ball(self, dt):
        self.ball.update()

class Ball(Widget):
    def update(self):
        self.x += self.velocity_x
        if self.x < 0 or self.x > self.parent.width:
            self.velocity_x *= -1

class MyApp(App):
    def build(self):
        # ...
        self.ball.bind(on_touch_down=self.on_touch_down)
        return layout

    def on_touch_down(self, instance, touch):
        if self.ball.collide_point(*touch.pos):
            self.ball.velocity_y = -10

if __name__ == '__main__':
    MyApp().run()

