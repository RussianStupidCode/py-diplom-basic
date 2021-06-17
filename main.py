from keeper import PhotosKeeper
from mytoken import YA_TOKEN

if __name__ == "__main__":
    photo_keeper = PhotosKeeper()
    photo_keeper.save_yandex_token(YA_TOKEN)
    photo_keeper.query_save_photos_vk(552934290)
    photo_keeper.query_save_photos_ok(576783256198)