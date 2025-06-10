<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: UWBAnchor  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Device/blob/master/UWBAnchor/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Modello di dati per l'ancoraggio a banda ultra larga (UWB) che è un dispositivo elettronico che rileva gli impulsi UWB emessi dai tag UWB e li inoltra al server di localizzazione per calcolare la posizione dei tag **.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `data[object]`: Dati corrispondenti dell'ancora UWB.  	- `anchorData[array]`: Informazioni sui dati di ancoraggio.    
	- `coordinates[object]`: Dati sulle coordinate.    
	- `metrics[object]`: Dati metrici.    
	- `moving[boolean]`: Stato di avanzamento.    
	- `tagData[object]`: Informazioni sui dati del tag.    
	- `zones[array]`: Informazioni sulle zone.    
- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `success[boolean]`: Stato di successo.  - `tagId[string]`: Tag ID.  - `timestamp[number]`: Timestamp dei dati.  - `type[string]`: Tipo di entità NGSI. Deve essere UWBAnchor  - `version[string]`: Versione dei dati.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `tagId`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### Valori delle chiavi UWBAnchor NGSI-v2 Esempio  
Ecco un esempio di UWBAnchor in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### UWBAnchor NGSI-v2 normalizzato Esempio  
Ecco un esempio di UWBAnchor in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
#### Valori chiave di UWBAnchor NGSI-LD Esempio  
Ecco un esempio di UWBAnchor in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### UWBAnchor NGSI-LD normalizzato Esempio  
Ecco un esempio di UWBAnchor in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
