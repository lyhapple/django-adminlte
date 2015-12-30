#目录说明
仅显示两级目录
##应用都是默认在内部建立相关配置.
.
├── apps                            #此目录用于放置非核心app
├── core                            #此目录用于放置核心目录
│   ├── adminlte                    #权限控制目录
│   ├── messageset                  #消息
│   ├── organization                #公司基础信息
│   └── registration                #调用
├── install                         #安装相关
│   ├── bin                         #启动文件
│   ├── conf                        #配置文件
│   ├── data                        #初始数据
│   ├── docs                        #文档
│   └── requirement                 #安装相关
├── logs                            #日志存储-可能需要创建
├── lteadmin                        #django 默认目录
├── media                           #上传内容
│   └── adminlte                        #上传存储目录
└── static                          #js信息