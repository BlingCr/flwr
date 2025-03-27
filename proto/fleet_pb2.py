# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flwr/proto/fleet.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import node_pb2 as flwr_dot_proto_dot_node__pb2
from flwr.proto import task_pb2 as flwr_dot_proto_dot_task__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2
from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import message_pb2 as flwr_dot_proto_dot_message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66lwr/proto/fleet.proto\x12\nflwr.proto\x1a\x15\x66lwr/proto/node.proto\x1a\x15\x66lwr/proto/task.proto\x1a\x14\x66lwr/proto/run.proto\x1a\x14\x66lwr/proto/fab.proto\x1a\x18\x66lwr/proto/message.proto\"*\n\x11\x43reateNodeRequest\x12\x15\n\rping_interval\x18\x01 \x01(\x01\"4\n\x12\x43reateNodeResponse\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\"3\n\x11\x44\x65leteNodeRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\"\x14\n\x12\x44\x65leteNodeResponse\"D\n\x0bPingRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x15\n\rping_interval\x18\x02 \x01(\x01\"\x1f\n\x0cPingResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"F\n\x12PullTaskInsRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x10\n\x08task_ids\x18\x02 \x03(\t\"k\n\x13PullTaskInsResponse\x12(\n\treconnect\x18\x01 \x01(\x0b\x32\x15.flwr.proto.Reconnect\x12*\n\rtask_ins_list\x18\x02 \x03(\x0b\x32\x13.flwr.proto.TaskIns\"`\n\x12PushTaskResRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12*\n\rtask_res_list\x18\x02 \x03(\x0b\x32\x13.flwr.proto.TaskRes\"\xae\x01\n\x13PushTaskResResponse\x12(\n\treconnect\x18\x01 \x01(\x0b\x32\x15.flwr.proto.Reconnect\x12=\n\x07results\x18\x02 \x03(\x0b\x32,.flwr.proto.PushTaskResResponse.ResultsEntry\x1a.\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"J\n\x13PullMessagesRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12\x13\n\x0bmessage_ids\x18\x02 \x03(\t\"l\n\x14PullMessagesResponse\x12(\n\treconnect\x18\x01 \x01(\x0b\x32\x15.flwr.proto.Reconnect\x12*\n\rmessages_list\x18\x02 \x03(\x0b\x32\x13.flwr.proto.Message\"a\n\x13PushMessagesRequest\x12\x1e\n\x04node\x18\x01 \x01(\x0b\x32\x10.flwr.proto.Node\x12*\n\rmessages_list\x18\x02 \x03(\x0b\x32\x13.flwr.proto.Message\"\xb0\x01\n\x14PushMessagesResponse\x12(\n\treconnect\x18\x01 \x01(\x0b\x32\x15.flwr.proto.Reconnect\x12>\n\x07results\x18\x02 \x03(\x0b\x32-.flwr.proto.PushMessagesResponse.ResultsEntry\x1a.\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"\x1e\n\tReconnect\x12\x11\n\treconnect\x18\x01 \x01(\x04\x32\xb6\x05\n\x05\x46leet\x12M\n\nCreateNode\x12\x1d.flwr.proto.CreateNodeRequest\x1a\x1e.flwr.proto.CreateNodeResponse\"\x00\x12M\n\nDeleteNode\x12\x1d.flwr.proto.DeleteNodeRequest\x1a\x1e.flwr.proto.DeleteNodeResponse\"\x00\x12;\n\x04Ping\x12\x17.flwr.proto.PingRequest\x1a\x18.flwr.proto.PingResponse\"\x00\x12P\n\x0bPullTaskIns\x12\x1e.flwr.proto.PullTaskInsRequest\x1a\x1f.flwr.proto.PullTaskInsResponse\"\x00\x12S\n\x0cPullMessages\x12\x1f.flwr.proto.PullMessagesRequest\x1a .flwr.proto.PullMessagesResponse\"\x00\x12P\n\x0bPushTaskRes\x12\x1e.flwr.proto.PushTaskResRequest\x1a\x1f.flwr.proto.PushTaskResResponse\"\x00\x12S\n\x0cPushMessages\x12\x1f.flwr.proto.PushMessagesRequest\x1a .flwr.proto.PushMessagesResponse\"\x00\x12\x41\n\x06GetRun\x12\x19.flwr.proto.GetRunRequest\x1a\x1a.flwr.proto.GetRunResponse\"\x00\x12\x41\n\x06GetFab\x12\x19.flwr.proto.GetFabRequest\x1a\x1a.flwr.proto.GetFabResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.fleet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PUSHTASKRESRESPONSE_RESULTSENTRY']._options = None
  _globals['_PUSHTASKRESRESPONSE_RESULTSENTRY']._serialized_options = b'8\001'
  _globals['_PUSHMESSAGESRESPONSE_RESULTSENTRY']._options = None
  _globals['_PUSHMESSAGESRESPONSE_RESULTSENTRY']._serialized_options = b'8\001'
  _globals['_CREATENODEREQUEST']._serialized_start=154
  _globals['_CREATENODEREQUEST']._serialized_end=196
  _globals['_CREATENODERESPONSE']._serialized_start=198
  _globals['_CREATENODERESPONSE']._serialized_end=250
  _globals['_DELETENODEREQUEST']._serialized_start=252
  _globals['_DELETENODEREQUEST']._serialized_end=303
  _globals['_DELETENODERESPONSE']._serialized_start=305
  _globals['_DELETENODERESPONSE']._serialized_end=325
  _globals['_PINGREQUEST']._serialized_start=327
  _globals['_PINGREQUEST']._serialized_end=395
  _globals['_PINGRESPONSE']._serialized_start=397
  _globals['_PINGRESPONSE']._serialized_end=428
  _globals['_PULLTASKINSREQUEST']._serialized_start=430
  _globals['_PULLTASKINSREQUEST']._serialized_end=500
  _globals['_PULLTASKINSRESPONSE']._serialized_start=502
  _globals['_PULLTASKINSRESPONSE']._serialized_end=609
  _globals['_PUSHTASKRESREQUEST']._serialized_start=611
  _globals['_PUSHTASKRESREQUEST']._serialized_end=707
  _globals['_PUSHTASKRESRESPONSE']._serialized_start=710
  _globals['_PUSHTASKRESRESPONSE']._serialized_end=884
  _globals['_PUSHTASKRESRESPONSE_RESULTSENTRY']._serialized_start=838
  _globals['_PUSHTASKRESRESPONSE_RESULTSENTRY']._serialized_end=884
  _globals['_PULLMESSAGESREQUEST']._serialized_start=886
  _globals['_PULLMESSAGESREQUEST']._serialized_end=960
  _globals['_PULLMESSAGESRESPONSE']._serialized_start=962
  _globals['_PULLMESSAGESRESPONSE']._serialized_end=1070
  _globals['_PUSHMESSAGESREQUEST']._serialized_start=1072
  _globals['_PUSHMESSAGESREQUEST']._serialized_end=1169
  _globals['_PUSHMESSAGESRESPONSE']._serialized_start=1172
  _globals['_PUSHMESSAGESRESPONSE']._serialized_end=1348
  _globals['_PUSHMESSAGESRESPONSE_RESULTSENTRY']._serialized_start=838
  _globals['_PUSHMESSAGESRESPONSE_RESULTSENTRY']._serialized_end=884
  _globals['_RECONNECT']._serialized_start=1350
  _globals['_RECONNECT']._serialized_end=1380
  _globals['_FLEET']._serialized_start=1383
  _globals['_FLEET']._serialized_end=2077
# @@protoc_insertion_point(module_scope)
