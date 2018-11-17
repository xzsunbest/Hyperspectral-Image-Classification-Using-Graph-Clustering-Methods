import gdal
import sys
import numpy as np

def multiband_to_array(path):

    src_ds = gdal.Open(path)
    if src_ds is None:
        print('Unable to open %s'% path)
        sys.exit(1)

    xcount = src_ds.RasterXSize # width
    ycount = src_ds.RasterYSize # height
    ibands = src_ds.RasterCount # band number

    for band in range(ibands):
        band += 1
        srcband = src_ds.GetRasterBand(band)
        if srcband is None:
            continue

        # Read raster as arrays
        dataraster = srcband.ReadAsArray(0, 0, xcount, ycount).astype(np.float32)
        if band == 1:
            data = dataraster.reshape((ycount,xcount,1))
        else:
            data = np.append(data,dataraster.reshape((ycount,xcount,1)),axis=2)

    src_ds = None
    return data