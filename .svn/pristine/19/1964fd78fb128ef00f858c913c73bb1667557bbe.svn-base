-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 2019-01-30 06:19:24
-- 服务器版本： 5.7.21
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jiajia_spider`
--

-- --------------------------------------------------------

--
-- 表的结构 `jiajia_spider_article`
--

DROP TABLE IF EXISTS `jiajia_spider_article`;
CREATE TABLE IF NOT EXISTS `jiajia_spider_article` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `type` tinyint(3) UNSIGNED NOT NULL COMMENT '文章类型：1: 普通文章 2. 菜谱',
  `title` varchar(255) NOT NULL,
  `description` text,
  `material` text,
  `content` text,
  `source` varchar(255) DEFAULT NULL,
  `url` varchar(1024) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `jiajia_spider_article`
--



-- --------------------------------------------------------

--
-- 表的结构 `jiajia_spider_article_tag_rel`
--

DROP TABLE IF EXISTS `jiajia_spider_article_tag_rel`;
CREATE TABLE IF NOT EXISTS `jiajia_spider_article_tag_rel` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `articleid` int(10) UNSIGNED NOT NULL,
  `tagid` int(10) UNSIGNED NOT NULL,
  PRIMARY KEY (`id`),
  KEY `articleid` (`articleid`),
  KEY `tagid` (`tagid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `jiajia_spider_article_tag_rel`
--


-- --------------------------------------------------------

--
-- 表的结构 `jiajia_spider_food_step`
--

DROP TABLE IF EXISTS `jiajia_spider_food_step`;
CREATE TABLE IF NOT EXISTS `jiajia_spider_food_step` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `articleid` int(10) UNSIGNED NOT NULL,
  `step` tinyint(3) UNSIGNED NOT NULL,
  `image` varchar(1024) DEFAULT NULL,
  `detail` text,
  PRIMARY KEY (`id`),
  KEY `articleid` (`articleid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jiajia_spider_tag`
--

DROP TABLE IF EXISTS `jiajia_spider_tag`;
CREATE TABLE IF NOT EXISTS `jiajia_spider_tag` (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(1024) NOT NULL,
  `type` tinyint(3) UNSIGNED NOT NULL COMMENT '标签类型：1. 食材大类 2. 食材小类 3. 日期大类 4. 日期小类 5. 功能 6. 推荐 7. 不推荐 8. 其他（默认）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `jiajia_spider_tag`
--


-- --------------------------------------------------------

--
-- 表的结构 `jiajia_spider_url`
--

DROP TABLE IF EXISTS `jiajia_spider_url`;
CREATE TABLE IF NOT EXISTS `jiajia_spider_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(1024) NOT NULL COMMENT '完整url值',
  `hash` varchar(255) NOT NULL COMMENT 'Hash值',
  `articleid` int(11) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `url` (`url`),
  UNIQUE KEY `hash` (`hash`),
  KEY `articleid` (`articleid`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `jiajia_spider_url`
--



--
-- 限制导出的表
--

--
-- 限制表 `jiajia_spider_article_tag_rel`
--
ALTER TABLE `jiajia_spider_article_tag_rel`
  ADD CONSTRAINT `jiajia_spider_article_tag_rel_ibfk_1` FOREIGN KEY (`articleid`) REFERENCES `jiajia_spider_article` (`id`),
  ADD CONSTRAINT `jiajia_spider_article_tag_rel_ibfk_2` FOREIGN KEY (`tagid`) REFERENCES `jiajia_spider_tag` (`id`);

--
-- 限制表 `jiajia_spider_food_step`
--
ALTER TABLE `jiajia_spider_food_step`
  ADD CONSTRAINT `jiajia_spider_food_step_ibfk_1` FOREIGN KEY (`articleid`) REFERENCES `jiajia_spider_article` (`id`);

--
-- 限制表 `jiajia_spider_url`
--
ALTER TABLE `jiajia_spider_url`
  ADD CONSTRAINT `jiajia_spider_url_ibfk_1` FOREIGN KEY (`articleid`) REFERENCES `jiajia_spider_article` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
