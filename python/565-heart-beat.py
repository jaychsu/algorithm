class HeartBeat:

    def __init__(self):
        self.slaves_ip_list = {}

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    def initialize(self, slaves_ip_list, k):
        self.k = k
        for ip in slaves_ip_list: self.slaves_ip_list[ip] = 0

    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    def ping(self, timestamp, slave_ip):
        if slave_ip not in self.slaves_ip_list:
            return
        self.slaves_ip_list[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    def getDiedSlaves(self, timestamp):
        return [
            ip
            for ip, last_live in self.slaves_ip_list.items()
            if last_live + 2 * self.k <= timestamp
        ]
