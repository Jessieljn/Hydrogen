DEFAULT_IP = '140.193.228.26'
DEFAULT_PORT = 9559
VIDEO_SUBSCRIBE_NAME = "NaoVideo"


class Camera:
    Top, \
    Bottom, \
    Both \
        = range(3)
#END class


class CameraResolution:
    # In order of resolution
    # 160 * 120px
    # 320*240px
    # 640*480px
    # 1280*960px
    QQVGA, \
    QVGA, \
    VGA, \
    FOUR_VGA \
        = range(4)
#END class


class Direction:
    Neutral, \
    Up, \
    Down, \
    Left, \
    Right \
        = range(5)
#END class


class LEDNames:
    All = "AllLeds"
    Brain = "BrainLeds"
    Ears = "EarLeds"
    LeftEar = "LeftEarLeds"
    RightEar = "RightEarLeds"
    Face = "FaceLeds"
    FaceLeft = "LeftFaceLeds"
    FaceRight = "RightFaceLeds"
    Chest = "ChestLeds"
    Feet = "FeetLeds"
#END class
