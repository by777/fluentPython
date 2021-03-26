# -*- coding: utf-8 -*-
# @TIME : 2021/3/26 12:37
# @AUTHOR : Xu Bai
# @FILE : 5-3-1.TensorBoard.py
# @DESCRIPTION :
from tensorboard_logger import Logger

# ternsorboard --logdir experimient_cnn
# 构建logger对象，logdir用来指定log文件路径
# flush_secs指定刷新同步间隔
logger = Logger(logdir='experimient_cnn', flush_secs=2)
for ii in range(100):
    logger.log_value('loss', 10 - ii * .5, step=ii)
    logger.log_value('accuracy', ii * .5 / 10)
