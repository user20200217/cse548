from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.topo import Topo
from random import random
from math import trunc

class goo( Topo ):
    def __init__( self ):
        # Initialize topology
        Topo.__init__( self )
        print('Adding hosts...\n')
        self.addHost('h1', ip='10.0.1.10/16', mac='00:00:00:00:00:01')
        self.addHost('h2', ip='10.0.2.20/16', mac='00:00:00:00:00:02')
        self.addHost('h3', ip='10.0.3.30/16', mac='00:00:00:00:00:03')
        self.addHost('h4', ip='10.0.4.40/16', mac='00:00:00:00:00:04')
        print('Adding switches...\n')
        self.addSwitch('s1', ip='10.0.0.1/16', mac='10:00:00:00:00:00')
        print('Adding links...\n')
        self.addLink('s1', 'h1')
        self.addLink('s1', 'h2')
        self.addLink('s1', 'h3')
        self.addLink('s1', 'h4')

print('Building from Topo object...\n')
net = Mininet(topo=goo(),build=False)
net.addController(RemoteController(name='c1', ip='127.0.0.1', port=6655))
net.build()
print('Starting network...\n')
net.start()
print('Creating more links...\n')
net.addLink('c1', 's1')
print('Flooding the network...\n')
po = net.get('h1').popen('hping3 10.0.4.40 -c 10000 -S --flood -a 10.0.10.1 -V')
#h = ['h1', 'h2', 'h3']
#i = trunc(random()*3)
#print('Using '+h[i])
#po = net.get(h[i]).popen('hping3 10.0.4.40 -c 10000 -S --flood --rand-source -V')
CLI(net)
net.stop()
