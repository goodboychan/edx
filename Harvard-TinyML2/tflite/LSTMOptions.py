# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class LSTMOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLSTMOptions(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LSTMOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def LSTMOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # LSTMOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # LSTMOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # LSTMOptions
    def CellClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # LSTMOptions
    def ProjClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def LSTMOptionsStart(builder): builder.StartObject(3)
def LSTMOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def LSTMOptionsAddCellClip(builder, cellClip): builder.PrependFloat32Slot(1, cellClip, 0.0)
def LSTMOptionsAddProjClip(builder, projClip): builder.PrependFloat32Slot(2, projClip, 0.0)
def LSTMOptionsEnd(builder): return builder.EndObject()


class LSTMOptionsT(object):

    # LSTMOptionsT
    def __init__(self):
        self.fusedActivationFunction = 0  # type: int
        self.cellClip = 0.0  # type: float
        self.projClip = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        lSTMOptions = LSTMOptions()
        lSTMOptions.Init(buf, pos)
        return cls.InitFromObj(lSTMOptions)

    @classmethod
    def InitFromObj(cls, lSTMOptions):
        x = LSTMOptionsT()
        x._UnPack(lSTMOptions)
        return x

    # LSTMOptionsT
    def _UnPack(self, lSTMOptions):
        if lSTMOptions is None:
            return
        self.fusedActivationFunction = lSTMOptions.FusedActivationFunction()
        self.cellClip = lSTMOptions.CellClip()
        self.projClip = lSTMOptions.ProjClip()

    # LSTMOptionsT
    def Pack(self, builder):
        LSTMOptionsStart(builder)
        LSTMOptionsAddFusedActivationFunction(builder, self.fusedActivationFunction)
        LSTMOptionsAddCellClip(builder, self.cellClip)
        LSTMOptionsAddProjClip(builder, self.projClip)
        lSTMOptions = LSTMOptionsEnd(builder)
        return lSTMOptions
