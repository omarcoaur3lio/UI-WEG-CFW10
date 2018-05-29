#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Summary

Attributes:
    liga (int): Armazena o estado lógico do motor
    sentido (int): Armazena o estado lógico e realiza a inversão do motor
    var_pwm (TYPE): Armazena os valores PWM para variação de velocidade
"""

import RPi.GPIO as gpio
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

liga = 0
sentido = 0
var_pwm = gpio.PWM(23, 100)

# Configuração dos pinos de I/O
gpio.setmode(gpio.BOARD)
gpio.setup(23, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(21, gpio.OUT)

# Silenciando avisos gpio
gpio.setwarnings(False)
# Inicializando PWM
var_pwm.start(0)


class TelaMenu(Screen):

    """Summary:
        Classe que contem os componentes da tela inicial da aplicação.
    """
    pass


class TelaDigital(Screen):

    """Summary:
        Tela contendo as funções de controle digital da aplicação

    Attributes:
        img (TYPE): Objeto responsável por receber a animação indicando
        o funcionamento do motor e o sentido de giro
    """

    img = ObjectProperty()

    def partida_motor(self):
        """Summary:
            Função que realiza o acionamento do motor
        """
        global liga

        if (liga == 0):
            self.img.source = "./img/fan-right.gif"
            self.img.anim_delay = 0.12
            self.ids.info_motor.text = "[color=#1F2526FF]Girando para[/color]"\
                " [color=#20BED8FF][b]DIREITA[/b][/color]"
            liga = 1
            gpio.output(19, gpio.HIGH)
            print("MOTOR LIGADO")
        else:
            self.img.source = "./img/fan-stoped.png"
            self.img.anim_delay = 0.00
            self.ids.info_motor.text = "[color=#1F2526FF]Motor "\
                "[b]DESLIGADO[/b][/color]"
            liga = 0
            gpio.output(19, gpio.LOW)
            print("MOTOR DESLIGADO")

    def inverte_giro(self):
        """Summary:
            Função que realiza a inversão no sentido de giro do motor
        """
        global sentido
        global liga
        self.img.anim_delay = 0.00

        if ((sentido == 1) and (liga == 1)):
            self.img.source = "./img/fan-right.gif"
            self.ids.info_motor.text = "[color=#1F2526FF]Girando para[/color]"\
                " [color=#20BED8FF][b]DIREITA[/b][/color]"
            self.img.anim_delay = 0.12
            sentido = 0
            gpio.output(21, gpio.HIGH)
            print("Sentido HORARIO")

        elif ((sentido == 0) and (liga == 1)):
            self.img.source = "./img/fan-left.gif"
            self.ids.info_motor.text = "[color=#1F2526FF]Girando para[/color]"\
                " [color=#20D8BAFF][b]ESQUERDA[/b][/color]"
            self.img.anim_delay = 0.12
            sentido = 1
            gpio.output(21, gpio.LOW)
            print("Sentido ANTI-HORARIO")


class TelaAnalog(Screen):

    """Summary:
        Classe contendo os comandos para ajustar a velocidade do motor

    Attributes:
        valor (int): Armazenará o valor (em %) desejado para a velocidade
    """

    valor = 0

    def valor_velocidade(self):
        """Summary:
            Função para escolha da velocidade desejada (em %).
        """
        global valor
        valor = int(self.ids.slider.value)
        self.ids.lbl_vel.text = "[b][color=#1F2526FF]Velocidade: "\
            "[/color][color=#20BED8FF] %s%%[/color][/b]" % valor

    def set_speed(self):
        """Summary:
            Função que ajustará e enviará para o inversor (via PWM), o nível de
            velocidade escolhido.
        """
        global valor
        var_pwm.ChangeDutyCycle(int(valor))
        print("Velocidade: ", valor)
