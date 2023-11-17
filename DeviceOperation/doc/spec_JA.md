<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティデバイス操作    
============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Device/blob/master/DeviceOperation/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバル記述：**このエンティティには、汎用デバイス操作エンティティの調和された記述が含まれる。デバイス操作エンティティは、デバイスによって報告される動的データを含むため、すべての IoT セグメントおよび関連する IoT アプリケーションに適用可能である。    
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
- `addressedAt[date-time]`: イベントまたはフォルトがアドレスされた、またはクリアされたタイムスタンプ  - `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `device[*]`: このデバイス操作に関連するデバイスへの参照。  - `endedAt[date-time]`: 操作が実際に終了したタイムスタンプ  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `name[string]`: このアイテムの名前  - `operationType[string]`: 列挙されたリストからの選択  . Model: [event, maintenance, fault, installation, upgrade, other](event, maintenance, fault, installation, upgrade, other)- `operator[*]`: 運航を実施するオペレーターに関する言及  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `plannedEndAt[date-time]`: 操作の終了予定日/タイムスタンプ。これは助言的なものであり、実際の操作の終了時刻は計画された終了時刻の前後になる可能性があることに注意。  - `plannedStartAt[date-time]`: 予定されている操作の開始日/タイムスタンプ。これは助言的なものであり、実際の操作開始時刻は計画された開始時刻の前後になる可能性があることに注意してください。  - `reportedAt[date-time]`: イベント/障害が報告されたときのタイムスタンプ  - `result[string]`: 操作の結果。Enum:'OK、中止、失敗'  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `startedAt[date-time]`: 実際に操作が開始されたタイムスタンプ  - `status[string]`: ステータスを表す列挙リストからの選択。列挙:'計画中、進行中、終了、予定、キャンセル'  - `type[string]`: NGSI エンティティ識別子。これは DeviceOperation でなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
<!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
デバイスとは、何らかのロジックを含み、データのプロデューサおよび/またはコンシューマである有形物体のことである。デバイスは常に、ネットワークを介して電子的に通信できるものとする。このデータモデルは、携帯電話事業者および[GSMA](https://www.gsma.com/iot/iot-big-data/)との協力により部分的に開発された。このデータモデルは、[ETSI](http://www.etsi.org)標準の[SAREFオントロジー](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf)の一部から来た概念を再利用している。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
DeviceOperation:      
  description: This entity contains a harmonised description of a generic device operation entity. The device operation entity contains dynamic data reported by a device and is therefore applicable to all IoT segments and related IoT applications.      
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
    addressedAt:      
      description: The timestamp when an event or fault was addressed or cleared      
      format: date-time      
      type: string      
      x-ngsi:      
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
    device:      
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
      description: A reference to the associated Device for this device operation      
      x-ngsi:      
        type: Relationship      
    endedAt:      
      description: Timestamp when the operation actually finished      
      format: date-time      
      type: string      
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
    operationType:      
      description: A choice from an enumerated list      
      enum:      
        - event      
        - fault      
        - installation      
        - maintenance      
        - other      
        - upgrade      
      type: string      
      x-ngsi:      
        model: 'event, maintenance, fault, installation, upgrade, other'      
        type: Property      
    operator:      
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
      description: Reference to the operator conducting the operation      
      x-ngsi:      
        type: Relationship      
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
    plannedEndAt:      
      description: The planned end date/timestamp for the operation. Note that this is advisory and the actual time the operation finishes may be before or after the planned end      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    plannedStartAt:      
      description: The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    reportedAt:      
      description: Timestamp when the event/ fault was reported      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    result:      
      description: 'The result of the operation. Enum:''ok, aborted, failed'''      
      enum:      
        - aborted      
        - failed      
        - ok      
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
    startedAt:      
      description: Timestamp when the operation actually started to be performed      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    status:      
      description: 'A choice from an enumerated list describing the status. Enum:''planned, ongoing, finished, scheduled, cancelled'''      
      enum:      
        - cancelled      
        - finished      
        - ongoing      
        - planned      
        - scheduled      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: NGSI Entity identifier. It has to be DeviceOperation      
      enum:      
        - DeviceOperation      
      type: string      
      x-ngsi:      
        type: Property      
  required: []      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/DeviceOperation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/DeviceOperation/schema.json      
  x-model-tags: GSMA      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### DeviceOperation NGSI-v2 キー値の例    
JSON-LD形式のDeviceOperationのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "device": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
  "operationType": "fault",  
  "description": "Backup battery needs replacement",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "ongoing",  
  "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "addressedAt": "2016-08-28T10:18:16Z"  
}  
```  
</details>    
#### デバイス操作 NGSI-v2 正規化例    
以下は、正規化されたJSON-LDフォーマットのDeviceOperationの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "device": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "operationType": {  
    "type": "Text",  
    "value": "fault"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Backup battery needs replacement"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "plannedEndAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "status": {  
    "type": "Text",  
    "value": "ongoing"  
  },  
  "operator": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "reportedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "addressedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  }  
}  
```  
</details>    
#### DeviceOperation NGSI-LD キー値の例    
以下は、DeviceOperationをJSON-LD形式でkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "addressedAt": "2016-08-28T10:18:16Z",  
  "dataProvider": "https://provider.example.com",  
  "description": "Backup battery needs replacement",  
  "device": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "operationType": "fault",  
  "operator": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "reportedAt": "2016-08-28T10:18:16Z",  
  "result": "ok",  
  "source": "https://source.example.com",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "status": "ongoing",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### デバイス操作 NGSI-LD 正規化例    
以下は、正規化されたJSON-LDフォーマットのDeviceOperationの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:DeviceOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "DeviceOperation",  
  "addressedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Backup battery needs replacement"  
  },  
  "device": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Device:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "endedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "operationType": {  
    "type": "Property",  
    "value": "fault"  
  },  
  "operator": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Person:fe018d4e-46f8-11e8-ae6b-df5577f85836"  
  },  
  "plannedEndAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "plannedStartAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "reportedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "result": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "startedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "status": {  
    "type": "Property",  
    "value": "ongoing"  
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
