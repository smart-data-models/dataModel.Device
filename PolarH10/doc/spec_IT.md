<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: PolarH10  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Device/blob/master/PolarH10/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Modello dati del sensore di frequenza cardiaca Polar H10 con RR, HRV, HR ed ECG**  
versione: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `acc[array]`: Dati dell'accelerometro con frequenze di campionamento di 25Hz, 50Hz, 100Hz e 200Hz e intervallo di 2G, 4G e 8G. Dati di accelerazione specifici dell'asse in mG.  - `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Il paese. Ad esempio, la Spagna  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La località in cui si trova l'indirizzo civico e che si trova nella regione  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La regione in cui si trova la località, e che si trova nel paese  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un distretto è un tipo di divisione amministrativa che, in alcuni Paesi, è gestita dal governo locale.    
	- `postOfficeBoxNumber[string]`: Il numero di casella postale per gli indirizzi di casella postale. Ad esempio, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Il codice postale. Ad esempio, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'indirizzo stradale  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numero che identifica una proprietà specifica su una strada pubblica    
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientId[string]`: ID cliente  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzati  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `deviceId[string]`: ID dispositivo  - `ecg[array]`: Dati elettrocardiografici (ECG) in µV con frequenza di campionamento di 130 Hz.  - `hr[number]`: Frequenza cardiaca (HR) con tempo di campionamento di un secondo o con tempo di campionamento di cinque secondi  - `hrv[number]`: Variabilità della frequenza cardiaca (HRV) variabilità della frequenza cardiaca  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `rr[array]`: Intervalli tra battiti cardiaci successivi (RR) in ms  - `sampleRate[number]`: Velocità di acquisizione dei dati  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sensorTimeStamp[number]`: Timestamp del sensore  - `sessionId[number]`: ID sessione  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `timeStamp[number]`: Timestamp del telefono  - `type[string]`: Tipo di entità NGSI. Deve essere PolarH10TopicACC  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PolarH10:    
  description: A Data Model of Polar H10 Heart Rate Sensor with RR, HRV, HR, and ECG    
  properties:    
    acc:    
      description: Accelerometer data with sample rates of 25Hz, 50Hz, 100Hz and 200Hz and range of 2G, 4G and 8G. Axis specific acceleration data in mG.    
      items:    
        description: Each of the measurement of the accelerometer    
        items:    
          description: Each of the measurement of the accelerometer in the X, Y, Z coordinates    
          type: integer    
          x-ngsi:    
            type: Property    
        maxItems: 3    
        minItems: 3    
        type: array    
        x-ngsi:    
          type: Property    
      maxItems: 36    
      minItems: 36    
      type: array    
      x-ngsi:    
        type: Property    
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
    clientId:    
      description: Client ID    
      type: string    
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
    deviceId:    
      description: Device ID    
      type: string    
      x-ngsi:    
        type: Property    
    ecg:    
      description: Electrocardiography (ECG) data in µV with sample rate 130Hz.    
      items:    
        description: Each of the ECG measurements    
        type: integer    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    hr:    
      description: Heart Rate (HR) with one second sample time or with five second sample time    
      type: number    
      x-ngsi:    
        type: Property    
    hrv:    
      description: Heart Rate Variability (HRV) heart rate variability    
      type: number    
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
    rr:    
      description: Intervals between successive heartbeats (RR) in ms    
      items:    
        description: Each of the measurements of the RR    
        type: integer    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    sampleRate:    
      description: Data acquisition rate    
      type: number    
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
    sensorTimeStamp:    
      description: Sensor Timestamp    
      type: number    
      x-ngsi:    
        type: Property    
    sessionId:    
      description: Session ID    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    timeStamp:    
      description: Phone Timestamp    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be PolarH10TopicACC    
      enum:    
        - PolarH10    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - id    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/PolarH10/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.Device/tree/master/PolarH10/schema.json    
  x-model-tags: P2CODE    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori chiave di PolarH10 NGSI-v2 Esempio  
Ecco un esempio di PolarH10 in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PolarH10:47542370",  
  "type": "PolarH10",  
  "clientId": "user123",  
  "deviceId": "polar-h10-001",  
  "sessionId": 12345,  
  "sampleRate": 100,  
  "timeStamp": 1656633600,  
  "sensorTimeStamp": 1656633601,  
  "acc": [  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 12, 22, 32 ]  
  ],  
  "hr": 75,  
  "hrv": 50.5,  
  "rr": [  
    800,  
    810,  
    820,  
    830,  
    840,  
    850,  
    860,  
    870,  
    880,  
    890  
  ],  
  "ecg": [  
    104,  
    116,  
    116,  
    111,  
    111,  
    92,  
    72,  
    194,  
    478,  
    733,  
    687,  
    199,  
    -267,  
    -153,  
    126,  
    94,  
    41,  
    99,  
    99,  
    97,  
    128,  
    128,  
    133,  
    145,  
    131,  
    138,  
    179,  
    191,  
    179,  
    196,  
    223,  
    216,  
    235,  
    276,  
    289,  
    296,  
    313,  
    303,  
    315,  
    354,  
    352,  
    327,  
    306,  
    264,  
    213,  
    177,  
    140,  
    102,  
    65,  
    41,  
    29,  
    29,  
    41,  
    53,  
    51,  
    38,  
    41,  
    53,  
    63,  
    75,  
    94,  
    89,  
    65,  
    68,  
    85,  
    80,  
    87,  
    99,  
    89,  
    89,  
    109,  
    109,  
    92  
  ]  
}  
```  
</details>  
#### PolarH10 NGSI-v2 normalizzato Esempio  
Ecco un esempio di PolarH10 in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PolarH10:47542370",  
    "type": "PolarH10",  
    "clientId": {  
        "type": "Text",  
        "value": "user123"  
    },  
    "deviceId": {  
        "type": "Text",  
        "value": "polar-h10-001"  
    },  
    "sessionId": {  
        "type": "Number",  
        "value": 12345  
    },  
    "sampleRate": {  
        "type": "Number",  
        "value": 100  
    },  
    "timeStamp": {  
        "type": "Number",  
        "value": 1656633600  
    },  
    "sensorTimeStamp": {  
        "type": "Number",  
        "value": 1656633601  
    },  
    "acc": {  
        "type": "Array",  
        "value": [  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 12, 22, 32 ]  
        ]  
    },  
    "hr": {  
        "type": "Number",  
        "value": 75.5  
    },  
    "hrv": {  
        "type": "Number",  
        "value": 50  
    },  
    "rr": {  
        "type": "Array",  
        "value": [  
            800,  
            810,  
            820,  
            830,  
            840,  
            850,  
            860,  
            870,  
            880,  
            890  
        ]  
    },  
    "ecg": {  
        "type": "Array",  
        "value": [  
            104,  
            116,  
            116,  
            111,  
            111,  
            92,  
            72,  
            194,  
            478,  
            733,  
            687,  
            199,  
            -267,  
            -153,  
            126,  
            94,  
            41,  
            99,  
            99,  
            97,  
            128,  
            128,  
            133,  
            145,  
            131,  
            138,  
            179,  
            191,  
            179,  
            196,  
            223,  
            216,  
            235,  
            276,  
            289,  
            296,  
            313,  
            303,  
            315,  
            354,  
            352,  
            327,  
            306,  
            264,  
            213,  
            177,  
            140,  
            102,  
            65,  
            41,  
            29,  
            29,  
            41,  
            53,  
            51,  
            38,  
            41,  
            53,  
            63,  
            75,  
            94,  
            89,  
            65,  
            68,  
            85,  
            80,  
            87,  
            99,  
            89,  
            89,  
            109,  
            109,  
            92  
        ]  
    }  
}  
```  
</details>  
#### PolarH10 Valori chiave NGSI-LD Esempio  
Ecco un esempio di PolarH10 in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PolarH10:47542370",  
  "type": "PolarH10",  
  "clientId": "user123",  
  "deviceId": "polar-h10-001",  
  "sessionId": 12345,  
  "sampleRate": 100,  
  "timeStamp": 1656633600,  
  "sensorTimeStamp": 1656633601,  
  "acc": [  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 12, 22, 32 ]  
  ],  
  "hr": 75,  
  "hrv": 50.5,  
  "rr": [  
    800,  
    810,  
    820,  
    830,  
    840,  
    850,  
    860,  
    870,  
    880,  
    890  
  ],  
  "ecg": [  
    104,  
    116,  
    116,  
    111,  
    111,  
    92,  
    72,  
    194,  
    478,  
    733,  
    687,  
    199,  
    -267,  
    -153,  
    126,  
    94,  
    41,  
    99,  
    99,  
    97,  
    128,  
    128,  
    133,  
    145,  
    131,  
    138,  
    179,  
    191,  
    179,  
    196,  
    223,  
    216,  
    235,  
    276,  
    289,  
    296,  
    313,  
    303,  
    315,  
    354,  
    352,  
    327,  
    306,  
    264,  
    213,  
    177,  
    140,  
    102,  
    65,  
    41,  
    29,  
    29,  
    41,  
    53,  
    51,  
    38,  
    41,  
    53,  
    63,  
    75,  
    94,  
    89,  
    65,  
    68,  
    85,  
    80,  
    87,  
    99,  
    89,  
    89,  
    109,  
    109,  
    92  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/refs/heads/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PolarH10 NGSI-LD normalizzato Esempio  
Ecco un esempio di PolarH10 in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PolarH10:47542370",  
    "type": "PolarH10",  
    "clientId": {  
        "type": "Property",  
        "value": "user123"  
    },  
    "deviceId": {  
        "type": "Property",  
        "value": "polar-h10-001"  
    },  
    "sessionId": {  
        "type": "Property",  
        "value": 12345  
    },  
    "sampleRate": {  
        "type": "Property",  
        "value": 100  
    },  
    "timeStamp": {  
        "type": "Property",  
        "value": 1656633600  
    },  
    "sensorTimeStamp": {  
        "type": "Property",  
        "value": 1656633601  
    },  
    "acc": {  
        "type": "Property",  
        "value": [  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 12, 22, 32 ]  
        ]  
    },  
    "hr": {  
        "type": "Property",  
        "value": 75.5  
    },  
    "hrv": {  
        "type": "Property",  
        "value": 50  
    },  
    "rr": {  
        "type": "Property",  
        "value": [  
            800,  
            810,  
            820,  
            830,  
            840,  
            850,  
            860,  
            870,  
            880,  
            890  
        ]  
    },  
    "ecg": {  
        "type": "Property",  
        "value": [  
            104,  
            116,  
            116,  
            111,  
            111,  
            92,  
            72,  
            194,  
            478,  
            733,  
            687,  
            199,  
            -267,  
            -153,  
            126,  
            94,  
            41,  
            99,  
            99,  
            97,  
            128,  
            128,  
            133,  
            145,  
            131,  
            138,  
            179,  
            191,  
            179,  
            196,  
            223,  
            216,  
            235,  
            276,  
            289,  
            296,  
            313,  
            303,  
            315,  
            354,  
            352,  
            327,  
            306,  
            264,  
            213,  
            177,  
            140,  
            102,  
            65,  
            41,  
            29,  
            29,  
            41,  
            53,  
            51,  
            38,  
            41,  
            53,  
            63,  
            75,  
            94,  
            89,  
            65,  
            68,  
            85,  
            80,  
            87,  
            99,  
            89,  
            89,  
            109,  
            109,  
            92  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/refs/heads/master/context.jsonld"  
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
