from __future__ import annotations

from enum import Enum
from ipaddress import IPv4Address, IPv6Address
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class CategoryEnum(Enum):
    actuator = 'actuator'
    beacon = 'beacon'
    endgun = 'endgun'
    HVAC = 'HVAC'
    implement = 'implement'
    irrSection = 'irrSection'
    irrSystem = 'irrSystem'
    meter = 'meter'
    multimedia = 'multimedia'
    network = 'network'
    sensor = 'sensor'


class ConfigurationItem(BaseModel):
    parameter: Optional[str] = Field(
        None, description='Name of the parameter in the configuration of the device'
    )
    value: Optional[str] = Field(
        None, description='Value of the parameter in the configuration of the device'
    )


class ControlledPropertyEnum(Enum):
    airPollution = 'airPollution'
    atmosphericPressure = 'atmosphericPressure'
    averageVelocity = 'averageVelocity'
    batteryLife = 'batteryLife'
    batterySupply = 'batterySupply'
    cdom = 'cdom'
    conductance = 'conductance'
    conductivity = 'conductivity'
    depth = 'depth'
    eatingActivity = 'eatingActivity'
    electricityConsumption = 'electricityConsumption'
    energy = 'energy'
    fillingLevel = 'fillingLevel'
    freeChlorine = 'freeChlorine'
    gasConsumption = 'gasConsumption'
    gateOpening = 'gateOpening'
    heading = 'heading'
    humidity = 'humidity'
    light = 'light'
    location = 'location'
    milking = 'milking'
    motion = 'motion'
    movementActivity = 'movementActivity'
    noiseLevel = 'noiseLevel'
    occupancy = 'occupancy'
    orp = 'orp'
    pH = 'pH'
    power = 'power'
    precipitation = 'precipitation'
    pressure = 'pressure'
    refractiveIndex = 'refractiveIndex'
    salinity = 'salinity'
    smoke = 'smoke'
    soilMoisture = 'soilMoisture'
    solarRadiation = 'solarRadiation'
    speed = 'speed'
    tds = 'tds'
    temperature = 'temperature'
    trafficFlow = 'trafficFlow'
    tss = 'tss'
    turbidity = 'turbidity'
    uvLampIntensity = 'uvLampIntensity'
    uvOrganicLoad = 'uvOrganicLoad'
    waterConsumption = 'waterConsumption'
    waterFlow = 'waterFlow'
    waterLevel = 'waterLevel'
    waterPollution = 'waterPollution'
    weatherConditions = 'weatherConditions'
    weight = 'weight'
    windDirection = 'windDirection'
    windSpeed = 'windSpeed'


class DeviceCategoryEnum(Enum):
    actuator = 'actuator'
    beacon = 'beacon'
    endgun = 'endgun'
    HVAC = 'HVAC'
    implement = 'implement'
    irrSection = 'irrSection'
    irrSystem = 'irrSystem'
    meter = 'meter'
    multimedia = 'multimedia'
    network = 'network'
    sensor = 'sensor'


class Direction(Enum):
    Inlet = 'Inlet'
    Outlet = 'Outlet'
    Entry = 'Entry'
    Exit = 'Exit'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class SupportedProtocolEnum(Enum):
    field_3g = '3g'
    bluetooth = 'bluetooth'
    bluetooth_LE = 'bluetooth LE'
    cat_m = 'cat-m'
    coap = 'coap'
    ec_gsm_iot = 'ec-gsm-iot'
    gprs = 'gprs'
    http = 'http'
    lwm2m = 'lwm2m'
    lora = 'lora'
    lte_m = 'lte-m'
    mqtt = 'mqtt'
    nb_iot = 'nb-iot'
    onem2m = 'onem2m'
    sigfox = 'sigfox'
    ul20 = 'ul20'
    websocket = 'websocket'


class Type6(Enum):
    Device = 'Device'


class Device(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    batteryLevel: Optional[
        Union[confloat(ge=0.0, le=1.0), confloat(ge=-1.0, le=-1.0)]
    ] = Field(
        None,
        description='Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined',
    )
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category",
    )
    configuration: Optional[List[ConfigurationItem]] = Field(
        None,
        description="Device's technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model",
    )
    controlledAsset: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='List of the asset(s) (building, object, etc.) controlled by the device',
    )
    controlledProperty: Optional[List[ControlledPropertyEnum]] = Field(
        None,
        description="Anything that can be sensed, measured or controlled by. Enum:'airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'",
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateFirstUsed: Optional[AwareDatetime] = Field(
        None, description='A timestamp which denotes when the device was first used'
    )
    dateInstalled: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes when the device was installed (if it requires installation)',
    )
    dateLastCalibration: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes when the last calibration of the device happened',
    )
    dateLastValueReported: Optional[AwareDatetime] = Field(
        None,
        description='A timestamp which denotes the last time when the device successfully reported data to the cloud',
    )
    dateManufactured: Optional[AwareDatetime] = Field(
        None, description='A timestamp which denotes when the device was manufactured'
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    dateObserved: Optional[AwareDatetime] = Field(
        None, description='Date of the observed entity defined by the user'
    )
    depth: Optional[float] = Field(
        None,
        description='Location of this device represented by a depth from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceCategory: Optional[List[DeviceCategoryEnum]] = Field(
        None,
        description="Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category",
    )
    deviceState: Optional[str] = Field(
        None,
        description='State of this device from an operational point of view. Its value can be vendor dependent',
    )
    direction: Optional[Direction] = Field(
        None,
        description="Enum:'Inlet, Outlet, Entry, Exit'. A timestamp which denotes when the device was installed (if it requires installation)",
    )
    distance: Optional[float] = Field(
        None,
        description='Location of this device represented by a distance from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
    )
    dstAware: Optional[bool] = Field(
        None,
        description='Indicates a device which is Daylight Savings Time Aware (True). In case it is then the Timestamp is automatically adjusted by the device to reflect DST changes. If not (False) the time adjustments must be taken care of by the user',
    )
    firmwareVersion: Optional[str] = Field(
        None, description='The firmware version of this device'
    )
    hardwareVersion: Optional[str] = Field(
        None, description='The hardware version of this device'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    ipAddress: Optional[List[Union[IPv4Address, IPv6Address]]] = Field(
        None,
        description='List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    macAddress: Optional[
        constr(pattern=r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    ] = Field(None, description='The MAC address of the device')
    mcc: Optional[str] = Field(
        None, description='This property identifies the Mobile Country Code'
    )
    mnc: Optional[str] = Field(
        None,
        description="This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a 'MCC / MNC tuple') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks",
    )
    name: Optional[str] = Field(None, description='The name of this item')
    osVersion: Optional[str] = Field(
        None, description='The version of the host operating system device'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    provider: Optional[str] = Field(None, description='The provider of the device')
    refDeviceModel: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Model of the device')
    relativePosition: Optional[str] = Field(
        None,
        description='Location of this device in a coordinate system according to its local emplacement',
    )
    rssi: Optional[float] = Field(
        None,
        description='Received signal strength indicator for a wireless enabled device. It must be expressed in dBm or mW, use unitcode to set it out. ',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serialNumber: Optional[str] = Field(
        None, description='The serial number assigned by the manufacturer'
    )
    softwareVersion: Optional[str] = Field(
        None, description='The software version of this device'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    supportedProtocol: Optional[List[SupportedProtocolEnum]] = Field(
        None, description='Supported protocol(s) or networks'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI Entity type. It has to be Device'
    )
    value: Optional[str] = Field(
        None,
        description="A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value 'on' of type 'Text'. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to 'off'",
    )
