create database blog_app;
use blog_app;

CREATE TABLE `user_info` (
  `username` varchar(20) NOT NULL COMMENT '用户名',
  `password` varchar(64) NOT NULL COMMENT '登录密码',
  `is_super` tinyint(1) DEFAULT '0' COMMENT '是否超级用户，0：否，1：是',
  `status` tinyint(1) DEFAULT '0' COMMENT '用户状态，0：正常，1：冻结，2：注销',
  `last_login_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '上次登录时间',
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `first_name` char(3) DEFAULT NULL COMMENT '姓',
  `last_name` varchar(10) DEFAULT NULL COMMENT '名',
  `email` varchar(32) DEFAULT NULL COMMENT '邮箱',
  `mobile` int(11) DEFAULT NULL COMMENT '手机号',
  `github_account` varchar(64) DEFAULT NULL COMMENT 'github账号',
  `city` varchar(20) DEFAULT NULL COMMENT '所在城市',
  `creator_id` varchar(20) DEFAULT NULL COMMENT '创建者用户名',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`username`),
  UNIQUE KEY `user_info_username_uindex` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户信息表';

