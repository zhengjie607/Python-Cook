import os
import math
import ctypes

from msl.loadlib import Server32

class Extmdl32(Server32):
    def __init__(self, host, port, quiet, **kwargs):
        super(Extmdl32, self).__init__(os.path.join(os.path.dirname(__file__), 'ExtMdl'),
                                    'windll', host, port, quiet)
    def GT_OpenExtMdl(self):
        '''
        指令说明：调用 GT_OpenExtMdl 指令打开扩展模块，以获取对扩展模块的访问权。当
        扩展模块与运动控制器的运动控制功能同时使用时，需要先打开运动控制功能，再打开
        扩展模块功能。打开扩展模块功能时，需要指定运动控制功能所使用的动态链接库的文
        件名称。
        指令参数：
        *pDllName：需要指定的运动控制功能动态链接库的文件名称。
        '''
        self.lib.GT_OpenExtMdl.restype = ctypes.c_short
        return self.lib.GT_OpenExtMdl(ctypes.create_string_buffer(b'gts.dll'))

    def GT_CloseExtMdl(self):
        '''
        指令说明：关闭扩展模块，当不再使用扩展模块时，调用该指令以释放扩展模块的访问
        权。
        指令参数：无。
        '''
        self.lib.GT_CloseExtMdl()
    def GT_SwitchtoCardNoExtMdl(self,card):
        '''
        指令说明：该指令用于切换当前扩展模块相关的运动控制器卡号。
        指令参数：
        card：将被设为当前运动控制器的卡号。
        '''
        self.lib.GT_SwitchtoCardNoExtMdl(ctypes.c_short(card))

    def GT_ResetExtMdl(self):
        '''
        指令说明：该指令用于复位扩展模块，调用该指令后，系统会扫描所有连接的扩展模块，
        所有连接的工作正常的模块都会被使能。
        '''
        self.lib.GT_ResetExtMdl()
    def GT_LoadExtConfig(self,pFileName):
        '''
        指令说明：加载扩展模块系统配置文件，关于该文件的格式以及内容说明，参照第四节。
        指令参数：
        *pFileName：配置文件的文件名。
        '''
        self.lib.GT_LoadExtConfig(ctypes.create_string_buffer(bytes(pFileName,encoding='utf-8')))

    def GT_SetExtIoValue(self,mdl,value):
        '''
        指令说明：设置数字量 IO 扩展模块的输出值，按字(16 位)操作。
        指令参数：
        mdl：模块的编号，即参照配置文件，该数字量 IO 的模块编号。范围[0，15]。
        Value：输出到数字量 IO 上的 16 位值。
        '''
        self.lib.GT_SetExtIoValue(ctypes.c_short(mdl),ctypes.c_ushort(value))
    def GT_GetExtIoValue(self,mdl,pValue):
        '''
        指令说明：读取数字量 IO 扩展模块的输入值，按字(16 位)操作。
        指令参数：
        mdl：模块的编号，即参照配置文件，该数字量 IO 的模块编号。
        *pValue：读取的数字量 IO 上的 16 位值。,unsigned short
        '''
        self.lib.GT_GetExtIoValue(ctypes.c_short(mdl),ctypes.pointer(pValue))

    def GT_SetExtIoBit(self,mdl,index,value):
        '''
        指令说明：设置数字量 IO 扩展模块的输出值，按位操作。
        指令参数：
        mdl：模块的编号，即参照配置文件，该数字量 IO 的模块编号，范围[0，15]。
        Index：所要操作的位，取值范围[0,15]。
        Value：所要输出的 IO 的值，取值范围[0,1]。
        '''
        self.lib.GT_SetExtIoBit(ctypes.c_short(mdl),ctypes.c_short(index),ctypes.c_ushort(value))
    def GT_GetExtIoBit(self,mdl,index,pValue):
        '''
        指令说明：读取数字量 IO 扩展模块的输入值，按位操作。
        指令参数：
        mdl：模块的编号，即参照配置文件，该数字量 IO 的模块编号，范围[0，15]。
        Index：所要操作的位，取值范围[0,15]。
        *pValue：所读取的输入 IO 相应位的值。unsigned short
        '''
        self.lib.GT_GetExtIoBit(ctypes.c_short(mdl),ctypes.c_short(index),ctypes.pointer(pValue))

    def GT_GetExtAdValue(self,mdl,chn,pValue):
        '''
        指令说明：读取 AD 扩展模块输入的转换值。
        指令参数：
        mdl：模块的编号，即参照配置文件，该 AD 扩展模块的模块编号，范围[0，15]。
        Chn：需要读取的 AD 扩展模块中的通道号。
        *pValue：读取的 AD 扩展模块转换位的值。unsigned short
        '''
        self.lib.GT_GetExtAdValue(ctypes.c_short(mdl),ctypes.c_short(chn),ctypes.pointer(pValue))
    def GT_GetExtAdVoltage(self,mdl,chn,pValue):
        '''
        指令说明：读取 AD 扩展模块输入的电压值。
        指令参数：
        mdl：模块的编号，即参照配置文件，该 AD 扩展模块的模块编号，范围[0，15]。
        Chn：需要读取的 AD 扩展模块中的通道号。
        *pValue：读取的 AD 扩展模块输入的电压值。double
        '''
        self.lib.GT_GetExtAdVoltage(ctypes.c_short(mdl),ctypes.c_short(chn),ctypes.pointer(pValue))

    def GT_SetExtDaValue(self,mdl,chn,value):
        '''
        指令说明：设置 DA 扩展模块输出电压的转换值。
        指令参数：
        mdl：模块的编号，即参照配置文件，该 DA 扩展模块的模块编号，范围[0，15]。
        Chn：需要设置的 DA 扩展模块中的通道号，范围[0,模块可用通道数-1]。
        Value：设置的 DA 扩展模块输出值。
        '''
        self.lib.GT_SetExtDaValue(ctypes.c_short(mdl),ctypes.c_short(chn),ctypes.c_ushort(value))
    def GT_SetExtDaVoltage(self,mdl,chn,value):
        '''
        指令说明：设置 DA 扩展模块输出电压的电压值。
        指令参数：
        mdl：模块的编号，即参照配置文件，该 DA 扩展模块的模块编号，范围[0，15]。
        Chn：需要设置的 DA 扩展模块中的通道号。
        Value：设置的 DA 扩展模块输出电压值，范围[0,模块可用通道数-1]。
        '''
        self.lib.GT_SetExtDaVoltage(ctypes.c_short(mdl),ctypes.c_short(chn),ctypes.c_double(value))

    def GT_GetStsExtMdl(self,mdl,chn,pStatus):
        '''
        指令说明：读取扩展模块的状态，当该模块通信工作正常时，读回的值为 0，否则为 1。
        指令参数：
        mdl：模块的编号，即参照配置文件，相应扩展模块的模块编号，范围[0，15]。
        Chn：当模块为 AD 模块或者 DA 模块时，需要制定的通道号。当为数字量输入/输出模
        块时，该参数无效。
        *pStatus：读取的状态值，0：工作正常；1：有故障。unsigned short
        '''
        self.lib.GT_GetStsExtMdl(ctypes.c_short(mdl),ctypes.c_short(chn),ctypes.pointer(pStatus))
    def GT_SetExtMdlMode(self,mode):
        '''
        指令说明：设置当前扩展模块的工作模式。
        扩展模块有两种工作模式，直接控制模式和内部控制模式，默认为直接控制模式。
        如果用户希望通过运动控制程序（运动控制程序是固高 GTS 系列运动控制器的一
        个功能，详情请参考固高 GTS 运动控制器的相关资料），则需要将扩展模块的工作方式
        设置为内部工作模式。
        其他情况下，请使用直接控制模式。
        注意：该指令必须用于 GT_LoadExtConfig 指令之后。
        指令参数：
        mode：模式，0—直接模式，1—内部控制模块。
        '''
        self.lib.GT_SetExtMdlMode(ctypes.c_short(mode))

    def GT_GetExtMdlMode(self,pMode):
        '''
        指令说明：读取当前扩展模块的工作模式。
        指令参数：
        pMode：模式，0—直接模式，1—内部控制模块。short
        '''
        self.lib.GT_GetExtMdlMode(ctypes.pointer(pMode))
    