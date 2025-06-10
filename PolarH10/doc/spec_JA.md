<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティPolarH10  
==============<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Device/blob/master/PolarH10/LICENSE.md)  
[文書が自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**RR、HRV、HR、ECGを備えたPolar H10心拍センサーのデータモデル**。  
バージョン: 0.1.0  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `acc[array]`: サンプル・レート25Hz、50Hz、100Hz、200Hz、レンジ2G、4G、8Gの加速度計データ。軸別加速度データ（単位：mG）。  - `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。    
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 公道上の特定の物件を特定する番号    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `clientId[string]`: クライアントID  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `deviceId[string]`: デバイスID  - `ecg[array]`: 心電図（ECG）データ（μV、サンプルレート130Hz）。  - `hr[number]`: 心拍数（HR）（1秒サンプル時間または5秒サンプル時間  - `hrv[number]`: 心拍変動（HRV） 心拍変動  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `rr[array]`: 連続する心拍の間隔（RR）（単位：ms  - `sampleRate[number]`: データ取得率  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `sensorTimeStamp[number]`: センサー・タイムスタンプ  - `sessionId[number]`: セッションID  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `timeStamp[number]`: 電話のタイムスタンプ  - `type[string]`: NGSIエンティティタイプ。PolarH10TopicACCでなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必須プロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順（クリックで詳細表示）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PolarH10:    
  description: A Data Model of Polar H10 Heart Rate Sensor with RR, HRV, HR, and ECG    
  properties:    
    acc:    
      description: Accelerometer data with sample rates of 25Hz, 50Hz, 100Hz and 200Hz and range of 2G, 4G and 8G. Axis specific acceleration data in mG.    
      items:    
        description: Each of the measurement of the accelerometer    
        items:    
          description: Each of the measurement of the accelerometer in the X, Y, Z coordinates    
          type: integer    
          x-ngsi:    
            type: Property    
        maxItems: 3    
        minItems: 3    
        type: array    
        x-ngsi:    
          type: Property    
      maxItems: 36    
      minItems: 36    
      type: array    
      x-ngsi:    
        type: Property    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: The country. For example, Spain    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: The locality in which the street address is, and which is in the region    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: The region in which the locality is, and which is in the country    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: A district is a type of administrative division that, in some countries, is managed by the local government    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: The post office box number for PO box addresses. For example, 03578    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: The postal code. For example, 24004    
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
    clientId:    
      description: Client ID    
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
    deviceId:    
      description: Device ID    
      type: string    
      x-ngsi:    
        type: Property    
    ecg:    
      description: Electrocardiography (ECG) data in µV with sample rate 130Hz.    
      items:    
        description: Each of the ECG measurements    
        type: integer    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    hr:    
      description: Heart Rate (HR) with one second sample time or with five second sample time    
      type: number    
      x-ngsi:    
        type: Property    
    hrv:    
      description: Heart Rate Variability (HRV) heart rate variability    
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
        type: Relationship    
    location:    
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon    
      oneOf:    
        - description: Geojson reference to the item. Point    
          properties:    
            bbox:    
              description: BBox of the  Point    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Point    
              items:    
                type: number    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the LineString    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the Polygon    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the Polygon    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MulitPoint    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: BBox coordinates of the LineString    
              items:    
                type: number    
              minItems: 4    
              type: array    
              x-ngsi:    
                type: Property    
            coordinates:    
              description: Coordinates of the MultiLineString    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
              x-ngsi:    
                type: Property    
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
              description: Coordinates of the MultiPolygon    
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
              x-ngsi:    
                type: Property    
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
          type: Relationship    
      type: array    
      x-ngsi:    
        type: Property    
    rr:    
      description: Intervals between successive heartbeats (RR) in ms    
      items:    
        description: Each of the measurements of the RR    
        type: integer    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    sampleRate:    
      description: Data acquisition rate    
      type: number    
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
    sensorTimeStamp:    
      description: Sensor Timestamp    
      type: number    
      x-ngsi:    
        type: Property    
    sessionId:    
      description: Session ID    
      type: number    
      x-ngsi:    
        type: Property    
    source:    
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    timeStamp:    
      description: Phone Timestamp    
      type: number    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be PolarH10TopicACC    
      enum:    
        - PolarH10    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - type    
    - id    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/PolarH10/LICENSE.md    
  x-model-schema: https://github.com/smart-data-models/dataModel.Device/tree/master/PolarH10/schema.json    
  x-model-tags: P2CODE    
  x-version: 0.1.0    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### PolarH10 NGSI-v2 キー値の例  
以下は、PolarH10をJSON-LD形式でkey-valuesとした例である。options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PolarH10:47542370",  
  "type": "PolarH10",  
  "clientId": "user123",  
  "deviceId": "polar-h10-001",  
  "sessionId": 12345,  
  "sampleRate": 100,  
  "timeStamp": 1656633600,  
  "sensorTimeStamp": 1656633601,  
  "acc": [  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 12, 22, 32 ]  
  ],  
  "hr": 75,  
  "hrv": 50.5,  
  "rr": [  
    800,  
    810,  
    820,  
    830,  
    840,  
    850,  
    860,  
    870,  
    880,  
    890  
  ],  
  "ecg": [  
    104,  
    116,  
    116,  
    111,  
    111,  
    92,  
    72,  
    194,  
    478,  
    733,  
    687,  
    199,  
    -267,  
    -153,  
    126,  
    94,  
    41,  
    99,  
    99,  
    97,  
    128,  
    128,  
    133,  
    145,  
    131,  
    138,  
    179,  
    191,  
    179,  
    196,  
    223,  
    216,  
    235,  
    276,  
    289,  
    296,  
    313,  
    303,  
    315,  
    354,  
    352,  
    327,  
    306,  
    264,  
    213,  
    177,  
    140,  
    102,  
    65,  
    41,  
    29,  
    29,  
    41,  
    53,  
    51,  
    38,  
    41,  
    53,  
    63,  
    75,  
    94,  
    89,  
    65,  
    68,  
    85,  
    80,  
    87,  
    99,  
    89,  
    89,  
    109,  
    109,  
    92  
  ]  
}  
```  
</details>  
#### PolarH10 NGSI-v2 正規化例  
以下は、正規化されたJSON-LD形式のPolarH10の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PolarH10:47542370",  
    "type": "PolarH10",  
    "clientId": {  
        "type": "Text",  
        "value": "user123"  
    },  
    "deviceId": {  
        "type": "Text",  
        "value": "polar-h10-001"  
    },  
    "sessionId": {  
        "type": "Number",  
        "value": 12345  
    },  
    "sampleRate": {  
        "type": "Number",  
        "value": 100  
    },  
    "timeStamp": {  
        "type": "Number",  
        "value": 1656633600  
    },  
    "sensorTimeStamp": {  
        "type": "Number",  
        "value": 1656633601  
    },  
    "acc": {  
        "type": "Array",  
        "value": [  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 12, 22, 32 ]  
        ]  
    },  
    "hr": {  
        "type": "Number",  
        "value": 75.5  
    },  
    "hrv": {  
        "type": "Number",  
        "value": 50  
    },  
    "rr": {  
        "type": "Array",  
        "value": [  
            800,  
            810,  
            820,  
            830,  
            840,  
            850,  
            860,  
            870,  
            880,  
            890  
        ]  
    },  
    "ecg": {  
        "type": "Array",  
        "value": [  
            104,  
            116,  
            116,  
            111,  
            111,  
            92,  
            72,  
            194,  
            478,  
            733,  
            687,  
            199,  
            -267,  
            -153,  
            126,  
            94,  
            41,  
            99,  
            99,  
            97,  
            128,  
            128,  
            133,  
            145,  
            131,  
            138,  
            179,  
            191,  
            179,  
            196,  
            223,  
            216,  
            235,  
            276,  
            289,  
            296,  
            313,  
            303,  
            315,  
            354,  
            352,  
            327,  
            306,  
            264,  
            213,  
            177,  
            140,  
            102,  
            65,  
            41,  
            29,  
            29,  
            41,  
            53,  
            51,  
            38,  
            41,  
            53,  
            63,  
            75,  
            94,  
            89,  
            65,  
            68,  
            85,  
            80,  
            87,  
            99,  
            89,  
            89,  
            109,  
            109,  
            92  
        ]  
    }  
}  
```  
</details>  
#### PolarH10 NGSI-LD キー値の例  
以下は、PolarH10をJSON-LD形式でkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PolarH10:47542370",  
  "type": "PolarH10",  
  "clientId": "user123",  
  "deviceId": "polar-h10-001",  
  "sessionId": 12345,  
  "sampleRate": 100,  
  "timeStamp": 1656633600,  
  "sensorTimeStamp": 1656633601,  
  "acc": [  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 10, 20, 30 ],  
    [ 11, 21, 31 ],  
    [ 12, 22, 32 ],  
    [ 12, 22, 32 ]  
  ],  
  "hr": 75,  
  "hrv": 50.5,  
  "rr": [  
    800,  
    810,  
    820,  
    830,  
    840,  
    850,  
    860,  
    870,  
    880,  
    890  
  ],  
  "ecg": [  
    104,  
    116,  
    116,  
    111,  
    111,  
    92,  
    72,  
    194,  
    478,  
    733,  
    687,  
    199,  
    -267,  
    -153,  
    126,  
    94,  
    41,  
    99,  
    99,  
    97,  
    128,  
    128,  
    133,  
    145,  
    131,  
    138,  
    179,  
    191,  
    179,  
    196,  
    223,  
    216,  
    235,  
    276,  
    289,  
    296,  
    313,  
    303,  
    315,  
    354,  
    352,  
    327,  
    306,  
    264,  
    213,  
    177,  
    140,  
    102,  
    65,  
    41,  
    29,  
    29,  
    41,  
    53,  
    51,  
    38,  
    41,  
    53,  
    63,  
    75,  
    94,  
    89,  
    65,  
    68,  
    85,  
    80,  
    87,  
    99,  
    89,  
    89,  
    109,  
    109,  
    92  
  ],  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/refs/heads/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PolarH10 NGSI-LD 正規化例  
以下は、正規化されたJSON-LDフォーマットのPolarH10の例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PolarH10:47542370",  
    "type": "PolarH10",  
    "clientId": {  
        "type": "Property",  
        "value": "user123"  
    },  
    "deviceId": {  
        "type": "Property",  
        "value": "polar-h10-001"  
    },  
    "sessionId": {  
        "type": "Property",  
        "value": 12345  
    },  
    "sampleRate": {  
        "type": "Property",  
        "value": 100  
    },  
    "timeStamp": {  
        "type": "Property",  
        "value": 1656633600  
    },  
    "sensorTimeStamp": {  
        "type": "Property",  
        "value": 1656633601  
    },  
    "acc": {  
        "type": "Property",  
        "value": [  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 10, 20, 30 ],  
            [ 11, 21, 31 ],  
            [ 12, 22, 32 ],  
            [ 12, 22, 32 ]  
        ]  
    },  
    "hr": {  
        "type": "Property",  
        "value": 75.5  
    },  
    "hrv": {  
        "type": "Property",  
        "value": 50  
    },  
    "rr": {  
        "type": "Property",  
        "value": [  
            800,  
            810,  
            820,  
            830,  
            840,  
            850,  
            860,  
            870,  
            880,  
            890  
        ]  
    },  
    "ecg": {  
        "type": "Property",  
        "value": [  
            104,  
            116,  
            116,  
            111,  
            111,  
            92,  
            72,  
            194,  
            478,  
            733,  
            687,  
            199,  
            -267,  
            -153,  
            126,  
            94,  
            41,  
            99,  
            99,  
            97,  
            128,  
            128,  
            133,  
            145,  
            131,  
            138,  
            179,  
            191,  
            179,  
            196,  
            223,  
            216,  
            235,  
            276,  
            289,  
            296,  
            313,  
            303,  
            315,  
            354,  
            352,  
            327,  
            306,  
            264,  
            213,  
            177,  
            140,  
            102,  
            65,  
            41,  
            29,  
            29,  
            41,  
            53,  
            51,  
            38,  
            41,  
            53,  
            63,  
            75,  
            94,  
            89,  
            65,  
            68,  
            85,  
            80,  
            87,  
            99,  
            89,  
            89,  
            109,  
            109,  
            92  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/refs/heads/master/context.jsonld"  
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
