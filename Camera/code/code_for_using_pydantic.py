from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class CameraOrientation(BaseModel):
    annotatedMap: Optional[AnyUrl] = None
    comments: Optional[str] = None


class CameraType(Enum):
    FIXED = 'FIXED'
    PTZ = 'PTZ'
    DOME = 'DOME'
    DAY_NIGHT = 'DAY/NIGHT'
    C_MOUNT = 'C-MOUNT'
    BULLET = 'BULLET'


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class Type6(Enum):
    Camera = 'Camera'


class Camera(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    cameraName: Optional[str] = Field(
        None, description='Name of the camera corresponding to this observation'
    )
    cameraNum: Optional[float] = Field(
        None, description='Camera number corresponding to this observation'
    )
    cameraOrientation: Optional[CameraOrientation] = Field(
        None,
        description='Orientation information for the camera corresponding to this observation',
    )
    cameraType: Optional[CameraType] = Field(
        None,
        description="Type of the camera corresponding to this observation. Enum:'FIXED, PTZ, DOME, DAY/NIGHT, C-MOUNT, BULLET'",
    )
    cameraUsage: Optional[str] = Field(
        None,
        description='Purpose of the camera corresponding to this observation. Enum: [SURVEILLANCE, RLVD, ANPR/LPR, TRAFFIC]',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    endDateTime: Optional[AwareDatetime] = Field(
        None, description='Reported end time corresponding to this observation'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    imageSnapshot: Optional[str] = Field(
        None,
        description='Camera feed snapshot download link for the camera corresponding to this observation',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    mediaURL: Optional[AnyUrl] = Field(
        None,
        description='URL providing further information of any image(s) or media of the complaint or place',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    on: Optional[bool] = Field(
        None, description='Indicates if the device is on (true) or off (false)'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startDateTime: Optional[AwareDatetime] = Field(
        None, description='Reported start time corresponding to this observation'
    )
    streamName: Optional[str] = Field(
        None,
        description='Name of the video stream from the camera corresponding to this observation',
    )
    streamURL: Optional[str] = Field(
        None,
        description='URL providing video streaming information for the camera corresponding to this observation',
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be Camera'
    )
