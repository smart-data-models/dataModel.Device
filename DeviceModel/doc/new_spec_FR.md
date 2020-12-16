Entité : DeviceModel  
====================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceModel/LICENSE.md)  
Description globale : **Cette entité capture les propriétés statiques d'un appareil. **  

## Liste des biens  

- `alternateName`: Un autre nom pour cet article  - `annotations`: Annotations sur le sujet  - `brandName`: Nom de la marque de l'appareil.  - `color`: La couleur du produit  - `controlledProperty`: Enum :température, humidité, lumière, mouvement, remplissageNiveau, occupation, puissance, pression, fumée, énergie, airPollution, bruitNiveau, conditions météorologiquesConditions, précipitations, ventVitesse, ventDirection, pression atmosphérique, rayonnement solaire, profondeur, pH, conductivité, conductance, tss, tds, turbidité, salinité, orp, cdom, eauPollution, localisation, vitesse, cap, poids, consommation d'eau, consommation de gaz, consommation d'électricité, humidité du sol, circulationFlux, alimentationActivité, traite, mouvementActivité".  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il est généralement attribué par la plate-forme de stockage.  - `description`: Une description de cet article  - `deviceClass`: Classe de dispositif sous contrainte, comme spécifié par la RFC 7228. Si le dispositif n'est pas un dispositif sous contrainte, cette propriété ne doit pas être présente. Références normatives : [RFC7228] (https://tools.ietf.org/html/rfc7228#section-3). Enumération : "C0, C1, C2".  - `documentation`: Un lien vers la documentation de l'appareil.  - `energyLimitationClass`: Classe de limitation d'énergie de l'appareil selon la RFC 7228. Références normatives : [RFC7228](https://tools.ietf.org/html/rfc7228#page-11). Enumération : "E0, E1, E2, E9".  - `function`: La fonctionnalité nécessaire pour accomplir la tâche pour laquelle un appareil est conçu. Un dispositif peut être conçu pour remplir plus d'une fonction. Défini par [SAREF] (https://w3id.org/saref#Function). Enum : "levelControl, sensing, onOff, openClose, metering, eventNotification  - `id`: Identifiant unique de l'entité  - `image`: Une image de l'objet  - `manufacturerName`: Nom du fabricant de l'appareil.  - `modelName`: Nom du modèle de l'appareil.  - `name`: Le nom de cet article.  - `owner`: Une liste contenant une séquence de caractères codés en JSON faisant référence aux Ids uniques du ou des propriétaires  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur le sujet  - `source`: Une séquence de caractères donnant comme URL la source originale des données de l'entité. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source, ou l'URL de l'objet source.  - `supportedUnits`: Unités de mesure supportées par l'appareil. Le code de l'unité de mesure (texte) est donné en utilisant le [code commun du CEFACT-ONU] (http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes) (3 caractères maximum).  - `type`: NGSI Entity type. Il doit s'agir de DeviceModel    
Propriétés requises  
- `brandName`  - `category`  - `controlledProperty`  - `id`  - `manufacturerName`  - `modelName`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
    color:    
      description: 'The color of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/color    
    controlledProperty:    
      description: 'Enum:''temperature, humidity, light, motion, fillingLevel,occupancy, power, pressure, smoke, energy, airPollution, noiseLevel, weatherConditions, precipitation, windSpeed, windDirection, atmosphericPressure, solarRadiation, depth, pH,conductivity, conductance, tss, tds, turbidity, salinity,orp, cdom, waterPollution, location, speed, heading,weight, waterConsumption, gasConsumption, electricityConsumption, soilMoisture, trafficFlow, eatingActivity, milking, movementActivity''.'    
      items:    
        enum:    
          - temperature    
          - humidity    
          - light    
          - motion    
          - fillingLevel    
          - occupancy    
          - power    
          - pressure    
          - smoke    
          - energy    
          - airPollution    
          - noiseLevel    
          - weatherConditions    
          - precipitation    
          - windSpeed    
          - windDirection    
          - atmosphericPressure    
          - solarRadiation    
          - depth    
          - pH    
          - conductivity    
          - conductance    
          - tss    
          - tds    
          - turbidity    
          - salinity    
          - orp    
          - cdom    
          - waterPollution    
          - location    
          - speed    
          - heading    
          - weight    
          - waterConsumption    
          - gasConsumption    
          - electricityConsumption    
          - soilMoisture    
          - trafficFlow    
          - eatingActivity    
          - milking    
          - movementActivity    
        type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/DateTime    
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
            - format: uri    
              type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
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
## Exemples de charges utiles  
#### DeviceModel NGSI V2 valeurs clés Exemple  
Voici un exemple de DeviceModel au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
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
#### DeviceModel NGSI V2 normalisé Exemple  
Voici un exemple de DeviceModel au format JSON tel que normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
#### DeviceModel NGSI-LD valeurs clés Exemple  
Voici un exemple de DeviceModel au format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{"@context": ["https://schema.lab.fiware.org/ld/context",  
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],  
 "brandName": "myDevice",  
 "category": ["sensor"],  
 "controlledProperty": ["fillingLevel", "temperature"],  
 "function": ["sensing"],  
 "id": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
 "manufacturerName": "myDevice Inc.",  
 "modelName": "S4Container 345",  
 "name": "myDevice Sensor for Containers 345",  
 "type": "DeviceModel"}  
```  
#### DeviceModel NGSI-LD normalisé Exemple  
Voici un exemple de DeviceModel au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "https://schema.lab.fiware.org/ld/context",  
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
    ]  
}  
```  
