# Hello World Demo

安装后，`helloworld` 会下载指定的 GitHub Release 文件，校验 SHA-256，设置执行权限并运行。远端文件是 Linux x86-64 可执行程序。

## 远程安装

从 GitHub 源码安装：

```bash
python3 -m pip install git+https://github.com/wyl091256/helloworld-package.git
helloworld
```

也可以从 GitHub Release 安装 wheel：

```bash
python3 -m pip install https://github.com/wyl091256/helloworld-package/releases/download/v0.2.1/hello_world_demo-0.2.1-py3-none-any.whl
helloworld
```

传给 `helloworld` 的参数会继续传给下载的程序：

```bash
helloworld --help
```
