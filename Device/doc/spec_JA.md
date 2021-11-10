エンティティデバイス  
==========  
[オープンライセンス](https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**特定のタスク（環境を感知する、作動するなど）を達成することを目的とした装置（ハードウェア＋ソフトウェア＋ファームウェア）のこと。  
バージョン: 0.0.6  

## プロパティのリスト  

- `address`: 郵送先住所  - `alternateName`: このアイテムの別称  - `areaServed`: サービスや提供されるアイテムが提供される地理的なエリア  - `batteryLevel`: デバイスのバッテリーレベル。バッテリーが満タンの場合は1.0、空の場合は0.0となります。0.0はバッテリーが空のとき。一時的に判断できない場合は-1。  - `category`: センサー。光、動き、温度変化など、物理的環境における事象や変化を検出し、応答する装置。https://w3id.org/saref#Sensor. アクチュエータ : メカニズムやシステムを動かしたり、制御したりする役割を担う装置。https://w3id.org/saref#Actuator.計器 : 人間が読める形で量を正確に検出し、表示するために作られた装置のこと。SAREFで一部定義されている。HVAC : 室内環境の快適さを提供する暖房、換気、空調（HVAC）機器。https://w3id.org/saref#HVAC。ネットワーク : LANやセンサーネットワークにおけるハブ、スイッチ、ルーターなど、ネットワーク内で他の機器を接続するための装置。(https://w3id.org/saref#Network。マルチメディア。音声、画像、アニメーション、ビデオなどのマルチメディアコンテンツを表示、保存、記録、再生するための装置。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'.  - `configuration`: デバイスの技術的設定。この属性は、デバイスの設定に関連するパラメータ（タイムアウト、レポート期間など）をキャプチャするプロパティとその値の配列を意図しており、このモデルで定義された標準的な属性では現在カバーされていません。  - `controlledAsset`: 本機が制御するアセット（建物、物体など）のリスト。  - `controlledProperty`: 感知、測定、制御が可能なもの。イナム。'airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity,noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateFirstUsed`: デバイスが初めて使用された日時を示すタイムスタンプ。  - `dateInstalled`: デバイスがインストールされたことを示すタイムスタンプ（インストールが必要な場合）。  - `dateLastCalibration`: デバイスの最後のキャリブレーションがいつ行われたかを示すタイムスタンプです。  - `dateLastValueReported`: デバイスがクラウドへのデータ報告に成功した最後の時間を示すタイムスタンプ。  - `dateManufactured`: デバイスがいつ製造されたかを示すタイムスタンプ。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateObserved`: ユーザーによって定義された、観測されたエンティティの日付。  - `depth`: 本機の位置を、出発点からの深さで表したもの。単位はすべて[CEFACT](https://www.unece.org/cefact.html)のコードで受け付けます。  - `description`: このアイテムの説明  - `deviceState`: このデバイスの運用面での状態。この値はベンダーに依存します。  - `direction`: Enum:'Inlet, Outlet, Entry, Exit'.デバイスがインストールされた時刻を示すタイムスタンプ（インストールが必要な場合）。  - `distance`: 本機の位置を、出発点からの距離で表したもの。単位はすべて[CEFACT](https://www.unece.org/cefact.html)のコードで受け付けています。  - `dstAware`: 夏時間を認識しているデバイスを示す（True）。夏時間を認識している場合、タイムスタンプは夏時間の変更を反映してデバイスによって自動的に調整されます。そうでない場合（False）は、ユーザーが時間調整を行う必要があります。  - `firmwareVersion`: 本機のファームウェアのバージョン。  - `hardwareVersion`: 本機のハードウェアバージョンです。  - `id`: エンティティのユニークな識別子  - `ipAddress`: デバイスのIPアドレスのリスト。デバイスが複数のIPアドレスを持っている場合は、カンマで区切ったリストにすることができます。  - `location`: アイテムへのGeojson参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygonのいずれかです。  - `macAddress`: 機器のMACアドレスです。  - `mcc`: 本プロパティは、携帯電話の国番号を示す。  - `mnc`: 本プロパティは、機器が接続されているネットワークのモバイルネットワークコード（MNC） を示す。MNCは、GSM、CDMA、iDEN、TETRA、3G/4Gの公営陸上移動体通信網や一部の衛星移動体通信網を利用する携帯電話事業者を一意に識別するために、MCC（Mobile Country Code）と組み合わせて使用される（「MCC / MNCタプル」とも呼ばれる）。  - `name`: このアイテムの名前です。  - `osVersion`: ホストOSデバイスのバージョンです。  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `provider`: デバイスの提供者です。  - `refDeviceModel`: デバイスのモデル  - `relativePosition`: このデバイスの座標系における位置は、そのローカルな配置に従っています。  - `rssi`: ワイヤレス対応機器の受信信号強度表示。単位は dBm または mW で、ユニットコードを使用して設定します。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `serialNumber`: メーカーから割り当てられたシリアルナンバー。  - `softwareVersion`: 本機のソフトウェアのバージョン。  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `supportedProtocol`: 対応するプロトコルやネットワーク  - `type`: NGSIのEntityタイプ。デバイスである必要があります。  - `value`: 観察された値または報告された値。アクチュエータデバイスの場合は、制御アプリケーションがアクチュエータの設定を変更するための属性です。例えば、現在_on_であるスイッチ・デバイスは、'Text'タイプの値'on'を報告することができる。明らかに、参照されたスイッチを切り替えるためには、この属性値を'off'に変更する必要があります。    
必須項目  
- `controlledProperty`  - `id`  - `type`    
デバイスとは、何らかのロジックを含み、データの生成・消費を行う有形の物体です。デバイスは、常にネットワークを介して電子的に通信することができると想定されています。このデータモデルは、移動体通信事業者および[GSMA](https://www.gsma.com/iot/iot-big-data/)の協力を得て一部作成されました。このデータモデルは、[ETSI](http://www.etsi.org)規格の一部である[SAREF Ontology](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf)に由来する概念を再利用しています。  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Device:    
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'    
  modelTags: ""    
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
    batteryLevel:    
      description: 'Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined.'    
      oneOf:    
        - maximum: 1    
          minimum: 0    
          type: number    
        - const: -1    
          type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    configuration:    
      description: 'Device''s technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model.'    
      items:    
        properties:    
          parameter:    
            type: string    
          value:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    controlledAsset:    
      description: 'List of the asset(s) (building, object, etc.) controlled by the device.'    
      items:    
        oneOf:    
          - format: uri    
            type: string    
          - anyOf: &device_-_properties_-_id_-_anyof    
              - description: 'Property. Identifier format of any NGSI entity'    
                maxLength: 256    
                minLength: 1    
                pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
                type: string    
              - description: 'Property. Identifier format of any NGSI entity'    
                format: uri    
                type: string    
            description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    dateFirstUsed:    
      description: 'A timestamp which denotes when the device was first used.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateInstalled:    
      description: 'A timestamp which denotes when the device was installed (if it requires installation).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastCalibration:    
      description: 'A timestamp which denotes when the last calibration of the device happened.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateLastValueReported:    
      description: 'A timestamp which denotes the last time when the device successfully reported data to the cloud.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateManufactured:    
      description: 'A timestamp which denotes when the device was manufactured.'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/DateTime    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateObserved:    
      description: 'Date of the observed entity defined by the user.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    depth:    
      description: 'Location of this device represented by a depth from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: number    
      x-ngsi:    
        model: https://schema.org/depth    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    deviceState:    
      description: 'State of this device from an operational point of view. Its value can be vendor dependent.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    direction:    
      description: 'Enum:''Inlet, Outlet, Entry, Exit''. A timestamp which denotes when the device was installed (if it requires installation).'    
      enum:    
        - Inlet    
        - Outlet    
        - Entry    
        - Exit    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/DateTime'    
        type: Property    
    distance:    
      description: 'Location of this device represented by a distance from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Distance    
        type: Property    
    dstAware:    
      description: 'Indicates a device which is Daylight Savings Time Aware (True). In case it is then the Timestamp is automatically adjusted by the device to reflect DST changes. If not (False) the time adjustments must be taken care of by the user.'    
      type: boolean    
      x-ngsi:    
        type: Property    
    firmwareVersion:    
      description: 'The firmware version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hardwareVersion:    
      description: 'The hardware version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: *device_-_properties_-_id_-_anyof    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    ipAddress:    
      description: 'List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address.'    
      items:    
        oneOf:    
          - format: ipv4    
          - format: ipv6    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
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
    macAddress:    
      description: 'The MAC address of the device.'    
      pattern: ^([[A-Fa-f0-9]]{2}[:.-]?){5}[[A-Fa-f0-9]]{2}$    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    mcc:    
      description: 'This property identifies the Mobile Country Code'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    mnc:    
      description: 'This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a ''MCC / MNC tuple'') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    osVersion:    
      description: 'The version of the host operating system device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *device_-_properties_-_id_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    provider:    
      description: 'The provider of the device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/provider    
        type: Property    
    refDeviceModel:    
      description: 'Model of the device'    
      oneOf:    
        - format: uri    
          type: string    
        - anyOf: *device_-_properties_-_id_-_anyof    
          description: 'Property. Unique identifier of the entity'    
      x-ngsi:    
        type: Relationship    
    relativePosition:    
      description: 'Location of this device in a coordinate system according to its local emplacement.'    
      type: string    
      x-ngsi:    
        type: Property    
    rssi:    
      description: 'Received signal strength indicator for a wireless enabled device. It must be expressed in dBm or mW, use unitcode to set it out. '    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
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
    serialNumber:    
      description: 'The serial number assigned by the manufacturer.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/serialNumber    
        type: Property    
    softwareVersion:    
      description: 'The software version of this device.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    type:    
      description: 'NGSI Entity type. It has to be Device'    
      enum:    
        - Device    
      type: string    
      x-ngsi:    
        type: Property    
    value:    
      description: 'A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value ''on'' of type ''Text''. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to ''off''.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/QuantitativeValue    
        type: Property    
  required:    
    - id    
    - type    
    - controlledProperty    
  type: object    
  version: 0.0.6    
```  
</details>    
## ペイロードの例  
#### デバイス NGSI-v2 キー・バリューの例  
Deviceをkey-valuesとしてJSON-LD形式で出力した例です。これは`options=keyValues`を使用した場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": [  
    "sensor"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "controlledAsset": [  
    "wastecontainer-Osuna-100"  
  ],  
  "ipAddress": [  
    "192.14.56.78"  
  ],  
  "mcc": "214",  
  "mnc": "07",  
  "batteryLevel": 0.75,  
  "serialNumber": "9845A",  
  "refDeviceModel": "myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "deviceState": "ok",  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "owner": [  
    "http://person.org/leon"  
  ]  
}  
```  
#### デバイス NGSI-v2 正規化例  
ここでは、JSON-LD形式のDeviceを正規化した例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "category": {  
    "type": "Text",  
    "value": [  
      "sensor"  
    ]  
  },  
  "batteryLevel": {  
    "type": "Number",  
    "value": 0.75  
  },  
  "dateFirstUsed": {  
    "type": "DateTime",  
    "value": "2014-09-11T11:00:00Z"  
  },  
  "controlledAsset": {  
    "type": "Relationship",  
    "value": [  
      "wastecontainer-Osuna-100"  
    ]  
  },  
  "serialNumber": {  
    "type": "Text",  
    "value": "9845A"  
  },  
  "mcc": {  
    "type": "Text",  
    "value": "214"  
  },  
  "value": {  
    "type": "Text",  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "refDeviceModel": {  
    "type": "Relationship",  
    "value": "myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "type": "Number",  
    "value": 0.86  
  },  
  "controlledProperty": {  
    "type": "array",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "owner": {  
    "type": "array",  
    "value": [  
      "http://person.org/leon"  
    ]  
  },  
  "mnc": {  
    "type": "Text",  
    "value": "07"  
  },  
  "ipAddress": {  
    "type": "array",  
    "value": [  
      "192.14.56.78"  
    ]  
  },  
  "deviceState": {  
    "type": "Text",  
    "value": "ok"  
  }  
}  
```  
#### デバイス NGSI-LD のキーバリューの例  
Deviceをkey-valuesとしてJSON-LD形式で出力した例です。これは、`options=keyValues`を使用した場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "category": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "batteryLevel": 0.75,  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "controlledAsset": [  
    "urn:ngsi-ld::wastecontainer-Osuna-100"  
  ],  
  "serialNumber": "9845A",  
  "mcc": "214",  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "refDeviceModel": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "owner": [  
    "http://person.org/leon"  
  ],  
  "mnc": "07",  
  "ipAddress": [  
    "192.14.56.78"  
  ],  
  "deviceState": "ok",  
  "distance": 20,  
  "depth": 3,  
  "direction": "Outlet",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### デバイス NGSI-LDの正規化例  
ここでは、JSON-LD形式のDeviceを正規化した例を示します。これは、オプションを使用しない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": {  
    "type": "Property",  
    "value": 0.75  
  },  
  "category": {  
    "type": "Property",  
    "value": [  
      "sensor"  
    ]  
  },  
  "controlledAsset": {  
    "type": "Relationship",  
    "object": [  
      "urn:ngsi-ld::wastecontainer-Osuna-100"  
    ]  
  },  
  "controlledProperty": {  
    "type": "Property",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "dateFirstUsed": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2014-09-11T11:00:00Z"  
    }  
  },  
  "deviceState": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "ipAddress": {  
    "type": "Property",  
    "value": [  
      "192.14.56.78"  
    ]  
  },  
  "mcc": {  
    "type": "Property",  
    "value": "214"  
  },  
  "mnc": {  
    "type": "Property",  
    "value": "07"  
  },  
  "owner": {  
    "type": "Property",  
    "value": [  
      "http://person.org/leon"  
    ]  
  },  
  "refDeviceModel": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "type": "Property",  
    "value": 0.86  
  },  
  "serialNumber": {  
    "type": "Property",  
    "value": "9845A"  
  },  
  "value": {  
    "type": "Property",  
    "value": "l%3D0.22%3Bt%3D21.2"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld",  
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"  
  ]  
}  
```  
