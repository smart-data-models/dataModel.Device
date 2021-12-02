Entidad: DeviceMeasurement  
==========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceMeasurement/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Descripción de una entidad de medición genérica procedente de un dispositivo u otra fuente de datos.**  
versión: 0.1.0  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `controlledProperty`: Propiedad que mide el dispositivo  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `dateObserved`: La fecha y la hora de esta observación en formato ISO8601 UTC  - `description`: Una descripción de este artículo  - `deviceType`: Tipo de dispositivo que realiza la medición  - `id`: Identificador único de la entidad  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `measurementType`: El tipo de medición que se va a realizar  - `name`: El nombre de este artículo.  - `numValue`: Valor numérico de la medida  - `outlier`: Valor para marcar la medida a procesar especialmente  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `refDevice`: Dispositivo que realiza la medición  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `textValue`: Valor textual de la medida  - `type`: Tipo de entidad NGSI. Tiene que ser Medición  - `unit`: Unidades de medida. En caso de utilizar un acrónimo, utilice las unidades aceptadas en el código [CEFACT](https://www.unece.org/cefact.html).    
Propiedades requeridas  
- `id`  - `type`    
Los estándares NGSIv2 y NGSI-LD tienen formas de incluir unidades en cada propiedad. Sin embargo, existe una propiedad llamada "Unidad" por razones de compatibilidad. Es opcional.  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DeviceMeasurement:    
  description: 'Description of a generic measurement entity coming from a device or other data source.'    
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
    controlledProperty:    
      description: 'Property being measured by the device'    
      type: string    
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
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'The date and time of this observation in ISO8601 UTC format'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceType:    
      description: 'Type of device taking the measurement'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &devicemeasurement_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
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
    measurementType:    
      description: 'The type of measurement to be taken'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    numValue:    
      description: 'Numerical value of the measurement'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    outlier:    
      description: 'Value for marking the measurement to be specially processed'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *devicemeasurement_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Device taking the measurement'    
      x-ngsi:    
        type: Relationship    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    textValue:    
      description: 'Textual value of the measurement'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. It has to be Measurement'    
      enum:    
        - DeviceMeasurement    
      type: string    
      x-ngsi:    
        type: Property    
    unit:    
      description: 'Units of the measurement. In case of use of an acronym use units accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  version: 0.1.0    
```  
</details>    
## Ejemplo de carga útil  
#### DeviceMeasurement NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un DeviceMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:MEASUREMENT:id:PMZY:77452386",  
  "dateCreated": "2021-09-03T07:33:18Z",  
  "dateModified": "2021-09-03T07:33:18Z",  
  "source": "Datacenter",  
  "name": "Simple measurement",  
  "alternateName": "",  
  "description": "DAta center measurement values",  
  "dataProvider": "",  
  "owner": [  
    "urn:ngsi-ld:MEASUREMENT:seeAlso:owner:00001"  
  ],  
  "seeAlso": [  
    "urn:ngsi-ld:MEASUREMENT:seeAlso:ZMHH:32977"  
  ],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      60.170833,  
      24.9375  
    ]  
  },  
  "address": {  
    "streetAddress": "Pohjoisesplanadi 11-13 ",  
    "addressLocality": "Helsinki",  
    "addressRegion": "Helsinki",  
    "addressCountry": "Finland",  
    "postalCode": "00099",  
    "postOfficeBoxNumber": "1"  
  },  
  "areaServed": "Helsinki council",  
  "type": "DeviceMeasurement",  
  "numValue": 55.2,  
  "textValue": "",  
  "controlledProperty": "humidity",  
  "refDevice": "urn:ngsi-ld:MEASUREMENT:refDevice:ZMHH:32871158",  
  "deviceType": "sensor",  
  "measurementType": "FillingLevelSensor",  
  "dateObserved": "2021-09-03T07:33:18Z",  
  "outlier": true,  
  "unit": "UDT0000016"  
}  
```  
#### DeviceMeasurement NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un DeviceMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:MEASUREMENT:id:PMZY:77452386",  
  "type": "DeviceMeasurement",  
  "dateCreated": {  
    "type": "string",  
    "value": "2021-09-03T07:33:18Z"  
  },  
  "dateModified": {  
    "type": "string",  
    "value": "2021-09-03T07:33:18Z"  
  },  
  "source": {  
    "type": "string",  
    "value": "Datacenter"  
  },  
  "name": {  
    "type": "string",  
    "value": "Simple measurement"  
  },  
  "alternateName": {  
    "type": "string",  
    "value": ""  
  },  
  "description": {  
    "type": "string",  
    "value": "DAta center measurement values"  
  },  
  "dataProvider": {  
    "type": "string",  
    "value": ""  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
    ]  
  },  
  "seeAlso": {  
    "type": "array",  
    "value": [  
    ]  
  },  
  "location": {  
    "type": "object",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        60.170833,  
        24.9375  
      ]  
    }  
  },  
  "address": {  
    "type": "object",  
    "value": {  
      "streetAddress": "Pohjoisesplanadi 11-13 ",  
      "addressLocality": "Helsinki",  
      "addressRegion": "Helsinki",  
      "addressCountry": "Finland",  
      "postalCode": "00099",  
      "postOfficeBoxNumber": "1"  
    }  
  },  
  "areaServed": {  
    "type": "string",  
    "value": "Helsinki council"  
  },  
  "numValue": {  
    "type": "Number",  
    "value": 55.2  
  },  
  "textValue": {  
    "type": "string",  
    "value": ""  
  },  
  "controlledProperty": {  
    "type": "string",  
    "value": "humidity"  
  },  
  "refDevice": {  
    "type": "string",  
    "value": "urn:ngsi-ld:MEASUREMENT:refDevice:ZMHH:32871158"  
  },  
  "deviceType": {  
    "type": "string",  
    "value": "sensor"  
  },  
  "measurementType": {  
    "type": "string",  
    "value": "FillingLevelSensor"  
  },  
  "dateObserved": {  
    "type": "string",  
    "value": "2021-09-03T07:33:18Z"  
  },  
  "outlier": {  
    "type": "Boolean",  
    "value": true  
  },  
  "unit": {  
    "type": "string",  
    "value": "UDT0000016"  
  }  
}  
```  
#### DeviceMeasurement NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un DeviceMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:MEASUREMENT:id:PMZY:77452386",  
  "dateCreated": "2021-09-03T07:33:18Z",  
  "dateModified": "2021-09-03T07:33:18Z",  
  "source": "Datacenter",  
  "name": "Simple measurement",  
  "alternateName": "",  
  "description": "DAta center measurement values",  
  "dataProvider": "",  
  "owner": [],  
  "seeAlso": [],  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      60.170833,  
      24.9375  
    ]  
  },  
  "address": {  
    "streetAddress": "Pohjoisesplanadi 11-13 ",  
    "addressLocality": "Helsinki",  
    "addressRegion": "Helsinki",  
    "addressCountry": "Finland",  
    "postalCode": "00099",  
    "postOfficeBoxNumber": "1"  
  },  
  "areaServed": "Helsinki council",  
  "type": "DeviceMeasurement",  
  "numValue": 55.2,  
  "textValue": "",  
  "controlledProperty": "humidity",  
  "refDevice": "urn:ngsi-ld:MEASUREMENT:refDevice:ZMHH:32871158",  
  "deviceType": "sensor",  
  "measurementType": "FillingLevelSensor",  
  "dateObserved": "2021-09-03T07:33:18Z",  
  "outlier": true,  
  "unit": "UDT0000016",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### DeviceMeasurement NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un DeviceMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:MEASUREMENT:id:PMZY:77452386",  
  "type": "DeviceMeasurement",  
  "dateCreated": {  
    "type": "Property",  
    "value": "2021-09-03T07:33:18Z"  
  },  
  "dateModified": {  
    "type": "Property",  
    "value": "2021-09-03T07:33:18Z"  
  },  
  "source": {  
    "type": "Property",  
    "value": "Datacenter"  
  },  
  "name": {  
    "type": "Property",  
    "value": "Simple measurement"  
  },  
  "alternateName": {  
    "type": "Property",  
    "value": ""  
  },  
  "description": {  
    "type": "Property",  
    "value": "DAta center measurement values"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": ""  
  },  
  "owner": {  
    "type": "Property",  
    "value": []  
  },  
  "seeAlso": {  
    "type": "Property",  
    "value": []  
  },  
  "location": {  
    "type": "Property",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        60.170833,  
        24.9375  
      ]  
    }  
  },  
  "address": {  
    "type": "Property",  
    "value": {  
      "streetAddress": "Pohjoisesplanadi 11-13 ",  
      "addressLocality": "Helsinki",  
      "addressRegion": "Helsinki",  
      "addressCountry": "Finland",  
      "postalCode": "00099",  
      "postOfficeBoxNumber": "1"  
    }  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "Helsinki council"  
  },  
  "numValue": {  
    "type": "Property",  
    "value": 55.2  
  },  
  "textValue": {  
    "type": "Property",  
    "value": ""  
  },  
  "controlledProperty": {  
    "type": "Property",  
    "value": "humidity"  
  },  
  "refDevice": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:MEASUREMENT:refDevice:ZMHH:32871158"  
  },  
  "deviceType": {  
    "type": "Property",  
    "value": "sensor"  
  },  
  "measurementType": {  
    "type": "Property",  
    "value": "FillingLevelSensor"  
  },  
  "dateObserved": {  
    "type": "Property",  
    "value": "2021-09-03T07:33:18Z"  
  },  
  "outlier": {  
    "type": "Property",  
    "value": true  
  },  
  "unit": {  
    "type": "Property",  
    "value": "UDT0000016"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud