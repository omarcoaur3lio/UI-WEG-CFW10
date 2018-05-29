#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
DocString for main.py.
Created by Marco Aurélio (C) 2018
Notes:
    Aplicação para controle de inversor WEG FW10
Examples:
    $ python main.py

"""
from telas import *
from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager

# Carregando arquivo de configuração personalizado
Config.read("config.ini")
# Nova instância de ScreenManager que receberá as telas da aplicação
screen_manager = ScreenManager()


class InversorApp(App):

    """Classe responsável pela
       criação da aplicação
    """

    def build(self):
        """Função que contruirá a aplicação
        Returns:
            screen_manager: Retorna as telas disponíveis na aplicação
        """
        tela_menu = TelaMenu(name="menu")
        self.icon = 'img/icon.png'
        self.title = 'Controle Inversor WEG CFW10'

        screen_manager.add_widget(tela_menu)
        screen_manager.add_widget(TelaAnalog(name="analogica"))
        screen_manager.add_widget(TelaDigital(name="digital"))

        return screen_manager


if __name__ == '__main__':
    InversorApp().run()
