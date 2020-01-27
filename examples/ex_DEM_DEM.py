import os
import inspect

import IHEWAcollect


def main():

    path = os.path.join(
        os.getcwd(),
        os.path.dirname(
            inspect.getfile(
                inspect.currentframe()))
    )

    product = 'DEM'
    version = 'v1'
    parameter = 'DEM'
    resolution = '30s'
    variable = 'af'
    bbox = {
        'w': -19.0,
        's': -35.0,
        'e': 55.0,
        'n': 38.0
    }
    period = {
        's': '',
        'e': ''
    }
    nodata = -9999

    download = IHEWAcollect.Download(workspace=path,
                                     product=product,
                                     version=version,
                                     parameter=parameter,
                                     resolution=resolution,
                                     variable=variable,
                                     bbox=bbox,
                                     period=period,
                                     nodata=nodata,
                                     is_status=False)


if __name__ == "__main__":
    main()