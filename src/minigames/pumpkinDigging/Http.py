#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.core.HTTPCommunication import HTTPConnection

class Http(object):
    def __init__(self):
        self.__http: HTTPConnection = HTTPConnection()

    def game_available(self) -> bool:
        try:
            response, content = self.__http.sendRequest('main.php?page=garden')
            content = content.decode('UTF-8')
            self.__http.update_token_from_content(content)
            self.__http.checkIfHTTPStateIsOK(response)
            return 'id="diggame_bar_img" class="autumn"' in content
        except:
            raise

    def init_game(self):
        try:
            response, content = self.__http.sendRequest(f'ajax/ajax.php?do=diggame_init&token={self.__http.token()}')
            self.__http.checkIfHTTPStateIsOK(response)
            return self.__http.generateJSONContentAndCheckForOK(content)
        except:
            raise

    def hit(self, zone: int):
        try:
            response, content = self.__http.sendRequest(f'ajax/ajax.php?do=diggame_map_hit&zone={zone}&token={self.__http.token()}')
            self.__http.checkIfHTTPStateIsOK(response)
            return self.__http.generateJSONContentAndCheckForOK(content)
        except:
            raise

    def finish_game(self):
        try:
            response, content = self.__http.sendRequest(f'ajax/ajax.php?do=diggame_map_finish&option=1&token={self.__http.token()}')
            self.__http.checkIfHTTPStateIsOK(response)
            return self.__http.generateJSONContentAndCheckForOK(content)
        except:
            raise