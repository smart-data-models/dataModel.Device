Entidad: DeviceModel  
====================  
Esta especificación es una **versión temporal**. Se genera automáticamente a partir de las propiedades documentadas descritas en el schema.json condensadas en el archivo `model.yaml`. Se ha creado un archivo temporal `nuevo_modelo.yaml` en cada modelo de datos para evitar el impacto en los scripts existentes. Por lo tanto, la especificación estará incompleta mientras el schema.json no se actualice al nuevo formato (documentando las propiedades). Una vez actualizado el `modelo.yaml` (`nuevo_modelo.yaml`) necesita ser actualizado también (automáticamente) . Más información en este [link](https://github.com/smart-data-models/data-models/blob/master/specs/warning_message_new_spec.md). Mientras sea un formato provisional cualquier [feedback es bienvenido en este formulario](https://smartdatamodels.org/index.php/submit-an-issue-2/) eligiendo la opción `Feedback on the new specification`.  
Descripción global: **Esta entidad captura las propiedades estáticas de un dispositivo. **  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `annotations`:   - `brandName`: La marca del dispositivo.  - `color`: El color del producto.  - `controlledProperty`: Enum:temperatura, humedad, luz, movimiento, nivel de llenado, ocupación, potencia, presión, humo, energía, airePolución, ruidoNivel, condiciones meteorológicas, precipitación, velocidad del viento, dirección del viento, presión atmosférica, radiación solar, profundidad, pH, conductividad, conductancia, tss, tds, turbidez, salinidad,orp, cdom, aguaContaminación, ubicación, velocidad, rumbo, peso, aguaConsumo, gasConsumo, electricidadConsumo, sueloHumedad, tráficoFlujo, alimentaciónActividad, ordeño, movimientoActividad'.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Sello de tiempo de creación de la entidad. Normalmente será asignado por la plataforma de almacenamiento.  - `dateModified`: Sello de tiempo de la última modificación de la entidad. Esta será normalmente asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `deviceClass`: Clase de dispositivo restringido como se especifica en el RFC 7228. Si el dispositivo no es un dispositivo restringido esta propiedad no estará presente. Referencias normativas: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'.  - `documentation`: Un enlace a la documentación del dispositivo.  - `energyLimitationClass`: La clase de limitación de energía del dispositivo según la RFC 7228. Referencias normativas: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'.  - `function`: La funcionalidad necesaria para cumplir la tarea para la que un dispositivo está diseñado. Un dispositivo puede ser diseñado para realizar más de una función. Definido por [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensar, onOff, abrirCerrar, medir, eventoNotificación  - `id`:   - `image`: Una imagen del artículo.  - `manufacturerName`: El nombre del fabricante del dispositivo.  - `modelName`: El nombre del modelo del dispositivo.  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificados JSON que hace referencia a los Ids únicos de los propietarios  - `seeAlso`: lista de uri que apunta a recursos adicionales sobre el tema  - `source`: Una secuencia de caracteres que da como URL la fuente original de los datos de la entidad. Se recomienda que sea el nombre de dominio completamente calificado del proveedor de la fuente, o la URL del objeto fuente.  - `supportedUnits`: Unidades de medida soportadas por el dispositivo. El código de la unidad (texto) de medida dado usando el [Código Común UN/CEFACT](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (máx. 3 caracteres).  - `type`: Tipo de entidad NGSI. Tiene que ser DeviceModel    
Propiedades requeridas  
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  ## Modelo de datos Descripción de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
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
      description: 'Device''s brand name.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    color:    
      description: 'The color of the product.'    
      type: string    
    controlledProperty:    
      description: 'Enum:''temperature, humidity, light, motion, fillingLevel,occupancy, power, pressure, smoke, energy, airPollution, noiseLevel, weatherConditions, precipitation, windSpeed, windDirection, atmosphericPressure, solarRadiation, depth, pH,conductivity, conductance, tss, tds, turbidity, salinity,orp, cdom, waterPollution, location, speed, heading,weight, waterConsumption, gasComsumption, electricityConsumption, soilMoisture, trafficFlow,eatingActivity, milking, movementActivity''.'    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
      description: "Class of constrained device as specified by RFC 7228. If the device is not a constrained device this property shall not be present. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'"    
      enum:    
        - C0    
        - C1    
        - C2    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    documentation:    
      description: 'A link to device''s documentation.'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    energyLimitationClass:    
      description: "Device's class of energy limitation as per RFC 7228. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'"    
      enum:    
        - E0    
        - E1    
        - E2    
        - E9    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    function:    
      description: "The functionality necessary to accomplish the task for which a Device is designed. A device can be designed to perform more than one function. Defined by [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification"    
      items:    
        enum:    
          - levelControl    
          - sensing    
          - onOff    
          - openClose    
          - metering    
          - eventNotification    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      description: 'Device''s manufacturer name.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    modelName:    
      description: 'Device''s model name.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *devicemodel_-_properties_-_owner_-_items_-_anyof    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    supportedUnits:    
      description: 'Units of measurement supported by the device. The unit code (text) of measurement given using the [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters).'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. it has to be DeviceModel'    
      enum:    
        - DeviceModel    
      type: Property    
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
## Ejemplo de cargas útiles  
#### Ejemplo de valores clave de DeviceModel NGSI V2  
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
#### DeviceModel NGSI V2 normalizado Ejemplo  
Aquí hay un ejemplo de un modelo de dispositivo en formato JSON como normalizado. Es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### Ejemplo de valores clave de DeviceModel NGSI-LD  
Aquí hay un ejemplo de un modelo de dispositivo en formato JSON-LD como valores clave. Es compatible con NGSI-LD cuando se utiliza `opciones=valores-clave` y devuelve los datos de contexto de una entidad individual.  
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
#### DeviceModel NGSI-LD normalizado Ejemplo  
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
