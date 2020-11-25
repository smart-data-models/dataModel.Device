Entity: DeviceModel  
===================  
This specification is a **temporal version**. It is automatically generated from the  documented properties described in the schema.json condensed into the file `model.yaml`. A temporary `new_model.yaml` file has been created in every data model to avoid impacting into existing scripts. Thus, the specification will be incomplete as long as the schema.json is not updated to the new format (documenting properties). Once updated the `model.yaml` (`new_model.yaml`) needs to be updated as well (automatically) . Further info in this [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). As long as it is a provisional format any [feedback is welcomed in this form](https://smartdatamodels.org/index.php/submit-an-issue-2/) choosing option `Feedback on the new specification`  
Global description: **This entity captures the static properties of a Device. **  

## List of properties  

- `alternateName`: An alternative name for this item  - `annotations`:   - `brandName`:   - `color`: The color of the product.  - `controlledProperty`:   - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `deviceClass`:   - `documentation`:   - `energyLimitationClass`:   - `function`:   - `id`:   - `image`: An image of the item.  - `manufacturerName`:   - `modelName`:   - `name`: The name of this item.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso`:   - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `supportedUnits`:   - `type`: NGSI Entity type  ## Data Model description of properties  
Sorted alphabetically  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DeviceModel:    
  description: 'This entity captures the static properties of a Device. '    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      items:    
        type: string    
      type: array    
    brandName:    
      type: string    
    color:    
      description: 'The color of the product.'    
      type: string    
    controlledProperty:    
      items:    
        enum:    
          - temperature    
          - humidity    
          - light    
          - motion    
          - fillingLevel    
          - occupancy    
          - power    
          - pressure    
          - smoke    
          - energy    
          - airPollution    
          - noiseLevel    
          - weatherConditions    
          - precipitation    
          - windSpeed    
          - windDirection    
          - atmosphericPressure    
          - solarRadiation    
          - depth    
          - pH    
          - conductivity    
          - conductance    
          - tss    
          - tds    
          - turbidity    
          - salinity    
          - orp    
          - cdom    
          - waterPollution    
          - location    
          - speed    
          - heading    
          - weight    
          - waterConsumption    
          - gasComsumption    
          - electricityConsumption    
          - soilMoisture    
          - trafficFlow    
        type: string    
      type: array    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    deviceClass:    
      enum:    
        - C0    
        - C1    
        - C2    
      type: string    
    documentation:    
      format: uri    
      type: string    
    energyLimitationClass:    
      enum:    
        - E0    
        - E1    
        - E2    
        - E9    
      type: string    
    function:    
      items:    
        enum:    
          - levelControl    
          - sensing    
          - onOff    
          - openClose    
          - metering    
          - eventNotification    
        type: string    
      type: array    
    id:    
      anyOf: &devicemodel_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
    image:    
      description: 'An image of the item.'    
      format: uri    
      type: string    
    manufacturerName:    
      type: string    
    modelName:    
      type: string    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *devicemodel_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    seeAlso:    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    supportedUnits:    
      items:    
        type: string    
      type: array    
    type:    
      description: 'NGSI Entity type'    
      enum:    
        - DeviceModel    
      type: string    
  required:    
    - id    
    - type    
    - category    
    - controlledProperty    
    - manufacturerName    
    - brandName    
    - modelName    
  type: object    
```  
</details>    
#### DeviceModel NGSI V2 key-values Example    
Here is an example of a DeviceModel in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "name": "myDevice Sensor for Containers 345",  
  "brandName": "myDevice",  
  "modelName": "S4Container 345",  
  "manufacturerName": "myDevice Inc.",  
  "category": ["sensor"],  
  "function": ["sensing"],  
  "controlledProperty": ["fillingLevel", "temperature"]  
}  
```  
#### DeviceModel NGSI V2 normalized Example    
Here is an example of a DeviceModel in JSON format as normalized. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "category": {  
    "value": ["sensor"]  
  },  
  "function": {  
    "value": ["sensing"]  
  },  
  "modelName": {  
    "value": "S4Container 345"  
  },  
  "name": {  
    "value": "myDevice Sensor for Containers 345"  
  },  
  "brandName": {  
    "value": "myDevice"  
  },  
  "manufacturerName": {  
    "value": "myDevice Inc."  
  },  
  "controlledProperty": {  
    "value": ["fillingLevel", "temperature"]  
  }  
}  
```  
#### DeviceModel NGSI-LD key-values Example    
Here is an example of a DeviceModel in JSON-LD format as key-values. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "myDevice",  
 "category": ["sensor"],  
 "controlledProperty": ["fillingLevel", "temperature"],  
 "function": ["sensing"],  
 "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
 "manufacturerName": "myDevice Inc.",  
 "modelName": "S4Container 345",  
 "name": "myDevice Sensor for Containers 345",  
 "type": "DeviceModel"}  
```  
#### DeviceModel NGSI-LD normalized Example    
Here is an example of a DeviceModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
    "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
    "type": "DeviceModel",  
    "category": {  
        "type": "Property",  
        "value": [  
            "sensor"  
        ]  
    },  
    "function": {  
        "type": "Property",  
        "value": [  
            "sensing"  
        ]  
    },  
    "modelName": {  
        "type": "Property",  
        "value": "S4Container 345"  
    },  
    "name": {  
        "type": "Property",  
        "value": "myDevice Sensor for Containers 345"  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "myDevice"  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "myDevice Inc."  
    },  
    "controlledProperty": {  
        "type": "Property",  
        "value": [  
            "fillingLevel",  
            "temperature"  
        ]  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
