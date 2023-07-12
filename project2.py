from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.topo import Topo

class goo( Topo ):
    def __init__( self ):
        # Initialize topology
        Topo.__init__( self )
        print('Adding hosts...\n')
        self.addHost('h1', ip='10.0.2.10', mac='00:00:00:00:00:01')
        self.addHost('h2', ip='10.0.2.20', mac='00:00:00:00:00:02')
        self.addHost('h3', ip='192.168.2.30', mac='00:00:00:00:00:03')
        self.addHost('h4', ip='192.168.2.40', mac='00:00:00:00:00:04')
        print('Adding switches...\n')
        self.addSwitch('s1')
        self.addSwitch('s2')
        print('Adding links...\n')
        self.addLink('s1', 'h1')
        self.addLink('s1', 'h2')
        self.addLink('s2', 'h3')
        self.addLink('s2', 'h4')
        self.addLink('s2', 'h1')

print('Building from Topo object...\n')
net = Mininet(topo=goo(),build=False)
net.addController(RemoteController(name='c1', ip='127.0.0.1', port=6633))
net.addController(RemoteController(name='c2', ip='127.0.0.1', port=6655))
net.build()
print('Starting network...\n')
net.start()
print('Creating more links...\n')
net.addLink('c1', 's1')
net.addLink('c2', 's2')
print('Assigning ip...\n')
net.get('h1').setIP(ip='192.168.2.10', intf='h1-eth1')
CLI(net)
net.stop()
