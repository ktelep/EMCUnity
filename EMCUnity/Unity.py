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
        # TODO: work with Exceptions for easier troubleshooting
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
            payload = json.dumps(payload)
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
        return self.unity_request(url_path, method='GET', payload = payload)

    def post(self, url_path, payload = None):
        """ Wrapper for performing a POST unity request """
        return self.unity_request(url_path, method='POST', payload = payload)

    def delete(self, url_path, payload = None):
        """ Wrapper for performing a DELETE unity request """
        return self.unity_request(url_path, method='DELETE', payload = payload)

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

    def raidGroup(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('raidGroup',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def storageResource(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('storageResource',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def storageResourceCapabilityProfile(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('storageResourceCapabilityProfile',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def storageTier(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('storageTier',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def treeQuota(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('treeQuota',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def userQuota(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('userQuota',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def virtualVolume(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('virtualVolume',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Environment Management
    def battery(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('battery',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def dae(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('dae',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def disk(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('disk',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def dpe(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('dpe',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def encryption(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('encryption',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ethernetPort(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ethernetPort',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fan(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fan',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def fcPort(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('fcPort',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ioModule(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ioModule',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def lcc(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('lcc',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def memoryModule(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('memoryModule',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def powerSupply(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('powerSupply',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def sasPort(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('sasPort',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ssc(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ssc',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ssd(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ssd',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def storageProcessor(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('storageProcessor',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def uncommittedPort(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('uncommittedPort',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Managing the System
    def basicSystemInfo(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('basicSystemInfo',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def candidateSoftwareVersion(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('candidateSoftwareVersion',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def feature(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('feature',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def installedSoftwareVersion(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('installedSoftwareVersion',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def license(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('license',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)
    def ntpServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ntpServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def remoteSyslog(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('remoteSyslog',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def serviceContract(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('serviceContract',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def softwareUpgradeSession(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('softwareUpgradeSession',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def system(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('system',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def systemInformation(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('systemInformation',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def systemLimit(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('systemLimit',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def systemTime(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('systemTime',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Monitoring capacity and performance
    def metric(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('metric',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def metricCollection(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('metricCollection',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def metricQueryResult(self, item_filter = None, item_id=None, item_name=None):
        """ metricQueryResult is an odd request, as it REQUIRES a specific filter
            to be passed to it.  For the user, we're taking that as either a part
            of the filter, or we're creating the filter for them """

        if item_id:
            if "queryId" not in item_filter:
                if item_filter:
                    item_filter = "queryId EQ %s && %s" % (item_id, item_filter)
                else:
                    item_filter = "queryId EQ %s" % item_id
        
        if "queryId" not in item_filter:
            # TODO, we really should throw an exception here
            return None

        return self.get_object('metricQueryResult',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def metricRealTimeQuery(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('metricRealTimeQuery',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def metricService(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('metricService',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def metricValue(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('metricValue',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Protecting Data
    def ldapServer(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ldapServer',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def remoteInterface(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('remoteInterface',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def replicationInterface(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('replicationInterface',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def replicationSession(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('replicationSession',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def snap(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('snap',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def snapSchedule(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('snapSchedule',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Quality of Service
    def ioLimitPolicy(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ioLimitPolicy',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ioLimitRule(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ioLimitRule',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def ioLimitSetting(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('ioLimitSetting',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Servicing the System
    def configCaptureResult(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('configCaptureResult',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def dataCollectionResult(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('dataCollectionResult',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def esrsParam(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('esrsParam',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def esrsPolicymanager(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('esrsPolicymanager',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def serviceAction(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('serviceAction',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def serviceInfo(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('serviceInfo',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def supportAsset(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('supportAsset',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def supportService(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('supportService',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def technicalAdvisory(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('technicalAdvisory',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Users and Security
    def crl(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('crl',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def loginSessionInfo(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('loginSessionInfo',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def role(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('role',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def roleMapping(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('roleMapping',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def securitySettings(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('securitySettings',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def user(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('user',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    def x509Certificate(self, item_filter = None, item_id=None, item_name=None):
        return self.get_object('x509Certificate',item_filter=item_filter,
                               item_id=item_id, item_name=item_name)

    # Helper Functions

    def delete_storageResource(self, lun_id):
        response = self.delete('/instances/storageResource/%s' % lun_id)
        return response

    def delete_lun(self, lun_id):
        """ Deletes a LUN based on the lun_id """
        response = self.delete_storageResource(lun_id)
        return response

    def create_lun(self, lun_name, pool_id, size, lun_description=None):
        """ Creates a new block LUN in pool_id, returns a lun object """
        payload = {'name':lun_name,
                   'lunParameters':{'pool':{'id':pool_id},
                   'size':size}}

        response = self.post('/types/storageResource/action/createLun',payload)

        new_id = response.json()['content']['storageResource']['id']
        return self.lun(item_id=new_id)

    def create_lun(self, lun_object):
        """ Creates a new block LUN based on a lun_object being passed """
        payload = {'name': lun_object.name,
                   'lunParameters':{'pool':{'id':lun_object.pool},
                                    'size': lun_object.sizeTotal}}

        response = self.post('/types/storageResource/action/createLun',payload)

        new_id = response.json()['content']['storageResource']['id']
        return self.lun(item_id=new_id)

    def __repr__(self):
        return "<Unity Array: %s>" % self.ip_addr
        
