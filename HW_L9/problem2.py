class Image:
    DB = {
        '/images/img1': 'Image1',
        '/images/img2': 'Image2',
        '/images/img3': 'Image3',
    }

    def show(self, path):
        print(f'Showing image at {path} - {Image.DB[path]}.')

class ImageProxy:

    def __init__(self):
        self.is_loaded = {
            '/images/img1': False,
            '/images/img2': False,
            '/images/img3': False,
        }
        self.image = None

    def show(self, path):
        if self.__check_loaded(path):
            self.image = Image()
            self.image.show(path)
        else:
            print(f'The image at {path} is loading ...')

            self.is_loaded[path] = True

            print(f'The image at {path} is loaded ...')

    def __check_loaded(self, path):
        print(f'Proxy: Checking whether image at {path} is loaded prior to displaying it ...')

        return self.is_loaded[path]

image_proxy = ImageProxy()

image_proxy.show('/images/img2')
image_proxy.show('/images/img1')
image_proxy.show('/images/img1')
image_proxy.show('/images/img2')
image_proxy.show('/images/img3')
image_proxy.show('/images/img1')