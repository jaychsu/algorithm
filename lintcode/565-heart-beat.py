class HeartBeat:

    def __init__(self):
        self.slaves_ip_list = {}

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    def initialize(self, slaves_ip_list, k):
        self.slaves_ip_list.update(dict.fromkeys(slaves_ip_list, 0))
        self.ttl = 2 * k

    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    def ping(self, timestamp, slave_ip):
        if slave_ip in self.slaves_ip_list:
            self.slaves_ip_list[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    def getDiedSlaves(self, timestamp):
        if not timestamp:
            return []
        return [ ip
            for ip, t0 in self.slaves_ip_list.items()
            if timestamp - t0 >= self.ttl
        ]
