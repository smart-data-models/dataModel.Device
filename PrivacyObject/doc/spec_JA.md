<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティプライバシーオブジェクト  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Device/blob/master/PrivacyObject/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**IoT デバイスのプライバシーに関する情報**。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `category[array]`: センサー：光、動き、温度変化など、物理的環境における出来事や変化を検出し、それに応答する装置。https://w3id.org/saref#Sensor。 アクチュエーター : 機構やシステムを動かしたり、制御したりする役割を担う装置。https://w3id.org/saref#Actuator。メーター（Meter）：量を正確に検出し、人間が読み取り可能な形で表示するために作られた装置。SAREFによって部分的に定義されている。HVAC : 室内環境の快適性を提供する暖房、換気、空調（HVAC）装置。https://w3id.org/saref#HVAC。ネットワーク : LANまたはセンサーネットワークにおけるハブ、スイッチ、ルーターなど、ネットワーク内の他の機器を接続するために使用される装置。(https://w3id.org/saref#Network.マルチメディア：音声、画像、アニメーション、ビデオなどのマルチメディア・コンテンツを表示、保存、記録、再生するために設計された装置。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'.未加工のカテゴリは非推奨となります。カテゴリという名前の他のaqttributesとの衝突を避けるために、代わりにdeviceCategoryを使用してください。  . Model: [https://schema.org/Text](https://schema.org/Text)- `crossborderTransfer[string]`: 事業体に関連するクロスボーダー移転に関する表示  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `floor[number]`: ビル内またはそれに準ずる場所で、装置が設置されているフロア  - `id[*]`: エンティティの一意識別子  - `image[uri]`: 商品の画像  . Model: [https://schema.org/URL](https://schema.org/URL)- `isIndoor[boolean]`: 実体が屋内に設置されているか屋外に設置されているかを示すフラグ  - `isPersonalData[boolean]`: 事業体が個人データを提供しているか、または個人データを含んでいるかを示すフラグ  - `legitimateInterest[string]`: 事業体に関連する正当な利益。これは、データ収集がどのような高レベルの最終目的のために行われるかを意味する。  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `purpose[string]`: データ収集の目的  - `recipientList[array]`: 受信者を含むリスト。受信者は、センサーによって生成されたデータを使用する受益者である。各受領者は、その一意な識別を可能にするURIによって表される。プライバシー:'Low'  . Model: [https://schema.org/URL](https://schema.org/URL)- `refDevice[*]`: ソースデータセットからの一意の識別子  - `retentionPeriod[string]`: データ保持期間  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `type[string]`: NGSI タイププロパティ。これは PrivacyObject でなければなりません。  - `user[uri]`: 匿名ユーザーの識別子。この識別子は実際にはユニークなURNであり、匿名ユーザーを認識するために使用できます。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
PrivacyObjectエンティティは、このIoTデバイスに直接リンクされたプライバシーに関する情報を持つIoTデバイス（典型的にはセンサー）を表す。プライバシーの文脈でIoTデバイスを記述するために、いくつかの属性が使用される。特に、ある属性はIoTデバイスの位置を提供し、他の2つの属性は正確な位置に関する詳細情報を提供する。属性はまた、IoTデバイスを説明するために使用され、2番目の属性はIoTセンサーの目的を与える。他の属性は、IoTデバイスに関連する情報を分類する目的で、プライバシーとGDPRに非常に重点を置いている。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
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
## ペイロードの例  
#### プライバシーオブジェクト NGSI-v2 キー値の例  
以下は、PrivacyObjectをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### プライバシーオブジェクト NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のPrivacyObjectの例である。これはNGSI-v2と互換性があり、オプションを使用しない場合、個々のエンティティのコンテキストデータを返します。  
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
#### プライバシーオブジェクト NGSI-LD キー値の例  
PrivacyObjectをJSON-LD形式でkey-valuesとした例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### プライバシーオブジェクト NGSI-LD 正規化例  
以下は、正規化されたJSON-LD形式のPrivacyObjectの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
