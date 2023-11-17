<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティデバイス    
==========<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**特定のタスク（環境の感知、作動など）を達成するための装置（ハードウェア＋ソフトウェア＋ファームウェア）。    
バージョン: 0.0.8    
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[*]`: デバイスのバッテリー残量。バッテリーが満タンの場合は1.0。バッテリーが空の場合は0.0。過渡的に決定できない場合は-1  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: センサー：光、動き、温度変化など、物理的環境における出来事や変化を検出し、それに応答する装置。https://w3id.org/saref#Sensor。 アクチュエーター : 機構やシステムを動かしたり、制御したりする役割を担う装置。https://w3id.org/saref#Actuator。メーター（Meter）：量を正確に検出し、人間が読み取り可能な形で表示するために作られた装置。SAREFによって部分的に定義されている。HVAC : 室内環境の快適性を提供する暖房、換気、空調（HVAC）装置。https://w3id.org/saref#HVAC。ネットワーク : LANまたはセンサーネットワークにおけるハブ、スイッチ、ルーターなど、ネットワーク内の他の機器を接続するために使用される装置。(https://w3id.org/saref#Network.マルチメディア：音声、画像、アニメーション、ビデオなどのマルチメディア・コンテンツを表示、保存、記録、再生するために設計された装置。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'.未加工のカテゴリは非推奨となります。カテゴリという名前の他のaqttributesとの衝突を避けるために、代わりにdeviceCategoryを使用してください。  . Model: [https://schema.org/Text](https://schema.org/Text)- `configuration[array]`: デバイスの技術構成。この属性は、デバイスの設定（タイムアウト、報告期間など）に関係し、このモデルで定義された標準属性では現在カバーされていないパラメータを捕捉する配列プロパティとその値を意図しています。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `controlledAsset[array]`: デバイスが制御するアセット（建物、物体など）のリスト  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlledProperty[array]`: 感知、測定、制御できるもの。列挙する：'大気汚染、大気圧、平均速度、電池寿命、電池供給量、cdom、コンダクタンス、導電率、深度、摂食活動、電力消費、エネルギー、充填レベル、遊離塩素、ガス消費、開門、ヘディング、湿度、光、位置、搾乳、運動、運動活動、noiseLevel、occupancy、orp、pH、power、precipitation、pressure、refractiveIndex、salinity、smoke、soilMoisture、solarRadiation、speed、tds、temperature、trafficFlow、tss、turbidity、waterConsumption、waterFlow、waterLevel、waterPollution、weatherConditions、weight、windDirection、windSpeed'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateFirstUsed[date-time]`: デバイスが最初に使用された日時を示すタイムスタンプ。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateInstalled[date-time]`: デバイスがいつインストールされたかを示すタイムスタンプ（インストールが必要な場合）  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastCalibration[date-time]`: デバイスの最後の較正がいつ行われたかを示すタイムスタンプ。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[date-time]`: デバイスがクラウドへのデータ報告に成功した最後の時刻を示すタイムスタンプ。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateManufactured[date-time]`: デバイスがいつ製造されたかを示すタイムスタンプ。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateObserved[date-time]`: ユーザーが定義した観測されたエンティティの日付  - `depth[number]`: 始点からの深さで表されるこの装置の位置。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コードで受け入れられます。  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: この商品の説明  - `deviceCategory[array]`: センサー：光、動き、温度変化など、物理的環境における出来事や変化を検出し、それに応答する装置。https://w3id.org/saref#Sensor。 アクチュエーター : 機構やシステムを動かしたり、制御したりする役割を担う装置。https://w3id.org/saref#Actuator。メーター（Meter）：量を正確に検出し、人間が読み取り可能な形で表示するために作られた装置。SAREFによって部分的に定義されている。HVAC : 室内環境の快適性を提供する暖房、換気、空調（HVAC）装置。https://w3id.org/saref#HVAC。ネットワーク : LANまたはセンサーネットワークにおけるハブ、スイッチ、ルーターなど、ネットワーク内の他の機器を接続するために使用される装置。(https://w3id.org/saref#Network.マルチメディア：音声、画像、アニメーション、ビデオなどのマルチメディア・コンテンツを表示、保存、記録、再生するために設計された装置。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'.未加工のカテゴリは非推奨となります。カテゴリという名前の他のaqttributesとの衝突を避けるために、代わりにdeviceCategoryを使用してください。  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceState[string]`: このデバイスの動作上の状態。この値はベンダーに依存します。  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction[string]`: Enum:'Inlet, Outlet, Entry, Exit'.デバイスがインストールされた日時を示すタイムスタンプ（インストールが必要な場合）  . Model: [ https://schema.org/DateTime]( https://schema.org/DateTime)- `distance[number]`: 出発点からの距離で表されるこのデバイスの位置。単位はすべて[CEFACT](https://www.unece.org/cefact.html)コードです。  . Model: [https://schema.org/Distance](https://schema.org/Distance)- `dstAware[boolean]`: 夏時間を認識している(True)デバイスを示します。もしそうであれば、夏時間の変更を反映するために、タイムスタンプはデバイスによって自動的に調整されます。そうでない場合(False)、時刻の調整はユーザーが行う必要があります。  - `firmwareVersion[string]`: このデバイスのファームウェアのバージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: このデバイスのハードウェア・バージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意識別子  - `ipAddress[array]`: デバイスのIPアドレスのリスト。デバイスに複数のIPアドレスがある場合は、カンマ区切りの値のリストにすることができます。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `macAddress[string]`: デバイスのMACアドレス  . Model: [https://schema.org/Text](https://schema.org/Text)- `mcc[string]`: このプロパティは、モバイル国コードを識別する。  . Model: [https://schema.org/Text](https://schema.org/Text)- `mnc[string]`: このプロパティは、デバイスが接続されているネットワークの Mobile Network Code（MNC）を識別する。MNCは、GSM、CDMA、iDEN、TETRA、3G / 4G公衆陸上モバイルネットワーク、および一部の衛星モバイルネットワークを使用する携帯電話事業者/キャリアを一意に識別するために、モバイル国コード（MCC）と組み合わせて使用されます（「MCC / MNCタプル」としても知られています）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: このアイテムの名前  - `osVersion[string]`: ホストOSデバイスのバージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `provider[string]`: デバイスの提供者  . Model: [https://schema.org/provider](https://schema.org/provider)- `refDeviceModel[*]`: 装置のモデル  - `relativePosition[string]`: このデバイスの座標系における位置。  - `rssi[number]`: ワイヤレス対応デバイスの受信信号強度インジケーター。dBmまたはmWで表す必要があり、unitcodeを使って設定する。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `serialNumber[string]`: 製造者によって割り当てられたシリアル番号  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `softwareVersion[string]`: このデバイスのソフトウェアのバージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `supportedProtocol[array]`: 対応プロトコルまたはネットワーク  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `type[string]`: NGSI エンティティタイプ。これは Device でなければならない。  - `value[string]`: 観測値または報告値。アクチュエータデバイスの場合、制御アプリケーションが作動設定を変更できるようにする属性である。例えば、現在「オン」になっているスイッチデバイスは、タイプ「テキスト」の値「オン」を報告することができる。明らかに、参照されたスイッチを切り替えるには、この属性値を'off'に変更する必要があります。  . Model: [https://schema.org/QuantitativeValue](https://schema.org/QuantitativeValue)<!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `controlledProperty`  - `id`  - `type`  <!-- /35-RequiredProperties -->    
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
Device:      
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'      
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
    batteryLevel:      
      description: Device battery level. It must be equal to 1.0 when battery is full. 0.0 when battery is empty. -1 when transiently cannot be determined      
      oneOf:      
        - maximum: 1      
          minimum: 0      
          type: number      
        - maximum: -1      
          minimum: -1      
          type: number      
      x-ngsi:      
        model: https://schema.org/Number      
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
    configuration:      
      description: 'Device''s technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model'      
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
      description: 'List of the asset(s) (building, object, etc.) controlled by the device'      
      items:      
        oneOf:      
          - format: uri      
            type: string      
          - anyOf:      
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
    dateFirstUsed:      
      description: A timestamp which denotes when the device was first used      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateInstalled:      
      description: A timestamp which denotes when the device was installed (if it requires installation)      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastCalibration:      
      description: A timestamp which denotes when the last calibration of the device happened      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateLastValueReported:      
      description: A timestamp which denotes the last time when the device successfully reported data to the cloud      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateManufactured:      
      description: A timestamp which denotes when the device was manufactured      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/DateTime      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateObserved:      
      description: Date of the observed entity defined by the user      
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
    deviceState:      
      description: State of this device from an operational point of view. Its value can be vendor dependent      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    direction:      
      description: 'Enum:''Inlet, Outlet, Entry, Exit''. A timestamp which denotes when the device was installed (if it requires installation)'      
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
      description: Indicates a device which is Daylight Savings Time Aware (True). In case it is then the Timestamp is automatically adjusted by the device to reflect DST changes. If not (False) the time adjustments must be taken care of by the user      
      type: boolean      
      x-ngsi:      
        type: Property      
    firmwareVersion:      
      description: The firmware version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    hardwareVersion:      
      description: The hardware version of this device      
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
    ipAddress:      
      description: List of IP address of the device. It can be a comma separated list of values if the device has more than one IP address      
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
    macAddress:      
      description: The MAC address of the device      
      pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    mcc:      
      description: This property identifies the Mobile Country Code      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    mnc:      
      description: 'This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a ''MCC / MNC tuple'') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks'      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    osVersion:      
      description: The version of the host operating system device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    provider:      
      description: The provider of the device      
      type: string      
      x-ngsi:      
        model: https://schema.org/provider      
        type: Property      
    refDeviceModel:      
      description: Model of the device      
      oneOf:      
        - format: uri      
          type: string      
        - anyOf:      
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
      x-ngsi:      
        type: Relationship      
    relativePosition:      
      description: Location of this device in a coordinate system according to its local emplacement      
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
    serialNumber:      
      description: The serial number assigned by the manufacturer      
      type: string      
      x-ngsi:      
        model: https://schema.org/serialNumber      
        type: Property      
    softwareVersion:      
      description: The software version of this device      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    type:      
      description: NGSI Entity type. It has to be Device      
      enum:      
        - Device      
      type: string      
      x-ngsi:      
        type: Property      
    value:      
      description: 'A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value ''on'' of type ''Text''. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to ''off'''      
      type: string      
      x-ngsi:      
        model: https://schema.org/QuantitativeValue      
        type: Property      
  required:      
    - id      
    - type      
    - controlledProperty      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/Device/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/Device/schema.json      
  x-model-tags: ""      
  x-version: 0.0.8      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### デバイス NGSI-v2 キー値の例    
JSON-LD形式のDeviceのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "deviceCategory": [  
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
</details>    
#### デバイス NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のDeviceの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "device-9845A",  
  "type": "Device",  
  "deviceCategory": {  
    "type": "StructuredValue",  
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
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "myDevice-wastecontainer-sensor-345"  
  },  
  "rssi": {  
    "type": "Number",  
    "value": 0.86  
  },  
  "controlledProperty": {  
    "type": "StructuredValue",  
    "value": [  
      "fillingLevel",  
      "temperature"  
    ]  
  },  
  "owner": {  
    "type": "StructuredValue",  
    "value": [  
      "http://person.org/leon"  
    ]  
  },  
  "mnc": {  
    "type": "Text",  
    "value": "07"  
  },  
  "ipAddress": {  
    "type": "StructuredValue",  
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
</details>    
#### デバイス NGSI-LD キー値の例    
JSON-LD形式のDeviceのkey-valuesの例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": 0.75,  
  "deviceCategory": [  
    "sensor"  
  ],  
  "controlledAsset": [  
    "urn:ngsi-ld::wastecontainer-Osuna-100"  
  ],  
  "controlledProperty": [  
    "fillingLevel",  
    "temperature"  
  ],  
  "dateFirstUsed": "2014-09-11T11:00:00Z",  
  "depth": 3,  
  "deviceState": "ok",  
  "direction": "Outlet",  
  "distance": 20,  
  "ipAddress": [  
    "192.14.56.78"  
  ],  
  "mcc": "214",  
  "mnc": "07",  
  "owner": [  
    "http://person.org/leon"  
  ],  
  "refDeviceModel": "urn:ngsi-ld:DeviceModel:myDevice-wastecontainer-sensor-345",  
  "rssi": 0.86,  
  "serialNumber": "9845A",  
  "value": "l%3D0.22%3Bt%3D21.2",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### デバイス NGSI-LD 正規化例    
以下は、正規化されたJSON-LD形式のDeviceの例である。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": {  
    "type": "Property",  
    "value": 0.75  
  },  
  "deviceCategory": {  
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
    "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld",  
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
