### 对Django的认识？
1. Django是走大而全的方向，它最出名的是其全自动化的管理后台：只需要使用起ORM，做简单的对象定义，它就能自动生成数据库结构、以及全功能的管理后台。

2. Django内置的ORM跟框架内的其他模块耦合程度高。应用程序必须使用Django内置的ORM，否则就不能享受到框架内提供的种种基于其ORM的便利；理论上可以切换掉其ORM模块，但这就相当于要把装修完毕的房子拆除重新装修，倒不如一开始就去毛胚房做全新的装修。

3. Django的卖点是超高的开发效率，其性能扩展有限；采用Django的项目，在流量达到一定规模后，都需要对其进行重构，才能满足性能的要求。

4. Django适用的是中小型的网站，或者是作为大型网站快速实现产品雏形的工具。

5. Django模板的设计哲学是彻底的将代码、样式分离； Django从根本上杜绝在模板中进行编码、处理数据的可能。 

### Django 、Flask、Tornado的对比
- Django走的是大而全的方向,开发效率高。它的MTV框架,自带的ORM,admin后台管理,自带的sqlite数据库和开发测试用的服务器给开发者提高了超高的开发效率

- Flask是轻量级的框架,自由,灵活,可扩展性很强,核心基于Werkzeug WSGI工具和jinja2模板引擎

- Tornado走的是少而精的方向,性能优越。它最出名的是异步非阻塞的设计方式Tornado的两大核心模块： 1、iostraem：对非阻塞式的socket进行简单的封装 2、ioloop：对I/O多路复用的封装，它实现了一个单例

 

### 什么是wsgi,uwsgi,uWSGI？
WSGI:web服务器网关接口,是一套协议。用于接收用户请求并将请求进行初次封装，然后将请求交给web框架

实现wsgi协议的模块： 1.wsgiref,本质上就是编写一个socket服务端，用于接收用户请求(django) 2.werkzeug,本质上就是编写一个socket服务端，用于接收用户请求(flask)

uwsgi:与WSGI一样是一种通信协议，它是uWSGI服务器的独占协议,用于定义传输信息的类型

uWSGI:是一个web服务器,实现了WSGI协议,uWSGI协议,http协议,

 

### django请求的生命周期？
1. wsgi,请求封装后交给web框架 （Flask、Django）

2. 中间件，对请求进行校验或在请求对象中添加其他相关数据，例如：csrf、request.session -

3. 路由匹配 根据浏览器发送的不同url去匹配不同的视图函数

4. 视图函数，在视图函数中进行业务逻辑的处理，可能涉及到：orm、templates => 渲染 -

5. 中间件，对响应的数据进行处理。

6. wsgi,将响应的内容发送给浏览器。

### 简述什么是FBV和CBV？
FBV和CBV本质是一样的 基于函数的视图叫做FBV，基于类的视图叫做CBV 在python中使用CBV的优点：

1.提高了代码的复用性，可以使用面向对象的技术，比如Mixin（多继承）

2.可以用不同的函数针对不同的HTTP方法处理，而不是通过很多if判断，提高代码可读性

 

### 如何给CBV的程序添加装饰器？
引入method_decorator模块

1.直接在类上加装饰器

```python
@method_decorator(test,name='dispatch') 
class Loginview(View): 
     pass
```

2.直接在处理的函数前加装饰器

```python
@method_decorator(test) 
def post(self,request,*args,**kwargs):
        pass
```

### 简述MVC和MTV
MVC软件系统分为三个基本部分：模型(Model)、视图(View)和控制器(Controller) Model：负责业务对象与数据库的映射(ORM) View：负责与用户的交互 Control：接受用户的输入调用模型和视图完成用户的请求

Django框架的MTV设计模式借鉴了MVC框架的思想,三部分为：Model、Template和View 

Model(模型)：负责业务对象与数据库的对象(ORM) 

Template(模版)：负责如何把页面展示给用户 

View(视图)：负责业务逻辑，并在适当的时候调用Model和Template 此外,Django还有一个urls分发器, 它将一个个URL的页面请求分发给不同的view处理,view再调用相应的Model和Template

### django路由系统中name的作用？
用于反向解析路由,相当于给url取个别名，只要这个名字不变,即使对应的url改变 通过该名字也能找到该条url

### 列举django的内置组件？
1. Admin是对model中对应的数据表进行增删改查提供的组件

2. model组件：负责操作数据库

3. form组件：1.生成HTML代码2.数据有效性校验3校验信息返回并展示

4. ModelForm组件即用于数据库操作,也可用于用户请求的验证

 

### 说一下Django，MIDDLEWARES中间件的作用和应用场景？
中间件是介于request与response处理之间的一道处理过程,用于在全局范围内改变Django的输入和输出。 #简单的来说中间件是帮助我们在视图函数执行之前和执行之后都可以做一些额外的操作 例如：

1.Django项目中默认启用了csrf保护,每次请求时通过CSRF中间件检查请求中是否有正确token值 
2.当用户在页面上发送请求时，通过自定义的认证中间件，判断用户是否已经登陆，未登陆就去陆。 
3.当有用户请求过来时，判断用户是否在白名单或者在黑名单里
4.统计
列举django中间件的5个方法？

- process_request : 请求进来时,权限认证

- process_view : 路由匹配之后,能够得到视图函数

- process_exception : 异常时执行

- process_template_responseprocess : 模板渲染时执行

- process_response : 请求有响应时执行

 

### django的request对象是在什么时候创建的？
class WSGIHandler(base.BaseHandler): # request = self.request_class(environ) 请求走到WSGIHandler类的时候，执行cell方法，将environ封装成了request

### Django重定向是如何实现的？用的什么状态码？
1.使用HttpResponseRedirect from django.http import HttpResponseRedirect

2.使用redirect和reverse 状态码：301和302 #301和302的区别： 

相同点：都表示重定向，浏览器在拿到服务器返回的这个状态码后会自动跳转到一个新的URL地址 

不同点： 301比较常用的场景是使用域名跳转。

- 比如，我们访问 http://www.baidu.com 会跳转到 https://www.baidu.com 表示旧地址A的资源已经被永久地移除了 .302用来做临时跳转，比如未登陆的用户访问用户中心重定向到登录页面。表示旧地址A的资源还在（仍然可以访问），这个重定向只是临时地从旧地址A跳转到地址B

### django中csrf的实现机制
第一步：django第一次响应来自某个客户端的请求时,后端随机产生一个token值，把这个token保存在SESSION状态中;同时,后端把这个token放到cookie中交给前端页面；

第二步：下次前端需要发起请求（比如发帖）的时候把这个token值加入到请求数据或者头信息中,一起传给后端；Cookies:{csrftoken:xxxxx}

第三步：后端校验前端请求带过来的token和SESSION里的token是否一致；

### 基于django使用ajax发送post请求时，都可以使用哪种方法携带csrf token？
1.后端将csrftoken传到前端，发送post请求时携带这个值发送data: {csrfmiddlewaretoken: '{{ csrf_token }}' }, 2.获取form中隐藏标签的csrftoken值，加入到请求数据中传给后端 data: {csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val()},

3.cookie中存在csrftoken,将csrftoken值放到请求头中headers:{ "X-CSRFtoken":$.cookie("csrftoken")}，

 

### Django本身提供了runserver，为什么不能用来部署？(runserver与uWSGI的区别)
1. runserver方法是调试 Django 时经常用到的运行方式，它使用Django自带的 WSGI Server 运行，主要在测试和开发中使用，并且 runserver 开启的方式也是单进程 。

2. uWSGI是一个Web服务器，它实现了WSGI协议、uwsgi、http 等协议。注意uwsgi是一种通信协议，而uWSGI是实现uwsgi协议和WSGI协议的 Web 服务器。 uWSGI具有超快的性能、低内存占用和多app管理等优点，并且搭配着Nginx就是一个生产环境了，能够将用户访问请求与应用 app 隔离开，实现真正的部署 。 相比来讲，支持的并发量更高，方便管理多进程，发挥多核的优势，提升性能。

### cookie和session的区别：
1.cookie:

 cookie是保存在浏览器端的键值对,可以用来做用户认证 
2.session： 将用户的会话信息保存在服务端,key值是随机产生的自符串,value值时session的内容 ,依赖于cookie将每个用户的随机字符串保存到用户浏览器上

Django中session默认保存在数据库中：django_session表 flask,session默认将加密的数据写在用户的cookie中

### 列举django orm 中所有的方法（QuerySet对象的所有方法）
all(): 查询所有结果

filter(**kwargs): 它包含了与所给筛选条件相匹配的对象。获取不到返回None

get(**kwargs): 返回与所给筛选条件相匹配的对象，返回结果有且只有一个。获取不到会抛异常如果符合筛选条件的对象超过一个或者没有都会抛出错误。

exclude(**kwargs): 它包含了与所给筛选条件不匹配的对象

order_by(*field): 对查询结果排序

reverse(): 对查询结果反向排序

count(): 返回数据库中匹配查询(QuerySet)的对象数量。

first(): 返回第一条记录

last(): 返回最后一条记录

exists(): 如果QuerySet包含数据，就返回True，否则返回False

values(*field): 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的并不是一系 model的实例化对象，而是一个可迭代的字典序列 values_list(*field): 它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列

distinct(): 从返回结果中剔除重复纪录

 

### only和defer的区别？
only:从数据库中只取指定字段的内容 defer：指定字段的内容不被检索

### select_related和prefetch_related的区别？
有外键存在时，可以很好的减少数据库请求的次数,提高性能 #select_related通过多表join关联查询,一次性获得所有数据,只执行一次SQL查询 #prefetch_related分别查询每个表,然后根据它们之间的关系进行处理,执行两次查询

 

### filter和exclude的区别？
取到的值都是QuerySet对象,filter选择满足条件的,exclude:排除满足条件的.

### django的Form和ModeForm的作用？
Form作用：1.在前端生成HTML代码 # 2.对数据作有效性校验 # 3.返回校验信息并展示 #ModeForm：根据模型类生成From组件,并且可以操作数据库

 

django的Form组件中,如果字段中包含choices参数，请使用两种方式实现数据源实时更新。
1.重写构造函数

```python
def def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["city"].widget.choices = models.City.objects.all().values_list("id", "name") 
```



2.利用ModelChoiceField字段,参数为queryset对象

### django orm 中如何设置读写分离？
1. 手动读写分离:通过.using(db_name)来指定要使用的数据库 ;
2. 自动读写分离:

 1.定义类：如Router # 
 2.配置Router  settings.py中指定DATABASE_ROUTERS 
 DATABASE_ROUTERS = ['myrouter.Router',] 

提高读的性能：多配置几个数据库,并在读取时,随机选取。写的时候写到主库 实现app之间的数据库分离：分库分表

 

### django内置的缓存机制？
全站缓存

```python
MIDDLEWARE_CLASSES = (
    ‘django.middleware.cache.UpdateCacheMiddleware’, #第一
    'django.middleware.common.CommonMiddleware',
    ‘django.middleware.cache.FetchFromCacheMiddleware’, #最后
) 
```



视图缓存

```python
from django.views.decorators.cache import cache_page import time

@cache_page(15)          #超时时间为15秒
def index(request):
     t=time.time()      #获取当前时间
     return render(request,"index.html",locals()) 
```



模板缓存

{% load cache %}
 <h3 style="color: green">不缓存:-----{{ t }}</h3>

{% cache 2 'name' %} # 存的key
 <h3>缓存:-----:{{ t }}</h3>
{% endcache %}

### 使用orm和原生sql的优缺点？
1.orm的开发速度快,操作简单。使开发更加对象化 #执行速度慢。处理多表联查等复杂操作时,ORM的语法会变得复杂 

2.sql开发速度慢,执行速度快。性能强

 

### django中如何根据数据库表生成model中的类？
1.在settings中设置要连接的数据库2.生成model模型文件python manage.py inspectdb3.模型文件导入到models中 python manage.py inspectdb > app/models.py

 

### 为什么要使用django rest framework框架？
能自动生成符合 RESTful 规范的 API #1.在开发REST API的视图中，虽然每个视图具体操作的数据不同， #但增、删、改、查的实现流程基本一样,这部分的代码可以简写 #2.在序列化与反序列化时，虽然操作的数据不同，但是执行的过程却相似,这部分的代码也可以简写 #REST framework可以帮助简化上述两部分的代码编写，大大提高REST API的开发速度

 

### django rest framework框架中都有那些组件？
1. 序列化组件:serializers 对queryset序列化以及对请求数据格式校验

2. 路由组件routers 进行路由分发

3. 视图组件ModelViewSet 帮助开发者提供了一些类，并在类中提供了多个方法

4. 认证组件 写一个类并注册到认证类(authentication_classes)，在类的的authticate方法中编写认证逻

5. 权限组件 写一个类并注册到权限类(permission_classes)，在类的的has_permission方法中编写认证逻辑。

6. 频率限制 写一个类并注册到频率类(throttle_classes)，在类的的allow_request/wait 方法中编写认证逻辑

7. 解析器 选择对数据解析的类，在解析器类中注册(parser_classes)

8. 渲染器 定义数据如何渲染到到页面上,在渲染器类中注册(renderer_classes)

9. 分页 对获取到的数据进行分页处理, pagination_class

10. 版本 版本控制用来在不同的客户端使用不同的行为 #在url中设置version参数，用户请求时候传入参数。在request.version中获取版本，根据版本不同 做不同处理

