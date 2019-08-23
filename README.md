# EusWhitelist-Program  
## Minecraft Online Server's Whitelist Registration Tool By Python with MCRCON.   
## 由Python，Mcrcon完成的我的世界正版服务器白名单注册组件  
###**Powered by.leaves123 and ElaBosak233**

This software is a revision of EusWhitelist-CoolQ. It can get rid of the dependence of coolQ and perform whitelisting operation on the software. Users who have the ability can change the software to web version, hope to share your results, please don't forget Notice @ElaBosak233 and @leavessoft  
本软件是EusWhitelist-CoolQ的改版，可以摆脱CoolQ的依赖，在软件上执行添加白名单的操作，有能力的使用者可以将本软件改为网页版，希望能分享出你的成果，请不要忘了通知 @ElaBosak233 and @leavessoft  

Version comparison 版本对比  

EusWhitelist-Program|EusWhitelist-CoolQ
 --- | ---
Lighter environment更轻量的环境|More complete dependence更完整的依赖
Must open python program必须打开python程序|Must use CoolQ robot必须使用酷Q机器人
Remodelable可改造|Not recommended for renovation不推荐改造
Suitable for beginners适合初学者|Suitable for advanced programmers适合高级程序员
Powered by leavessoft and ElaBosak233|***Also*** powered by leavessoft and ElaBosak233 :)


**White List Module Code** ***key Annotations*** **白名单模块** ***重点注解***  
```
async def updateWhitelist():
    async with MinecraftClient('address', 'port', 'passwd') as mc:
        output = await mc.send('whitelist add ' + name)
        print(output)
#asyncio.run(updateWhitelist())
#Please use the above code as appropriate. 请按照情况使用上面的代码( asyncio.run(updateWhitelist())  )
```
**Fill 'address' , port , 'passwd' in the code (verifiction.py) 填充'地址',端口,'密码'在代码中(verifiction.py)**  
*Attention:address and passwd need quotation marks as strings, but port don't. 注意：地址和密码作为字符串需要加引号，但是端口不用*  
***Waring:Do not disclose your password, address, port, please try to choose non-25575 and other common ports 警告：不要透露你的密码、地址、端口，请尽量选择非25575等常见端口***  

★If a program error is found, please immediately feedback the vulnerability and attach a report chart,thanks. 若发现程序错误，请立即反馈漏洞并附上报告图，谢谢！  

☆Reference Statement 引用声明  
MrReacher's async-mcrcon (https://github.com/MrReacher/async-mcrcon)  

★Use recommendations 使用建议  
1.Please do not arbitrarily spread the software that has been filled in with the address, port and password to others, otherwise we will not be responsible for it.请不要随意将已填入地址、端口、密码的软件传播给他人，否则我们概不负责  
2.If you want to do whitelist operation with CoolQ, you can do it through another program of ours.**(https://github.com/ElaBosak233/EusWhitelist-CoolQ)**  若想通过酷Q进行白名单操作，你可以通过我们的另一个程序进行操作  **(https://github.com/ElaBosak233/EusWhitelist-CoolQ)**  
***3.Although we have a python environment(venv), we recommend that users have their own global python environment. 虽然我们有python环境(venv)，但是我们建议使用者再自备一个全局的python环境***

