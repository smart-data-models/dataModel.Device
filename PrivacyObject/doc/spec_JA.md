Entity:プライバシーオブジェクト  
===================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Device/blob/master/PrivacyObject/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな説明です。**IoTデバイスのプライバシーに関する情報**。  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `category`: センサー。光、動き、温度変化など、物理的環境における事象や変化を検出し、応答する装置。https://w3id.org/saref#Sensor. アクチュエータ : メカニズムやシステムを動かしたり、制御したりする役割を担う装置。https://w3id.org/saref#Actuator.計器 : 人間が読める形で量を正確に検出し、表示するために作られた装置のこと。SAREFで一部定義されている。HVAC : 室内環境の快適性を提供する暖房、換気、空調（HVAC）機器。https://w3id.org/saref#HVAC。ネットワーク : LANやセンサーネットワークにおけるハブ、スイッチ、ルーターなど、ネットワーク内で他の機器を接続するための装置。(https://w3id.org/saref#Network。マルチメディア。音声、画像、アニメーション、ビデオなどのマルチメディアコンテンツを表示、保存、記録、再生するための装置。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'.  - `crossborderTransfer`: エンティティにリンクしたクロスボーダー転送に関する表示。  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `floor`: 建物内にあるときに機器が設置されている階、またはそれに準ずる階。  - `id`: エンティティのユニークな識別子  - `image`: アイテムのイメージ  - `isIndoor`: エンティティが屋内に設置されているか、屋外に設置されているかを示すフラグ。  - `isPersonalData`: エンティティが個人データを提供しているか、または含んでいるかを示すフラグ。  - `legitimateInterest`: 企業に関連する正当な利益。これは、データ収集が高度な最終目的のために行われることを意味します。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `name`: このアイテムの名前です。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `purpose`: データ収集の目的。  - `recipientList`: 受信者を含むリスト。受信者とは，センサが生成したデータを利用する受益者のことです．各受信者は，その受信者を一意に識別できるURIで表される．プライバシー:'低'  - `refDevice`: ソースデータセットからのユニークな識別子。  - `retentionPeriod`: データ保持の期間。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSIタイプのプロパティです。これはPrivacyObjectでなければなりません。  - `user`: 匿名ユーザーの識別子。この識別子は実際にはユニークなURNであり、匿名でユーザーを認識するために使用することができます。    
必須項目  
- `id`  - `type`    
PrivacyObjectエンティティは、このIoTデバイスに直接リンクされたプライバシーに関する情報を持つIoTデバイス（通常はセンサー）を表します。いくつかの属性は、プライバシーの文脈でIoTデバイスを記述するために使用されます。特に、1つの属性はIoTデバイスの位置を提供し、他の2つの属性は正確な位置に関する詳細情報を提供する。また、IoTデバイスの説明にも属性が使用されており、2つ目の属性はIoTセンサーの目的を示しています。その他の属性は、IoTデバイスに関連する情報を分類することを目的として、プライバシーとGDPRに非常に焦点を当てています。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます）  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PrivacyObject:    
  description: 'Information about privacy for an IoT device'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
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
    crossborderTransfer:    
      description: 'Indication about the crossborder transfer linked to the entity.'    
      type: string    
      x-ngsi:    
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
    floor:    
      description: 'The floor where the device is installed when in building or equivalent.'    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &privacyobject_-_properties_-_owner_-_items_-_anyof    
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
    isIndoor:    
      description: 'Flag to indicate if the entity is installed indoor or outdoor.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    isPersonalData:    
      description: 'Flag to indicate if the entity is providing or contains personal data.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    legitimateInterest:    
      description: 'Legitimate interest associated to the entity. This means for which high-level finality the data collection is made.'    
      type: string    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *privacyobject_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    purpose:    
      description: 'Purpose of the data gathering.'    
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
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Relationship. Device linked to this PrivacyObject entity. Model:''https://schema.org/URL'''    
          format: uri    
          type: string    
      description: 'Unique identifier from the source data set.'    
      x-ngsi:    
        type: Property    
    retentionPeriod:    
      description: 'Period of data retention.'    
      type: string    
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
    type:    
      description: 'NGSI type property. It has to be PrivacyObject.'    
      enum:    
        - PrivacyObject    
      type: string    
      x-ngsi:    
        type: Property    
    user:    
      description: 'Identifier of an anonymous user. This identifier is in fact a unique URN which can be used to recognize anonymously a user.'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/PrivacyObject/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/PrivacyObject/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
## ペイロードの例  
#### PrivacyObject NGSI-v2 key-valuesの例。  
JSON-LD形式でkey-valuesとしてPrivacyObjectを表現した例です。これは`options=keyValues`を使った場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### プライバシーオブジェクト NGSI-v2 正規化例  
ここでは、正規化されたJSON-LD形式のPrivacyObjectの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
    "type": "Text",  
    "value": "false"  
  },  
  "floor": {  
    "type": "Text",  
    "value": "false"  
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
    "type": "Text",  
    "value": "false"  
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
#### PrivacyObject NGSI-LD key-valuesの例。  
ここでは、JSON-LD形式でPrivacyObjectをkey-valuesにした例を紹介します。これは`options=keyValues`を使った場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
  "description_fr": "Capteur electromagnetique et ultrasons",  
  "user": "urn:ngsi-ld:User:abcdef",  
  "purpose": "Detecting the presence of a vehicle on a parking slot.",  
  "purpose_fr": "Detecter la presence d'un vehicule sur une place de parc.",  
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
  "image": "http://www.example.com/device1.jpg",  
  "@context": [  
    "https://smart-data-models.github.io/data-models/context.jsonld"  
  ]  
}  
```  
#### プライバシーオブジェクト NGSI-LD 正規化例  
ここでは、正規化されたJSON-LD形式のPrivacyObjectの例を示します。これはオプションを使わない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:PrivacyObject:1044_parking",  
  "type": "PrivacyObject",  
  "refDevice": {  
    "type": "Relationship",  
    "value": "Device:1044_parking"  
  },  
  "name": {  
    "type": "Property",  
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
    "type": "Property",  
    "value": "false"  
  },  
  "floor": {  
    "type": "Property",  
    "value": "false"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Electromagnetic and ultrasonic sensor"  
  },  
  "description_fr": {  
    "type": "Property",  
    "value": "Capteur electromagnetique et ultrasons"  
  },  
  "user": {  
    "type": "Property",  
    "value": "urn:ngsi-ld:User:abcdef"  
  },  
  "purpose": {  
    "type": "Property",  
    "value": "Detecting the presence of a vehicle on a parking slot."  
  },  
  "purpose_fr": {  
    "type": "string",  
    "value": "Detecter la presence d'un vehicule sur une place de parc."  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "recipientList": {  
    "type": "Property",  
    "value": [  
      "urn:ngsi-ld:User:CommunalAdministration",  
      "urn:ngsi-ld:User:Motorists"  
    ]  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "ngsi-ld:city:CityofCarouge"  
    ]  
  },  
  "isPersonalData": {  
    "type": "Property",  
    "value": "false"  
  },  
  "retentionPeriod": {  
    "type": "Property",  
    "value": "< 1 month"  
  },  
  "legitimateInterest": {  
    "type": "Property",  
    "value": "Facilitate and understand parking habits"  
  },  
  "crossborderTransfer": {  
    "type": "Property",  
    "value": "None"  
  },  
  "image": {  
    "type": "Property",  
    "value": "http://www.example.com/device1.jpg"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。