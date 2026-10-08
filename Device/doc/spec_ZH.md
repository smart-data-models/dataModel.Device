<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：设备  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可证](https://github.com/smart-data-models/dataModel.Device/blob/master/Device/LICENSE.md)  
[文档自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**旨在完成特定任务（环境感知、执行等）的设备（硬件 + 软件 + 固件）。**  
version: 0.0.10  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果某个属性没有类型，是因为它可能有多种类型或不同的格式/模式</sub></sup>  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地区内的地点  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 所在地所在的地区，且该地区位于国家内  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 行政区是一种行政划分，在某些国家由地方政府管理。    
	- `postOfficeBoxNumber[string]`: 邮政信箱地址的邮政信箱号码。例如，03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如，24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 识别公共街道上特定物业的号码    
- `alternateName[string]`: 此项目的替代名称  - `areaServed[string]`: 提供服务或所提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[*]`: 设备电池电量。电池满电时必须等于 1.0；电池空电时为 0.0；暂时无法确定时为 -1  . Model: [https://schema.org/Number](https://schema.org/Number)- `batteryTemperature[number]`: 设备当前的电池温度。必须以摄氏度表示，使用 unitcode 进行设置  . Model: [https://schema.org/Number](https://schema.org/Number)- `category[array]`: 传感器：一种检测并响应物理环境中事件或变化的设备，例如光线、运动或温度变化。https://w3id.org/saref#Sensor。执行器：负责移动或控制机构或系统的设备。https://w3id.org/saref#Actuator。仪表：一种旨在准确检测和以人类可读形式显示数量的设备。部分由 SAREF 定义。HVAC：提供室内环境舒适度的供暖、通风和空调 (HVAC) 设备。https://w3id.org/saref#HVAC。网络：用于连接网络中其他设备的设备，例如局域网或传感器网络中的集线器、交换机或路由器。(https://w3id.org/saref#Network。多媒体：设计用于显示、存储、录制或播放多媒体内容（如音频、图像、动画、视频）的设备。枚举：'执行器, 信标, 喷枪末端, HVAC, 工具, 灌溉段, 灌溉系统, 仪表, 多媒体, 网络, 传感器'。原始类别将被弃用，请使用 deviceCategory 以避免与其他名为 category 的属性冲突。  . Model: [https://schema.org/Text](https://schema.org/Text)- `configuration[array]`: 设备的技​​术配置。此属性旨在作为属性及其值的数组，用于捕获与设备配置（超时、报告周期等）相关的参数，而这些参数目前未涵盖在此模型定义的标准属性中。  . Model: [https://schema.org/StructuredValue](https://schema.org/StructuredValue)- `controlledAsset[array]`: 设备控制的资产（建筑物、物体等）列表  . Model: [https://schema.org/Text](https://schema.org/Text)- `controlledProperty[array]`: 任何可以被感知、测量或控制的东西。枚举：'空气污染、大气压、平均速度、电池寿命、电池供电、CDOM、电导、电导率、深度、饮食活动、电力消耗、能源、填充水平、游离氯、燃气消耗、闸门开启、航向、湿度、光照、位置、挤奶、运动、活动、噪声水平、占用率、氧化还原电位、pH值、功率、降水、压力、折射率、盐度、烟雾、土壤湿度、太阳辐射、速度、总溶解固体、温度、交通流量、总悬浮固体、浊度、水消耗、水流量、水位、水污染、天气状况、重量、风向、风速'  . Model: [https://schema.org/Text](https://schema.org/Text)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。这通常由存储平台分配。  - `dateFirstUsed[date-time]`: 表示设备首次使用的时间戳  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateInstalled[date-time]`: 表示设备安装时间（如果需要安装）的时间戳  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastCalibration[date-time]`: 表示设备上次校准发生的时间戳  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateLastValueReported[date-time]`: 表示设备上次成功向云端报告数据的时间戳  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateManufactured[date-time]`: 表示设备制造时间的时间戳  . Model: [https://schema.org/DateTime](https://schema.org/DateTime)- `dateModified[date-time]`: 实体最后修改的时间戳。这通常由存储平台分配。  - `dateObserved[date-time]`: 用户定义的观测实体的日期  - `depth[number]`: 此设备相对于起始点的深度表示的位置。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码。  . Model: [https://schema.org/depth](https://schema.org/depth)- `description[string]`: 此项目的描述  - `deviceCategory[array]`: 传感器：一种检测并响应物理环境中事件或变化的设备，例如光线、运动或温度变化。https://w3id.org/saref#Sensor。执行器：负责移动或控制机构或系统的设备。https://w3id.org/saref#Actuator。仪表：一种旨在准确检测和以人类可读形式显示数量的设备。部分由 SAREF 定义。HVAC：提供室内环境舒适度的供暖、通风和空调 (HVAC) 设备。https://w3id.org/saref#HVAC。网络：用于连接网络中其他设备的设备，例如局域网或传感器网络中的集线器、交换机或路由器。(https://w3id.org/saref#Network。多媒体：设计用于显示、存储、录制或播放多媒体内容（如音频、图像、动画、视频）的设备。枚举：'执行器, 信标, 喷枪末端, HVAC, 工具, 灌溉段, 灌溉系统, 仪表, 多媒体, 网络, 传感器'。原始类别将被弃用，请使用 deviceCategory 以避免与其他名为 category 的属性冲突。  . Model: [https://schema.org/Text](https://schema.org/Text)- `deviceState[string]`: 从操作角度看此设备的状态。其值可能因供应商而异。  . Model: [https://schema.org/Text](https://schema.org/Text)- `direction[string]`: 枚举：'Inlet, Outlet, Entry, Exit'。表示设备安装时间的时间戳（如果需要安装）  . Model: [ https://schema.org/DateTime]( https://schema.org/DateTime)- `distance[number]`: 此设备相对于起始点的距离表示的位置。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码。  . Model: [https://schema.org/Distance](https://schema.org/Distance)- `dstAware[boolean]`: 指示设备是否支持夏令时 (True)。如果支持，则设备会自动调整时间戳以反映夏令时变化。如果不支持 (False)，则时间调整必须由用户负责。  - `firmwareVersion[string]`: 此设备的固件版本  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: 此设备的硬件版本  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: 实体的唯一标识符  - `ipAddress[array]`: 设备 IP 地址列表。如果设备有多个 IP 地址，可以是以逗号分隔的值列表  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson 对项目的引用。可以是 Point, LineString, Polygon, MultiPoint, MultiLineString 或 MultiPolygon。  - `macAddress[string]`: 设备的 MAC 地址  . Model: [https://schema.org/Text](https://schema.org/Text)- `mcc[string]`: 此属性标识移动国家代码 (MCC)  . Model: [https://schema.org/Text](https://schema.org/Text)- `mnc[string]`: 此属性标识设备所属网络的移动网络代码 (MNC)。MNC 与移动国家代码 (MCC) 结合使用（也称为“MCC / MNC 元组”），用于通过 GSM、CDMA、iDEN、TETRA 和 3G / 4G 公共陆地移动网络以及某些卫星移动网络来唯一标识移动电话运营商/载体  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 此项目的名称  - `osVersion[string]`: 主机操作系统设备的版本  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 包含 JSON 编码字符序列的列表，引用所有者的唯一 ID  - `provider[string]`: 设备提供商  . Model: [https://schema.org/provider](https://schema.org/provider)- `refDeviceModel[*]`: 设备型号  - `relativePosition[string]`: 此设备在其当地位置的坐标系中的位置  - `rssi[number]`: 无线启用设备的接收信号强度指示。必须以 dBm 或 mW 表示，请使用 unitcode 进行设置。  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: 指向有关该项目的其他资源的 URI 列表  - `serialNumber[string]`: 制造商分配的序列号  . Model: [https://schema.org/serialNumber](https://schema.org/serialNumber)- `softwareVersion[string]`: 此设备的软件版本  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: 一个字符序列，提供实体数据的原始来源，作为 URL。建议使用来源提供商的完全限定域名，或指向来源对象的 URL  - `supportedProtocol[array]`: 支持的协议或网络  . Model: [3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket](3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket)- `type[string]`: NGSI 实体类型。必须是 Device  - `value[string]`: 观察到或报告的值。对于执行器设备，它是一个允许控制应用程序更改执行器设置的属性。例如，一个当前处于“开”状态的开关设备可以报告类型为“Text”的“on”值。显然，为了切换所指的开关，此属性值必须更改为“off”。  . Model: [https://schema.org/QuantitativeValue](https://schema.org/QuantitativeValue)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必需属性  
- `controlledProperty`  - `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
设备是一个包含某些逻辑的实物对象，并且是数据的生产者和/或消费者。通常假设设备能够通过网络进行电子通信。此数据模型是与移动运营商及 [GSMA](https://www.gsma.com/iot/iot-big-data/) 合作共同开发的。该数据模型重用了 [ETSI](http://www.etsi.org) 标准中 [SAREF Ontology](http://www.etsi.org/deliver/etsi_ts/103200_103299/103264/01.01.01_60/ts_103264v010101p.pdf) 部分的概念。  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排序（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Device:    
  description: An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).    
  properties:    
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
    batteryTemperature:    
      description: Current battery temperature of the device. It must be expressed in degrees Celsius, use unitcode to set it out    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    category:    
      description: 'Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:''actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor''. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category'    
      items:    
        description: Every type of device that can be included in the array    
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
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    configuration:    
      description: Device's technical configuration. This attribute is intended to be a array properties and their values which capture parameters which have to do with the configuration of a device (timeouts, reporting periods, etc.) and which are not currently covered by the standard attributes defined by this model    
      items:    
        properties:    
          parameter:    
            description: Name of the parameter in the configuration of the device    
            type: string    
            x-ngsi:    
              type: Property    
          value:    
            description: Value of the parameter in the configuration of the device    
            type: string    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        model: https://schema.org/StructuredValue    
        type: Property    
    controlledAsset:    
      description: List of the asset(s) (building, object, etc.) controlled by the device    
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
        model: https://schema.org/Text    
        type: Property    
    controlledProperty:    
      description: Anything that can be sensed, measured or controlled by. Enum:'airPollution, atmosphericPressure, averageVelocity, batteryLife, batterySupply, cdom, conductance, conductivity, depth, eatingActivity, electricityConsumption, energy, fillingLevel, freeChlorine, gasConsumption, gateOpening, heading, humidity, light, location, milking, motion, movementActivity, noiseLevel, occupancy, orp, pH, power, precipitation, pressure, refractiveIndex, salinity, smoke, soilMoisture, solarRadiation, speed, tds, temperature, trafficFlow, tss, turbidity, waterConsumption, waterFlow, waterLevel, waterPollution, weatherConditions, weight, windDirection, windSpeed'    
      items:    
        description: Every possible property controlled by the device    
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
        x-ngsi:    
          type: Property    
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
      description: Location of this device represented by a depth from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code    
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
      description: 'Sensor: A device that detects and responds to events or changes in the physical environment such as light, motion, or temperature changes. https://w3id.org/saref#Sensor. actuator : A device responsible for moving or controlling a mechanism or system. https://w3id.org/saref#Actuator. Meter : A device built to accurately detect and display a quantity in a form readable by a human being. Partially defined by SAREF. HVAC : Heating, Ventilation and Air Conditioning (HVAC) device that provides indoor environmental comfort. https://w3id.org/saref#HVAC. Network : A device used to connect other devices in a network, such as hub, switch or router in a LAN or Sensor network. (https://w3id.org/saref#Network. Multimedia : A device designed to display, store, record or play multimedia content such as audio, images, animation, video. Enum:''actuator, beacon, endgun, HVAC, implement, irrSection, irrSystem, meter, multimedia, network, sensor''. Raw category will be deprecated use deviceCategory instead to avoid conflict with other aqttributes named category'    
      items:    
        description: Every type of device that can be included in the array    
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
        x-ngsi:    
          type: Property    
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
      description: Enum:'Inlet, Outlet, Entry, Exit'. A timestamp which denotes when the device was installed (if it requires installation)    
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
      description: Location of this device represented by a distance from a starting point. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code    
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
        type: Relationship    
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
      description: This property identifies the Mobile Network Code (MNC) of the network the device is attached to. The MNC is used in combination with a Mobile Country Code (MCC) (also known as a 'MCC / MNC tuple') to uniquely identify a mobile phone operator/carrier using the GSM, CDMA, iDEN, TETRA and 3G / 4G public land mobile networks and some satellite mobile networks    
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
          type: Relationship    
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
      description: Model of the device    
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
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object    
      type: string    
      x-ngsi:    
        type: Property    
    supportedProtocol:    
      description: Supported protocol(s) or networks    
      items:    
        description: Every type of protocols that can be used by the device    
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
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        model: 3g, bluetooth, bluetooth LE, cat-m, coap, ec-gsm-iot, gprs, http, lwm2m, lora, lte-m, mqtt, nb-iot, onem2m, sigfox, ul20, websocket    
        type: Property    
    type:    
      description: NGSI Entity type. It has to be Device    
      enum:    
        - Device    
      type: string    
      x-ngsi:    
        type: Property    
    value:    
      description: A observed or reported value. For actuator devices, it is an attribute that allows a controlling application to change the actuation setting. For instance, a switch device which is currently _on_ can report a value 'on' of type 'Text'. Obviously, in order to toggle the referred switch, this attribute value will have to be changed to 'off'    
      type: string    
      x-ngsi:    
        model: https://schema.org/QuantitativeValue    
        type: Property    
  required:    
    - id    
    - type    
    - controlledProperty    
  type: object    
  x-derived-from: ''    
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2023 Contributors to Smart Data Models Program    
  x-license-url: https://github.com/smart-data-models/dataModel.Device/blob/master/Device/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.Device/Device/schema.json    
  x-model-tags: ''    
  x-version: 0.0.10    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 示例负载   
#### 设备 NGSI-v2 键值对示例  
这是一个 JSON-LD 格式的 Device 示例，以键值对表示。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的情境数据。  
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
  "batteryTemperature": 34.1,  
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
#### 设备 NGSI-v2 标准化示例  
以下是标准化后的 JSON-LD 格式设备的示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
  "batteryTemperature": {  
    "type": "Number",  
    "value": 34.1,  
    "metadata": {  
      "unitCode": {  
        "value": "CEL"  
      }  
    }  
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
#### 设备 NGSI-LD 键值示例   
这是一个 JSON-LD 格式的 Device 示例，以键值对表示。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的情境数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": 0.75,  
  "batteryTemperature": 34.1,  
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
#### 设备 NGSI-LD 标准化示例  
这是一个 JSON-LD 格式的 Device 示例，已规范化。当不使用选项时，这与 NGSI-LD 兼容，并返回单个实体的情境数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Device:device-9845A",  
  "type": "Device",  
  "batteryLevel": {  
    "type": "Property",  
    "value": 0.75  
  },  
  "batteryTemperature": {  
    "type": "Property",  
    "value": 34.1,  
    "unitCode": "CEL"  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/) 以获取有关如何处理数量单位的答案  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
