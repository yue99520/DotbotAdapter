from serial.tools import list_ports
from pydobot import Dobot


port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=True)

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print()
print('|Before| x:{', x, '} y:{', y, '} z:{', z, '} r:{', r, '} j1:{', j1, '} j2:{', j2, '} j3:{', j3, '} j4:{', j4, '}')
print()
device.speed(10)
device.wait_for_cmd(device.move_to(206, 0, 134))
(x, y, z, r, j1, j2, j3, j4) = device.pose()
device.wait_for_cmd(device.move_to(x, y, -20))

(x, y, z, r, j1, j2, j3, j4) = device.pose()
print()
print('|After | x:{', x, '} y:{', y, '} z:{', z, '} r:{', r, '} j1:{', j1, '} j2:{', j2, '} j3:{', j3, '} j4:{', j4, '}')
print()

device.close()