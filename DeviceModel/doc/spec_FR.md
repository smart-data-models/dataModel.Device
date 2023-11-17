<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : DeviceModel    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceModel/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Cette entité capture les propriétés statiques d'un appareil. **    
version : 0.0.3    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `alternateName[string]`: Un nom alternatif pour ce poste  - `annotations[array]`: Annotations sur l'article  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: Nom de marque de l'appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: Capteur : Dispositif qui détecte et réagit à des événements ou à des changements dans l'environnement physique, tels que la lumière, le mouvement ou les changements de température. https://w3id.org/saref#Sensor. Actionneur : Dispositif chargé de déplacer ou de contrôler un mécanisme ou un système. https://w3id.org/saref#Actuator. Compteur : Dispositif construit pour détecter et afficher avec précision une quantité sous une forme lisible par un être humain. Partiellement défini par SAREF. CVC : Appareil de chauffage, de ventilation et de climatisation (CVC) qui assure le confort de l'environnement intérieur. https://w3id.org/saref#HVAC. Réseau : Dispositif utilisé pour connecter d'autres dispositifs dans un réseau, tel qu'un concentrateur, un commutateur ou un routeur dans un réseau local ou un réseau de capteurs. (https://w3id.org/saref#Network. Multimédia : Un appareil conçu pour afficher, stocker, enregistrer ou lire des contenus multimédias tels que de l'audio, des images, des animations, de la vidéo. Enum : "actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor". Raw category sera déprécié, utilisez deviceCategory à la place pour éviter les conflits avec d'autres aqttributes nommés category.  . Model: [https://schema.org/Text](https://schema.org/Text)- `color[string]`: La couleur du produit  . Model: [https://schema.org/color](https://schema.org/color)- `controlledProperty[array]`: Tout ce qui peut être détecté, mesuré ou contrôlé. Enum :'pollution de l'air, pression atmosphérique, vitesse moyenne, autonomie de la batterie, alimentation de la batterie, cdom, conductance, conductivité, profondeur, activité alimentaire, consommation d'électricité, énergie, niveau de remplissage, chlore libre, consommation de gaz, ouverture de la porte, cap, humidité, lumière, emplacement, traite, mouvement, activité de mouvement, niveau de bruit, occupation, orp, pH, puissance, précipitation, pression, indice de réfraction, salinité, fumée, humidité du sol, rayonnement solaire, vitesse, tds, température, flux de circulation, tss, turbidité, consommation d'eau, flux d'eau, niveau d'eau, pollution de l'eau, conditions météorologiques, poids, direction du vent, vitesse du vent".  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `deviceCategory[array]`: Capteur : Dispositif qui détecte et réagit à des événements ou à des changements dans l'environnement physique, tels que la lumière, le mouvement ou les changements de température. https://w3id.org/saref#Sensor. Actionneur : Dispositif chargé de déplacer ou de contrôler un mécanisme ou un système. https://w3id.org/saref#Actuator. Compteur : Dispositif construit pour détecter et afficher avec précision une quantité sous une forme lisible par un être humain. Partiellement défini par SAREF. CVC : Appareil de chauffage, de ventilation et de climatisation (CVC) qui assure le confort de l'environnement intérieur. https://w3id.org/saref#HVAC. Réseau : Dispositif utilisé pour connecter d'autres dispositifs dans un réseau, tel qu'un concentrateur, un commutateur ou un routeur dans un réseau local ou un réseau de capteurs. (https://w3id.org/saref#Network. Multimédia : Un appareil conçu pour afficher, stocker, enregistrer ou lire des contenus multimédias tels que de l'audio, des images, des animations, de la vidéo. Enum : "actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor". Raw category sera déprécié, utilisez deviceCategory à la place pour éviter les conflits avec d'autres aqttributes nommés category.  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceClass[string]`: Classe de dispositif contraint telle que spécifiée par la RFC 7228. Si le dispositif n'est pas un dispositif contraint, cette propriété ne doit pas être présente. Références normatives : [RFC7228](https://tools.ietf.org/html/rfc7228#section-3). Enum : "C0, C1, C2  . Model: [https://schema.org/Text](https://schema.org/Text)- `documentation[uri]`: Un lien vers la documentation de l'appareil  . Model: [https://schema.org/URL](https://schema.org/URL)- `energyLimitationClass[string]`: Classe de limitation d'énergie de l'appareil, conformément à la RFC 7228. Références normatives : [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enum : "E0, E1, E2, E9  . Model: [https://schema.org/Text](https://schema.org/Text)- `function[array]`: La fonctionnalité nécessaire pour accomplir la tâche pour laquelle un dispositif est conçu. Un dispositif peut être conçu pour remplir plus d'une fonction. Défini par [SAREF] (https://w3id.org/saref#Function). Enum : "levelControl, sensing, onOff, openClose, metering, eventNotification  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identifiant unique de l'entité  - `image[uri]`: Une image de l'objet  . Model: [https://schema.org/URL](https://schema.org/URL)- `macAddress[string]`: L'adresse MAC de l'appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `manufacturerName[string]`: Nom du fabricant de l'appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `modelName[string]`: Nom du modèle de l'appareil  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: Le nom de cet élément  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `supportedProtocol[array]`: Protocole(s) ou réseaux pris en charge  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `supportedUnits[array]`: Unités de mesure prises en charge par l'appareil. Le code d'unité (texte) de mesure donné en utilisant le [Code commun du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (max. 3 caractères)  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Type d'entité NGSI. Il doit s'agir de DeviceModel.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
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
## Exemples de charges utiles    
#### DeviceModel Valeurs clés NGSI-v2 Exemple    
Voici un exemple de DeviceModel au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### DeviceModel NGSI-v2 normalisé Exemple    
Voici un exemple de DeviceModel au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
#### DeviceModel Valeurs clés NGSI-LD Exemple    
Voici un exemple de DeviceModel au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
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
#### DeviceModel NGSI-LD normalisé Exemple    
Voici un exemple de DeviceModel au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
