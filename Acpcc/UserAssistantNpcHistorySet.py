# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Acpcc

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserAssistantNpcHistorySet(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserAssistantNpcHistorySet()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserAssistantNpcHistorySet(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserAssistantNpcHistorySet
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserAssistantNpcHistorySet
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # UserAssistantNpcHistorySet
    def Elements(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Acpcc.UserAssistantNpcHistorySetElement import UserAssistantNpcHistorySetElement
            obj = UserAssistantNpcHistorySetElement()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserAssistantNpcHistorySet
    def ElementsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserAssistantNpcHistorySet
    def ElementsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def UserAssistantNpcHistorySetStart(builder):
    builder.StartObject(2)

def Start(builder):
    UserAssistantNpcHistorySetStart(builder)

def UserAssistantNpcHistorySetAddId(builder, id):
    builder.PrependUint32Slot(0, id, 0)

def AddId(builder, id):
    UserAssistantNpcHistorySetAddId(builder, id)

def UserAssistantNpcHistorySetAddElements(builder, elements):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(elements), 0)

def AddElements(builder, elements):
    UserAssistantNpcHistorySetAddElements(builder, elements)

def UserAssistantNpcHistorySetStartElementsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartElementsVector(builder, numElems):
    return UserAssistantNpcHistorySetStartElementsVector(builder, numElems)

def UserAssistantNpcHistorySetEnd(builder):
    return builder.EndObject()

def End(builder):
    return UserAssistantNpcHistorySetEnd(builder)
