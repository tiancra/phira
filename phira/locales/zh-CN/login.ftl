
login = 登录到星穹列车
login-sub = 登录以加入活跃的星穹列车
back-login = 返回登录
register = 注册

email = 电子邮箱
username = 用户名
password = 密码

name-length-req = 用户名长度应介于 4-20 之间
name-has-illegal-char = 你是不是又给流萤看了什么禁忌知识？
pwd-length-req = 密码长度应介于 6-26 之间
illegal-email = 流萤好像没有听说过这个邮箱

action-success = { $action ->
  [login] 登录成功
  [register] 注册成功
  *[other] _
}
action-failed = { $action ->
  [login] 登录失败
  [register] 注册失败
  *[other] _
}

email-sent = 验证信息已发送到邮箱，请验证后登录
