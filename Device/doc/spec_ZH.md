<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。设备  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.Device/blob/master/Device/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述。**一种旨在完成特定任务（感知环境、执行等）的仪器（硬件+软件+固件）。  
版本：0.0.7  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[*]`: 设备电池水平。当电池充满时，它必须等于1.0。当电池为空时为0.0。瞬时无法确定时为-1。  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: 传感器。探测并对物理环境中的事件或变化做出反应的设备，如光、运动或温度变化。https://w3id.org/saref#Sensor。执行器：负责移动或控制一个机制或系统的设备。https://w3id.org/saref#Actuator。计量器 : 为准确检测并以人类可读的形式显示某一数量而建造的设备。部分由SAREF定义。HVAC : 暖气、通风和空调（HVAC）设备，提供室内环境舒适度。https://w3id.org/saref#HVAC。网络 : 用于连接网络中其他设备的设备，如局域网或传感器网络中的集线器、交换机或路由器。(https://w3id.org/saref#Network.多媒体 :用于显示、存储、记录或播放多媒体内容的设备，如音频、图像、动画、视频。Enum:'actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor'。  . Model: [https://schema.org/Text](https://schema.org/Text)- `configuration[array]`: 设备的技术配置。这个属性旨在成为一个数组属性和它们的值，捕获与设备配置有关的参数（超时、报告期等），这些参数目前没有被本模型定义的标准属性所覆盖。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `controlledAsset[array]`: 设备所控制的资产（建筑物、物体等）的清单。  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlledProperty[array]`: 任何可以被感知、测量或控制的东西。枚举。空气污染, 大气压力, 平均速度, 电池寿命, 电池供应, 电池容量, 电导率, 电导率, 深度, 饮食活动, 电力消耗, 能量, 填充水平, 自由氯, 气体消耗, 开门, 湿度, 光, 位置, 挤奶, 运动, 运动活动,噪声水平, 占用率, orp, pH值, 功率, 降水, 压力, 折射指数, 盐度, 烟雾, 土壤湿度, 太阳辐射, 速度, tds, 温度, 交通流量, tss, 浊度, 耗水量, 水流量, 水位, 水污染, 天气状况, 重量, 风向, 风速'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateFirstUsed[string]`: 一个时间戳，表示设备第一次被使用的时间。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateInstalled[string]`: 一个时间戳，表示设备的安装时间（如果需要安装）。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastCalibration[string]`: 表示设备最后一次校准的时间的时间戳。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[string]`: 一个时间戳，表示设备最后一次向云端成功报告数据的时间。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateManufactured[string]`: 一个时间戳，表示设备的制造时间。  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `dateObserved[string]`: 由用户定义的被观察实体的日期。  - `depth[number]`: 该设备的位置由从起点开始的深度表示。所有单位都接受[CEFACT](https://www.unece.org/cefact.html)代码。  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: 对这个项目的描述  - `deviceState[string]`: 从操作的角度看这个设备的状态。它的值可能取决于供应商。  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction[string]`: Enum:'Inlet, Outlet, Entry, Exit'。一个时间戳，表示设备的安装时间（如果需要安装）。  . Model: [ https://schema.org/DateTime]( https://schema.org/DateTime)- `distance[number]`: 该设备的位置，用与起点的距离表示。所有单位都接受[CEFACT](https://www.unece.org/cefact.html)代码。  . Model: [https://schema.org/Distance](https://schema.org/Distance)- `dstAware[boolean]`: 表示设备对夏令时有认识（真）。如果是，那么设备会自动调整时间戳以反映夏令时的变化。如果不是（False），时间调整必须由用户来处理。  - `firmwareVersion[string]`: 该设备的固件版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: 该设备的硬件版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `ipAddress[array]`: 设备的IP地址列表。如果设备有一个以上的IP地址，它可以是一个逗号分隔的数值列表。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `macAddress[string]`: 设备的MAC地址。  . Model: [https://schema.org/Text](https://schema.org/Text)- `mcc[string]`: 此属性标识了移动国家代码  . Model: [https://schema.org/Text](https://schema.org/Text)- `mnc[string]`: 此属性标识了设备所连接的网络的移动网络代码（MNC）。MNC与移动国家代码（MCC）结合使用（也称为 "MCC/MNC元组"），以唯一地识别使用GSM、CDMA、iDEN、TETRA和3G/4G公共陆地移动网络和一些卫星移动网络的移动电话运营商/运营商。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 这个项目的名称。  - `osVersion[string]`: 主机操作系统设备的版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `provider[string]`: 该设备的提供者。  . Model: [https://schema.org/provider](https://schema.org/provider)- `refDeviceModel[*]`: 设备的型号  - `relativePosition[string]`: 该设备在坐标系中的位置，根据其在当地的位置。  - `rssi[number]`: 无线设备的接收信号强度指标。它必须以dBm或mW表示，使用unitcode来设置。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `serialNumber[string]`: 制造商分配的序列号。  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `softwareVersion[string]`: 该设备的软件版本。  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `supportedProtocol[array]`: 支持的协议或网络  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `type[string]`: NGSI实体类型。它必须是设备  - `value[string]`: 一个观察到的或报告的值。对于执行器设备，它是一个属性，允许控制应用程序改变执行设置。例如，一个目前处于_开启状态的开关设备可以报告一个类型为'文本'的值'开启'。很明显，为了切换所指的开关，这个属性值必须改为'关闭'。  . Model: [https://schema.org/QuantitativeValue](https://schema.org/QuantitativeValue)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `controlledProperty`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
设备是一个有形的物体，它包含一些逻辑，是数据的生产者和/或消费者。一个设备总是被认为能够通过网络进行电子通信。这个数据模型部分是与移动运营商和[GSMA](https://www.gsma.com/iot/iot-big-data/)合作开发的。这个数据模型重用了来自[ETSI](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf)标准的[SAREF Ontology](http://www.etsi.org)部分的概念。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Device:    
  description: 'An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).'    
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
        - maximum: -1    
          minimum: -1    
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
      pattern: ^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/Device/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/Device/schema.json    
  x-model-tags: ""    
  x-version: 0.0.7    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### 设备NGSI-v2关键值示例  
这里是一个以JSON-LD格式作为key-values的设备的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### 设备NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的设备的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### 设备NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的设备的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Device:device-9845A",  
    "type": "Device",  
    "batteryLevel": 0.75,  
    "category": {  
        "type": "Property",  
        "value": [  
            "sensor"  
        ]  
    },  
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
#### 设备NGSI-LD规范化示例  
下面是一个以JSON-LD格式规范化的设备的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
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
    "controlledAsset": [  
        {  
            "type": "Relationship",  
            "object": "urn:ngsi-ld::wastecontainer-Osuna-100"  
        }  
    ],  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
