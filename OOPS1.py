class Computers:

    def __init__(self, name, color, operating_system):
        self.name = name
        self.color = color
        self.operating_system = operating_system

    def start(self):
        print('Starting my ' + self.name + ' computer')

    def re_start(self):
        print('Restarting my ' + self.name + ' computer')

    def shutdown(self):
        print('Shutting down my' + self.name + ' computer')

    def email(self):
        print('This method prints an email from the parent class')


class TabletComputers(Computers):

    def __init__(self):
        Computers.__init__(self, name='Microsoft Tablet', color='Purple', operating_system='Windows')
        #self.name = name
        print('This is the Tablet Computer Class init method')

    def download_app(self):
        print('Download tablet Apps')

    def email(self):
        super(TabletComputers, self).email()
        print('This method overrides the email function from the parent class')

    def print(self):
        print('This prints from the tablet computer')


tablet_comp = TabletComputers()
tablet_comp.start()
tablet_comp.shutdown()
tablet_comp.re_start()
tablet_comp.email()
tablet_comp.print()

tablet_comp1 = TabletComputers()
tablet_comp1.download_app()


apple = Computers('Macintosh', 'Green', 'MacOS')

print(apple.name)
print(apple.color)
print(apple.operating_system)
apple.start()
apple.shutdown()
apple.re_start()
apple.email()

hp = Computers('Hewlett Packard', 'Blue', 'Windows')

print(hp.name)
print(hp.color)
print(hp.operating_system)

dell = Computers('Dell', 'Black', 'Unix')

print(dell.name)
print(dell.color)
print(dell.operating_system)

