from dataclasses import dataclass
from typing import List


@dataclass
class Meta:
    source: str
    version: str


@dataclass
class Owner:
    id: str
    email: str
    name: str


@dataclass
class Faces:
    id: str
    sourceType: str
    imageHeight: int
    imageWidth: int
    boundingBoxX1: int
    boundingBoxX2: int
    boundingBoxY1: int
    boundingBoxY2: int


@dataclass
class People:
    id: str
    name: str
    birthDate: str
    faces: List[Faces]


@dataclass
class ExifInfo:
    dateTimeOriginal: str
    modifyDate: str
    make: str
    model: str
    orientation: str
    timeZone: str
    lensModel: str
    exposureTime: str
    city: str
    state: str
    country: str
    description: str
    ImageOrientation: str
    exifImageWidth: int
    exifImageHeight: int
    fileSizeInByte: int
    fNumber: int
    focalLength: int
    iso: int
    latitude: int
    longitude: int


@dataclass
class Assets:
    localDateTime: str
    owner: Owner
    id: str
    ownerId: str
    type: str
    originalFileName: str
    originalMimeType: str
    duration: str
    livePhotoVideoId: str
    checksum: str
    kioskBucket: str
    kioskBucketId: str
    people: List[People]
    tags: List
    unassignedFaces: List
    kioskAppearsIn: str
    exifInfo: ExifInfo
    isFavorite: bool
    isArchived: bool
    isTrashed: bool
    isPortrait: bool
    isLandscape: bool


@dataclass
class ClientData:
    fully_version: str
    fully_webview_version: str
    fully_android_version: str
    client_width: int
    client_height: int
    fully_screen_orientation: int
    fully_screen_brightness: int


@dataclass
class Weather:
    Name: str
    Lat: str
    Lon: str
    API: str
    Unit: str
    Lang: str
    Forecast: bool
    Default: bool


@dataclass
class Webhooks:
    url: str
    event: str
    secret: str


@dataclass
class OfflineMode:
    MaxSize: str
    NumberOfAssets: int
    ParallelDownloads: int
    ExpirationHours: int
    Enabled: bool


@dataclass
class Redirects:
    Name: str
    URL: str
    Type: str


@dataclass
class Kiosk:
    version: str
    configValidationLevel: str
    Redirects: List[Redirects]
    port: int
    fetchedAssetsSize: int
    httpTimeout: int
    behindProxy: bool
    disableURLQueries: bool
    disableConfigEndpoint: bool
    enableURLBuilder: bool
    watchConfig: bool
    cache: bool
    preFetch: bool
    assetWeighting: bool
    debug: bool
    debugVerbose: bool


@dataclass
class Config:
    user: List
    history: List
    ClientData: ClientData
    showTime: bool
    timeFormat: str
    showDate: bool
    dateFormat: str
    clockSource: str
    duration: int
    disableScreensaver: bool
    selectedUser: str
    menuPosition: str
    optimize_images: bool
    useGpu: bool
    burnInInterval: int
    burnInDuration: int
    burnInOpacity: int
    showArchived: bool
    people: List
    requireAllPeople: bool
    excludedPeople: List
    albums: List[str]
    album_order: str
    excluded_albums: List
    dates: List
    tags: List
    excluded_tags: List
    excluded_partners: List[str]
    memories: bool
    pastMemoryDays: int
    memoryWeight: int
    dateFilter: str
    showClearCacheButton: bool
    showProgressBar: bool
    progressBarPosition: str
    disableUi: bool
    disableNavigation: bool
    frameless: bool
    framePadding: List[int]
    hideCursor: bool
    fontSize: int
    backgroundBlur: bool
    backgroundBlurAmount: int
    theme: str
    layout: str
    sleepStart: str
    sleepEnd: str
    sleepIcon: bool
    sleepDimScreen: bool
    disableSleep: bool
    transition: str
    fadeTransitionDuration: int
    crossFadeTransitionDuration: int
    imageFit: str
    imageEffect: str
    imageEffectAmount: int
    useOriginalImage: bool
    showVideos: bool
    livePhotos: bool
    livePhotoLoopDelay: int
    showOwner: bool
    showAlbumName: bool
    showPersonName: bool
    showPersonAge: bool
    showAgeYearUnit: bool
    ageSwitchToYearsAfter: int
    showImageTime: bool
    imageTimeFormat: str
    showImageDate: bool
    imageDateFormat: str
    showImageDescription: bool
    showImageCamera: bool
    showImageExif: bool
    showImageLocation: bool
    showImageQR: bool
    hideCountries: List[str]
    showImageID: bool
    showUser: bool
    showMoreInfo: bool
    showMoreInfoImageLink: bool
    showMoreInfoQrCode: bool
    likeButtonAction: List[str]
    hideButtonAction: List[str]
    weather: List[Weather]
    iframe: List
    customCSSClass: str
    customCSS: bool
    webhooks: List[Webhooks]
    blacklist: List
    offlineMode: OfflineMode
    useOfflineMode: bool
    kiosk: Kiosk


@dataclass
class ImmichKioskWebhookPayload:
    meta: Meta
    event: str
    timestamp: str
    deviceID: str
    clientName: str
    assets: List[Assets]
    config: Config
    assetCount: int
