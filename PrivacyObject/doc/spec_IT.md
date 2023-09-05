<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: PrivacyObject  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Device/blob/master/PrivacyObject/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Informazioni sulla privacy per un dispositivo IoT**  
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
- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Sensore: Dispositivo che rileva e risponde a eventi o cambiamenti nell'ambiente fisico, come luce, movimento o variazioni di temperatura. https://w3id.org/saref#Sensor. Attuatore: Dispositivo responsabile del movimento o del controllo di un meccanismo o di un sistema. https://w3id.org/saref#Actuator. Misuratore : Dispositivo costruito per rilevare con precisione e visualizzare una quantità in una forma leggibile da un essere umano. Parzialmente definito da SAREF. HVAC : Dispositivo di riscaldamento, ventilazione e condizionamento dell'aria (HVAC) che fornisce il comfort ambientale interno. https://w3id.org/saref#HVAC. Rete : Dispositivo utilizzato per collegare altri dispositivi in una rete, come hub, switch o router in una rete LAN o Sensor. (https://w3id.org/saref#Network. Multimedia : Dispositivo progettato per visualizzare, memorizzare, registrare o riprodurre contenuti multimediali come audio, immagini, animazioni, video. Enum:'attuatore, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. La categoria grezza sarà deprecata. Utilizzare invece deviceCategory per evitare conflitti con altri aqttributi denominati categoria.  . Model: [https://schema.org/Text](https://schema.org/Text)- `crossborderTransfer[string]`: Indicazione del trasferimento transfrontaliero legato all'entità  - `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `floor[number]`: Il piano in cui è installato il dispositivo quando si trova nell'edificio o in un luogo equivalente.  - `id[*]`: Identificatore univoco dell'entità  - `image[uri]`: Un'immagine dell'articolo  . Model: [https://schema.org/URL](https://schema.org/URL)- `isIndoor[boolean]`: Flag per indicare se l'entità è installata all'interno o all'esterno.  - `isPersonalData[boolean]`: Flag per indicare se l'entità sta fornendo o contiene dati personali  - `legitimateInterest[string]`: Interesse legittimo associato all'entità. Ciò significa che la raccolta dei dati viene effettuata per un fine di alto livello.  - `location[*]`: Riferimento geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `name[string]`: Il nome di questo elemento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `purpose[string]`: Scopo della raccolta dati  - `recipientList[array]`: Elenco dei destinatari. Un destinatario è il beneficiario che utilizza i dati generati da un sensore. Ogni destinatario è rappresentato da un URI che ne consente l'identificazione univoca. Privacy:'Bassa'  . Model: [https://schema.org/URL](https://schema.org/URL)- `refDevice[*]`: Identificatore univoco del set di dati di origine  - `retentionPeriod[string]`: Periodo di conservazione dei dati  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Proprietà di tipo NGSI. Deve essere PrivacyObject  - `user[uri]`: Identificatore di un utente anonimo. Questo identificatore è in realtà un URN univoco che può essere utilizzato per riconoscere anonimamente un utente.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
L'entità PrivacyObject rappresenta un dispositivo IoT (tipicamente un sensore) con le informazioni sulla privacy direttamente collegate a questo dispositivo IoT. Diversi attributi sono utilizzati per descrivere il dispositivo IoT nel contesto della privacy. In particolare, un attributo fornisce la posizione del dispositivo IoT e altri due forniscono ulteriori informazioni sulla posizione esatta. Un attributo è utilizzato anche per descrivere il dispositivo IoT e un secondo attributo fornisce lo scopo del sensore IoT. Altri attributi sono incentrati sulla privacy e sul GDPR, con l'obiettivo di categorizzare le informazioni associate al dispositivo IoT.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PrivacyObject:    
  description: Information about privacy for an IoT device    
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
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category"    
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
      description: Indication about the crossborder transfer linked to the entity    
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
    floor:    
      description: The floor where the device is installed when in building or equivalent    
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
        type: Property    
    image:    
      description: An image of the item    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    isIndoor:    
      description: Flag to indicate if the entity is installed indoor or outdoor    
      type: boolean    
      x-ngsi:    
        type: Property    
    isPersonalData:    
      description: Flag to indicate if the entity is providing or contains personal data    
      type: boolean    
      x-ngsi:    
        type: Property    
    legitimateInterest:    
      description: Legitimate interest associated to the entity. This means for which high-level finality the data collection is made    
      type: string    
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
    purpose:    
      description: Purpose of the data gathering    
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
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Device linked to this PrivacyObject entity    
          format: uri    
          type: string    
          x-ngsi:    
            model: https://schema.org/URL    
            type: Relationship    
      description: Unique identifier from the source data set    
      x-ngsi:    
        type: Property    
    retentionPeriod:    
      description: Period of data retention    
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
    type:    
      description: NGSI type property. It has to be PrivacyObject    
      enum:    
        - PrivacyObject    
      type: string    
      x-ngsi:    
        type: Property    
    user:    
      description: Identifier of an anonymous user. This identifier is in fact a unique URN which can be used to recognize anonymously a user    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## Esempi di payload  
#### PrivacyObject NGSI-v2 valori-chiave Esempio  
Ecco un esempio di PrivacyObject in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### PrivacyObject NGSI-v2 normalizzato Esempio  
Ecco un esempio di PrivacyObject in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
    "type": "Geoproperty",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        46.18311,  
        6.14132  
      ]  
    }  
  },  
  "isIndoor": {  
    "type": "Boolean",  
    "value": false  
  },  
  "floor": {  
    "type": "Number",  
    "value": 0  
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
    "type": "Boolean",  
    "value": false  
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
#### PrivacyObject Valori chiave NGSI-LD Esempio  
Ecco un esempio di PrivacyObject in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### PrivacyObject NGSI-LD normalizzato Esempio  
Ecco un esempio di PrivacyObject in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
    "value": 0  
  },  
  "image": {  
    "type": "Property",  
    "value": "http://www.example.com/device1.jpg"  
  },  
  "isIndoor": {  
    "type": "Property",  
    "value": false  
  },  
  "isPersonalData": {  
    "type": "Property",  
    "value": false  
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
    "type": "Property",  
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
    "object": "Device:1044_parking"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
