Entität: DeviceModel  
====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceModel/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität erfasst die statischen Eigenschaften eines Geräts. **  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `annotations`: Anmerkungen zum Artikel  - `brandName`: Der Markenname des Geräts.  - `category`: Sensor: Ein Gerät, das Ereignisse oder Veränderungen in der physikalischen Umgebung wie Licht, Bewegung oder Temperaturänderungen erkennt und darauf reagiert. https://w3id.org/saref#Sensor. Aktor : Ein Gerät, das für die Bewegung oder Steuerung eines Mechanismus oder Systems verantwortlich ist. https://w3id.org/saref#Actuator. Messgerät : Ein Gerät, das zur genauen Erfassung und Anzeige einer Größe in einer für den Menschen lesbaren Form gebaut ist. Teilweise durch SAREF definiert. HVAC : Gerät für Heizung, Lüftung und Klimatisierung (HVAC), das für ein angenehmes Raumklima sorgt. https://w3id.org/saref#HVAC. Netzwerk : Ein Gerät, das dazu dient, andere Geräte in einem Netzwerk zu verbinden, z. B. Hub, Switch oder Router in einem LAN oder Sensor-Netzwerk. (https://w3id.org/saref#Network. Multimedia : Ein Gerät zum Anzeigen, Speichern, Aufnehmen oder Abspielen von Multimedia-Inhalten wie z. B. Audio, Bilder, Animationen, Video. Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'  - `color`: Die Farbe des Produkts  - `controlledProperty`: Alles, was von einem Sensor erfasst, gemessen oder gesteuert werden kann. Enum:'airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `deviceClass`: Klasse des eingeschränkten Geräts, wie in RFC 7228 angegeben. Wenn das Gerät kein eingeschränktes Gerät ist, darf diese Eigenschaft nicht vorhanden sein. Normative Verweise: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'  - `documentation`: Ein Link zur Dokumentation des Geräts.  - `energyLimitationClass`: Klasse der Energiebegrenzung des Geräts gemäß RFC 7228. Normative Referenzen: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'  - `function`: Die Funktionalität, die erforderlich ist, um die Aufgabe zu erfüllen, für die ein Gerät ausgelegt ist. Ein Gerät kann so konzipiert sein, dass es mehr als eine Funktion ausführt. Definiert durch [SAREF](https://w3id.org/saref#Function). Enum:'levelControl, sensing, onOff, openClose, metering, eventNotification  - `id`: Eindeutiger Bezeichner der Entität  - `image`: Ein Bild des Artikels  - `macAddress`: Die MAC-Adresse des Geräts.  - `manufacturerName`: Name des Geräteherstellers.  - `modelName`: Der Modellname des Geräts.  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `supportedProtocol`: Unterstützte(s) Protokoll(e) oder Netzwerke  - `supportedUnits`: Vom Gerät unterstützte Maßeinheiten. Der Einheitencode (Text) des Maßes, der unter Verwendung des [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) angegeben wird (max. 3 Zeichen).  - `type`: NGSI Entity-Typ. Es muss DeviceModel sein    
Erforderliche Eigenschaften  
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
DeviceModel:    
  description: 'This entity captures the static properties of a Device. '    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    annotations:    
      description: 'Annotations about the item'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    brandName:    
      description: 'Device''s brand name.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    controlledProperty:    
      description: 'Anything that can be sensed, measured or controlled by. Enum:''airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'''    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    deviceClass:    
      description: "Class of constrained device as specified by RFC 7228. If the device is not a constrained device this property shall not be present. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum:'C0, C1, C2'"    
      enum:    
        - C0    
        - C1    
        - C2    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    documentation:    
      description: 'A link to device''s documentation.'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    energyLimitationClass:    
      description: "Device's class of energy limitation as per RFC 7228. Normative References: [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum:'E0, E1, E2, E9'"    
      enum:    
        - E0    
        - E1    
        - E2    
        - E9    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
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
      type: Property    
    image:    
      description: 'An image of the item'    
      format: uri    
      type: Property    
      x-ngsi:    
        model: https://schema.org/URL    
    macAddress:    
      description: 'The MAC address of the device.'    
      pattern: ^([[:xdigit:]]{2}[:.-]?){5}[[:xdigit:]]{2}$    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    manufacturerName:    
      description: 'Device''s manufacturer name.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    modelName:    
      description: 'Device''s model name.'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *devicemodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
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
      type: Property    
      x-ngsi:    
        model: '3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket'    
    supportedUnits:    
      description: 'Units of measurement supported by the device. The unit code (text) of measurement given using the [UN/CEFACT Common Code](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 characters).'    
      items:    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI Entity type. it has to be DeviceModel'    
      enum:    
        - DeviceModel    
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
```  
</details>    
## Beispiel-Nutzlasten  
#### DeviceModel NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### DeviceModel NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "myDevice-wastecontainer-sensor-345",  
  "type": "DeviceModel",  
  "category": {  
    "value": ["sensor"]  
  },  
  "function": {  
    "value": ["sensing"]  
  },  
  "modelName": {  
    "value": "S4Container 345"  
  },  
  "name": {  
    "value": "myDevice Sensor for Containers 345"  
  },  
  "brandName": {  
    "value": "myDevice"  
  },  
  "manufacturerName": {  
    "value": "myDevice Inc."  
  },  
  "controlledProperty": {  
    "value": ["fillingLevel", "temperature"]  
  }  
}  
```  
#### DeviceModel NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### DeviceModel NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein DeviceModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ],  
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
  "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "manufacturerName": "myDevice Inc.",  
  "modelName": "S4Container 345",  
  "name": "myDevice Sensor for Containers 345",  
  "type": "DeviceModel"  
}  
```  
