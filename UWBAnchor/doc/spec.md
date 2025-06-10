<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: UWBAnchor  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.Device/blob/master/UWBAnchor/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Data model for the Ultra Wideband (UWB) Anchor which are electronic devices that detect UWB pulses emitted by UWB Tags and forward them to the location server for calculating tag positions.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `data[object]`: Corresponding data of the UWB Anchor.  	- `anchorData[array]`: Anchor data information.    
	- `coordinates[object]`: Coordinates data.    
	- `metrics[object]`: Metrics data.    
	- `moving[boolean]`: Moving status.    
	- `tagData[object]`: Tag data information.    
	- `zones[array]`: Zones information.    
- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `success[boolean]`: Success status.  - `tagId[string]`: Tag ID.  - `timestamp[number]`: Timestamp of the data.  - `type[string]`: NGSI entity type. It has to be UWBAnchor  - `version[string]`: Version of the data.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `tagId`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
UWBAnchor:    
  description: Data model for the Ultra Wideband (UWB) Anchor which are electronic devices that detect UWB pulses emitted by UWB Tags and forward them to the location server for calculating tag positions.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    data:    
      description: Corresponding data of the UWB Anchor.    
      properties:    
        anchorData:    
          description: Anchor data information.    
          items:    
            properties:    
              anchorId:    
                description: Anchor ID.    
                type: string    
                x-ngsi:    
                  type: Property    
              rss:    
                description: RSS value.    
                type: number    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
        coordinates:    
          description: Coordinates data.    
          properties:    
            x:    
              description: X-axis reading.    
              type: number    
              x-ngsi:    
                type: Property    
            y:    
              description: Y-axis reading.    
              type: number    
              x-ngsi:    
                type: Property    
            z:    
              description: Z-axis reading.    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        metrics:    
          description: Metrics data.    
          properties:    
            latency:    
              description: Latency value.    
              type: number    
              x-ngsi:    
                type: Property    
            rates:    
              description: Rates data.    
              properties:    
                success:    
                  description: Success rate.    
                  type: number    
                  x-ngsi:    
                    type: Property    
                update:    
                  description: Update rate.    
                  type: number    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        moving:    
          description: Moving status.    
          type: boolean    
          x-ngsi:    
            type: Property    
        tagData:    
          description: Tag data information.    
          properties:    
            accelerometer:    
              description: Accelerometer readings.    
              items:    
                description: Each of the accelaration measurements in X, Y, and Z-axis    
                properties:    
                  x:    
                    description: X-axis reading.    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  y:    
                    description: Y-axis reading.    
                    type: number    
                    x-ngsi:    
                      type: Property    
                  z:    
                    description: Z-axis reading.    
                    type: number    
                    x-ngsi:    
                      type: Property    
                type: object    
                x-ngsi:    
                  type: Property    
              type: array    
              x-ngsi:    
                type: Property    
            blinkIndex:    
              description: Blink index value.    
              type: number    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        zones:    
          description: Zones information.    
          items:    
            properties:    
              id:    
                description: Zone ID.    
                type: string    
                x-ngsi:    
                  type: Property    
              name:    
                description: Zone name.    
                type: string    
                x-ngsi:    
                  type: Property    
            type: object    
          type: array    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
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
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
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
          type: Relationship    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    success:    
      description: Success status.    
      type: boolean    
      x-ngsi:    
        type: Property    
    tagId:    
      description: Tag ID.    
      type: string    
      x-ngsi:    
        type: Property    
    timestamp:    
      description: Timestamp of the data.    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be UWBAnchor    
      enum:    
        - UWBAnchor    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: Version of the data.    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - id    
    - tagId    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/UWBAnchor/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Aeronautics/UWB/schema.json    
  x-model-tags: P2CODE    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### UWBAnchor NGSI-v2 key-values Example    
Here is an example of a UWBAnchor in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": "0.1",  
    "tagId": "10006789",  
    "timestamp": 1671165464.3779979,  
    "success": true,  
    "data": {  
        "coordinates": {  
            "x": 29340,  
            "y": 69521,  
            "z": 1000  
        },  
        "tagData": {  
            "blinkIndex": 1896215,  
            "accelerometer": [  
                {  
                    "x": 402,  
                    "y": -890,  
                    "z": -27  
                }  
        ]  
        },  
        "anchorData": [  
            {  
                "anchorId": "4678",  
                "rss": -85  
            },  
            {  
                "anchorId": "5565",  
                "rss": -100  
            },  
            {  
                "anchorId": "4589",  
                "rss": -102  
            },  
            {  
                "anchorId": "8902",  
                "rss": -86  
            },  
            {  
                "anchorId": "5470",  
                "rss": -84  
            },  
            {  
                "anchorId": "3497",  
                "rss": -84  
            }  
        ],  
        "metrics": {  
            "latency": 22,  
            "rates": {  
                "success": 1,  
                "update": 1  
            }  
        },  
        "zones": [  
            {  
                "id": "638a0dert89e49ae7jioy8cc",  
                "name": "Office"  
            }  
        ],  
        "moving": false  
    }  
}  
```  
</details>  
#### UWBAnchor NGSI-v2 normalized Example    
Here is an example of a UWBAnchor in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": {  
        "type": "Text",  
        "value": "0.1"  
    },  
    "tagId": {  
        "type": "Text",  
        "value": "10006789"  
    },  
    "timestamp": {  
        "type": "Number",  
        "value": 1671165464.3779979  
    },  
    "success": {  
        "type": "Boolean",  
        "value": true  
    },  
    "data": {  
        "type": "StructuredValue",  
        "value": {  
            "coordinates": {  
                "x": 29340,  
                "y": 69521,  
                "z": 1000  
            },  
            "tagData": {  
                "blinkIndex": 1896215,  
                "accelerometer": [  
                    {  
                        "x": 402,  
                        "y": -890,  
                        "z": -27  
                    }  
                ]  
            },  
            "anchorData": [  
                {  
                    "anchorId": "4678",  
                    "rss": -85  
                },  
                {  
                    "anchorId": "5565",  
                    "rss": -100  
                },  
                {  
                    "anchorId": "4589",  
                    "rss": -102  
                },  
                {  
                    "anchorId": "8902",  
                    "rss": -86  
                },  
                {  
                    "anchorId": "5470",  
                    "rss": -84  
                },  
                {  
                    "anchorId": "3497",  
                    "rss": -84  
                }  
            ],  
            "metrics": {  
                "latency": 22,  
                "rates": {  
                    "success": 1,  
                    "update": 1  
                }  
            },  
            "zones": [  
                {  
                    "id": "638a0dert89e49ae7jioy8cc",  
                    "name": "Office"  
                }  
            ],  
            "moving": false  
        }  
    }  
}  
```  
</details>  
#### UWBAnchor NGSI-LD key-values Example    
Here is an example of a UWBAnchor in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": "0.1",  
    "tagId": "10006789",  
    "timestamp": 1671165464.3779979,  
    "success": true,  
    "data": {  
        "coordinates": {  
            "x": 29340,  
            "y": 69521,  
            "z": 1000  
        },  
        "tagData": {  
            "blinkIndex": 1896215,  
            "accelerometer": [  
                {  
                    "x": 402,  
                    "y": -890,  
                    "z": -27  
                }  
        ]  
        },  
        "anchorData": [  
            {  
                "anchorId": "4678",  
                "rss": -85  
            },  
            {  
                "anchorId": "5565",  
                "rss": -100  
            },  
            {  
                "anchorId": "4589",  
                "rss": -102  
            },  
            {  
                "anchorId": "8902",  
                "rss": -86  
            },  
            {  
                "anchorId": "5470",  
                "rss": -84  
            },  
            {  
                "anchorId": "3497",  
                "rss": -84  
            }  
        ],  
        "metrics": {  
            "latency": 22,  
            "rates": {  
                "success": 1,  
                "update": 1  
            }  
        },  
        "zones": [  
            {  
                "id": "638a0dert89e49ae7jioy8cc",  
                "name": "Office"  
            }  
        ],  
        "moving": false  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Aeronautics/refs/heads/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### UWBAnchor NGSI-LD normalized Example    
Here is an example of a UWBAnchor in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:UWBAnchor:b85e3da145c1",  
    "type": "UWBAnchor",  
    "version": {  
        "type": "Property",  
        "value": "0.1"  
    },  
    "tagId": {  
        "type": "Property",  
        "value": "10006789"  
    },  
    "timestamp": {  
        "type": "Property",  
        "value": 1671165464.3779979  
    },  
    "success": {  
        "type": "Property",  
        "value": true  
    },  
    "data": {  
        "type": "Property",  
        "value": {  
            "coordinates": {  
                "x": 29340,  
                "y": 69521,  
                "z": 1000  
            },  
            "tagData": {  
                "blinkIndex": 1896215,  
                "accelerometer": [  
                    {  
                        "x": 402,  
                        "y": -890,  
                        "z": -27  
                    }  
                ]  
            },  
            "anchorData": [  
                {  
                    "anchorId": "4678",  
                    "rss": -85  
                },  
                {  
                    "anchorId": "5565",  
                    "rss": -100  
                },  
                {  
                    "anchorId": "4589",  
                    "rss": -102  
                },  
                {  
                    "anchorId": "8902",  
                    "rss": -86  
                },  
                {  
                    "anchorId": "5470",  
                    "rss": -84  
                },  
                {  
                    "anchorId": "3497",  
                    "rss": -84  
                }  
            ],  
            "metrics": {  
                "latency": 22,  
                "rates": {  
                    "success": 1,  
                    "update": 1  
                }  
            },  
            "zones": [  
                {  
                    "id": "638a0dert89e49ae7jioy8cc",  
                    "name": "Office"  
                }  
            ],  
            "moving": false  
        }  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Aeronautics/refs/heads/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
