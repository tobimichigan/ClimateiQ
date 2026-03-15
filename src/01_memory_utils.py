
import gc, os, psutil, torch

def get_memory_mb():
    return psutil.Process(os.getpid()).memory_info().rss / 1e6

def force_cleanup(*objs):
    for o in objs:
        try:
            del o
        except:
            pass
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
