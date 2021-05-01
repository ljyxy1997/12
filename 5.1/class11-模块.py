import max #导入了max模块
a=max.fun_max(1,2)
print(a)

from max import fun_max #从max模块导入fun_max函数
a=fun_max(1,2)
print(a)

from max import * #导入max模块中所有的内容

import max as m #导入max,用as指定max的别名为m
a=m.fun_max(1,2)
print(a)