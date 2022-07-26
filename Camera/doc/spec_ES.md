[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: Cámara  
===============  
[Licencia abierta](https://github.com/smart-data-models//dataModel.Device/blob/master/Camera/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descripción global: **Un modelo de datos para las instalaciones de cámaras en una ciudad.**  
versión: 0.1.1  

## Lista de propiedades  

- `address`: La dirección postal  - `alternateName`: Un nombre alternativo para este artículo  - `areaServed`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  - `cameraName`: Nombre de la cámara correspondiente a esta observación.  - `cameraNum`: Número de cámara correspondiente a esta observación.  - `cameraOrientation`: Información sobre la orientación de la cámara correspondiente a esta observación  - `cameraType`: Tipo de cámara correspondiente a esta observación. Enum:'FIXED, PTZ, DOME, DAY/NIGHT, C-MOUNT, BULLET'.  - `cameraUsage`: Finalidad de la cámara correspondiente a esta observación. Enum: [VIGILANCIA, RLVD, ANPR/LPR].  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `endDateTime`: Hora de finalización comunicada correspondiente a esta observación.  - `id`: Identificador único de la entidad  - `imageSnapshot`: Enlace de descarga de la instantánea de la cámara correspondiente a esta observación  - `location`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `mediaURL`: URL que proporciona más información de cualquier imagen o medio de comunicación de la denuncia o el lugar.  - `name`: El nombre de este artículo.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `startDateTime`: Hora de inicio informada correspondiente a esta observación.  - `streamName`: Nombre del flujo de vídeo de la cámara correspondiente a esta observación  - `streamURL`: URL que proporciona información de transmisión de vídeo para la cámara correspondiente a esta observación  - `type`: Tipo de entidad NGSI. Tiene que ser Cámara    
Propiedades requeridas  
- `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Camera:    
  description: 'A Data Model for camera installations in a city.'    
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
    cameraName:    
      description: 'Name of the camera corresponding to this observation.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    cameraNum:    
      description: 'Camera number corresponding to this observation.'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    cameraOrientation:    
      description: 'Orientation information for the camera corresponding to this observation'    
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
      description: 'Type of the camera corresponding to this observation. Enum:''FIXED, PTZ, DOME, DAY/NIGHT, C-MOUNT, BULLET''.'    
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
      description: 'Purpose of the camera corresponding to this observation. Enum: [SURVEILLANCE, RLVD, ANPR/LPR].'    
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
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    endDateTime:    
      description: 'Reported end time corresponding to this observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    id:    
      anyOf: &camera_-_properties_-_owner_-_items_-_anyof    
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
    imageSnapshot:    
      description: 'Camera feed snapshot download link for the camera corresponding to this observation'    
      type: string    
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
    mediaURL:    
      description: 'URL providing further information of any image(s) or media of the complaint or place.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *camera_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
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
    startDateTime:    
      description: 'Reported start time corresponding to this observation.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    streamName:    
      description: 'Name of the video stream from the camera corresponding to this observation'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    streamURL:    
      description: 'URL providing video streaming information for the camera corresponding to this observation'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be Camera'    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/Camera/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/CrossSector/Camera/schema.json    
  x-model-tags: ""    
  x-version: 0.1.1    
```  
</details>    
## Ejemplo de carga útil  
#### Cámara NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una Cámara en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
  "imageSnapshot": "https://drive.google.com/file/d/1cLMYzvbaciGcRRD0HV3MAoK4XbNkOukr/view?usp=sharing",  
  "streamName": "Agartala_OrientChowmuhani_Surv_Fixed_RSBhawan_Cam2",  
  "mediaURL": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing"  
}  
```  
#### Cámara NGSI-v2 normalizada Ejemplo  
He aquí un ejemplo de una cámara en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
    "type": "Property",  
    "value": {  
      "@type": "Datetime",  
      "@value": "2021-05-11T06:30:00.020Z"  
    }  
  },  
  "location": {  
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        23.831796,  
        91.28076  
      ]  
    }  
  },  
  "cameraOrientation": {  
    "type": "Property",  
    "value": {  
      "comments": "Camera facing RSBhawan",  
      "annotatedMap": "https://drive.google.com/file/d/1RXDGogU5UMmzRppqFaNKTzcr69Kl0wjb/view?usp=sharing"  
    }  
  },  
  "endDateTime": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-05-11T06:35:20.065Z"  
    }  
  },  
  "cameraNum": {  
    "type": "Property",  
    "value": 2  
  },  
  "imageSnapshot": {  
    "type": "Property",  
    "value": "https://drive.google.com/file/d/1cLMYzvbaciGcRRD0HV3MAoK4XbNkOukr/view?usp=sharing"  
  },  
  "streamName": {  
    "type": "Property",  
    "value": "Agartala_OrientChowmuhani_Surv_Fixed_RSBhawan_Cam2"  
  },  
  "mediaURL": {  
    "type": "Property",  
    "value": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### Cámara NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una Cámara en formato JSON-LD como valores-clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
#### Cámara NGSI-LD normalizada Ejemplo  
He aquí un ejemplo de una cámara en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:Smart Data Models-Camera",  
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
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                23.831796,  
                91.28076  
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
    "@context": []  
}  
```  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
