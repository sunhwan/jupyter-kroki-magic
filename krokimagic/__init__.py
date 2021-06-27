from .krokimagic import KrokiMagic

def load_ipython_extension(ipython):
    ipython.register_magics(KrokiMagic)
