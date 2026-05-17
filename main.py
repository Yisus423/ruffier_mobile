from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.uix.button import Button
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, NumericProperty

from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

from seconds import Seconds


def check_int(str_num):
    # retorna un número o False si la cadena no es convertida
    try:
        return int(str_num)
    except:
        return False


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = MDLabel(text=txt_instruction)

        lbl1 = MDLabel(text="Ingresa tu nombre:", halign="right")
        self.in_name = MDTextField(multiline=False)
        lbl2 = MDLabel(text="Ingresa tu edad:", halign="right")

        self.in_age = MDTextField(text="7", multiline=False)
        self.btn = Button(
            text="Iniciar", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        app = MDApp.get_running_app()
        app.name = self.in_name.text
        age = check_int(self.in_age.text)
        if age is False or age < 7:
            app.age = 7
            self.in_age.text = str(app.age)
        else:
            app.age = age
        self.manager.current = "pulse1"


class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        instr = MDLabel(text=txt_test1)
        # lbl1 = Label(text='Cuenta tu pulso')
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)

        line = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl_result = MDLabel(text="Ingresa el resultado:", halign="right")
        self.in_result = MDTextField(text="0", multiline=False)
        self.in_result.set_disabled(True)

        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        self.btn = Button(
            text="Iniciar", size_hint=(0.3, 0.4), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        # outer.add_widget(lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "Continuar"

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            app = MDApp.get_running_app()
            p1 = check_int(self.in_result.text)
            if p1 is not False and p1 > 0:
                app.p1 = p1
                self.manager.current = "sits"
            else:
                app.p1 = 0
                self.in_result.text = "0"


class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = MDLabel(text=txt_sits)

        self.btn = Button(
            text="Continuar", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        self.manager.current = "pulse2"


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False

        self.stage = 0
        super().__init__(**kwargs)

        instr = MDLabel(text=txt_test3)

        line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl1 = MDLabel(text="Cuenta tu pulso")

        lbl_result1 = MDLabel(text="Resultado:", halign="right")
        self.in_result1 = MDTextField(text="0", multiline=False)

        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        lbl_result2 = MDLabel(text="Resultado después de descanso:", halign="right")
        self.in_result2 = MDTextField(text="0", multiline=False)

        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)

        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)

        self.btn = Button(
            text="Iniciar", size_hint=(0.3, 0.5), pos_hint={"center_x": 0.5}
        )
        self.btn.on_press = self.next

        outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                # hemos terminado el primer conteo; vamos a descansar
                self.stage = 1
                self.lbl1.text = "Descansa"
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                # hemos terminado nuestro descanso; cuenta de nuevo
                self.stage = 2
                self.lbl1.text = "Cuenta tu pulso"
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = "Completar"
                self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            app = MDApp.get_running_app()
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)

            valid_p2 = p2 is not False and p2 > 0
            valid_p3 = p3 is not False and p3 > 0

            if not valid_p2:
                app.p2 = 0
                self.in_result1.text = "0"
            else:
                app.p2 = p2

            if not valid_p3:
                app.p3 = 0
                self.in_result2.text = "0"
            else:
                app.p3 = p3

            if valid_p2 and valid_p3:
                self.manager.current = "result"


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.instr = MDLabel(text="")
        self.outer.add_widget(self.instr)

        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        app = MDApp.get_running_app()
        self.instr.text = app.name + "\n" + test(app.p1, app.p2, app.p3, app.age)


class HeartCheck(MDApp):
    name = StringProperty("")
    age = NumericProperty(7)
    p1 = NumericProperty(0)
    p2 = NumericProperty(0)
    p3 = NumericProperty(0)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PulseScr(name="pulse1"))
        sm.add_widget(CheckSits(name="sits"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(Result(name="result"))
        return sm


app = HeartCheck()
app.run()
