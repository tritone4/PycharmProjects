import sys

class VendingMachine():
    def __init__(self, type, seq_no):
        self.type = type
        self.seqno = seq_no
        self.address = ''
        self.total = 0

    def set_address(self, address):
        self.address = address

    def set_total(self, total):
        self.total = total

vm = VendingMachine(type=99, seq_no=101)
vm.set_address('Tokyou Ymato City')
vm.set_total(10000)

print(type(vm))
print(vm.type, vm.seqno, vm.address, vm.total)