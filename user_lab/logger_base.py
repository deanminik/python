import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('data_layer.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Message from the level debug')
    log.info('Message from the level info')
    log.warning('Message from the level warning')
    log.error('Message from the level error')
    log.critical('Message from the level critical')
