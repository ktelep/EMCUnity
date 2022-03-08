import collections


def namedtuple_defaults(typename, field_names, default_values=()):
    ''' This makes our objects simple named tuples with default values of None
        standard namedtuples, require all values '''
    T = collections.namedtuple(typename, field_names)
    T.__new__.__defaults__ = (None,) * len(T._fields)
    if isinstance(default_values, collections.Mapping):
        prototype = T(**default_values)
    else:
        prototype = T(*default_values)
    T.__new__.__defaults__ = tuple(prototype)
    return T

UnityaclUser = namedtuple_defaults('UnityaclUser', [
                                                    'id',
                                                    'sid',
                                                    'domainName',
                                                    'userName',
                                                    ])


Unityalert = namedtuple_defaults('Unityalert', [
                                                'id',
                                                'timestamp',
                                                'severity',
                                                'component',
                                                'messageId',
                                                'message',
                                                'descriptionId',
                                                'description',
                                                'resolutionId',
                                                'resolution',
                                                'isAcknowledged',
                                                ])


UnityalertConfig = namedtuple_defaults('UnityalertConfig', [
                                                            'id',
                                                            'locale',
                                                            'isThresholdAlertsEnabled',
                                                            'minEmailNotificationSeverity',
                                                            'destinationEmails',
                                                            'minSNMPTrapNotificationSeverity',
                                                            ])


UnityalertConfigSNMPTarget = namedtuple_defaults('UnityalertConfigSNMPTarget', [
                                                                                'id',
                                                                                'address',
                                                                                'version',
                                                                                'username',
                                                                                'authProto',
                                                                                'privacyProto',
                                                                                ])


UnitybaseRequest = namedtuple_defaults('UnitybaseRequest', [
                                                            ])


UnitybaseResponse = namedtuple_defaults('UnitybaseResponse', [
                                                              ])


UnitybasicSystemInfo = namedtuple_defaults('UnitybasicSystemInfo', [
                                                                    'id',
                                                                    'model',
                                                                    'name',
                                                                    'softwareVersion',
                                                                    'apiVersion',
                                                                    'earliestApiVersion',
                                                                    ])


Unitybattery = namedtuple_defaults('Unitybattery', [
                                                    'id',
                                                    'health',
                                                    'needsReplacement',
                                                    'parent',
                                                    'slotNumber',
                                                    'name',
                                                    'manufacturer',
                                                    'model',
                                                    'firmwareVersion',
                                                    'emcPartNumber',
                                                    'emcSerialNumber',
                                                    'vendorPartNumber',
                                                    'vendorSerialNumber',
                                                    'parentStorageProcessor',
                                                    ])


UnityblockHostAccess = namedtuple_defaults('UnityblockHostAccess', [
                                                                    'host',
                                                                    'accessMask',
                                                                    ])


UnitycandidateSoftwareVersion = namedtuple_defaults('UnitycandidateSoftwareVersion', [
                                                                                      'id',
                                                                                      'version',
                                                                                      'revision',
                                                                                      'releaseDate',
                                                                                      'type',
                                                                                      ])


UnitycapabilityProfile = namedtuple_defaults('UnitycapabilityProfile', [
                                                                        'id',
                                                                        'vmwareUUID',
                                                                        'name',
                                                                        'description',
                                                                        'pool',
                                                                        'driveTypes',
                                                                        'fastCacheStates',
                                                                        'raidTypes',
                                                                        'spaceEfficiencies',
                                                                        'tieringPolicies',
                                                                        'serviceLevels',
                                                                        'usageTags',
                                                                        'inUse',
                                                                        'health',
                                                                        'virtualVolumes',
                                                                        ])


UnitycertificateScope = namedtuple_defaults('UnitycertificateScope', [
                                                                      'nasServer',
                                                                      ])


UnitycifsServer = namedtuple_defaults('UnitycifsServer', [
                                                          'id',
                                                          'name',
                                                          'description',
                                                          'netbiosName',
                                                          'domain',
                                                          'lastUsedOrganizationalUnit',
                                                          'workgroup',
                                                          'isStandalone',
                                                          'health',
                                                          'nasServer',
                                                          'fileInterfaces',
                                                          'smbcaSupported',
                                                          'smbMultiChannelSupported',
                                                          'smbProtocolVersions',
                                                          ])


UnitycifsShare = namedtuple_defaults('UnitycifsShare', [
                                                        'id',
                                                        'type',
                                                        'filesystem',
                                                        'snap',
                                                        'isReadOnly',
                                                        'name',
                                                        'path',
                                                        'exportPaths',
                                                        'description',
                                                        'creationTime',
                                                        'modifiedTime',
                                                        'isContinuousAvailabilityEnabled',
                                                        'isEncryptionEnabled',
                                                        'isACEEnabled',
                                                        'isABEEnabled',
                                                        'isBranchCacheEnabled',
                                                        'isDFSEnabled',
                                                        'offlineAvailability',
                                                        'umask',
                                                        ])


UnitycifsShareACE = namedtuple_defaults('UnitycifsShareACE', [
                                                              'sid',
                                                              'accessType',
                                                              'accessLevel',
                                                              ])


UnityconfigCaptureResult = namedtuple_defaults('UnityconfigCaptureResult', [
                                                                            'id',
                                                                            'name',
                                                                            'creationTime',
                                                                            ])


Unitycrl = namedtuple_defaults('Unitycrl', [
                                            'id',
                                            'service',
                                            'scope',
                                            'version',
                                            'crlNumber',
                                            'signatureAlgorithm',
                                            'issuer',
                                            'thisUpdate',
                                            'nextUpdate',
                                            'certificates',
                                            'deltaCRLIndicator',
                                            ])


Unitydae = namedtuple_defaults('Unitydae', [
                                            'id',
                                            'health',
                                            'needsReplacement',
                                            'parent',
                                            'slotNumber',
                                            'name',
                                            'manufacturer',
                                            'model',
                                            'emcPartNumber',
                                            'emcSerialNumber',
                                            'vendorPartNumber',
                                            'vendorSerialNumber',
                                            'enclosureType',
                                            'busId',
                                            'driveTypes',
                                            'currentPower',
                                            'avgPower',
                                            'maxPower',
                                            'currentTemperature',
                                            'avgTemperature',
                                            'maxTemperature',
                                            'currentSpeed',
                                            'maxSpeed',
                                            'parentSystem',
                                            ])


UnitydataCollectionResult = namedtuple_defaults('UnitydataCollectionResult', [
                                                                              'id',
                                                                              'name',
                                                                              'creationTime',
                                                                              ])


Unitydatastore = namedtuple_defaults('Unitydatastore', [
                                                        'id',
                                                        'storageResource',
                                                        'name',
                                                        'format',
                                                        'host',
                                                        'sizeTotal',
                                                        'sizeUsed',
                                                        'vmDisks',
                                                        'vms',
                                                        ])


UnitydhsmServer = namedtuple_defaults('UnitydhsmServer', [
                                                          'id',
                                                          'nasServer',
                                                          'username',
                                                          ])


Unitydisk = namedtuple_defaults('Unitydisk', [
                                              'id',
                                              'health',
                                              'needsReplacement',
                                              'parent',
                                              'slotNumber',
                                              'busId',
                                              'name',
                                              'manufacturer',
                                              'model',
                                              'version',
                                              'emcPartNumber',
                                              'emcSerialNumber',
                                              'tierType',
                                              'diskGroup',
                                              'rpm',
                                              'isSED',
                                              'currentSpeed',
                                              'maxSpeed',
                                              'pool',
                                              'isInUse',
                                              'isFastCacheInUse',
                                              'size',
                                              'rawSize',
                                              'vendorSize',
                                              'wwn',
                                              'diskTechnology',
                                              'parentDae',
                                              'parentDpe',
                                              'bank',
                                              'bankSlotNumber',
                                              'bankSlot',
                                              ])


UnitydiskGroup = namedtuple_defaults('UnitydiskGroup', [
                                                        'id',
                                                        'name',
                                                        'emcPartNumber',
                                                        'tierType',
                                                        'diskTechnology',
                                                        'isFASTCacheAllowable',
                                                        'diskSize',
                                                        'advertisedSize',
                                                        'rpm',
                                                        'speed',
                                                        'totalDisks',
                                                        'minHotSpareCandidates',
                                                        'hotSparePolicyStatus',
                                                        'unconfiguredDisks',
                                                        ])


UnitydnsServer = namedtuple_defaults('UnitydnsServer', [
                                                        'id',
                                                        'domain',
                                                        'addresses',
                                                        'origin',
                                                        ])


Unitydpe = namedtuple_defaults('Unitydpe', [
                                            'id',
                                            'health',
                                            'needsReplacement',
                                            'parent',
                                            'slotNumber',
                                            'name',
                                            'manufacturer',
                                            'model',
                                            'emcPartNumber',
                                            'emcSerialNumber',
                                            'vendorPartNumber',
                                            'vendorSerialNumber',
                                            'enclosureType',
                                            'busId',
                                            'driveTypes',
                                            'currentPower',
                                            'avgPower',
                                            'maxPower',
                                            'currentTemperature',
                                            'avgTemperature',
                                            'maxTemperature',
                                            'currentSpeed',
                                            'maxSpeed',
                                            'parentSystem',
                                            ])


Unityencryption = namedtuple_defaults('Unityencryption', [
                                                          'id',
                                                          'encryptionMode',
                                                          'encryptionStatus',
                                                          'encryptionPercentage',
                                                          'keyManagerBackupKeyStatus',
                                                          ])


UnityesrsParam = namedtuple_defaults('UnityesrsParam', [
                                                        'id',
                                                        'enabled',
                                                        'isCentralized',
                                                        'status',
                                                        'proxyIsEnabled',
                                                        'proxyAddress',
                                                        'proxyIsHTTP',
                                                        'proxyUserName',
                                                        'esrsVeAddress',
                                                        'siteId',
                                                        'esrsConfigStatus',
                                                        'isEsrsVeEulaAccepted',
                                                        ])


UnityesrsPolicyManager = namedtuple_defaults('UnityesrsPolicyManager', [
                                                                        'id',
                                                                        'isEnabled',
                                                                        'address',
                                                                        'useHTTPS',
                                                                        'sslStrength',
                                                                        'proxyIsEnabled',
                                                                        'proxyAddress',
                                                                        'proxyUseSocks',
                                                                        'proxyUserName',
                                                                        ])


UnityethernetPort = namedtuple_defaults('UnityethernetPort', [
                                                              'id',
                                                              'health',
                                                              'storageProcessor',
                                                              'needsReplacement',
                                                              'name',
                                                              'portNumber',
                                                              'speed',
                                                              'mtu',
                                                              'connectorType',
                                                              'bond',
                                                              'isLinkUp',
                                                              'macAddress',
                                                              'isRSSCapable',
                                                              'isRDMACapable',
                                                              'requestedSpeed',
                                                              'parentIOModule',
                                                              'parentStorageProcessor',
                                                              'supportedSpeeds',
                                                              'requestedMtu',
                                                              'supportedMtus',
                                                              'parent',
                                                              'sfpSupportedSpeeds',
                                                              'sfpSupportedProtocols',
                                                              ])


Unityevent = namedtuple_defaults('Unityevent', [
                                                'id',
                                                'node',
                                                'creationTime',
                                                'severity',
                                                'messageId',
                                                'arguments',
                                                'message',
                                                'username',
                                                'category',
                                                'source',
                                                ])


Unityfan = namedtuple_defaults('Unityfan', [
                                            'id',
                                            'health',
                                            'parent',
                                            'slotNumber',
                                            'name',
                                            'emcPartNumber',
                                            'emcSerialNumber',
                                            'manufacturer',
                                            'model',
                                            'vendorPartNumber',
                                            'vendorSerialNumber',
                                            'needsReplacement',
                                            'parentDpe',
                                            'parentDae',
                                            ])


UnityfastCache = namedtuple_defaults('UnityfastCache', [
                                                        'id',
                                                        'health',
                                                        'sizeTotal',
                                                        'sizeFree',
                                                        'numberOfDisks',
                                                        'raidLevel',
                                                        'raidGroups',
                                                        ])


UnityfastVP = namedtuple_defaults('UnityfastVP', [
                                                  'id',
                                                  'status',
                                                  'relocationRate',
                                                  'isScheduleEnabled',
                                                  'scheduleDays',
                                                  'scheduleStartTime',
                                                  'scheduleEndTime',
                                                  'sizeMovingDown',
                                                  'sizeMovingUp',
                                                  'sizeMovingWithin',
                                                  'relocationDurationEstimate',
                                                  ])


UnityfcPort = namedtuple_defaults('UnityfcPort', [
                                                  'id',
                                                  'health',
                                                  'parent',
                                                  'slotNumber',
                                                  'wwn',
                                                  'availableSpeeds',
                                                  'currentSpeed',
                                                  'requestedSpeed',
                                                  'sfpSupportedSpeeds',
                                                  'sfpSupportedProtocols',
                                                  'connectorType',
                                                  'storageProcessor',
                                                  'needsReplacement',
                                                  'nPortId',
                                                  'name',
                                                  'parentIOModule',
                                                  'parentStorageProcessor',
                                                  ])


Unityfeature = namedtuple_defaults('Unityfeature', [
                                                    'id',
                                                    'name',
                                                    'state',
                                                    'reason',
                                                    'license',
                                                    ])


UnityfileDNSServer = namedtuple_defaults('UnityfileDNSServer', [
                                                                'id',
                                                                'nasServer',
                                                                'addresses',
                                                                'domain',
                                                                'replicationPolicy',
                                                                'sourceParameters',
                                                                ])


UnityfileInterface = namedtuple_defaults('UnityfileInterface', [
                                                                'id',
                                                                'nasServer',
                                                                'ipPort',
                                                                'health',
                                                                'ipAddress',
                                                                'ipProtocolVersion',
                                                                'netmask',
                                                                'v6PrefixLength',
                                                                'gateway',
                                                                'vlanId',
                                                                'macAddress',
                                                                'name',
                                                                'role',
                                                                'isPreferred',
                                                                'replicationPolicy',
                                                                'sourceParameters',
                                                                'isDisabled',
                                                                ])


UnityfileKerberosServer = namedtuple_defaults('UnityfileKerberosServer', [
                                                                          'id',
                                                                          'nasServer',
                                                                          'realm',
                                                                          'addresses',
                                                                          'portNumber',
                                                                          ])


UnityfileLDAPServer = namedtuple_defaults('UnityfileLDAPServer', [
                                                                  'id',
                                                                  'nasServer',
                                                                  'authority',
                                                                  'profileDN',
                                                                  'serverAddresses',
                                                                  'portNumber',
                                                                  'authenticationType',
                                                                  'protocol',
                                                                  'verifyServerCertificate',
                                                                  'bindDN',
                                                                  'isCifsAccountUsed',
                                                                  'principal',
                                                                  'realm',
                                                                  'schemeType',
                                                                  'replicationPolicy',
                                                                  'sourceParameters',
                                                                  ])


UnityfileNDMPServer = namedtuple_defaults('UnityfileNDMPServer', [
                                                                  'id',
                                                                  'nasServer',
                                                                  'username',
                                                                  ])


UnityfileNISServer = namedtuple_defaults('UnityfileNISServer', [
                                                                'id',
                                                                'nasServer',
                                                                'addresses',
                                                                'domain',
                                                                'replicationPolicy',
                                                                'sourceParameters',
                                                                ])


Unityfilesystem = namedtuple_defaults('Unityfilesystem', [
                                                          'id',
                                                          'health',
                                                          'name',
                                                          'description',
                                                          'type',
                                                          'sizeTotal',
                                                          'sizeUsed',
                                                          'sizeAllocated',
                                                          'isReadOnly',
                                                          'isThinEnabled',
                                                          'storageResource',
                                                          'isCIFSSyncWritesEnabled',
                                                          'pool',
                                                          'isCIFSOpLocksEnabled',
                                                          'nasServer',
                                                          'isCIFSNotifyOnWriteEnabled',
                                                          'isCIFSNotifyOnAccessEnabled',
                                                          'cifsNotifyOnChangeDirDepth',
                                                          'tieringPolicy',
                                                          'supportedProtocols',
                                                          'metadataSize',
                                                          'metadataSizeAllocated',
                                                          'perTierSizeUsed',
                                                          'snapsSize',
                                                          'snapsSizeAllocated',
                                                          'snapCount',
                                                          'isSMBCA',
                                                          'accessPolicy',
                                                          'format',
                                                          'hostIOSize',
                                                          'poolFullPolicy',
                                                          'cifsShare',
                                                          'nfsShare',
                                                          ])


UnityftpServer = namedtuple_defaults('UnityftpServer', [
                                                        'id',
                                                        'nasServer',
                                                        'isFtpEnabled',
                                                        'isSftpEnabled',
                                                        'isCifsUserEnabled',
                                                        'isUnixUserEnabled',
                                                        'isAnonymousUserEnabled',
                                                        'isHomedirLimitEnabled',
                                                        'defaultHomedir',
                                                        'welcomeMsg',
                                                        'motd',
                                                        'isAuditEnabled',
                                                        'auditDir',
                                                        'auditMaxSize',
                                                        'hostsList',
                                                        'usersList',
                                                        'groupsList',
                                                        'isAllowHost',
                                                        'isAllowUser',
                                                        'isAllowGroup',
                                                        ])


Unityhealth = namedtuple_defaults('Unityhealth', [
                                                  'value',
                                                  'descriptionIds',
                                                  'descriptions',
                                                  'resolutionIds',
                                                  'resolutions',
                                                  ])


Unityhost = namedtuple_defaults('Unityhost', [
                                              'id',
                                              'health',
                                              'name',
                                              'description',
                                              'type',
                                              'osType',
                                              'hostUUID',
                                              'hostPushedUUID',
                                              'hostPolledUUID',
                                              'lastPollTime',
                                              'autoManageType',
                                              'registrationType',
                                              'hostContainer',
                                              'fcHostInitiators',
                                              'iscsiHostInitiators',
                                              'hostIPPorts',
                                              'storageResources',
                                              'hostLUNs',
                                              'datastores',
                                              'nfsShareAccesses',
                                              'hostVVolDatastore',
                                              'vms',
                                              ])


UnityhostContainer = namedtuple_defaults('UnityhostContainer', [
                                                                'id',
                                                                'lastPollTime',
                                                                'port',
                                                                'name',
                                                                'type',
                                                                'address',
                                                                'description',
                                                                'productName',
                                                                'productVersion',
                                                                'health',
                                                                'hosts',
                                                                ])


UnityhostInitiator = namedtuple_defaults('UnityhostInitiator', [
                                                                'id',
                                                                'health',
                                                                'type',
                                                                'initiatorId',
                                                                'parentHost',
                                                                'isIgnored',
                                                                'nodeWWN',
                                                                'portWWN',
                                                                'chapUserName',
                                                                'isChapSecretEnabled',
                                                                'paths',
                                                                'iscsiType',
                                                                'isBound',
                                                                'sourceType',
                                                                ])


UnityhostInitiatorPath = namedtuple_defaults('UnityhostInitiatorPath', [
                                                                        'id',
                                                                        'registrationType',
                                                                        'isLoggedIn',
                                                                        'hostPushName',
                                                                        'sessionIds',
                                                                        'initiator',
                                                                        'fcPort',
                                                                        'iscsiPortal',
                                                                        ])


UnityhostIPPort = namedtuple_defaults('UnityhostIPPort', [
                                                          'id',
                                                          'name',
                                                          'type',
                                                          'address',
                                                          'netmask',
                                                          'v6PrefixLength',
                                                          'isIgnored',
                                                          'host',
                                                          ])


UnityhostLUN = namedtuple_defaults('UnityhostLUN', [
                                                    'id',
                                                    'host',
                                                    'type',
                                                    'hlu',
                                                    'lun',
                                                    'snap',
                                                    'isReadOnly',
                                                    ])


UnityhostVVolDatastore = namedtuple_defaults('UnityhostVVolDatastore', [
                                                                        'id',
                                                                        'storageResource',
                                                                        'host',
                                                                        ])


UnityinstalledSoftwareVersion = namedtuple_defaults('UnityinstalledSoftwareVersion', [
                                                                                      'id',
                                                                                      'version',
                                                                                      'revision',
                                                                                      'releaseDate',
                                                                                      'languages',
                                                                                      'hotFixes',
                                                                                      'packageVersions',
                                                                                      ])


UnityioLimitParameters = namedtuple_defaults('UnityioLimitParameters', [
                                                                        'ioLimitPolicy',
                                                                        ])


UnityioLimitPolicy = namedtuple_defaults('UnityioLimitPolicy', [
                                                                'id',
                                                                'name',
                                                                'description',
                                                                'isShared',
                                                                'ioLimitRules',
                                                                'luns',
                                                                'snaps',
                                                                ])


UnityioLimitRule = namedtuple_defaults('UnityioLimitRule', [
                                                            'id',
                                                            'name',
                                                            'description',
                                                            'maxIOPS',
                                                            'maxKBPS',
                                                            'ioLimitpolicy',
                                                            ])


UnityioLimitSetting = namedtuple_defaults('UnityioLimitSetting', [
                                                                  'id',
                                                                  'isPaused',
                                                                  ])


UnityioModule = namedtuple_defaults('UnityioModule', [
                                                      'id',
                                                      'health',
                                                      'needsReplacement',
                                                      'parent',
                                                      'slotNumber',
                                                      'name',
                                                      'manufacturer',
                                                      'model',
                                                      'emcPartNumber',
                                                      'emcSerialNumber',
                                                      'vendorPartNumber',
                                                      'vendorSerialNumber',
                                                      'systemName',
                                                      'parentStorageProcessor',
                                                      ])


UnityipInterface = namedtuple_defaults('UnityipInterface', [
                                                            'id',
                                                            'ipPort',
                                                            'ipProtocolVersion',
                                                            'ipAddress',
                                                            'netmask',
                                                            'v6PrefixLength',
                                                            'gateway',
                                                            'vlanId',
                                                            'type',
                                                            ])


UnityipPort = namedtuple_defaults('UnityipPort', [
                                                  'id',
                                                  'name',
                                                  'shortName',
                                                  'macAddress',
                                                  'isLinkUp',
                                                  'storageProcessor',
                                                  ])


UnityiscsiNode = namedtuple_defaults('UnityiscsiNode', [
                                                        'id',
                                                        'name',
                                                        'ethernetPort',
                                                        'alias',
                                                        ])


UnityiscsiPortal = namedtuple_defaults('UnityiscsiPortal', [
                                                            'id',
                                                            'ethernetPort',
                                                            'iscsiNode',
                                                            'ipAddress',
                                                            'netmask',
                                                            'v6PrefixLength',
                                                            'gateway',
                                                            'vlanId',
                                                            'ipProtocolVersion',
                                                            ])


UnityiscsiSettings = namedtuple_defaults('UnityiscsiSettings', [
                                                                'id',
                                                                'isForwardCHAPRequired',
                                                                'reverseCHAPUserName',
                                                                'forwardGlobalCHAPUserName',
                                                                'iSNSServer',
                                                                ])


Unityjob = namedtuple_defaults('Unityjob', [
                                            'id',
                                            'description',
                                            'state',
                                            'stateChangeTime',
                                            'submitTime',
                                            'startTime',
                                            'endTime',
                                            'elapsedTime',
                                            'estRemainTime',
                                            'progressPct',
                                            'tasks',
                                            'parametersOut',
                                            'messageOut',
                                            'isJobCancelable',
                                            'isJobCancelled',
                                            'clientData',
                                            ])


Unitylcc = namedtuple_defaults('Unitylcc', [
                                            'id',
                                            'health',
                                            'needsReplacement',
                                            'parent',
                                            'slotNumber',
                                            'name',
                                            'manufacturer',
                                            'model',
                                            'sasExpanderVersions',
                                            'emcPartNumber',
                                            'emcSerialNumber',
                                            'vendorPartNumber',
                                            'vendorSerialNumber',
                                            'currentSpeed',
                                            'maxSpeed',
                                            'parentDae',
                                            ])


UnityldapServer = namedtuple_defaults('UnityldapServer', [
                                                          'id',
                                                          'authority',
                                                          'serverAddress',
                                                          'bindDN',
                                                          'protocol',
                                                          'userSearchPath',
                                                          'groupSearchPath',
                                                          'userIdAttribute',
                                                          'groupNameAttribute',
                                                          'userObjectClass',
                                                          'groupObjectClass',
                                                          'groupMemberAttribute',
                                                          'timeout',
                                                          ])


Unitylicense = namedtuple_defaults('Unitylicense', [
                                                    'id',
                                                    'name',
                                                    'isInstalled',
                                                    'version',
                                                    'isValid',
                                                    'issued',
                                                    'expires',
                                                    'isPermanent',
                                                    'feature',
                                                    ])


UnitylinkAggregation = namedtuple_defaults('UnitylinkAggregation', [
                                                                    'id',
                                                                    'name',
                                                                    'shortName',
                                                                    'masterPort',
                                                                    'ports',
                                                                    'mtuSize',
                                                                    'supportedMtus',
                                                                    'macAddress',
                                                                    'isLinkUp',
                                                                    'parent',
                                                                    'parentStorageProcessor',
                                                                    ])


UnitylocalizedMessage = namedtuple_defaults('UnitylocalizedMessage', [
                                                                      'locale',
                                                                      'message',
                                                                      ])


UnityloginSessionInfo = namedtuple_defaults('UnityloginSessionInfo', [
                                                                      'id',
                                                                      'user',
                                                                      'roles',
                                                                      'idleTimeout',
                                                                      'isPasswordChangeRequired',
                                                                      ])


Unitylun = namedtuple_defaults('Unitylun', [
                                            'id',
                                            'health',
                                            'name',
                                            'description',
                                            'type',
                                            'sizeTotal',
                                            'sizeUsed',
                                            'sizeAllocated',
                                            'perTierSizeUsed',
                                            'isThinEnabled',
                                            'storageResource',
                                            'pool',
                                            'wwn',
                                            'tieringPolicy',
                                            'defaultNode',
                                            'isReplicationDestination',
                                            'currentNode',
                                            'snapSchedule',
                                            'isSnapSchedulePaused',
                                            'ioLimitPolicy',
                                            'metadataSize',
                                            'metadataSizeAllocated',
                                            'snapWwn',
                                            'snapsSize',
                                            'snapsSizeAllocated',
                                            'hostAccess',
                                            'snapCount',
                                            ])


UnitylunMemberReplication = namedtuple_defaults('UnitylunMemberReplication', [
                                                                              'srcStatus',
                                                                              'networkStatus',
                                                                              'dstStatus',
                                                                              'srcLunId',
                                                                              'dstLunId',
                                                                              ])


UnitymemoryModule = namedtuple_defaults('UnitymemoryModule', [
                                                              'id',
                                                              'health',
                                                              'needsReplacement',
                                                              'parent',
                                                              'slotNumber',
                                                              'name',
                                                              'manufacturer',
                                                              'model',
                                                              'firmwareVersion',
                                                              'size',
                                                              'emcPartNumber',
                                                              'emcSerialNumber',
                                                              'vendorPartNumber',
                                                              'vendorSerialNumber',
                                                              'parentStorageProcessor',
                                                              'isInserted',
                                                              ])


Unitymessage = namedtuple_defaults('Unitymessage', [
                                                    'severity',
                                                    'errorCode',
                                                    'created',
                                                    'httpStatusCode',
                                                    'messages',
                                                    ])


Unitymetric = namedtuple_defaults('Unitymetric', [
                                                  'id',
                                                  'name',
                                                  'path',
                                                  'type',
                                                  'description',
                                                  'isHistoricalAvailable',
                                                  'isRealtimeAvailable',
                                                  'unitDisplayString',
                                                  ])


UnitymetricCollection = namedtuple_defaults('UnitymetricCollection', [
                                                                      'id',
                                                                      'interval',
                                                                      'oldest',
                                                                      'retention',
                                                                      ])


UnitymetricQueryResult = namedtuple_defaults('UnitymetricQueryResult', [
                                                                        'queryId',
                                                                        'path',
                                                                        'timestamp',
                                                                        'values',
                                                                        ])


UnitymetricRealTimeQuery = namedtuple_defaults('UnitymetricRealTimeQuery', [
                                                                            'id',
                                                                            'paths',
                                                                            'interval',
                                                                            'expiration',
                                                                            ])


UnitymetricService = namedtuple_defaults('UnitymetricService', [
                                                                'id',
                                                                'isHistoricalEnabled',
                                                                ])


UnitymetricValue = namedtuple_defaults('UnitymetricValue', [
                                                            'path',
                                                            'timestamp',
                                                            'interval',
                                                            'values',
                                                            ])


UnitymgmtInterface = namedtuple_defaults('UnitymgmtInterface', [
                                                                'id',
                                                                'configMode',
                                                                'ethernetPort',
                                                                'protocolVersion',
                                                                'ipAddress',
                                                                'netmask',
                                                                'v6PrefixLength',
                                                                'gateway',
                                                                ])


UnitymgmtInterfaceSettings = namedtuple_defaults('UnitymgmtInterfaceSettings', [
                                                                                'id',
                                                                                'v4ConfigMode',
                                                                                'v6ConfigMode',
                                                                                ])


UnitynasServer = namedtuple_defaults('UnitynasServer', [
                                                        'id',
                                                        'name',
                                                        'health',
                                                        'homeSP',
                                                        'currentSP',
                                                        'pool',
                                                        'sizeAllocated',
                                                        'isReplicationEnabled',
                                                        'isReplicationDestination',
                                                        'replicationType',
                                                        'defaultUnixUser',
                                                        'defaultWindowsUser',
                                                        'currentUnixDirectoryService',
                                                        'isMultiProtocolEnabled',
                                                        'isWindowsToUnixUsernameMappingEnabled',
                                                        'allowUnmappedUser',
                                                        'cifsServer',
                                                        'preferredInterfaceSettings',
                                                        'fileDNSServer',
                                                        'fileInterface',
                                                        'virusChecker',
                                                        ])


UnitynfsServer = namedtuple_defaults('UnitynfsServer', [
                                                        'id',
                                                        'hostName',
                                                        'nasServer',
                                                        'fileInterfaces',
                                                        'nfsv4Enabled',
                                                        'isSecureEnabled',
                                                        'kdcType',
                                                        'servicePrincipalName',
                                                        'isExtendedCredentialsEnabled',
                                                        'credentialsCacheTTL',
                                                        ])


UnitynfsShare = namedtuple_defaults('UnitynfsShare', [
                                                      'id',
                                                      'type',
                                                      'role',
                                                      'filesystem',
                                                      'snap',
                                                      'name',
                                                      'path',
                                                      'exportPaths',
                                                      'description',
                                                      'isReadOnly',
                                                      'creationTime',
                                                      'modificationTime',
                                                      'defaultAccess',
                                                      'minSecurity',
                                                      'noAccessHosts',
                                                      'readOnlyHosts',
                                                      'readWriteHosts',
                                                      'rootAccessHosts',
                                                      'hostAccesses',
                                                      ])


UnityntpServer = namedtuple_defaults('UnityntpServer', [
                                                        'id',
                                                        'addresses',
                                                        ])


Unitypool = namedtuple_defaults('Unitypool', [
                                              'id',
                                              'health',
                                              'name',
                                              'description',
                                              'storageResourceType',
                                              'raidType',
                                              'sizeFree',
                                              'sizeTotal',
                                              'sizeUsed',
                                              'sizeSubscribed',
                                              'alertThreshold',
                                              'isFASTCacheEnabled',
                                              'tiers',
                                              'creationTime',
                                              'isEmpty',
                                              'poolFastVP',
                                              'isHarvestEnabled',
                                              'harvestState',
                                              'isSnapHarvestEnabled',
                                              'poolSpaceHarvestHighThreshold',
                                              'poolSpaceHarvestLowThreshold',
                                              'snapSpaceHarvestHighThreshold',
                                              'snapSpaceHarvestLowThreshold',
                                              'metadataSizeSubscribed',
                                              'snapSizeSubscribed',
                                              'metadataSizeUsed',
                                              'snapSizeUsed',
                                              'rebalanceProgress',
                                              ])


UnitypoolConsumer = namedtuple_defaults('UnitypoolConsumer', [
                                                              'id',
                                                              ])


UnitypoolConsumerAllocation = namedtuple_defaults('UnitypoolConsumerAllocation', [
                                                                                  'id',
                                                                                  'pool',
                                                                                  'consumer',
                                                                                  'consumerType',
                                                                                  'sizeAllocatedTotal',
                                                                                  'snapsSizeAllocated',
                                                                                  ])


UnitypoolUnit = namedtuple_defaults('UnitypoolUnit', [
                                                      'id',
                                                      'type',
                                                      'health',
                                                      'name',
                                                      'description',
                                                      'wwn',
                                                      'sizeTotal',
                                                      'tierType',
                                                      'pool',
                                                      ])


UnitypowerSupply = namedtuple_defaults('UnitypowerSupply', [
                                                            'id',
                                                            'health',
                                                            'needsReplacement',
                                                            'parent',
                                                            'slotNumber',
                                                            'name',
                                                            'manufacturer',
                                                            'model',
                                                            'firmwareVersion',
                                                            'emcSerialNumber',
                                                            'vendorPartNumber',
                                                            'vendorSerialNumber',
                                                            'emcPartNumber',
                                                            'parentDae',
                                                            'parentDpe',
                                                            ])


UnitypreferredInterfaceSettings = namedtuple_defaults('UnitypreferredInterfaceSettings', [
                                                                                          'id',
                                                                                          'nasServer',
                                                                                          'productionIpV4',
                                                                                          'productionIpV6',
                                                                                          'backupIpV4',
                                                                                          'backupIpV6',
                                                                                          'sourceParameters',
                                                                                          'replicationPolicy',
                                                                                          ])


UnityquotaConfig = namedtuple_defaults('UnityquotaConfig', [
                                                            'id',
                                                            'filesystem',
                                                            'treeQuota',
                                                            'quotaPolicy',
                                                            'isUserQuotaEnabled',
                                                            'isAccessDenyEnabled',
                                                            'gracePeriod',
                                                            'defaultHardLimit',
                                                            'defaultSoftLimit',
                                                            'lastUpdateTimeOfTreeQuotas',
                                                            'lastUpdateTimeOfUserQuotas',
                                                            ])


UnityraidGroup = namedtuple_defaults('UnityraidGroup', [
                                                        'id',
                                                        'type',
                                                        'health',
                                                        'name',
                                                        'description',
                                                        'wwn',
                                                        'sizeTotal',
                                                        'tierType',
                                                        'pool',
                                                        'diskGroup',
                                                        'raidType',
                                                        'stripeWidth',
                                                        'parityDisks',
                                                        'disks',
                                                        ])


UnityremoteInterface = namedtuple_defaults('UnityremoteInterface', [
                                                                    'id',
                                                                    'remoteId',
                                                                    'name',
                                                                    'address',
                                                                    'remoteSystem',
                                                                    'node',
                                                                    'capability',
                                                                    ])


UnityremoteSyslog = namedtuple_defaults('UnityremoteSyslog', [
                                                              'id',
                                                              'address',
                                                              'protocol',
                                                              'facility',
                                                              'enabled',
                                                              ])


UnityremoteSystem = namedtuple_defaults('UnityremoteSystem', [
                                                              'id',
                                                              'name',
                                                              'model',
                                                              'serialNumber',
                                                              'health',
                                                              'managementAddress',
                                                              'connectionType',
                                                              'syncFcPorts',
                                                              'username',
                                                              'localSPAInterfaces',
                                                              'localSPBInterfaces',
                                                              'remoteSPAInterfaces',
                                                              'remoteSPBInterfaces',
                                                              ])


UnityreplicationInterface = namedtuple_defaults('UnityreplicationInterface', [
                                                                              'id',
                                                                              'ipPort',
                                                                              'health',
                                                                              'ipAddress',
                                                                              'ipProtocolVersion',
                                                                              'netmask',
                                                                              'v6PrefixLength',
                                                                              'gateway',
                                                                              'vlanId',
                                                                              'macAddress',
                                                                              'name',
                                                                              ])


UnityreplicationSession = namedtuple_defaults('UnityreplicationSession', [
                                                                          'id',
                                                                          'name',
                                                                          'replicationResourceType',
                                                                          'status',
                                                                          'health',
                                                                          'maxTimeOutOfSync',
                                                                          'srcStatus',
                                                                          'networkStatus',
                                                                          'dstStatus',
                                                                          'lastSyncTime',
                                                                          'syncState',
                                                                          'remoteSystem',
                                                                          'localRole',
                                                                          'srcResourceId',
                                                                          'srcSPAInterface',
                                                                          'srcSPBInterface',
                                                                          'dstResourceId',
                                                                          'dstSPAInterface',
                                                                          'dstSPBInterface',
                                                                          'members',
                                                                          'syncProgress',
                                                                          'currentTransferEstRemainTime',
                                                                          ])


UnityresourceRef = namedtuple_defaults('UnityresourceRef', [
                                                            'resource',
                                                            'id',
                                                            ])


Unityrole = namedtuple_defaults('Unityrole', [
                                              'id',
                                              'name',
                                              'description',
                                              ])


UnityroleMapping = namedtuple_defaults('UnityroleMapping', [
                                                            'id',
                                                            'authorityName',
                                                            'roleName',
                                                            'entityName',
                                                            'mappingType',
                                                            ])


Unityroute = namedtuple_defaults('Unityroute', [
                                                'id',
                                                'ipInterface',
                                                'destination',
                                                'netmask',
                                                'v6PrefixLength',
                                                'gateway',
                                                ])


UnityrpChapSettings = namedtuple_defaults('UnityrpChapSettings', [
                                                                  'id',
                                                                  'outgoingForwardChapUsername',
                                                                  ])


UnitysasPort = namedtuple_defaults('UnitysasPort', [
                                                    'id',
                                                    'health',
                                                    'needsReplacement',
                                                    'parent',
                                                    'name',
                                                    'port',
                                                    'currentSpeed',
                                                    'connectorType',
                                                    'parentStorageProcessor',
                                                    ])


UnitysecuritySettings = namedtuple_defaults('UnitysecuritySettings', [
                                                                      'id',
                                                                      'isFIPSEnabled',
                                                                      'isSSOEnabled',
                                                                      'isTLS1Enabled',
                                                                      ])


UnityserviceAction = namedtuple_defaults('UnityserviceAction', [
                                                                'id',
                                                                'scope',
                                                                'name',
                                                                'description',
                                                                'isApplicable',
                                                                'applyCondition',
                                                                ])


UnityserviceContract = namedtuple_defaults('UnityserviceContract', [
                                                                    'id',
                                                                    'contractId',
                                                                    'contractNumber',
                                                                    'contractStatus',
                                                                    'levelOfService',
                                                                    'serviceLineId',
                                                                    'lastUpdated',
                                                                    'productStartDate',
                                                                    'productEndDate',
                                                                    ])


UnityserviceInfo = namedtuple_defaults('UnityserviceInfo', [
                                                            'id',
                                                            'productName',
                                                            'productSerialNumber',
                                                            'systemUUID',
                                                            'isSSHEnabled',
                                                            'esrsStatus',
                                                            'sps',
                                                            ])


UnitysmtpServer = namedtuple_defaults('UnitysmtpServer', [
                                                          'id',
                                                          'address',
                                                          'type',
                                                          ])


Unitysnap = namedtuple_defaults('Unitysnap', [
                                              'id',
                                              'name',
                                              'description',
                                              'storageResource',
                                              'lun',
                                              'snapGroup',
                                              'parentSnap',
                                              'creationTime',
                                              'expirationTime',
                                              'creatorType',
                                              'creatorUser',
                                              'creatorSchedule',
                                              'isSystemSnap',
                                              'isModifiable',
                                              'attachedWWN',
                                              'accessType',
                                              'isReadOnly',
                                              'lastWritableTime',
                                              'isModified',
                                              'isAutoDelete',
                                              'state',
                                              'size',
                                              'ioLimitPolicy',
                                              ])


UnitysnapSchedule = namedtuple_defaults('UnitysnapSchedule', [
                                                              'id',
                                                              'name',
                                                              'isDefault',
                                                              'isModified',
                                                              'version',
                                                              'rules',
                                                              'storageResources',
                                                              ])


UnitysoftwareUpgradeSession = namedtuple_defaults('UnitysoftwareUpgradeSession', [
                                                                                  'id',
                                                                                  'type',
                                                                                  'candidate',
                                                                                  'caption',
                                                                                  'status',
                                                                                  'messages',
                                                                                  'creationTime',
                                                                                  'elapsedTime',
                                                                                  'percentComplete',
                                                                                  'tasks',
                                                                                  ])


Unityssc = namedtuple_defaults('Unityssc', [
                                            'id',
                                            'health',
                                            'needsReplacement',
                                            'parent',
                                            'slotNumber',
                                            'name',
                                            'parentDae',
                                            ])


Unityssd = namedtuple_defaults('Unityssd', [
                                            'id',
                                            'health',
                                            'needsReplacement',
                                            'parent',
                                            'slotNumber',
                                            'name',
                                            'manufacturer',
                                            'model',
                                            'firmwareVersion',
                                            'emcPartNumber',
                                            'emcSerialNumber',
                                            'vendorPartNumber',
                                            'vendorSerialNumber',
                                            'parentStorageProcessor',
                                            ])


UnitystorageProcessor = namedtuple_defaults('UnitystorageProcessor', [
                                                                      'id',
                                                                      'parent',
                                                                      'health',
                                                                      'needsReplacement',
                                                                      'isRescueMode',
                                                                      'model',
                                                                      'slotNumber',
                                                                      'name',
                                                                      'emcPartNumber',
                                                                      'emcSerialNumber',
                                                                      'manufacturer',
                                                                      'vendorPartNumber',
                                                                      'vendorSerialNumber',
                                                                      'sasExpanderVersion',
                                                                      'biosFirmwareRevision',
                                                                      'postFirmwareRevision',
                                                                      'memorySize',
                                                                      'parentDpe',
                                                                      ])


UnitystorageResource = namedtuple_defaults('UnitystorageResource', [
                                                                    'id',
                                                                    'health',
                                                                    'name',
                                                                    'description',
                                                                    'type',
                                                                    'isReplicationDestination',
                                                                    'replicationType',
                                                                    'sizeTotal',
                                                                    'sizeUsed',
                                                                    'sizeAllocated',
                                                                    'thinStatus',
                                                                    'esxFilesystemMajorVersion',
                                                                    'esxFilesystemBlockSize',
                                                                    'snapSchedule',
                                                                    'isSnapSchedulePaused',
                                                                    'relocationPolicy',
                                                                    'perTierSizeUsed',
                                                                    'blockHostAccess',
                                                                    'metadataSize',
                                                                    'metadataSizeAllocated',
                                                                    'snapsSizeTotal',
                                                                    'snapsSizeAllocated',
                                                                    'snapCount',
                                                                    'vmwareUUID',
                                                                    'pools',
                                                                    'datastores',
                                                                    'filesystem',
                                                                    'hostVVolDatastore',
                                                                    'luns',
                                                                    'virtualVolumes',
                                                                    ])


UnitystorageResourceCapabilityProfile = namedtuple_defaults('UnitystorageResourceCapabilityProfile', [
                                                                                                      'id',
                                                                                                      'storageResource',
                                                                                                      'capabilityProfile',
                                                                                                      'isInUse',
                                                                                                      'sizeUsed',
                                                                                                      'sizeAllocated',
                                                                                                      'sizeTotal',
                                                                                                      'logicalSizeUsed',
                                                                                                      ])


UnitystorageTier = namedtuple_defaults('UnitystorageTier', [
                                                            'id',
                                                            'tierType',
                                                            'raidConfigurations',
                                                            'disksTotal',
                                                            'disksUnused',
                                                            'virtualDisksTotal',
                                                            'virtualDisksUnused',
                                                            'sizeTotal',
                                                            'sizeFree',
                                                            ])


UnitystorageTierConfiguration = namedtuple_defaults('UnitystorageTierConfiguration', [
                                                                                      'storageTier',
                                                                                      'raidType',
                                                                                      'stripeWidth',
                                                                                      'disksTotal',
                                                                                      'sizeTotal',
                                                                                      'diskGroupConfigurations',
                                                                                      ])


UnitysupportAsset = namedtuple_defaults('UnitysupportAsset', [
                                                              'id',
                                                              'name',
                                                              'description',
                                                              ])


UnitysupportService = namedtuple_defaults('UnitysupportService', [
                                                                  'id',
                                                                  'supportUsername',
                                                                  'supportCredentialStatus',
                                                                  'isEMCServiced',
                                                                  'isContractReportEnabled',
                                                                  ])


Unitysystem = namedtuple_defaults('Unitysystem', [
                                                  'id',
                                                  'health',
                                                  'name',
                                                  'model',
                                                  'serialNumber',
                                                  'internalModel',
                                                  'platform',
                                                  'macAddress',
                                                  'isEULAAccepted',
                                                  'isUpgradeComplete',
                                                  'isAutoFailbackEnabled',
                                                  'currentPower',
                                                  'avgPower',
                                                  ])


UnitysystemInformation = namedtuple_defaults('UnitysystemInformation', [
                                                                        'id',
                                                                        'contactFirstName',
                                                                        'contactLastName',
                                                                        'contactCompany',
                                                                        'contactPhone',
                                                                        'contactEmail',
                                                                        'locationName',
                                                                        'streetAddress',
                                                                        'city',
                                                                        'state',
                                                                        'zipcode',
                                                                        'country',
                                                                        'siteId',
                                                                        'contactMobilePhone',
                                                                        ])


UnitysystemLimit = namedtuple_defaults('UnitysystemLimit', [
                                                            'id',
                                                            'name',
                                                            'description',
                                                            'unit',
                                                            'limitValue',
                                                            'thresholdValue',
                                                            'resources',
                                                            'license',
                                                            ])


UnitysystemTime = namedtuple_defaults('UnitysystemTime', [
                                                          'id',
                                                          'time',
                                                          ])


UnitytechnicalAdvisory = namedtuple_defaults('UnitytechnicalAdvisory', [
                                                                        'id',
                                                                        'knowledgeBaseId',
                                                                        'description',
                                                                        'modificationTime',
                                                                        ])


UnitytreeQuota = namedtuple_defaults('UnitytreeQuota', [
                                                        'id',
                                                        'filesystem',
                                                        'quotaConfig',
                                                        'path',
                                                        'description',
                                                        'state',
                                                        'hardLimit',
                                                        'softLimit',
                                                        'remainingGracePeriod',
                                                        'sizeUsed',
                                                        ])


UnityuncommittedPort = namedtuple_defaults('UnityuncommittedPort', [
                                                                    'id',
                                                                    'health',
                                                                    'name',
                                                                    'portNumber',
                                                                    'connectorType',
                                                                    'sfpSupportedSpeeds',
                                                                    'sfpSupportedProtocols',
                                                                    'needsReplacement',
                                                                    'storageProcessor',
                                                                    'parentIOModule',
                                                                    'parentStorageProcessor',
                                                                    'parent',
                                                                    ])


UnityurServer = namedtuple_defaults('UnityurServer', [
                                                      'address',
                                                      'id',
                                                      ])


Unityuser = namedtuple_defaults('Unityuser', [
                                              'id',
                                              'name',
                                              'role',
                                              ])


UnityuserQuota = namedtuple_defaults('UnityuserQuota', [
                                                        'id',
                                                        'filesystem',
                                                        'treeQuota',
                                                        'uid',
                                                        'state',
                                                        'hardLimit',
                                                        'softLimit',
                                                        'remainingGracePeriod',
                                                        'sizeUsed',
                                                        ])


UnityvirtualVolume = namedtuple_defaults('UnityvirtualVolume', [
                                                                'id',
                                                                'health',
                                                                'name',
                                                                'vvolType',
                                                                'replicaType',
                                                                'parent',
                                                                'storageResource',
                                                                'pool',
                                                                'capabilityProfile',
                                                                'policyProfileName',
                                                                'isCompliant',
                                                                'isThinEnabled',
                                                                'sizeTotal',
                                                                'sizeUsed',
                                                                'bindings',
                                                                'vmUUID',
                                                                'vm',
                                                                'vmDisk',
                                                                ])


UnityvirusChecker = namedtuple_defaults('UnityvirusChecker', [
                                                              'id',
                                                              'nasServer',
                                                              'isEnabled',
                                                              ])


Unityvm = namedtuple_defaults('Unityvm', [
                                          'id',
                                          'datastore',
                                          'name',
                                          'guestAddresses',
                                          'guestHostName',
                                          'notes',
                                          'osType',
                                          'host',
                                          'state',
                                          'vmDisks',
                                          'virtualVolumes',
                                          ])


UnityvmDisk = namedtuple_defaults('UnityvmDisk', [
                                                  'datastore',
                                                  'id',
                                                  'vm',
                                                  'name',
                                                  'spaceTotal',
                                                  'type',
                                                  'virtualVolumes',
                                                  ])


UnityvmwareNasPEServer = namedtuple_defaults('UnityvmwareNasPEServer', [
                                                                        'id',
                                                                        'nasServer',
                                                                        'fileInterfaces',
                                                                        'boundVVolCount',
                                                                        ])


UnityvmwarePE = namedtuple_defaults('UnityvmwarePE', [
                                                      'id',
                                                      'vmwareNasPEServer',
                                                      'name',
                                                      'type',
                                                      'vmwareUUID',
                                                      'exportPath',
                                                      'ipAddress',
                                                      'defaultNode',
                                                      'currentNode',
                                                      'wwn',
                                                      'naa',
                                                      'vvolds',
                                                      'host',
                                                      'boundVVolCount',
                                                      'health',
                                                      ])


Unityx509Certificate = namedtuple_defaults('Unityx509Certificate', [
                                                                    'id',
                                                                    'type',
                                                                    'service',
                                                                    'scope',
                                                                    'isTrustAnchor',
                                                                    'version',
                                                                    'serialNumber',
                                                                    'signatureAlgorithm',
                                                                    'issuer',
                                                                    'validFrom',
                                                                    'validTo',
                                                                    'subject',
                                                                    'subjectAlternativeName',
                                                                    'publicKeyAlgorithm',
                                                                    'keyLength',
                                                                    'thumbprintAlgorithm',
                                                                    'thumbprint',
                                                                    'hasPrivateKey',
                                                                    ])


