#composition
#processor class
class Processor:
    def __init__(self, manufacturer, speed):
        #assign values to the instance variables
        self.manufacturer = manufacturer
        self.speed = speed
    def get_manufacturer(self):
        #return the manufacturer
        return self.manufacturer
    def get_speed(self):
        #return the speed
        return self.speed

    def boot(self):
        #boot the processor
        print('booting...')

#harddisk class
class HardDisk:
    def __init__(self, capacity):
        self.capacity = capacity

    def get_capacity(self):
        #return capacity
        return self.capacity

#computer class
class Computer:
    def __init__(self, make, processor, hdd):
        #assign values to the instance variables
        self.make = make
        self.processor = processor
        self.hdd = hdd
    def boot_computer(self):
        #call the boot method of the Processor class
        self.processor.boot()

    def get_hdd_size(self):
        #call the get_capacity method of the HardDisk class
        print('Hard disk size: ' + self.hdd.get_capacity())
    def get_processor_speed(self):
        #call the get_speed method of the processor
        print('Processor speed: ' + self.processor.get_speed())

#instantiating the Processor object
processor = Processor('Intel', '1.8GHz')

#instantiating the HardDisk object
hdd = HardDisk('500GB')
#instantiating the Computer object
comp = Computer('HP', processor, hdd)
#Accessing the methods of the Computer Class
comp.boot_computer()
comp.get_processor_speed()
comp.get_hdd_size()
