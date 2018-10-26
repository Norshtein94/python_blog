import hashlib
import logging
import base64

logger = logging.getLogger('crypto')


class CryptoUtil:

    @staticmethod
    def md5_encode(data):
        encode_data = data.encode(encoding='UTF-8')
        crypto = hashlib.md5(encode_data).hexdigest()
        logger.info('data is %s and crypto is %s', data, crypto)
        return crypto

    @staticmethod
    def base64_encode(data):
        crypto = base64.b64encode(data.encode(encoding='UTF-8'))
        return crypto


if __name__ == '__main__':
    a = CryptoUtil.md5_encode('admin')
    print(a)
    b = CryptoUtil.base64_encode('admin 1 2 3 ')
    print(b)
