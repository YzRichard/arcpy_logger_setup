# arcpy_logger_setup
## Requirement-要求
python 3.6及以上
windows 
## funtion- 功能
用于设置日志记录器的基本信息，该日志记录器可用于arcpy脚本工具的开发，arcpy的message,error,warning都可以被logging的level代替并输出到控制台，日志名称为日期格式化。日志存放路径需要自定义文件夹。
##  Usage-用法
```python
from logger_setup import LoggerConfig
import logging

# 创建LoggerConfig类的实例并调用setup_logging方法配置日志记录器
logger_config = LoggerConfig()
logger_config.setup_logging()

msg = 'Hello World'
logging.info(msg)
#arcpy.AddMessage(msg)
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
