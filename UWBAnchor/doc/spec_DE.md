<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: UWBAnchor  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Device/blob/master/UWBAnchor/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Datenmodell für den Ultra Wideband (UWB)-Anker, d.h. elektronische Geräte, die die von den UWB-Tags ausgesendeten UWB-Impulse erkennen und an den Ortungsserver weiterleiten, um die Position der Tags zu berechnen**.  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `data[object]`: Entsprechende Daten des UWB-Ankers.  	- `anchorData[array]`: Informationen zu den Ankerdaten.    
	- `coordinates[object]`: Koordinaten-Daten.    
	- `metrics[object]`: Metrische Daten.    
	- `moving[boolean]`: Umzugsstatus.    
	- `tagData[object]`: Informationen zu den Tag-Daten.    
	- `zones[array]`: Informationen zu den Zonen.    
- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `success[boolean]`: Erfolgsstatus.  - `tagId[string]`: Tag ID.  - `timestamp[number]`: Zeitstempel der Daten.  - `type[string]`: NGSI-Entitätstyp. Es muss UWBAnchor sein  - `version[string]`: Version der Daten.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `tagId`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### UWBAnchor NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen UWBAnchor im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### UWBAnchor NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen UWBAnchor im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### UWBAnchor NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen UWBAnchor im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### UWBAnchor NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen UWBAnchor im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
