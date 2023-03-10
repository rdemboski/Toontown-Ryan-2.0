from toontown.safezone import DGPlayground
from toontown.safezone import SafeZoneLoader


class DGSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = DGPlayground.DGPlayground
        self.musicFile = 'phase_3.5/audio/bgm/Littleroot_Town_NEW.mid' #todo: change ms=
        self.activityMusicFile = 'phase_3.5/audio/bgm/Littleroot_Town_Toontownified.mid'
        self.dnaFile = 'phase_8/dna/daisys_garden_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_DG_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.birdSound = map(base.loadSfx, ['phase_8/audio/sfx/SZ_DG_bird_01.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_02.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_03.ogg',
                                            'phase_8/audio/sfx/SZ_DG_bird_04.ogg'])

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.birdSound