# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clickhouse_path/format_schemas/nats.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n)clickhouse_path/format_schemas/nats.proto"+\n\rProtoKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\tb\x06proto3'
)


_PROTOKEYVALUE = DESCRIPTOR.message_types_by_name["ProtoKeyValue"]
ProtoKeyValue = _reflection.GeneratedProtocolMessageType(
    "ProtoKeyValue",
    (_message.Message,),
    {
        "DESCRIPTOR": _PROTOKEYVALUE,
        "__module__": "clickhouse_path.format_schemas.nats_pb2"
        # @@protoc_insertion_point(class_scope:ProtoKeyValue)
    },
)
_sym_db.RegisterMessage(ProtoKeyValue)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _PROTOKEYVALUE._serialized_start = 45
    _PROTOKEYVALUE._serialized_end = 88
# @@protoc_insertion_point(module_scope)
