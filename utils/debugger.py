from time import time_ns

from config import Configuration as Conf


class Debugger:
    t = 0

    @staticmethod
    def start():
        Debugger.t = time_ns()

    @staticmethod
    def print(comment: str):
        print(comment + ":", round((time_ns() - Debugger.t) / 1e6, 1), "ms")
        Debugger.start()
