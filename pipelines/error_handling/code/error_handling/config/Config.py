from prophecy.config import ConfigBase


class Config(ConfigBase):

    def __init__(self, loc: str=None, **kwargs):
        self.spark = None
        self.update(loc)

    def update(self, loc: str="dbfs:/Volumes/main/prophecy_lh/malformed/", **kwargs):
        prophecy_spark = self.spark
        self.loc = loc
        pass
