
from eduvpn.metadata import Metadata

def yubi_enroll_window(builder, oauth, meta: Metadata, config_dict: dict) -> None: ...
def _parse_user_input(builder, oauth, meta: Metadata, config_dict: dict) -> None: ...
def _enroll(builder, oauth, meta: Metadata, config_dict: dict, key: str) -> None: ...