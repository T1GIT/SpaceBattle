from time import time_ns


class Debugger:
    t, s, a = 0, 0, 0

    @staticmethod
    def start():
        t = time_ns()
        Debugger.s += t - Debugger.t
        Debugger.t = t
        Debugger.a += 1

    @staticmethod
    def print(comment: str):
        print(f"{comment:20}" + ":", round((time_ns() - Debugger.t) / 1e6, 4), "ms |",
              "average:", Debugger.s / Debugger.a, " ms")
        Debugger.t = time_ns()
