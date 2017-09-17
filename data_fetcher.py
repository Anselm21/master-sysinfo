import grequests


class DataFetcher:

    def __init__(self, servers_list):
        """ Constructor
         :param servers_list: List of cluster's server urls to make request for sysinfo
        """
        self.servers_list = servers_list
        self.failed_servers = {}

    def req_except_handler(self, request, exception):
        self.failed_servers[request.url] = str(exception)

    def get_info(self):
            shells = (grequests.get(server) for server in self.servers_list)
            responses = grequests.map(shells, exception_handler=self.req_except_handler)
            result = {}
            for r in responses:
                try:
                    result[r.url] = {'status': r.status_code, 'text': r.text}
                except:
                    pass
            for failed in self.failed_servers:
                result[failed] = {'text': self.failed_servers[failed], 'status': 500}
            return result
