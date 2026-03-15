
import glob, os

def discover_nc_files(root_dir):
    return sorted(glob.glob(os.path.join(root_dir,"**","*.nc"),recursive=True))
