from enum import Enum


class ProductErrorCode(Enum):
    ALREADY_EXISTS = "already_exists"
    DUPLICATED_INPUT_ITEM = "duplicated_input_item"
    GRAPHQL_ERROR = "graphql_error"
    INVALID = "invalid"
    PRODUCT_WITHOUT_CATEGORY = "product_without_category"
    NOT_PRODUCTS_IMAGE = "not_products_image"
    NOT_FOUND = "not_found"
    REQUIRED = "required"
    UNIQUE = "unique"
