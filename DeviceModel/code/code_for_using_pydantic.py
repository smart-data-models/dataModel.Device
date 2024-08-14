from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


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


class DeviceClass(Enum):
    C0 = 'C0'
    C1 = 'C1'
    C2 = 'C2'


class EnergyLimitationClass(Enum):
    E0 = 'E0'
    E1 = 'E1'
    E2 = 'E2'
    E9 = 'E9'


class FunctionEnum(Enum):
    levelControl = 'levelControl'
    sensing = 'sensing'
    onOff = 'onOff'
    openClose = 'openClose'
    metering = 'metering'
    eventNotification = 'eventNotification'


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


class Type(Enum):
    DeviceModel = 'DeviceModel'


class DeviceModel(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    annotations: Optional[List[str]] = Field(
        None, description='Annotations about the item'
    )
    brandName: Optional[str] = Field(None, description="Device's brand name")
    category: Optional[List[CategoryEnum]] = Field(
        None,
        description="Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category",
    )
    color: Optional[str] = Field(None, description='The color of the product')
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
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    deviceCategory: Optional[List[DeviceCategoryEnum]] = Field(
        None,
        description="Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category",
    )
    deviceClass: Optional[DeviceClass] = Field(
        None,
        description="Class of constrained device as specified by RFC 7228. If the device is not a constrained device this property shall not be present. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'",
    )
    documentation: Optional[AnyUrl] = Field(
        None, description="A link to device's documentation"
    )
    energyLimitationClass: Optional[EnergyLimitationClass] = Field(
        None,
        description="Device's class of energy limitation as per RFC 7228. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'",
    )
    function: Optional[List[FunctionEnum]] = Field(
        None,
        description="The functionality necessary to accomplish the task for which a Device is designed. A device can be designed to perform more than one function. Defined by [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification",
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
    image: Optional[AnyUrl] = Field(None, description='An image of the item')
    macAddress: Optional[
        constr(pattern=r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    ] = Field(None, description='The MAC address of the device')
    manufacturerName: Optional[str] = Field(
        None, description="Device's manufacturer name"
    )
    modelName: Optional[str] = Field(None, description="Device's model name")
    name: Optional[str] = Field(None, description='The name of this item')
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
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    supportedProtocol: Optional[List[SupportedProtocolEnum]] = Field(
        None, description='Supported protocol(s) or networks'
    )
    supportedUnits: Optional[List[str]] = Field(
        None,
        description='Units of measurement supported by the device. The unit code (text) of measurement given using the [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters)',
    )
    type: Optional[Type] = Field(
        None, description='NGSI Entity type. it has to be DeviceModel'
    )
