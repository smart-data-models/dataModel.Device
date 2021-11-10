Entità: DeviceModel  
===================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceModel/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità cattura le proprietà statiche di un dispositivo. **  
versione: 0.0.2  

## Elenco delle proprietà  

- `alternateName`: Un nome alternativo per questa voce  - `annotations`: Annotazioni sull'elemento  - `brandName`: Marchio del dispositivo.  - `category`: Sensore: Un dispositivo che rileva e risponde a eventi o cambiamenti nell'ambiente fisico come la luce, il movimento o i cambiamenti di temperatura. https://w3id.org/saref#Sensor. attuatore : Un dispositivo responsabile del movimento o del controllo di un meccanismo o di un sistema. https://w3id.org/saref#Actuator. Misuratore : Un dispositivo costruito per rilevare accuratamente e visualizzare una quantità in una forma leggibile da un essere umano. Parzialmente definito da SAREF. HVAC : Dispositivo di riscaldamento, ventilazione e condizionamento dell'aria (HVAC) che fornisce il comfort ambientale interno. https://w3id.org/saref#HVAC. Rete : Un dispositivo utilizzato per collegare altri dispositivi in una rete, come hub, switch o router in una rete LAN o di sensori. (https://w3id.org/saref#Network. Multimediale: Un dispositivo progettato per visualizzare, memorizzare, registrare o riprodurre contenuti multimediali come audio, immagini, animazione, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'  - `color`: Il colore del prodotto  - `controlledProperty`: Qualsiasi cosa che può essere percepita, misurata o controllata da. Enum:'airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `deviceClass`: Classe di dispositivo vincolato come specificato da RFC 7228. Se il dispositivo non è un dispositivo vincolato, questa proprietà non deve essere presente. Riferimenti normativi: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'.  - `documentation`: Un link alla documentazione del dispositivo.  - `energyLimitationClass`: Classe di limitazione dell'energia del dispositivo secondo RFC 7228. Riferimenti normativi: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum: "E0, E1, E2, E9".  - `function`: La funzionalità necessaria per realizzare il compito per il quale un dispositivo è progettato. Un dispositivo può essere progettato per eseguire più di una funzione. Definito da [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification  - `id`: Identificatore unico dell'entità  - `image`: Un'immagine dell'oggetto  - `macAddress`: L'indirizzo MAC del dispositivo.  - `manufacturerName`: Nome del produttore del dispositivo.  - `modelName`: Nome del modello del dispositivo.  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `supportedProtocol`: Protocollo/i o reti supportate  - `supportedUnits`: Unità di misura supportate dal dispositivo. Il codice dell'unità (testo) di misura dato usando il [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 caratteri).  - `type`: Tipo di entità NGSI. deve essere DeviceModel    
Proprietà richieste  
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DeviceModel:    
  description: 'This entity captures the static properties of a Device. '    
  modelTags: ""    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: 'Device''s brand name.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    category:    
      description: "Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'"    
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
    color:    
      description: 'The color of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/color    
        type: Property    
    controlledProperty:    
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'''    
      items:    
        enum:    
          - airPollution    
          - atmosphericPressure    
          - averageVelocity    
          - batteryLife    
          - batterySupply    
          - cdom    
          - conductance    
          - conductivity    
          - depth    
          - eatingActivity    
          - electricityConsumption    
          - energy    
          - fillingLevel    
          - freeChlorine    
          - gasConsumption    
          - gateOpening    
          - heading    
          - humidity    
          - light    
          - location    
          - milking    
          - motion    
          - movementActivity    
          - noiseLevel    
          - occupancy    
          - orp    
          - pH    
          - power    
          - precipitation    
          - pressure    
          - refractiveIndex    
          - salinity    
          - smoke    
          - soilMoisture    
          - solarRadiation    
          - speed    
          - tds    
          - temperature    
          - trafficFlow    
          - tss    
          - turbidity    
          - waterConsumption    
          - waterFlow    
          - waterLevel    
          - waterPollution    
          - weatherConditions    
          - weight    
          - windDirection    
          - windSpeed    
        type: string    
      type: array    
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
    deviceClass:    
      description: "Class of constrained device as specified by RFC 7228. If the device is not a constrained device this property shall not be present. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'"    
      enum:    
        - C0    
        - C1    
        - C2    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    documentation:    
      description: 'A link to device''s documentation.'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    energyLimitationClass:    
      description: "Device's class of energy limitation as per RFC 7228. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'"    
      enum:    
        - E0    
        - E1    
        - E2    
        - E9    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    function:    
      description: "The functionality necessary to accomplish the task for which a Device is designed. A device can be designed to perform more than one function. Defined by [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification"    
      items:    
        enum:    
          - levelControl    
          - sensing    
          - onOff    
          - openClose    
          - metering    
          - eventNotification    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &devicemodel_-_properties_-_owner_-_items_-_anyof    
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
    image:    
      description: 'An image of the item'    
      format: uri    
      type: string    
      x-ngsi:    
        model: https://schema.org/URL    
        type: Property    
    macAddress:    
      description: 'The MAC address of the device.'    
      pattern: ^([[A-Fa-f0-9]]{2}[:.-]?){5}[[A-Fa-f0-9]]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    manufacturerName:    
      description: 'Device''s manufacturer name.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    modelName:    
      description: 'Device''s model name.'    
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
        anyOf: *devicemodel_-_properties_-_owner_-_items_-_anyof    
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
    supportedProtocol:    
      description: 'Supported protocol(s) or networks'    
      items:    
        enum:    
          - 3g    
          - bluetooth    
          - 'bluetooth LE'    
          - cat-m    
          - coap    
          - ec-gsm-iot    
          - gprs    
          - http    
          - lwm2m    
          - lora    
          - lte-m    
          - mqtt    
          - nb-iot    
          - onem2m    
          - sigfox    
          - ul20    
          - websocket    
        type: string    
      type: array    
      x-ngsi:    
        model: '3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket'    
        type: Property    
    supportedUnits:    
      description: 'Units of measurement supported by the device. The unit code (text) of measurement given using the [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters).'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI Entity type. it has to be DeviceModel'    
      enum:    
        - DeviceModel    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - category    
    - controlledProperty    
    - manufacturerName    
    - brandName    
    - modelName    
  type: object    
  version: 0.0.2    
```  
</details>    
## Esempio di payloads  
#### DeviceModel NGSI-v2 valori chiave Esempio  
Ecco un esempio di un DeviceModel in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "name": "myDevice Sensor for Containers 345",  
  "brandName": "myDevice",  
  "modelName": "S4Container 345",  
  "manufacturerName": "myDevice Inc.",  
  "category": ["sensor"],  
  "function": ["sensing"],  
  "controlledProperty": ["fillingLevel", "temperature"]  
}  
```  
#### DeviceModel NGSI-v2 normalizzato Esempio  
Ecco un esempio di un DeviceModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "category": {  
    "type": "array",  
    "value": [  
      "sensor"  
    ]  
  },  
  "function": {  
    "type": "array",  
    "value": [  
      "sensing"  
    ]  
  },  
  "modelName": {  
    "type": "Text",  
    "value": "S4Container 345"  
  },  
  "name": {  
    "type": "Text",  
    "value": "myDevice Sensor for Containers 345"  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "myDevice"  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "myDevice Inc."  
  },  
  "controlledProperty": {  
    "type": "array",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  }  
}  
```  
#### DeviceModel NGSI-LD valori chiave Esempio  
Ecco un esempio di un DeviceModel in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "brandName": "myDevice",  
  "category": [  
    "sensor"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "function": [  
    "sensing"  
  ],  
  "manufacturerName": "myDevice Inc.",  
  "modelName": "S4Container 345",  
  "name": "myDevice Sensor for Containers 345",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
#### DeviceModel NGSI-LD normalizzato Esempio  
Ecco un esempio di un DeviceModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "category": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "function": {  
    "type": "Property",  
    "value": [  
      "sensing"  
    ]  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "S4Container 345"  
  },  
  "name": {  
    "type": "Property",  
    "value": "myDevice Sensor for Containers 345"  
  },  
  "brandName": {  
    "type": "Property",  
    "value": "myDevice"  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "myDevice Inc."  
  },  
  "controlledProperty": {  
    "type": "Property",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
