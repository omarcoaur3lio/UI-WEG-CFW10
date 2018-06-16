#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
DocString for Inversor.py.
Created by Marco Aurélio (C) 2018
Notes:
    Controle para Inversor
Examples:
    $ python Inversor.py

"""


import RPi.GPIO as gpio
from tkinter import *

var = 0
liga = 0
sentido = 0


gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

gpio.setup(23, gpio.OUT)
gpio.setup(19, gpio.OUT)
gpio.setup(21, gpio.OUT)
var_pwm = gpio.PWM(23, 100)
var_pwm.start(0)


class Application:
    def __init__(self, master=None):
        master.title("Inversor WEG CFW10")
        master["bg"] = "white"
        self.fontePadrao = ("Arial", "48")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["bg"] = "white"
        self.primeiroContainer["pady"] = 40
        self.primeiroContainer["padx"] = 200
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 10
        self.segundoContainer["padx"] = 200
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 10
        self.terceiroContainer["padx"] = 200
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 10
        self.quartoContainer["padx"] = 200
        self.quartoContainer.pack()

        self.quintoContainer = Frame(master)
        self.quintoContainer["pady"] = 40
        self.quintoContainer["padx"] = 200
        self.quintoContainer["bg"] = "white"
        self.quintoContainer.pack()

        self.titulo = Label(
            self.primeiroContainer,
            text="Controle para Inversor")
        self.titulo["font"] = ("Arial", "24", "bold")
        self.titulo["bg"] = ("white")
        self.titulo["fg"] = ("blue")
        self.titulo.pack()

        self.nomeLabel = Label(
            self.quintoContainer,
            text="Velocidade: ",
            bg="white",
            padx=3,
            font=("Arial", "16", "bold"))

        self.nomeLabel.pack(side=LEFT)

        self.nome = Scale(
            self.quintoContainer,
            bg="white",
            from_=0,
            to=100,
            orient=HORIZONTAL,
            activebackground="green",
            sliderlength=10,
            length=200,
            width=20,
            variable=var)
        self.nome.pack()

        self.autenticar = Button(self.segundoContainer)
        self.autenticar["text"] = "ON - OFF"
        self.autenticar["font"] = ("Arial", "16", "bold")
        self.autenticar["width"] = 25
        self.autenticar["height"] = 2
        self.autenticar["command"] = self.ligadesliga
        self.autenticar.pack()

        self.autenticar = Button(self.terceiroContainer)
        self.autenticar["text"] = "Inverter Sentido"
        self.autenticar["font"] = ("Arial", "16", "bold")
        self.autenticar["width"] = 25
        self.autenticar["height"] = 2
        self.autenticar["command"] = self.sentido
        self.autenticar.pack()

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Alterar Velocidade"
        self.autenticar["font"] = ("Arial", "16", "bold")
        self.autenticar["width"] = 25
        self.autenticar["height"] = 2
        self.autenticar["command"] = self.trocavel
        self.autenticar.pack(side=LEFT)

    def sentido(self):
        global sentido
        if (sentido == 0):
            print('Sentido Horario')
            sentido = 1
            gpio.output(21, gpio.HIGH)
        else:
            print('Sentido Anti-Horario')
            sentido = 0
            gpio.output(21, gpio.LOW)

    def ligadesliga(self):
        global liga
        if (liga == 0):
            print('Motor Ligado')
            liga = 1
            gpio.output(19, gpio.HIGH)
        else:
            print('Motor Desligado')
            liga = 0
            gpio.output(19, gpio.LOW)

    def trocavel(self):
        var_pwm.ChangeDutyCycle(self.nome.get())
        print('Velocidade:', self.nome.get(), '%')


root = Tk()
Application(root)
root.mainloop()
