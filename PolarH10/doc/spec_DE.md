<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: PolarH10  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Device/blob/master/PolarH10/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Ein Datenmodell des Polar H10 Herzfrequenz-Sensors mit RR, HRV, HR und EKG**  
Version: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `acc[array]`: Beschleunigungsmessdaten mit Abtastraten von 25Hz, 50Hz, 100Hz und 200Hz und einem Bereich von 2G, 4G und 8G. Achsenspezifische Beschleunigungsdaten in mG.  - `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Das Land. Zum Beispiel, Spanien  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: Die Ortschaft, in der sich die Adresse befindet, und die in der Region liegt  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: Die Region, in der sich der Ort befindet, und die auf dem Land liegt  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Ein Bezirk ist eine Art von Verwaltungseinheit, die in einigen Ländern von der lokalen Regierung verwaltet wird.    
	- `postOfficeBoxNumber[string]`: Die Postfachnummer für Postfachadressen. Zum Beispiel, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Die Postleitzahl. Zum Beispiel, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: Die Straßenanschrift  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Nummer zur Identifizierung eines bestimmten Grundstücks an einer öffentlichen Straße    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientId[string]`: Kunden-ID  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `deviceId[string]`: Geräte-ID  - `ecg[array]`: Elektrokardiographie (EKG)-Daten in µV mit einer Abtastrate von 130 Hz.  - `hr[number]`: Herzfrequenz (HR) mit einer Sekunde Abtastzeit oder mit fünf Sekunden Abtastzeit  - `hrv[number]`: Herzfrequenzvariabilität (HRV) Herzfrequenzvariabilität  - `id[*]`: Eindeutiger Bezeichner der Entität  - `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `rr[array]`: Intervalle zwischen aufeinanderfolgenden Herzschlägen (RR) in ms  - `sampleRate[number]`: Datenerfassungsrate  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `sensorTimeStamp[number]`: Sensor Zeitstempel  - `sessionId[number]`: Sitzungs-ID  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der vollständig qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `timeStamp[number]`: Telefon Zeitstempel  - `type[string]`: NGSI-Entitätstyp. Es muss PolarH10TopicACC sein.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### PolarH10 NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen PolarH10 im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### PolarH10 NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen PolarH10 im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### PolarH10 NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für einen PolarH10 im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### PolarH10 NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein PolarH10 im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
