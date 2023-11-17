<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : DeviceOperation    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceOperation/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Cette entité contient une description harmonisée d'une entité générique de fonctionnement d'un appareil. L'entité de fonctionnement de l'appareil contient des données dynamiques communiquées par un appareil et s'applique donc à tous les segments de l'IdO et aux applications de l'IdO correspondantes**.    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `address[object]`: L'adresse postale  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: Le pays. Par exemple, l'Espagne  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localité dans laquelle se trouve l'adresse postale et qui se trouve dans la région  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La région dans laquelle se trouve la localité et qui se trouve dans le pays  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un district est un type de division administrative qui, dans certains pays, est géré par le gouvernement local.      
	- `postOfficeBoxNumber[string]`: Le numéro de la boîte postale pour les adresses de boîtes postales. Par exemple, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: Le code postal. Par exemple, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: L'adresse de la rue  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `addressedAt[date-time]`: Date à laquelle un événement ou un défaut a été traité ou supprimé.  - `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `device[*]`: Une référence à l'appareil associé pour cette opération d'appareil  - `endedAt[date-time]`: Horodatage de la fin de l'opération  - `id[*]`: Identifiant unique de l'entité  - `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `name[string]`: Le nom de cet élément  - `operationType[string]`: Un choix dans une liste énumérée  . Model: [event, maintenance, fault, installation, upgrade, other](event, maintenance, fault, installation, upgrade, other)- `operator[*]`: Référence à l'opérateur menant l'opération  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `plannedEndAt[date-time]`: Date/heure de fin prévue pour l'opération. Notez qu'il s'agit d'une indication et que l'heure réelle de fin de l'opération peut être antérieure ou postérieure à la date de fin prévue.  - `plannedStartAt[date-time]`: La date et l'heure de début prévues pour l'opération. Notez qu'il s'agit d'une indication et que l'heure réelle de début de l'opération peut être antérieure ou postérieure à l'heure de début prévue.  - `reportedAt[date-time]`: Date à laquelle l'événement/la faute a été signalé(e)  - `result[string]`: Le résultat de l'opération. Enum : "ok, aborted, failed" (ok, abandonné, échoué)  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `startedAt[date-time]`: Date à laquelle l'opération a commencé à être exécutée  - `status[string]`: Un choix dans une liste énumérative décrivant le statut. Enum : "planifié, en cours, terminé, programmé, annulé  - `type[string]`: Identifiant de l'entité NGSI. Il doit s'agir de DeviceOperation  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
<!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Un dispositif est un objet tangible qui contient une certaine logique et qui est producteur et/ou consommateur de données. Un appareil est toujours supposé être capable de communiquer électroniquement par l'intermédiaire d'un réseau. Ce modèle de données a été partiellement développé en coopération avec les opérateurs de téléphonie mobile et la [GSMA] (https://www.gsma.com/iot/iot-big-data/). Ce modèle de données réutilise des concepts provenant de l'[Ontologie SAREF](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf) qui fait partie des normes de l'[ETSI](http://www.etsi.org).    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
DeviceOperation:      
  description: This entity contains a harmonised description of a generic device operation entity. The device operation entity contains dynamic data reported by a device and is therefore applicable to all IoT segments and related IoT applications.      
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
    addressedAt:      
      description: The timestamp when an event or fault was addressed or cleared      
      format: date-time      
      type: string      
      x-ngsi:      
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
    device:      
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
      description: A reference to the associated Device for this device operation      
      x-ngsi:      
        type: Relationship      
    endedAt:      
      description: Timestamp when the operation actually finished      
      format: date-time      
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
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationType:      
      description: A choice from an enumerated list      
      enum:      
        - event      
        - fault      
        - installation      
        - maintenance      
        - other      
        - upgrade      
      type: string      
      x-ngsi:      
        model: 'event, maintenance, fault, installation, upgrade, other'      
        type: Property      
    operator:      
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
      description: Reference to the operator conducting the operation      
      x-ngsi:      
        type: Relationship      
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
    plannedEndAt:      
      description: The planned end date/timestamp for the operation. Note that this is advisory and the actual time the operation finishes may be before or after the planned end      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    plannedStartAt:      
      description: The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    reportedAt:      
      description: Timestamp when the event/ fault was reported      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    result:      
      description: 'The result of the operation. Enum:''ok, aborted, failed'''      
      enum:      
        - aborted      
        - failed      
        - ok      
      type: string      
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
    startedAt:      
      description: Timestamp when the operation actually started to be performed      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    status:      
      description: 'A choice from an enumerated list describing the status. Enum:''planned, ongoing, finished, scheduled, cancelled'''      
      enum:      
        - cancelled      
        - finished      
        - ongoing      
        - planned      
        - scheduled      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity identifier. It has to be DeviceOperation      
      enum:      
        - DeviceOperation      
      type: string      
      x-ngsi:      
        type: Property      
  required: []      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/DeviceOperation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/DeviceOperation/schema.json      
  x-model-tags: GSMA      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### DeviceOperation Valeurs clés NGSI-v2 Exemple    
Voici un exemple de DeviceOperation au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "device": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
  "operationType": "fault",  
  "description": "Backup battery needs replacement",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "ongoing",  
  "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "addressedAt": "2016-08-28T10:18:16Z"  
}  
```  
</details>    
#### DeviceOperation NGSI-v2 normalisé Exemple    
Voici un exemple de DeviceOperation au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "device": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "fault"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Backup battery needs replacement"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "plannedEndAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "status": {  
    "type": "Text",  
    "value": "ongoing"  
  },  
  "operator": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "reportedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "addressedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  }  
}  
```  
</details>    
#### DeviceOperation Valeurs clés NGSI-LD Exemple    
Voici un exemple de DeviceOperation au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "addressedAt": "2016-08-28T10:18:16Z",  
  "dataProvider": "https://provider.example.com",  
  "description": "Backup battery needs replacement",  
  "device": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "fault",  
  "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "result": "ok",  
  "source": "https://source.example.com",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "status": "ongoing",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### DeviceOperation NGSI-LD normalisé Exemple    
Voici un exemple de DeviceOperation au format JSON-LD normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "addressedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Backup battery needs replacement"  
  },  
  "device": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "endedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "operationType": {  
    "type": "Property",  
    "value": "fault"  
  },  
  "operator": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
  },  
  "plannedEndAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "plannedStartAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "reportedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "result": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "startedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "status": {  
    "type": "Property",  
    "value": "ongoing"  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
