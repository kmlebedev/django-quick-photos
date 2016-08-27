from mezzanine.conf import register_setting

register_setting(
    name="INSTAGRAM_ACCESS_TOKEN",
    description="Get instagram access token https://www.instagram.com/developer/authentication/",
    editable=False,
    default="",
)
register_setting(
    name="INSTAGRAM_CLIENT_ID",
    description="Get instagram client ID https://www.instagram.com/developer/authentication/",
    editable=True,
    default="",
)
register_setting(
    name="INSTAGRAM_CLIENT_SECRET",
    description="Get instagram client secret https://www.instagram.com/developer/authentication/",
    editable=True,
    default="",
)