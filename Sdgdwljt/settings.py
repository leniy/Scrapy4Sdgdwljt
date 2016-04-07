# -*- coding: utf-8 -*-

BOT_NAME = 'Sdgdwljt'

SPIDER_MODULES = ['Sdgdwljt.spiders']
NEWSPIDER_MODULE = 'Sdgdwljt.spiders'

ITEM_PIPELINES = {
    'Sdgdwljt.pipelines.SdgdwljtPipeline': 300,
}
