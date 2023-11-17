<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: Cámara    
===============<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.Device/blob/master/Camera/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Un modelo de datos para instalaciones de cámaras en una ciudad.**    
versión: 0.1.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `cameraName[string]`: Nombre de la cámara correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `cameraNum[number]`: Número de cámara correspondiente a esta observación  . Model: [https://schema.org/Number](https://schema.org/Number)- `cameraOrientation[object]`: Información sobre la orientación de la cámara correspondiente a esta observación  	- `annotatedMap`:       
- `cameraType[string]`: Tipo de cámara correspondiente a esta observación. Enum:'FIJA, PTZ, DOMO, DÍA/NOCHE, C-MOUNT, BULLET'  . Model: [https://schema.org/Text](https://schema.org/Text)- `cameraUsage[string]`: Finalidad de la cámara correspondiente a esta observación. Enum: [VIGILANCIA, RLVD, ANPR/LPR, TRÁFICO]  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `endDateTime[date-time]`: Hora final notificada correspondiente a esta observación  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `id[*]`: Identificador único de la entidad  - `imageSnapshot[string]`: Enlace de descarga de la instantánea de la cámara correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `mediaURL[uri]`: URL que proporcione más información de cualquier imagen o medios de comunicación de la denuncia o el lugar  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo  - `on[boolean]`: Indica si el dispositivo está encendido (true) o apagado (false)  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startDateTime[date-time]`: Hora de inicio comunicada correspondiente a esta observación  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `streamName[string]`: Nombre del flujo de vídeo de la cámara correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `streamURL[string]`: URL que proporciona información de flujo de vídeo para la cámara correspondiente a esta observación  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI. Tiene que ser Cámara  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
Camera:      
  description: A Data Model for camera installations in a city.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    cameraName:      
      description: Name of the camera corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    cameraNum:      
      description: Camera number corresponding to this observation      
      type: number      
      x-ngsi:      
        model: https://schema.org/Number      
        type: Property      
    cameraOrientation:      
      description: Orientation information for the camera corresponding to this observation      
      properties:      
        annotatedMap:      
          format: uri      
          type: string      
        comments:      
          type: string      
      type: object      
      x-ngsi:      
        type: Property      
    cameraType:      
      description: 'Type of the camera corresponding to this observation. Enum:''FIXED, PTZ, DOME, DAY/NIGHT, C-MOUNT, BULLET'''      
      enum:      
        - FIXED      
        - PTZ      
        - DOME      
        - DAY/NIGHT      
        - C-MOUNT      
        - BULLET      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    cameraUsage:      
      description: 'Purpose of the camera corresponding to this observation. Enum: [SURVEILLANCE, RLVD, ANPR/LPR, TRAFFIC]'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    endDateTime:      
      description: Reported end time corresponding to this observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    imageSnapshot:      
      description: Camera feed snapshot download link for the camera corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    mediaURL:      
      description: URL providing further information of any image(s) or media of the complaint or place      
      format: uri      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    on:      
      description: Indicates if the device is on (true) or off (false)      
      type: boolean      
      x-ngsi:      
        model: https://schema.org/Boolean      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    startDateTime:      
      description: Reported start time corresponding to this observation      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    streamName:      
      description: Name of the video stream from the camera corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    streamURL:      
      description: URL providing video streaming information for the camera corresponding to this observation      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI entity type. It has to be Camera      
      enum:      
        - Camera      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/Camera/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/CrossSector/Camera/schema.json      
  x-model-tags: ""      
  x-version: 0.1.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### Cámara NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de una Cámara en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Camera:Cam2",  
  "type": "Camera",  
  "cameraName": "Cam2",  
  "streamURL": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing",  
  "cameraUsage": "SURVEILLANCE",  
  "cameraType": "FIXED",  
  "endDateTime": "2021-05-11T06:35:20.065Z",  
  "startDateTime": "2021-05-11T06:30:00.020Z",  
  "cameraOrientation": {  
    "comments": "Camera facing RSBhawan",  
    "annotatedMap": "https://drive.google.com/file/d/1RXDGogU5UMmzRppqFaNKTzcr69Kl0wjb/view?usp=sharing"  
  },  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      91.28076,  
      23.831796  
    ]  
  },  
  "cameraNum": 2,  
  "on": true,  
  "imageSnapshot": "https://drive.google.com/file/d/1cLMYzvbaciGcRRD0HV3MAoK4XbNkOukr/view?usp=sharing",  
  "streamName": "Agartala_OrientChowmuhani_Surv_Fixed_RSBhawan_Cam2",  
  "mediaURL": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing"  
}  
```  
</details>    
#### Cámara NGSI-v2 normalizada Ejemplo    
He aquí un ejemplo de una Cámara en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Smart Data Models-Camera",  
  "type": "Camera",  
  "cameraName": {  
    "type": "Text",  
    "value": "Cam2"  
  },  
  "streamURL": {  
    "type": "Text",  
    "value": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing"  
  },  
  "cameraUsage": {  
    "type": "Text",  
    "value": "SURVEILLANCE"  
  },  
  "cameraType": {  
    "type": "Text",  
    "value": "FIXED"  
  },  
  "startDateTime": {  
    "type": "DateTime",  
    "value": "2021-05-11T06:30:00.020Z"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        23.831796,  
        91.28076  
      ]  
    }  
  },  
  "cameraOrientation": {  
    "type": "StructuredValue",  
    "value": {  
      "comments": "Camera facing RSBhawan",  
      "annotatedMap": "https://drive.google.com/file/d/1RXDGogU5UMmzRppqFaNKTzcr69Kl0wjb/view?usp=sharing"  
    }  
  },  
  "endDateTime": {  
    "type": "DateTime",  
    "value": "2021-05-11T06:35:20.065Z"  
  },  
  "cameraNum": {  
    "type": "Number",  
    "value": 2  
  },  
  "imageSnapshot": {  
    "type": "Text",  
    "value": "https://drive.google.com/file/d/1cLMYzvbaciGcRRD0HV3MAoK4XbNkOukr/view?usp=sharing"  
  },  
  "streamName": {  
    "type": "Text",  
    "value": "Agartala_OrientChowmuhani_Surv_Fixed_RSBhawan_Cam2"  
  },  
  "mediaURL": {  
    "type": "Text",  
    "value": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing"  
  },  
  "on": {  
    "type": "Boolean",  
    "value": true  
  }  
}  
```  
</details>    
#### Cámara NGSI-LD key-values Ejemplo    
He aquí un ejemplo de Cámara en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Camera:Cam2",  
  "type": "Camera",  
  "cameraName": "Cam2",  
  "cameraNum": 2,  
  "cameraOrientation": {  
    "comments": "Camera facing RSBhawan",  
    "annotatedMap": "https://drive.google.com/file/d/1RXDGogU5UMmzRppqFaNKTzcr69Kl0wjb/view?usp=sharing"  
  },  
  "cameraType": "FIXED",  
  "cameraUsage": "SURVEILLANCE",  
  "endDateTime": "2021-05-11T06:35:20.065Z",  
  "imageSnapshot": "https://drive.google.com/file/d/1cLMYzvbaciGcRRD0HV3MAoK4XbNkOukr/view?usp=sharing",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      91.28076,  
      23.831796  
    ]  
  },  
  "mediaURL": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing",  
  "startDateTime": "2021-05-11T06:30:00.020Z",  
  "streamName": "Agartala_OrientChowmuhani_Surv_Fixed_RSBhawan_Cam2",  
  "streamURL": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing",  
  "on": true,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### Cámara NGSI-LD normalizada Ejemplo    
He aquí un ejemplo de una Cámara en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Smart-Data-Models-Camera",  
  "type": "Camera",  
  "cameraName": {  
    "type": "Property",  
    "value": "Cam2"  
  },  
  "cameraNum": {  
    "type": "Property",  
    "value": 2  
  },  
  "cameraOrientation": {  
    "type": "Property",  
    "value": {  
      "comments": "Camera facing RSBhawan",  
      "annotatedMap": "https://drive.google.com/file/d/1RXDGogU5UMmzRppqFaNKTzcr69Kl0wjb/view?usp=sharing"  
    }  
  },  
  "cameraType": {  
    "type": "Property",  
    "value": "FIXED"  
  },  
  "cameraUsage": {  
    "type": "Property",  
    "value": "SURVEILLANCE"  
  },  
  "endDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-05-11T06:35:20.065Z"  
    }  
  },  
  "imageSnapshot": {  
    "type": "Property",  
    "value": "https://drive.google.com/file/d/1cLMYzvbaciGcRRD0HV3MAoK4XbNkOukr/view?usp=sharing"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        23.831796,  
        81.28076  
      ]  
    }  
  },  
  "mediaURL": {  
    "type": "Property",  
    "value": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing"  
  },  
  "startDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "Datetime",  
      "@value": "2021-05-11T06:30:00.020Z"  
    }  
  },  
  "streamName": {  
    "type": "Property",  
    "value": "Agartala_OrientChowmuhani_Surv_Fixed_RSBhawan_Cam2"  
  },  
  "streamURL": {  
    "type": "Property",  
    "value": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing"  
  },  
  "on": {  
    "type": "Property",  
    "value": true  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
