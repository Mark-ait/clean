# clean
ITCT clean tools
##李联华的博客
                
### 绘制流程图 Flowchart

```flow
st=>start: 清理Temp文件
op=>operation: 清理缓存文件
cond=>condition: 清理目录下文件 Yes or No?
e=>end: 清理成功

st->op->cond
cond(yes)->e
cond(no)->op
```
                    
