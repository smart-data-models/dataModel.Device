<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SmartMeteringObservation  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.Device/blob/master/SmartMeteringObservation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Cette entité contient une description harmonisée de l'observation d'un compteur intelligent, généralement applicable aux maisons intelligentes, à l'industrie, aux villes et à l'agriculture. Elle est basée principalement sur la définition de l'entité GSMA, mais elle est étendue**.  
version : 0.0.2  
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
- `alternateName[string]`: Un nom alternatif pour ce poste  - `areaServed[string]`: La zone géographique où un service ou un article est offert  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées  - `dateCreated[date-time]`: Horodatage de la création de l'entité. Celle-ci est généralement attribuée par la plate-forme de stockage  - `dateModified[date-time]`: Date de la dernière modification de l'entité. Cette date est généralement attribuée par la plate-forme de stockage  - `description[string]`: Une description de l'article  - `entityVersion[string]`: La version de la spécification de l'entité. Un numéro de version de 2.0 ou plus indique que l'entité est représentée à l'aide de la NGSI-LD.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identifiant unique de l'entité  - `image[uri]`: Une image de l'objet  . Model: [https://schema.org/URL](https://schema.org/URL)- `location[*]`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une chaîne de ligne, d'un polygone, d'un point multiple, d'une chaîne de ligne multiple ou d'un polygone multiple.  - `meterType[string]`: Le type d'approvisionnement mesuré, par exemple : Électricité, essence, eau, méthane, diesel  - `name[string]`: Le nom de cet élément  - `offPeakConsumption[number]`: La quantité totale de produit fournie pendant les heures creuses (en particulier pour la fourniture d'électricité), telle qu'enregistrée par le compteur depuis l'installation. Le code d'unité approprié doit être spécifié, par exemple KWH (Kilo Watt Hours) pour l'électricité, LTR (Litre) ou MTQ (Mètre cube) pour les gaz ou les liquides.  - `owner[array]`: Une liste contenant une séquence de caractères encodés JSON référençant les identifiants uniques du ou des propriétaires.  - `peakConsumption[number]`: La quantité totale de produit fournie pendant les heures de pointe (en particulier pour la fourniture d'électricité), telle qu'elle est enregistrée par le compteur depuis l'installation. Le code d'unité approprié doit être spécifié, par exemple KWH (Kilo Watt Hours) pour l'électricité, LTR (Litre) ou MTQ (Mètre cube) pour les gaz ou les liquides.  - `powerFactor[number]`: Concernant les alimentations électriques triphasées souvent utilisées dans l'industrie, le facteur de puissance varie de -1 à +1 en fonction de l'équilibre net entre les charges capacitives et inductives. S'il est utilisé, il mesure le facteur de puissance moyen depuis l'installation du compteur.  - `refDevice[*]`: Identifiant unique de l'entité (dispositif) liée à la SmartMeteringObservation  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires concernant l'élément  - `source[string]`: Séquence de caractères indiquant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine complet du fournisseur de la source ou l'URL de l'objet source.  - `totalConsumption[number]`: La quantité totale de produit fournie telle qu'enregistrée par le compteur depuis l'installation. Le code d'unité approprié doit être spécifié, par exemple KWH (Kilo Watt Hours) pour l'électricité, LTR (Litre) ou MTQ (Mètre cube) pour les gaz ou les liquides.  - `type[string]`: Il doit s'agir de SmartMeteringObservation. Type d'entité NGSI  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Adapté des modèles de données GSMA mais compatible avec tous les modèles de données smart. Élargi par des propriétés individuelles.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SmartMeteringObservation:    
  description: 'This entity contains a harmonised description of a Smart Meter Observation, generally applicable for Smart Homes, Industry, Cities and Agriculture. It is based mostly in the GSMA entity definition but it is extended'    
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
    entityVersion:    
      description: The entity specification version. A version number of 2.0 or later denotes the entity is represented using NGSI-LD    
      enum:    
        - 2.0    
        - LD    
      type: string    
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
    meterType:    
      description: 'The type of supply being metered e.g.: Electricity, Gasoline, Water, Methane, Diesel'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    offPeakConsumption:    
      description: 'The total amount of product supplied during ''off-peak'' hours (particularly relevant to Electricity supply) as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids'    
      type: number    
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
    peakConsumption:    
      description: 'The total amount of product supplied during ''peak'' hours (particularly relevant to Electricity supply) as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids'    
      type: number    
      x-ngsi:    
        type: Property    
    powerFactor:    
      description: Relevant to 3-Phase electricity supplies often used in industry - the power factor ranges from -1 to +1 depending on the net balance between capacitive and inductive loads. If used this measures the average power factor since meter installation    
      type: number    
      x-ngsi:    
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
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity (Device) linked to the SmartMeteringObservation    
      x-ngsi:    
        type: Relationship    
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
    totalConsumption:    
      description: 'The total amount of product supplied as recorded by the meter since installation. The relevant unitCode should be specified such as KWH (Kilo Watt Hours) for Electricity, LTR (Litre) or MTQ (Cubic Metre) for gases or liquids'    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: It has to be SmartMeteringObservation. NGSI entity type    
      enum:    
        - SmartMeteringObservation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/SmartMeteringObservation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/SmartMeteringObservation/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### SmartMeteringObservation Valeurs clés NGSI-v2 Exemple  
Voici un exemple de SmartMeteringObservation au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
  "type": "SmartMeteringObservation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "entityVersion": "2.0",  
  "meterType": "Electricity",  
  "refDevice": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac",  
  "location": {  
    "type": "Point",  
    "coordinates": [  
      -103.9904,  
      39.7564  
    ]  
  },  
  "image": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg==",  
  "address": {  
    "addressLocality": "London",  
    "postalCode": "EC4N 8AF",  
    "streetAddress": "25 Walbrook"  
  },  
  "totalConsumption": 7.0,  
  "peakConsumption": 9.3,  
  "offPeakConsumption": 8.0,  
  "powerFactor": 0.98  
}  
```  
</details>  
#### SmartMeteringObservation NGSI-v2 normalisé Exemple  
Voici un exemple de SmartMeteringObservation au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
  "type": "SmartMeteringObservation",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "entityVersion": {  
    "type": "Number",  
    "value": "2.0"  
  },  
  "meterType": {  
    "type": "Text",  
    "value": "Electricity"  
  },  
  "refDevice": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -103.9904,  
        39.7564  
      ]  
    }  
  },  
  "image": {  
    "type": "Text",  
    "value": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg=="  
  },  
  "address": {  
    "type": "StructuredValue",  
    "value": {  
      "addressLocality": "London",  
      "postalCode": "EC4N 8AF",  
      "streetAddress": "25 Walbrook"  
    }  
  },  
  "totalConsumption": {  
    "type": "Number",  
    "value": 7.0  
  },  
  "peakConsumption": {  
    "type": "Number",  
    "value": 9.3  
  },  
  "offPeakConsumption": {  
    "type": "Number",  
    "value": 8.0  
  },  
  "powerFactor": {  
    "type": "Number",  
    "value": 0.98  
  }  
}  
```  
</details>  
#### SmartMeteringObservation Valeurs clés NGSI-LD Exemple  
Voici un exemple de SmartMeteringObservation au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
    "type": "SmartMeteringObservation",  
    "address": {  
        "addressLocality": "London",  
        "postalCode": "EC4N 8AF",  
        "streetAddress": "25 Walbrook"  
    },  
    "dataProvider": "https://provider.example.com",  
    "entityVersion": "2.0",  
    "image": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg==",  
    "location": {  
        "type": "Point",  
        "coordinates": [  
            -103.9904,  
            39.7564  
        ]  
    },  
    "meterType": "Electricity",  
    "offPeakConsumption": 8.0,  
    "peakConsumption": 9.3,  
    "powerFactor": 0.98,  
    "refDevice": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac",  
    "source": "https://source.example.com",  
    "totalConsumption": 7.0,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SmartMeteringObservation NGSI-LD normalisé Exemple  
Voici un exemple de SmartMeteringObservation au format JSON-LD tel que normalisé. Ce format est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:SmartMeter:8ac0db56-9adf-11e8-ad67-e7308e2e8b15",  
    "type": "SmartMeteringObservation",  
    "address": {  
        "type": "Property",  
        "value": {  
            "addressLocality": "London",  
            "postalCode": "EC4N 8AF",  
            "streetAddress": "25 Walbrook"  
        }  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "entityVersion": {  
        "type": "Property",  
        "value": "2.0"  
    },  
    "image": {  
        "type": "Property",  
        "value": "urn:ngsi:iVBORw0KGgoAAAANSUhEUgAAAGcAAABkCAIAAAAUt...ErkJggg=="  
    },  
    "location": {  
        "type": "GeoProperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -103.9904,  
                39.7564  
            ]  
        }  
    },  
    "meterType": {  
        "type": "Property",  
        "value": "Electricity"  
    },  
    "offPeakConsumption": {  
        "type": "Property",  
        "value": 8.0  
    },  
    "peakConsumption": {  
        "type": "Property",  
        "value": 9.3  
    },  
    "powerFactor": {  
        "type": "Property",  
        "value": 0.98  
    },  
    "refDevice": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Device:7a0708f6-9668-11e8-8f77-abc2b62ebaac"  
    },  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "totalConsumption": {  
        "type": "Property",  
        "value": 7.0  
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
