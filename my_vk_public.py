import vk
from vk_public import VKPublic
from os import environ

# public_id = '-101534490' # posloosha.instagram : 119749591
public_id = '-101534490' # posloosha.periscope
# vksession = vk.AuthSession(user_login=environ.get("VK_EMAIL"),
#                            user_password=environ.get("VK_PASS"),
#                            app_id='5244211',
#                            scope='wall,photos,offline')
vksession = vk.Session(access_token=environ.get("VK_ACCESS_TOKEN"))
vkapi = vk.API(vksession, lang='ru')
vkpublic = VKPublic(vkapi, public_id)


def main():
    print(f"Posted suggests: {vkpublic.publish_suggests()}")

if __name__ == '__main__':
    main()
