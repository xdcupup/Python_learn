class Tiger():
    def run(self):
        print('爱跑')

class Lion():
    def shout(self):
        print('爱叫')


class Linger(Tiger,Lion):
    def eatmeat(self):
        print('爱吃肉')

l = Linger()
l.run()
l.shout()
l.eatmeat()