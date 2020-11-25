Entity: Device  
==============  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).**  

## List of properties  

`address`: The mailing address.  `alternateName`: An alternative name for this item  `areaServed`: The geographic area where a service or offered item is provided.  `batteryLevel`:   `configuration`:   `controlledAsset`:   `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  `dateFirstUsed`:   `dateInstalled`:   `dateLastCalibration`:   `dateLastValueReported`:   `dateManufactured`:   `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  `depth`:   `description`: A description of this item  `deviceState`:   `direction`:   `distance`:   `firmwareVersion`:   `hardwareVersion`:   `id`:   `ipAddress`:   `location`:   `macAddress`:   `mnc`:   `name`: The name of this item.  `osVersion`:   `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  `provider`:   `refDeviceModel`:   `relativePosition`:   `rssi`:   `seeAlso`:   `serialNumber`:   `softwareVersion`:   `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  `type`: NGSI Entity type  `value`:   ## Data Model description of properties  
Sorted alphabetically  
```yaml  
Device:    
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'    
  properties:    
    address:    
      description: 'The mailing address.'    
      properties:    
        addressCountry:    
          type: string    
        addressLocality:    
          type: string    
        addressRegion:    
          type: string    
        areaServed:    
          type: string    
        postOfficeBoxNumber:    
          type: string    
        postalCode:    
          type: string    
        streetAddress:    
          type: string    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided.'    
      type: Property    
    batteryLevel:    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
    configuration:    
      type: object    
    controlledAsset:    
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
      type: array    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateFirstUsed:    
      format: date-time    
      type: string    
    dateInstalled:    
      format: date-time    
      type: string    
    dateLastCalibration:    
      format: date-time    
      type: string    
    dateLastValueReported:    
      format: date-time    
      type: string    
    dateManufactured:    
      format: date-time    
      type: string    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    depth:    
      type: number    
    description:    
      description: 'A description of this item'    
      type: Property    
    deviceState:    
      type: string    
    direction:    
      enum:    
        - Inlet    
        - Outlet    
        - Entry    
        - Exit    
      type: string    
    distance:    
      type: number    
    firmwareVersion:    
      type: string    
    hardwareVersion:    
      type: string    
    id:    
      anyOf: *device_-_properties_-_id_-_anyof    
    ipAddress:    
      items:    
        oneOf:    
          - format: ipv4    
          - format: ipv6    
        type: string    
      type: array    
    location:    
      $id: https://geojson.org/schema/Geometry.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      oneOf:    
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
        - properties:    
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
      title: 'GeoJSON Geometry'    
    macAddress:    
      items:    
        pattern: ^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$    
        type: string    
      type: array    
    mnc:    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    osVersion:    
      type: string    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *device_-_properties_-_id_-_anyof    
      type: Property    
    provider:    
      type: string    
    refDeviceModel:    
      oneOf:    
        - format: uri    
          type: string    
        - anyOf: *device_-_properties_-_id_-_anyof    
    relativePosition:    
      type: string    
    rssi:    
      type: number    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    serialNumber:    
      type: string    
    softwareVersion:    
      type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - Device    
      type: string    
    value:    
      type: string    
  required:    
    - id    
    - type    
    - category    
    - controlledProperty    
  type: object    
```  
Here is an example of a Device in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": ["sensor"],  
  "controlledProperty": ["fillingLevel", "temperature"],  
  "controlledAsset": ["wastecontainer-Osuna-100"],  
  "ipAddress": ["192.14.56.78"],  
  "mcc": "214",  
  "mnc": "07",  
  "batteryLevel": 0.75,  
  "serialNumber": "9845A",  
  "refDeviceModel": "myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "deviceState": "ok",  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "owner": ["http://person.org/leon"]  
}  
```  
Here is an example of a Device in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": {  
    "value": ["sensor"]  
  },  
  "batteryLevel": {  
    "value": 0.75  
  },  
  "dateFirstUsed": {  
    "type": "DateTime",  
    "value": "2014-09-11T11:00:00Z"  
  },  
  "controlledAsset": {  
    "type": "Relationship",  
    "value": ["wastecontainer-Osuna-100"]  
  },  
  "serialNumber": {  
    "value": "9845A"  
  },  
  "mcc": {  
    "value": "214"  
  },  
  "value": {  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "refDeviceModel": {  
    "type": "Relationship",  
    "value": "myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "value": 0.86  
  },  
  "controlledProperty": {  
    "value": ["fillingLevel", "temperature"]  
  },  
  "owner": {  
    "value": ["http://person.org/leon"]  
  },  
  "mnc": {  
    "value": "07"  
  },  
  "ipAddress": {  
    "value": ["192.14.56.78"]  
  },  
  "deviceState": {  
    "value": "ok"  
  }  
}  
```  
Here is an example of a Device in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "batteryLevel": 0.75,  
 "category": ["sensor"],  
 "controlledAsset": ["urn:ngsi-ld::wastecontainer-Osuna-100"],  
 "controlledProperty": ["fillingLevel", "temperature"],  
 "dateFirstUsed": {"@type": "DateTime", "@value": "2014-09-11T11:00:00Z"},  
 "deviceState": "ok",  
 "id": "urn:ngsi-ld:Device:device-9845A",  
 "ipAddress": ["192.14.56.78"],  
 "mcc": "214",  
 "mnc": "07",  
 "owner": ["http://person.org/leon"],  
 "refDeviceModel": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
 "rssi": 0.86,  
 "serialNumber": "9845A",  
 "type": "Device",  
 "value": "l%3D0.22%3Bt%3D21.2"}  
```  
Here is an example of a Device in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
    "batteryLevel": {  
        "type": "Property",  
        "value": 0.75  
    },  
    "dateFirstUsed": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2014-09-11T11:00:00Z"  
        }  
    },  
    "controlledAsset": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld::wastecontainer-Osuna-100"  
        ]  
    },  
    "serialNumber": {  
        "type": "Property",  
        "value": "9845A"  
    },  
    "mcc": {  
        "type": "Property",  
        "value": "214"  
    },  
    "value": {  
        "type": "Property",  
        "value": "l%3D0.22%3Bt%3D21.2"  
    },  
    "refDeviceModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345"  
    },  
    "rssi": {  
        "type": "Property",  
        "value": 0.86  
    },  
    "controlledProperty": {  
        "type": "Property",  
        "value": [  
            "fillingLevel",  
            "temperature"  
        ]  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "http://person.org/leon"  
        ]  
    },  
    "mnc": {  
        "type": "Property",  
        "value": "07"  
    },  
    "ipAddress": {  
        "type": "Property",  
        "value": [  
            "192.14.56.78"  
        ]  
    },  
    "deviceState": {  
        "type": "Property",  
        "value": "ok"  
    },  
    "distance": {  
        "type": "Property",  
        "value": 20,  
        "unitCode": "MTR"  
    },  
    "depth": {  
        "type": "Property",  
        "value": 3,  
        "unitCode": "MTR"  
    },  
    "direction": {  
        "type": "Property",  
        "value": "Outlet"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
