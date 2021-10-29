Entity: Device  
==============  
[Open License](https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).**  
version: 0.0.6  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `batteryLevel`: Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined.  - `category`: Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'  - `configuration`: Device's technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model.  - `controlledAsset`: List of the asset(s) (building, object, etc.) controlled by the device.  - `controlledProperty`: Anything that can be sensed, measured or controlled by. Enum:'airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateFirstUsed`: A timestamp which denotes when the device was first used.  - `dateInstalled`: A timestamp which denotes when the device was installed (if it requires installation).  - `dateLastCalibration`: A timestamp which denotes when the last calibration of the device happened.  - `dateLastValueReported`: A timestamp which denotes the last time when the device successfully reported data to the cloud.  - `dateManufactured`: A timestamp which denotes when the device was manufactured.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `dateObserved`: Date of the observed entity defined by the user.  - `depth`: Location of this device represented by a depth from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code  - `description`: A description of this item  - `deviceState`: State of this device from an operational point of view. Its value can be vendor dependent.  - `direction`: Enum:'Inlet, Outlet, Entry, Exit'. A timestamp which denotes when the device was installed (if it requires installation).  - `distance`: Location of this device represented by a distance from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code  - `dstAware`: Indicates a device which is Daylight Savings Time Aware (True). In case it is then the Timestamp is automatically adjusted by the device to reflect DST changes. If not (False) the time adjustments must be taken care of by the user.  - `firmwareVersion`: The firmware version of this device.  - `hardwareVersion`: The hardware version of this device.  - `id`: Unique identifier of the entity  - `ipAddress`: List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address.  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `macAddress`: The MAC address of the device.  - `mcc`: This property identifies the Mobile Country Code  - `mnc`: This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a 'MCC / MNC tuple') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks.  - `name`: The name of this item.  - `osVersion`: The version of the host operating system device.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `provider`: The provider of the device.  - `refDeviceModel`: Model of the device  - `relativePosition`: Location of this device in a coordinate system according to its local emplacement.  - `rssi`: Received signal strength indicator for a wireless enabled device. It must be expressed in dBm or mW, use unitcode to set it out.   - `seeAlso`: list of uri pointing to additional resources about the item  - `serialNumber`: The serial number assigned by the manufacturer.  - `softwareVersion`: The software version of this device.  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `supportedProtocol`: Supported protocol(s) or networks  - `type`: NGSI Entity type. It has to be Device  - `value`: A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value 'on' of type 'Text'. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to 'off'.    
Required properties  
- `controlledProperty`  - `id`  - `type`    
A Device is a   tangible object which contains some logic and is producer and/or consumer of data. A Device is always assumed to be capable of communicating electronically via a network. This data model has been partially developed in cooperation with mobile operators and the [GSMA](https://www.gsma.com/iot/iot-big-data/). This data model reuses concepts coming from the [SAREF Ontology](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf) part of [ETSI](http://www.etsi.org) standards.  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Device:    
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'    
  modelTags: ""    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batteryLevel:    
      description: 'Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined.'    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'"    
      items:    
        enum:    
          - actuator    
          - beacon    
          - endgun    
          - HVAC    
          - implement    
          - irrSection    
          - irrSystem    
          - meter    
          - multimedia    
          - network    
          - sensor    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    configuration:    
      description: 'Device''s technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model.'    
      items:    
        properties:    
          parameter:    
            type: string    
          value:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    controlledAsset:    
      description: 'List of the asset(s) (building, object, etc.) controlled by the device.'    
      items:    
        oneOf:    
          - format: uri    
            type: string    
          - anyOf: &device_-_properties_-_id_-_anyof    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    controlledProperty:    
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'''    
      items:    
        enum:    
          - airPollution    
          - atmosphericPressure    
          - averageVelocity    
          - batteryLife    
          - batterySupply    
          - cdom    
          - conductance    
          - conductivity    
          - depth    
          - eatingActivity    
          - eatingActivity    
          - electricityConsumption    
          - energy    
          - fillingLevel    
          - freeChlorine    
          - gasConsumption    
          - gateOpening    
          - heading    
          - humidity    
          - light    
          - location    
          - milking    
          - motion    
          - movementActivity    
          - noiseLevel    
          - occupancy    
          - orp    
          - pH    
          - power    
          - precipitation    
          - pressure    
          - refractiveIndex    
          - salinity    
          - smoke    
          - soilMoisture    
          - solarRadiation    
          - speed    
          - tds    
          - temperature    
          - trafficFlow    
          - tss    
          - turbidity    
          - waterConsumption    
          - waterFlow    
          - waterLevel    
          - waterPollution    
          - weatherConditions    
          - weight    
          - windDirection    
          - windSpeed    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateFirstUsed:    
      description: 'A timestamp which denotes when the device was first used.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateInstalled:    
      description: 'A timestamp which denotes when the device was installed (if it requires installation).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastCalibration:    
      description: 'A timestamp which denotes when the last calibration of the device happened.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastValueReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data to the cloud.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateManufactured:    
      description: 'A timestamp which denotes when the device was manufactured.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'Date of the observed entity defined by the user.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    depth:    
      description: 'Location of this device represented by a depth from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceState:    
      description: 'State of this device from an operational point of view. Its value can be vendor dependent.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    direction:    
      description: 'Enum:''Inlet, Outlet, Entry, Exit''. A timestamp which denotes when the device was installed (if it requires installation).'    
      enum:    
        - Inlet    
        - Outlet    
        - Entry    
        - Exit    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/DateTime'    
        type: Property    
    distance:    
      description: 'Location of this device represented by a distance from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Distance    
        type: Property    
    dstAware:    
      description: 'Indicates a device which is Daylight Savings Time Aware (True). In case it is then the Timestamp is automatically adjusted by the device to reflect DST changes. If not (False) the time adjustments must be taken care of by the user.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    firmwareVersion:    
      description: 'The firmware version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hardwareVersion:    
      description: 'The hardware version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: *device_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    ipAddress:    
      description: 'List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address.'    
      items:    
        oneOf:    
          - format: ipv4    
          - format: ipv6    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    macAddress:    
      description: 'The MAC address of the device.'    
      pattern: ^([[A-Fa-f0-9]]{2}[:.-]?){5}[[A-Fa-f0-9]]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    mcc:    
      description: 'This property identifies the Mobile Country Code'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    mnc:    
      description: 'This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a ''MCC / MNC tuple'') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    osVersion:    
      description: 'The version of the host operating system device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *device_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    provider:    
      description: 'The provider of the device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/provider    
        type: Property    
    refDeviceModel:    
      description: 'Model of the device'    
      oneOf:    
        - format: uri    
          type: string    
        - anyOf: *device_-_properties_-_id_-_anyof    
          description: 'Property. Unique identifier of the entity'    
      x-ngsi:    
        type: Relationship    
    relativePosition:    
      description: 'Location of this device in a coordinate system according to its local emplacement.'    
      type: string    
      x-ngsi:    
        type: Property    
    rssi:    
      description: 'Received signal strength indicator for a wireless enabled device. It must be expressed in dBm or mW, use unitcode to set it out. '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    serialNumber:    
      description: 'The serial number assigned by the manufacturer.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    softwareVersion:    
      description: 'The software version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    supportedProtocol:    
      description: 'Supported protocol(s) or networks'    
      items:    
        enum:    
          - 3g    
          - bluetooth    
          - 'bluetooth LE'    
          - cat-m    
          - coap    
          - ec-gsm-iot    
          - gprs    
          - http    
          - lwm2m    
          - lora    
          - lte-m    
          - mqtt    
          - nb-iot    
          - onem2m    
          - sigfox    
          - ul20    
          - websocket    
        type: string    
      type: array    
      x-ngsi:    
        model: '3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket'    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Device'    
      enum:    
        - Device    
      type: string    
      x-ngsi:    
        type: Property    
    value:    
      description: 'A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value ''on'' of type ''Text''. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to ''off''.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/QuantitativeValue    
        type: Property    
  required:    
    - id    
    - type    
    - controlledProperty    
  type: object    
  version: 0.0.6    
```  
</details>    
## Example payloads    
#### Device NGSI-v2 key-values Example    
Here is an example of a Device in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": [  
    "sensor"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "controlledAsset": [  
    "wastecontainer-Osuna-100"  
  ],  
  "ipAddress": [  
    "192.14.56.78"  
  ],  
  "mcc": "214",  
  "mnc": "07",  
  "batteryLevel": 0.75,  
  "serialNumber": "9845A",  
  "refDeviceModel": "myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "deviceState": "ok",  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "owner": [  
    "http://person.org/leon"  
  ]  
}  
```  
#### Device NGSI-v2 normalized Example    
Here is an example of a Device in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": {  
    "type": "Text",  
    "value": [  
      "sensor"  
    ]  
  },  
  "batteryLevel": {  
    "type": "Number",  
    "value": 0.75  
  },  
  "dateFirstUsed": {  
    "type": "DateTime",  
    "value": "2014-09-11T11:00:00Z"  
  },  
  "controlledAsset": {  
    "type": "Relationship",  
    "value": [  
      "wastecontainer-Osuna-100"  
    ]  
  },  
  "serialNumber": {  
    "type": "Text",  
    "value": "9845A"  
  },  
  "mcc": {  
    "type": "Text",  
    "value": "214"  
  },  
  "value": {  
    "type": "Text",  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "refDeviceModel": {  
    "type": "Relationship",  
    "value": "myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "type": "Number",  
    "value": 0.86  
  },  
  "controlledProperty": {  
    "type": "array",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "http://person.org/leon"  
    ]  
  },  
  "mnc": {  
    "type": "Text",  
    "value": "07"  
  },  
  "ipAddress": {  
    "type": "array",  
    "value": [  
      "192.14.56.78"  
    ]  
  },  
  "deviceState": {  
    "type": "Text",  
    "value": "ok"  
  }  
}  
```  
#### Device NGSI-LD key-values Example    
Here is an example of a Device in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "category": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "batteryLevel": 0.75,  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "controlledAsset": [  
    "urn:ngsi-ld::wastecontainer-Osuna-100"  
  ],  
  "serialNumber": "9845A",  
  "mcc": "214",  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "refDeviceModel": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "owner": [  
    "http://person.org/leon"  
  ],  
  "mnc": "07",  
  "ipAddress": [  
    "192.14.56.78"  
  ],  
  "deviceState": "ok",  
  "distance": 20,  
  "depth": 3,  
  "direction": "Outlet",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### Device NGSI-LD normalized Example    
Here is an example of a Device in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": {  
    "type": "Property",  
    "value": 0.75  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "controlledAsset": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld::wastecontainer-Osuna-100"  
    ]  
  },  
  "controlledProperty": {  
    "type": "Property",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "dateFirstUsed": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2014-09-11T11:00:00Z"  
    }  
  },  
  "deviceState": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "ipAddress": {  
    "type": "Property",  
    "value": [  
      "192.14.56.78"  
    ]  
  },  
  "mcc": {  
    "type": "Property",  
    "value": "214"  
  },  
  "mnc": {  
    "type": "Property",  
    "value": "07"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "http://person.org/leon"  
    ]  
  },  
  "refDeviceModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "type": "Property",  
    "value": 0.86  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": "9845A"  
  },  
  "value": {  
    "type": "Property",  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
