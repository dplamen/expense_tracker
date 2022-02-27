from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Ensure this value contains only letters.")


def validate_max_image_size(value):
    allowed_size = 5.0
    if value.file.size > allowed_size * 1024 * 1024:
        raise ValidationError(f'Max file size is {allowed_size:.2f} MB')


@deconstructible
class ValidateMaxSizeImage:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {self.max_size:.2f} MB')
