from baserow.api.user.registries import UserDataType

from baserow_premium.license.handler import has_active_premium_license_for


class PremiumUserDataType(UserDataType):
    type = "premium"

    def get_user_data(self, user, request) -> dict:
        """
        Someone who authenticates via the API should know beforehand if the related
        user has a valid license for the premium version.
        """

        return {
            "valid_license": has_active_premium_license_for(user),
        }
