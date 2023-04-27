class smoke():
    man=''
    leaf = ''

    def take(self):
        print(f'{self.man}拿烟')

    def chou(self):
        print(f'抽{self.leaf}烟')



huazi = smoke()
huazi.man = '我'
huazi.leaf = '华子'
huazi.take()
huazi.chou()


yuxi = smoke()
yuxi.man = '你'
yuxi.leaf = '玉溪'
yuxi.take()
yuxi.chou()


znh = smoke()
znh.man = '他'
znh.leaf = '中南海'
znh.take() 
znh.chou()