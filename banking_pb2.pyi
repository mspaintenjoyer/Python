from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetBalanceRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UpdateBalanceRequest(_message.Message):
    __slots__ = ("user_id", "amount", "transaction_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    amount: float
    transaction_id: str
    def __init__(self, user_id: _Optional[str] = ..., amount: _Optional[float] = ..., transaction_id: _Optional[str] = ...) -> None: ...

class BalanceResponse(_message.Message):
    __slots__ = ("user_id", "balance")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    balance: float
    def __init__(self, user_id: _Optional[str] = ..., balance: _Optional[float] = ...) -> None: ...

class TransferRequest(_message.Message):
    __slots__ = ("from_user", "to_user", "amount")
    FROM_USER_FIELD_NUMBER: _ClassVar[int]
    TO_USER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    from_user: str
    to_user: str
    amount: float
    def __init__(self, from_user: _Optional[str] = ..., to_user: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...

class TransferResponse(_message.Message):
    __slots__ = ("status", "transaction_id", "timestamp")
    class TransferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUCCESS: _ClassVar[TransferResponse.TransferStatus]
        INSUFFICIENT_FUNDS: _ClassVar[TransferResponse.TransferStatus]
        INVALID_ACCOUNT: _ClassVar[TransferResponse.TransferStatus]
    SUCCESS: TransferResponse.TransferStatus
    INSUFFICIENT_FUNDS: TransferResponse.TransferStatus
    INVALID_ACCOUNT: TransferResponse.TransferStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    status: TransferResponse.TransferStatus
    transaction_id: str
    timestamp: str
    def __init__(self, status: _Optional[_Union[TransferResponse.TransferStatus, str]] = ..., transaction_id: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class HistoryRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class TransactionRecord(_message.Message):
    __slots__ = ("transaction_id", "counterparty", "amount", "timestamp")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    COUNTERPARTY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    counterparty: str
    amount: float
    timestamp: str
    def __init__(self, transaction_id: _Optional[str] = ..., counterparty: _Optional[str] = ..., amount: _Optional[float] = ..., timestamp: _Optional[str] = ...) -> None: ...

class HistoryResponse(_message.Message):
    __slots__ = ("transactions",)
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    transactions: _containers.RepeatedCompositeFieldContainer[TransactionRecord]
    def __init__(self, transactions: _Optional[_Iterable[_Union[TransactionRecord, _Mapping]]] = ...) -> None: ...
