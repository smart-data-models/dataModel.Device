<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : PolarH10  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Device/blob/master/PolarH10/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Modèle de données du capteur de fréquence cardiaque Polar H10 avec RR, VRC, FC et ECG**.  
version : 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `acc[array]`: Données de l'accéléromètre avec des taux d'échantillonnage de 25Hz, 50Hz, 100Hz et 200Hz et une gamme de 2G, 4G et 8G. Données d'accélération spécifiques à l'axe en mG.  - `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.    
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Numéro identifiant une propriété spécifique sur une voie publique    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientId[string]`: Identifiant du client  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `deviceId[string]`: ID de l'appareil  - `ecg[array]`: Données d'électrocardiographie (ECG) en µV avec une fréquence d'échantillonnage de 130 Hz.  - `hr[number]`: Fréquence cardiaque (FC) avec un temps d'échantillonnage d'une seconde ou avec un temps d'échantillonnage de cinq secondes  - `hrv[number]`: Variabilité de la fréquence cardiaque (VFC) Variabilité de la fréquence cardiaque  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `sampleRate[number]`: Taux d'acquisition des données  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `sensorTimeStamp[number]`: Horodatage du capteur  - `sessionId[number]`: ID de la session  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `timeStamp[number]`: Horodatage du téléphone  - `type[string]`: Type d'entité NGSI. Il doit s'agir de PolarH10TopicACC  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### PolarH10 NGSI-v2 valeurs-clés Exemple  
Voici un exemple de PolarH10 au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### PolarH10 NGSI-v2 normalisé Exemple  
Voici un exemple de PolarH10 au format JSON-LD tel que normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### PolarH10 Valeurs clés NGSI-LD Exemple  
Voici un exemple de PolarH10 au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### PolarH10 NGSI-LD normalisé Exemple  
Voici un exemple de PolarH10 au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
