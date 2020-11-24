Entidad: DeviceModel  
====================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad captura las propiedades estáticas de un dispositivo. **  

## Lista de propiedades  

`alternateName`: Un nombre alternativo para este artículo  `annotations`:   `brandName`:   `color`: El color del producto.  `controlledProperty`:   `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `dateModified`: Sello de tiempo de la última modificación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  `description`: Una descripción de este artículo  `deviceClass`:   `documentation`:   `energyLimitationClass`:   `function`:   `id`:   `image`: Una imagen del artículo.  `manufacturerName`:   `modelName`:   `name`: El nombre de este artículo.  `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  `seeAlso`:   `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  `supportedUnits`:   `type`: NGSI Tipo de entidad  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente  
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
Aquí hay un ejemplo de un modelo de dispositivo en formato JSON como valores clave. Es compatible con NGSI V2 cuando se utiliza "opciones=valores-clave" y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de un modelo de dispositivo en formato JSON como normalizado. Es compatible con NGSI V2 cuando se utiliza "opciones=valores clave" y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de un modelo de dispositivo en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
Aquí hay un ejemplo de un DeviceModel en formato JSON-LD normalizado. Este es compatible con NGSI-LD cuando no se usan opciones y devuelve los datos de contexto de una entidad individual.  
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
