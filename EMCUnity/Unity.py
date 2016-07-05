import requests
import json
import UnityClasses
from .UnityClasses import *

requests.packages.urllib3.disable_warnings()

class Unity:
    """ Class representing an EMC Unity Array """

    def __init__(self, ip_addr, username, password):
        self.ip_addr = ip_addr
        self.username = username
        self.password = password
        self.is_auth = False
        self.api_url = 'https://%s/api' % self.ip_addr

        self.headers = {'Accept':'application/json',
                        'Content-type':'application/json',
                        'X-EMC-REST-CLIENT':'true'}

        self.session = requests.Session()

        sys_info = self.unity_request('/instances/basicSystemInfo/0').json()
        self.name = sys_info['content']['name']
        self.model = sys_info['content']['model']
        self.software = sys_info['content']['softwareVersion']

    def process_response(self, response):
        """ Process the HTTPS response and set headers or raise exceptions """ 
        response.raise_for_status()

        if 'EMC-CSRF-TOKEN' not in self.headers:
            self.headers['EMC-CSRF-TOKEN'] = response.headers.get('emc-csrf-token')
            self.is_auth = True

        return
 
    def get_from_type(self, url_path, object_type, payload = None):
        """ 
        Performs a request of all fields for a given object_type unless
        specific fields have been requested as part of the payload
        """

        if not payload:
            payload = dict()

        if 'fields' not in payload:
            payload['fields'] = ",".join(object_type._fields)

        response = self.unity_request(url_path,'GET',payload = payload).json()

        if 'entries' in response:
            returned_items = []
            for item in response['entries']:
                returned_items.append(object_type(**item['content']))
            return returned_items

        elif 'content' in response:
            return object_type(**response['content'])
        
        else:
            return None

    def unity_request(self, url_path, method = 'GET', payload = None):
        """ Perform a request to the Unity array """

        if not payload:
            payload = dict()

        url = self.api_url + url_path

        if method == 'GET':
            request_function = self.session.get
        elif method == 'POST':
            request_function = self.session.post
        elif method == 'DELETE':
            request_function = self.session.delete
        else:
            return None

        if method != 'POST':
            if self.is_auth:
                response = request_function(url, verify = False, 
                                            headers = self.headers, 
                                            params = payload)
            else:
                response = request_function(url, verify = False, 
                                            auth = (self.username, self.password), 
                                            headers = self.headers,
                                            params = payload)
        else: # For POST requests, we pass data, not payload
            if self.is_auth:
                response = request_function(url, verify = False,
                                            headers = self.headers,
                                            data = payload)
            else:
                response = request_function(url, verify = False, 
                                            auth = (self.username, self.password), 
                                            headers = self.headers, 
                                            data = payload)
            
        self.process_response(response)

        return response     

    def get(self, url_path, payload = None):
        """ Wrapper for performing a GET unity request """
        self.unity_request(url_path, method='GET', payload = payload)

    def post(self, url_path, payload = None):
        """ Wrapper for performing a POST unity request """
        self.unity_request(url_path, method='POST', payload = payload)

    def delete(self, url_path, payload = None):
        """ Wrapper for performing a DELETE unity request """
        self.unity_request(url_path, method='DELETE', payload = payload)


    def get_object(self, unity_type, item_filter = None, item_id=None, item_name=None):
        """ Get an object (singular or a collection) """

        payload = dict()

        # Take the unity_type string passed in and determine the actual object
        unity_object = getattr(UnityClasses, "Unity%s" % unity_type)

        if item_filter:
            payload['filter'] = item_filter

        if not item_id and not item_name: # Request is for all objects
            response = self.get_from_type('/types/%s/instances' % unity_type, unity_object, payload = payload)
            return response

        if item_id:  # Request is for a specific ID
            response = self.get_from_type('/instances/%s/%s' % (unity_type, item_id), unity_object, payload = payload)
        elif item_name: # Request is for a specific name
            if 'filter' in payload:
                payload['filter'] = payload['filter'] + ' && name eq "%s"' % item_name
            else:
                payload['filter'] = 'name eq "%s"' % item_name

            response = self.get_from_type('/types/%s/instances' % unity_type, unity_object, payload = payload)

        return response

    # Network communications
    def cifsServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('cifsServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def dnsServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('dnsServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fileDNSServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fileDNSServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fileInterface(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fileInterface',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    
    def fileKerberosServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fileKerberosServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fileLDAPServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fileLDAPServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fileNDMPServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fileNDMPServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fileNISServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fileNISServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    
    def ftpServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ftpServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ipInterface(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ipInterface',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ipPort(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ipPort',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def iscsiNode(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('iscsiNode',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    
    def iscsiPortal(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('iscsiPortal',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def iscsiSettings(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('iscsiSettings',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def linkAggregation(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('linkAggregation',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    
    def mgmtInterface(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('mgmtInterface',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def mgmtInterfaceSettings(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('mgmtInterfaceSettings',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    
    def nasServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('nasServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def nfsServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('nfsServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def preferredInterfaceSettings(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('preferredInterfaceSettings',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def route(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('route',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def smtpServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('smtpServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def urServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('urServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def virusChecker(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('virusChecker',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def vmwareNasPEServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('vmwareNasPEServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    
    # Events and Alerts
    def alert(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('alert',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def alertConfig(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('alertConfig',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def alertConfigSNMPTarget(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('alertConfigSNMPTarget',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def event(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('event',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Jobs
    def job(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('job',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Remote Systems
    def cifsShare(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('cifsShare',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def datastore(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('datastore',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def host(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('host',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def hostContainer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('hostContainer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def hostIPPort(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('hostIPPort',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def hostInitiator(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('hostInitiator',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def hostInitiatorPath(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('hostInitiatorPath',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def hostLUN(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('hostLUN',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def hostVVolDatastore(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('hostVVolDatastore',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def nfsShare(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('nfsShare',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def remoteSystem(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('remoteSYstem',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def rpChapSettings(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('rpChapSettings',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def vm(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('vm',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def vmDisk(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('vmDisk',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def vmwarePE(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('vmwarePE',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Storage Management
    def aclUser(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('aclUser',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def capabilityProfile(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('capabilityProfile',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    
    def dhsmServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('dhsmServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def diskGroup(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('diskGroup',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fastCache(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fastCache',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
                               
    def fastVP(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fastVP',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def filesystem(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('filesystem',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def lun(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('lun',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def pool(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('pool',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def poolConsumer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('poolConsumer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
                               
    def poolConsumerAllocation(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('poolConsumerAllocation',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def poolUnit(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('poolUnit',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def quotaConfig(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('quotaConfig',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)





    def feature(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('feature',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def basicSystemInfo(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('basicSystemInfo',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ethernetPort(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ethernetPort',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def metric(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('metric', item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def statspaths(self, filt = None):
        if filt: 
            stats_filter = 'path lk "%s" && isRealtimeAvailable eq true' % filt
        else:
            stats_filter = 'isRealtimeAvailable eq true'

        r = self.get('/types/metric/instances', {'fields':'path', 'filter':stats_filter})

        stat_paths = []
        for i in r.json()['entries']:
            stat_paths.append(i['content']['path'])

        return stat_paths

    def create_rt_query(self, statspaths, interval):
        """ Creates a RealtimeQuery on the Unity array, returns the new ID """
        payload = json.dumps({'paths':statspaths,'interval':interval})
        r = unity.post('/types/metricRealTimeQuery/instances',payload)
        return r.json()['content']['id']

    def query_stats(self,query_id):
        r = self.get('/types/metricQueryResult/instances',{'filter':'queryId eq %s' % str(query_id)})
        data = r.json()
        for i in data['entries']:
            print i['content']

    def remove_rt_query(self, query_id):
        r = self.delete('/types/metricRealTimeQuery/instances',query_id)
            
    def destroy_lun(resource_id):
        r = self.delete('/instances/storageResource/%s', resource_id)
        return r 

    def create_block_lun(lun_name, pool_id, size):
        ''' Creates a new block LUN in pool_id, returns the StorageResource id '''
        payload = json.dumps({'name':lun_name,
                              'lunParameters':{'pool':{'id':pool_id},
                              'size':size}})
                            
        r = unity.post('/types/storageResource/action/createLun',payload)
        return r.json()['content']['storageResource']['id']

        
    def __repr__(self):
        return "<Unity Array: %s>" % self.ip_addr
        
