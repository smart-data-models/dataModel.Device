<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: PrivacyObject  
======================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Device/blob/master/PrivacyObject/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Información sobre la privacidad de un dispositivo IoT**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Sensor: Dispositivo que detecta y responde a eventos o cambios en el entorno físico, como la luz, el movimiento o los cambios de temperatura. https://w3id.org/saref#Sensor. Actuador : Dispositivo encargado de mover o controlar un mecanismo o sistema. https://w3id.org/saref#Actuator. Medidor : Dispositivo construido para detectar y mostrar con precisión una cantidad de forma legible por un ser humano. Definido parcialmente por la SAREF. HVAC : Dispositivo de Calefacción, Ventilación y Aire Acondicionado (HVAC) que proporciona confort ambiental en interiores. https://w3id.org/saref#HVAC. Red : Dispositivo utilizado para conectar otros dispositivos en una red, como el concentrador, el conmutador o el router en una red LAN o de sensores. (https://w3id.org/saref#Network. Multimedia : Dispositivo diseñado para mostrar, almacenar, grabar o reproducir contenidos multimedia como audio, imágenes, animación, vídeo. Enum:'actuador, baliza, pistola final, HVAC, implemento, irrSection, irrSystem, medidor, multimedia, red, sensor'  . Model: [https://schema.org/Text](https://schema.org/Text)- `crossborderTransfer[string]`: Indicación sobre la transferencia transfronteriza vinculada a la entidad.  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `floor[number]`: El piso donde se instala el dispositivo cuando está en el edificio o equivalente.  - `id[*]`: Identificador único de la entidad  - `image[string]`: Una imagen del artículo  . Model: [https://schema.org/URL](https://schema.org/URL)- `isIndoor[boolean]`: Bandera para indicar si la entidad está instalada en el interior o en el exterior.  - `isPersonalData[boolean]`: Bandera para indicar si la entidad proporciona o contiene datos personales.  - `legitimateInterest[string]`: Interés legítimo asociado a la entidad. Esto significa para qué finalidad de alto nivel se realiza la recogida de datos.  - `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name[string]`: El nombre de este artículo.  - `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `purpose[string]`: Objetivo de la recogida de datos.  - `recipientList[array]`: Lista que contiene los destinatarios. Un destinatario es el beneficiario que utiliza los datos generados por un sensor. Cada destinatario está representado por un URI que permite su identificación única. Privacidad:'Baja'  . Model: [https://schema.org/URL](https://schema.org/URL)- `refDevice[*]`: Identificador único del conjunto de datos de origen.  - `retentionPeriod[string]`: Período de conservación de los datos.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `type[string]`: Propiedad de tipo NGSI. Tiene que ser PrivacyObject.  - `user[string]`: Identificador de un usuario anónimo. Este identificador es, de hecho, un URN único que puede utilizarse para reconocer de forma anónima a un usuario.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
La entidad PrivacyObject representa un dispositivo IoT (normalmente un sensor) con la información sobre la privacidad directamente vinculada a este dispositivo IoT. Se utilizan varios atributos para describir el dispositivo IoT en el contexto de la privacidad. En particular, un atributo proporciona la ubicación del dispositivo IoT y otros dos dan más información sobre la posición exacta. También se utiliza un atributo para describir el dispositivo IoT y un segundo atributo da el propósito del sensor IoT. Otros atributos están muy centrados en la privacidad y el GDPR con el objetivo de categorizar la información asociada al dispositivo IoT.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PrivacyObject:    
  description: 'Information about privacy for an IoT device'    
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
    crossborderTransfer:    
      description: 'Indication about the crossborder transfer linked to the entity.'    
      type: string    
      x-ngsi:    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    floor:    
      description: 'The floor where the device is installed when in building or equivalent.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &privacyobject_-_properties_-_owner_-_items_-_anyof    
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
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    isIndoor:    
      description: 'Flag to indicate if the entity is installed indoor or outdoor.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isPersonalData:    
      description: 'Flag to indicate if the entity is providing or contains personal data.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    legitimateInterest:    
      description: 'Legitimate interest associated to the entity. This means for which high-level finality the data collection is made.'    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *privacyobject_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    purpose:    
      description: 'Purpose of the data gathering.'    
      type: string    
      x-ngsi:    
        type: Property    
    recipientList:    
      description: 'List containing the recipients. A recipient is the beneficiary using the data generated by a sensor. Each recipient is represented by an URI which allows its unique identification. Privacy:''Low'''    
      items:    
        format: uri    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    refDevice:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Relationship. Device linked to this PrivacyObject entity. Model:''https://schema.org/URL'''    
          format: uri    
          type: string    
      description: 'Unique identifier from the source data set.'    
      x-ngsi:    
        type: Property    
    retentionPeriod:    
      description: 'Period of data retention.'    
      type: string    
      x-ngsi:    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI type property. It has to be PrivacyObject.'    
      enum:    
        - PrivacyObject    
      type: string    
      x-ngsi:    
        type: Property    
    user:    
      description: 'Identifier of an anonymous user. This identifier is in fact a unique URN which can be used to recognize anonymously a user.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/PrivacyObject/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/PrivacyObject/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### PrivacyObject NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un PrivacyObject en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
  "type": "PrivacyObject",  
  "refDevice": "Device:1044_parking",  
  "name": "1004_parking",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      46.18311,  
      6.14132  
    ]  
  },  
  "isIndoor": false,  
  "floor": 0,  
  "description": "Electromagnetic and ultrasonic sensor",  
  "description_fr": "Capteur électromagnétique et à ultrasons",  
  "user": "urn:ngsi-ld:User:abcdef",  
  "purpose": "Detecting the presence of a vehicle on a parking slot.",  
  "purpose_fr": "Détecter la présence d'un véhicule sur une place de parc.",  
  "category": [  
    "sensor"  
  ],  
  "recipientList": [  
    "urn:ngsi-ld:User:CommunalAdministration",  
    "urn:ngsi-ld:User:Motorists"  
  ],  
  "owner": [  
    "ngsi-ld:city:CityofCarouge"  
  ],  
  "isPersonalData": false,  
  "retentionPeriod": "< 1 month",  
  "legitimateInterest": "Facilitate and understand parking habits",  
  "crossborderTransfer": "None",  
  "image": "http://www.example.com/device1.jpg"  
}  
```  
</details>  
#### PrivacyObject NGSI-v2 normalizado Ejemplo  
Este es un ejemplo de un PrivacyObject en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
  "type": "PrivacyObject",  
  "refDevice": {  
    "type": "Relationship",  
    "value": "Device:1044_parking"  
  },  
  "name": {  
    "type": "Text",  
    "value": "1004_parking"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        46.18311,  
        6.14132  
      ]  
    }  
  },  
  "isIndoor": {  
    "type": "Text",  
    "value": "false"  
  },  
  "floor": {  
    "type": "Text",  
    "value": "false"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Electromagnetic and ultrasonic sensor"  
  },  
  "description_fr": {  
    "type": "Text",  
    "value": "Capteur électromagnétique et à ultrasons"  
  },  
  "user": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:User:abcdef"  
  },  
  "purpose": {  
    "type": "Text",  
    "value": "Detecting the presence of a vehicle on a parking slot."  
  },  
  "purpose_fr": {  
    "type": "string",  
    "value": "Détecter la présence d'un véhicule sur une place de parc."  
  },  
  "category": {  
    "type": "array",  
    "value": [  
      "sensor"  
    ]  
  },  
  "recipientList": {  
    "type": "array",  
    "value": [  
      "urn:ngsi-ld:User:CommunalAdministration",  
      "urn:ngsi-ld:User:Motorists"  
    ]  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "ngsi-ld:city:CityofCarouge"  
    ]  
  },  
  "isPersonalData": {  
    "type": "Text",  
    "value": "false"  
  },  
  "retentionPeriod": {  
    "type": "Text",  
    "value": "< 1 month"  
  },  
  "legitimateInterest": {  
    "type": "Text",  
    "value": "Facilitate and understand parking habits"  
  },  
  "crossborderTransfer": {  
    "type": "Text",  
    "value": "None"  
  },  
  "image": {  
    "type": "Text",  
    "value": "http://www.example.com/device1.jpg"  
  }  
}  
```  
</details>  
#### PrivacyObject NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un PrivacyObject en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
    "type": "PrivacyObject",  
    "category": [  
        "sensor"  
    ],  
    "crossborderTransfer": "None",  
    "description": "Electromagnetic and ultrasonic sensor",  
    "description_fr": "Capteur electromagnetique et ultrasons",  
    "floor": 0,  
    "image": "http://www.example.com/device1.jpg",  
    "isIndoor": false,  
    "isPersonalData": false,  
    "legitimateInterest": "Facilitate and understand parking habits",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            46.18311,  
            6.14132  
        ]  
    },  
    "name": "1004_parking",  
    "owner": [  
        "ngsi-ld:city:CityofCarouge"  
    ],  
    "purpose": "Detecting the presence of a vehicle on a parking slot.",  
    "purpose_fr": "Detecter la presence d'un vehicule sur une place de parc.",  
    "recipientList": [  
        "urn:ngsi-ld:User:CommunalAdministration",  
        "urn:ngsi-ld:User:Motorists"  
    ],  
    "refDevice": "Device:1044_parking",  
    "retentionPeriod": "< 1 month",  
    "user": "urn:ngsi-ld:User:abcdef",  
    "@context": [  
        "https://smart-data-models.github.io/data-models/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### PrivacyObject NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un PrivacyObject en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
    "type": "PrivacyObject",  
    "category": {  
        "type": "Property",  
        "value": [  
            "sensor"  
        ]  
    },  
    "crossborderTransfer": {  
        "type": "Property",  
        "value": "None"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Electromagnetic and ultrasonic sensor"  
    },  
    "description_fr": {  
        "type": "Property",  
        "value": "Capteur electromagnetique et ultrasons"  
    },  
    "floor": {  
        "type": "Property",  
        "value": "false"  
    },  
    "image": {  
        "type": "Property",  
        "value": "http://www.example.com/device1.jpg"  
    },  
    "isIndoor": {  
        "type": "Property",  
        "value": "false"  
    },  
    "isPersonalData": {  
        "type": "Property",  
        "value": "false"  
    },  
    "legitimateInterest": {  
        "type": "Property",  
        "value": "Facilitate and understand parking habits"  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                46.18311,  
                6.14132  
            ]  
        }  
    },  
    "name": {  
        "type": "Property",  
        "value": "1004_parking"  
    },  
    "owner": {  
        "type": "Property",  
        "value": [  
            "ngsi-ld:city:CityofCarouge"  
        ]  
    },  
    "purpose": {  
        "type": "Property",  
        "value": "Detecting the presence of a vehicle on a parking slot."  
    },  
    "purpose_fr": {  
        "type": "string",  
        "value": "Detecter la presence d'un vehicule sur une place de parc."  
    },  
    "recipientList": {  
        "type": "Property",  
        "value": [  
            "urn:ngsi-ld:User:CommunalAdministration",  
            "urn:ngsi-ld:User:Motorists"  
        ]  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "value": "Device:1044_parking"  
    },  
    "retentionPeriod": {  
        "type": "Property",  
        "value": "< 1 month"  
    },  
    "user": {  
        "type": "Property",  
        "value": "urn:ngsi-ld:User:abcdef"  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
