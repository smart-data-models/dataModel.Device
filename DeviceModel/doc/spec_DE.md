<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: DeviceModel    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceModel/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Diese Einheit erfasst die statischen Eigenschaften eines Geräts. **    
Version: 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `annotations[array]`: Anmerkungen zum Artikel  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Markenname des Geräts  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Sensor: Ein Gerät, das Ereignisse oder Veränderungen in der physikalischen Umgebung wie Licht, Bewegung oder Temperaturveränderungen erkennt und darauf reagiert. https://w3id.org/saref#Sensor. Aktor: Ein Gerät, das für die Bewegung oder Steuerung eines Mechanismus oder Systems verantwortlich ist. https://w3id.org/saref#Actuator. Messgerät : Ein Gerät, das zur genauen Erfassung und Anzeige einer Größe in einer für den Menschen lesbaren Form dient. Teilweise durch SAREF definiert. HVAC : Heizungs-, Belüftungs- und Klimaanlagen (HVAC), die für ein angenehmes Raumklima sorgen. https://w3id.org/saref#HVAC. Netzwerk : Ein Gerät, das dazu dient, andere Geräte in einem Netzwerk zu verbinden, z. B. Hub, Switch oder Router in einem LAN oder Sensornetzwerk. (https://w3id.org/saref#Network. Multimedia : Ein Gerät zum Anzeigen, Speichern, Aufzeichnen oder Abspielen von Multimedia-Inhalten wie Audio, Bilder, Animationen, Video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category wird veraltet sein, stattdessen sollte deviceCategory verwendet werden, um Konflikte mit anderen aqttributes namens category zu vermeiden.  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: Die Farbe des Produkts  . Model: [https://schema.org/color](https://schema.org/color)- `controlledProperty[array]`: Alles, was von einem Sensor erfasst, gemessen oder kontrolliert werden kann. Enum:airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, motionActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `deviceCategory[array]`: Sensor: Ein Gerät, das Ereignisse oder Veränderungen in der physikalischen Umgebung wie Licht, Bewegung oder Temperaturveränderungen erkennt und darauf reagiert. https://w3id.org/saref#Sensor. Aktor: Ein Gerät, das für die Bewegung oder Steuerung eines Mechanismus oder Systems verantwortlich ist. https://w3id.org/saref#Actuator. Messgerät : Ein Gerät, das zur genauen Erfassung und Anzeige einer Größe in einer für den Menschen lesbaren Form dient. Teilweise durch SAREF definiert. HVAC : Heizungs-, Belüftungs- und Klimaanlagen (HVAC), die für ein angenehmes Raumklima sorgen. https://w3id.org/saref#HVAC. Netzwerk : Ein Gerät, das dazu dient, andere Geräte in einem Netzwerk zu verbinden, z. B. Hub, Switch oder Router in einem LAN oder Sensornetzwerk. (https://w3id.org/saref#Network. Multimedia : Ein Gerät zum Anzeigen, Speichern, Aufzeichnen oder Abspielen von Multimedia-Inhalten wie Audio, Bilder, Animationen, Video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'. Raw category wird veraltet sein, stattdessen sollte deviceCategory verwendet werden, um Konflikte mit anderen aqttributes namens category zu vermeiden.  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceClass[string]`: Klasse des eingeschränkten Geräts gemäß RFC 7228. Handelt es sich bei dem Gerät nicht um ein eingeschränktes Gerät, darf diese Eigenschaft nicht vorhanden sein. Normative Verweise: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'  . Model: [https://schema.org/Text](https://schema.org/Text)- `documentation[uri]`: Ein Link zur Dokumentation des Geräts  . Model: [https://schema.org/URL](https://schema.org/URL)- `energyLimitationClass[string]`: Klasse der Energiebegrenzung des Geräts gemäß RFC 7228. Normative Referenzen: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'  . Model: [https://schema.org/Text](https://schema.org/Text)- `function[array]`: Die Funktionalität, die erforderlich ist, um die Aufgabe zu erfüllen, für die ein Gerät konzipiert ist. Ein Gerät kann für mehr als eine Funktion ausgelegt sein. Definiert durch [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Eindeutiger Bezeichner der Entität  - `image[uri]`: Ein Bild des Artikels  . Model: [https://schema.org/URL](https://schema.org/URL)- `macAddress[string]`: Die MAC-Adresse des Geräts  . Model: [https://schema.org/Text](https://schema.org/Text)- `manufacturerName[string]`: Name des Geräteherstellers  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: Modellbezeichnung des Geräts  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Der Name dieses Artikels  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `supportedProtocol[array]`: Unterstützte(s) Protokoll(e) oder Netzwerk(e)  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `supportedUnits[array]`: Von dem Gerät unterstützte Maßeinheiten. Der Code der Maßeinheit (Text), der unter Verwendung des [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben wird (max. 3 Zeichen)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-Entitätstyp. Es muss DeviceModel sein  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
DeviceModel:      
  description: 'This entity captures the static properties of a Device. '      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    annotations:      
      description: Annotations about the item      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    brandName:      
      description: Device's brand name      
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
    color:      
      description: The color of the product      
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
          - uvLampIntensity      
          - uvOrganicLoad      
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
    deviceCategory:      
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
      description: A link to device's documentation      
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
    macAddress:      
      description: The MAC address of the device      
      pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    manufacturerName:      
      description: Device's manufacturer name      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    modelName:      
      description: Device's model name      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
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
    supportedProtocol:      
      description: Supported protocol(s) or networks      
      items:      
        enum:      
          - 3g      
          - bluetooth      
          - bluetooth LE      
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
      description: 'Units of measurement supported by the device. The unit code (text) of measurement given using the [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters)'      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI Entity type. it has to be DeviceModel      
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
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/DeviceModel/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/DeviceModel/schema.json      
  x-model-tags: ""      
  x-version: 0.0.3      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### DeviceModel NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "name": "myDevice Sensor for Containers 345",  
  "brandName": "myDevice",  
  "modelName": "S4Container 345",  
  "manufacturerName": "myDevice Inc.",  
  "deviceCategory": [  
    "sensor"  
  ],  
  "category": [  
    "sensor"  
  ],  
  "function": [  
    "sensing"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ]  
}  
```  
</details>    
#### DeviceModel NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "deviceCategory": {  
    "type": "StructuredValue",  
    "value": [  
      "sensor"  
    ]  
  },  
  "function": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "category": {  
    "type": "StructuredValue",  
    "value": [  
      "sensor"  
    ]  
  }  
}  
```  
</details>    
#### DeviceModel NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "brandName": "myDevice",  
  "deviceCategory": [  
    "sensor"  
  ],  
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
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### DeviceModel NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "brandName": {  
    "type": "Property",  
    "value": "myDevice"  
  },  
  "deviceCategory": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "controlledProperty": {  
    "type": "Property",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "function": {  
    "type": "Property",  
    "value": [  
      "sensing"  
    ]  
  },  
  "manufacturerName": {  
    "type": "Property",  
    "value": "myDevice Inc."  
  },  
  "modelName": {  
    "type": "Property",  
    "value": "S4Container 345"  
  },  
  "name": {  
    "type": "Property",  
    "value": "myDevice Sensor for Containers 345"  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
