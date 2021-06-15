from api.photos.vk.extractor import ExtractorVK
from api.photos.ok.extractor import ExtractorOK
from converter.photos_vk import ConverterVK
from converter.photos_ok import ConverterOK

if __name__ == "__main__":
    params = {
        'album_id': 'profile',
    }
    vk = ExtractorVK()
    photos = vk.get_photos(552934290, **params)
    photos = ConverterVK.convert(photos)

    for photo in photos:
        print(photo)

    ok = ExtractorOK()
    photos = ok.get_photos(576783256198)
    photos = ConverterOK.convert(photos)
    for photo in photos:
        print(photo)
