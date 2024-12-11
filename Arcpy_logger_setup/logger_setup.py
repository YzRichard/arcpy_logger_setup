# -*- coding:utf-8 -*-
# 作者：wyx
# 创建：2024-12-11
# 更新：2024-12-11
# 用意：用于设置一个arcpy的日志记录器，arcpy工具及脚本的信息流可以被logging记录


import arcpy
from logger_setup import LoggerConfig  # 从logger_setup模块中导入LoggerConfig类
import logging  # 导入logging库，用于后续记录日志操作
from datetime import datetime as times

# 创建LoggerConfig类的实例并调用setup_logging方法配置日志记录器
logger_config = LoggerConfig()
logger_config.setup_logging()

# 空值替换
def AltEmptyValue(lyrs):
    try:
        # 记录函数开始执行的时间以及相关操作信息
        msg = '{} 开始无字节空值替换\'<空>\''.format(str(times.now()).split('.')[0])
        logging.info(msg)
        #arcpy.AddMessage(msg)

        for lyr in lyrs:
            # 获取需要检查的字段
            field_list = []
            for name in arcpy.ListFields(lyr):
                field_list.append(name.baseName)
            logging.info(f"正在处理图层 {lyr}，需检查的字段为: {field_list}")

            # 开始替换空值
            with arcpy.da.UpdateCursor(lyr, field_list) as cursor:
                for row in cursor:
                    while '' in row:
                        row[row.index('')] = None
                        logging.debug(f"在图层 {lyr} 的行数据中发现空值，已替换为None")
                    cursor.updateRow(row)
            logging.info(f"图层 {lyr} 的无字节空值替换'<空>'操作完成")

        #arcpy.AddMessage('无字节空值替换\'<空>\'完成')
        logging.info('无字节空值替换\'<空>\'完成')
    except Exception as e:
        # 若出现异常，记录详细的错误信息
        msg = f"在无字节空值替换过程中出现错误: {str(e)}"
        logging.error(msg)
        #arcpy.AddMessage(msg)
