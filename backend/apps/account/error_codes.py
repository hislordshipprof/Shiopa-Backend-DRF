from enum import Enum


class AccountErrorCode(Enum):
    ACTIVATE_OWN_ACCOUNT = "activate_own_account"
    INACTIVE = "inactive"
    INVALID = "invalid"
    DUPLICATED_INPUT_ITEM = "duplicated_input_item"
    DEACTIVATE_OWN_ACCOUNT = "deactivate_own_account"
    DELETE_OWN_ACCOUNT = "delete_own_account"
    INVALID_PASSWORD = "invalid_password"
    INVALID_CREDENTIALS = "invalid_credentials"
    NOT_FOUND = "not_found"
    PASSWORD_TOO_COMMON = "password_too_common"
    PASSWORD_TOO_SHORT = "password_too_short"
    PASSWORD_TOO_SIMILAR = "password_too_similar"
    REQUIRED = "required"
    UNIQUE = "unique"
    JWT_SIGNATURE_EXPIRED = "signature_has_expired"
    JWT_INVALID_TOKEN = "invalid_token"
    JWT_MISSING_TOKEN = "missing_token"
    JWT_INVALID_CSRF_TOKEN = "invalid_csrf_token"

